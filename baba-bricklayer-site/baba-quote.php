<?php
/**
 * Baba Bricklayer: quote form endpoint.
 * Saves each request as a private "Quote request" post and emails it to the site admin address
 * (or to the address in the `baba_quote_recipient` option, if set).
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

add_action( 'init', function () {
	register_post_type( 'baba_quote', array(
		'labels'              => array( 'name' => 'Quote requests', 'singular_name' => 'Quote request' ),
		'public'              => false,
		'show_ui'             => true,
		'show_in_menu'        => true,
		'menu_icon'           => 'dashicons-email-alt',
		'supports'            => array( 'title', 'editor' ),
		'capability_type'     => 'page',
		'map_meta_cap'        => true,
		'exclude_from_search' => true,
	) );
} );

add_action( 'rest_api_init', function () {
	register_rest_route( 'baba/v1', '/quote', array(
		'methods'             => 'POST',
		'permission_callback' => '__return_true',
		'callback'            => 'baba_quote_handle',
	) );
} );

function baba_quote_handle( WP_REST_Request $req ) {
	$p = $req->get_json_params();
	if ( ! is_array( $p ) ) { $p = $req->get_body_params(); }

	// Honeypot: bots fill the hidden field. Pretend it worked.
	if ( ! empty( $p['website'] ) ) { return array( 'ok' => true ); }

	$ip  = isset( $_SERVER['REMOTE_ADDR'] ) ? sanitize_text_field( wp_unslash( $_SERVER['REMOTE_ADDR'] ) ) : '';
	$key = 'baba_q_' . md5( $ip );
	$hit = (int) get_transient( $key );
	if ( $hit >= 5 ) { return new WP_Error( 'too_many', 'Too many requests. Please call us instead.', array( 'status' => 429 ) ); }

	$name    = sanitize_text_field( $p['name'] ?? '' );
	$phone   = sanitize_text_field( $p['phone'] ?? '' );
	$email   = sanitize_email( $p['email'] ?? '' );
	$suburb  = sanitize_text_field( $p['suburb'] ?? '' );
	$job     = sanitize_text_field( $p['job'] ?? '' );
	$message = sanitize_textarea_field( $p['message'] ?? '' );

	if ( '' === $name || '' === $phone || '' === $message || ! is_email( $email ) ) {
		return new WP_Error( 'invalid', 'Name, phone, a valid email and a message are required.', array( 'status' => 400 ) );
	}
	if ( strlen( $message ) > 5000 || strlen( $name ) > 200 ) {
		return new WP_Error( 'invalid', 'That message is too long.', array( 'status' => 400 ) );
	}
	set_transient( $key, $hit + 1, HOUR_IN_SECONDS );

	$body = "Name: $name\nPhone: $phone\nEmail: $email\nSuburb: $suburb\nType of job: $job\n\n$message";

	$id = wp_insert_post( array(
		'post_type'    => 'baba_quote',
		'post_status'  => 'private',
		'post_title'   => $name . ( $job ? ' - ' . $job : '' ),
		'post_content' => $body,
	), true );
	if ( is_wp_error( $id ) ) {
		return new WP_Error( 'save_failed', 'Could not save the request.', array( 'status' => 500 ) );
	}

	$to = get_option( 'baba_quote_recipient' ) ?: get_option( 'admin_email' );
	wp_mail( $to, 'Quote request from ' . $name, $body, array( 'Reply-To: ' . $name . ' <' . $email . '>' ) );

	return array( 'ok' => true );
}
