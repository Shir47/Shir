<?php
/**
 * Baba Bricklayer: serves the static pages of the site.
 * /  -> index.html, /about/ -> about.html,
 * /services/brick-fences/ -> services-brick-fences.html
 * Also provides /sitemap.xml and the "page not found" page.
 *
 * The pages live in wp-content/baba-site/ when that folder exists,
 * otherwise in the active theme's site/ folder.
 * To switch the site off and fall back to the WordPress theme, disable this file.
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

function baba_site_dir() {
	$dir = WP_CONTENT_DIR . '/baba-site';
	return is_dir( $dir ) ? $dir : get_theme_file_path( 'site' );
}

function baba_site_url() {
	return is_dir( WP_CONTENT_DIR . '/baba-site' ) ? content_url( 'baba-site/' ) : trailingslashit( get_theme_file_uri( 'site' ) );
}

function baba_send_page( $file, $status = 200 ) {
	$html = file_get_contents( $file );
	$html = str_replace( array( 'assets/', '{{home}}' ), array( baba_site_url() . 'assets/', untrailingslashit( home_url() ) ), $html );
	if ( ! get_option( 'blog_public' ) && false === strpos( $html, 'name="robots"' ) ) {
		$html = str_replace( '<meta charset="utf-8">', '<meta charset="utf-8">' . "\n" . '<meta name="robots" content="noindex, nofollow">', $html );
	}
	status_header( $status );
	header( 'Content-Type: text/html; charset=utf-8' );
	echo $html; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
	exit;
}

function baba_page_paths() {
	$out = array();
	foreach ( (array) glob( baba_site_dir() . '/*.html' ) as $file ) {
		$name = basename( $file, '.html' );
		if ( '404' === $name ) { continue; }
		if ( 'index' === $name ) { $path = ''; }
		elseif ( 0 === strpos( $name, 'services-' ) ) { $path = 'services/' . substr( $name, 9 ) . '/'; }
		else { $path = $name . '/'; }
		$out[ $path ] = $file;
	}
	ksort( $out );
	return $out;
}

add_action( 'template_redirect', function () {
	if ( is_admin() || is_feed() || is_preview() || ( function_exists( 'is_customize_preview' ) && is_customize_preview() ) ) { return; }
	if ( isset( $_GET['elementor-preview'] ) || isset( $_GET['p'] ) || isset( $_GET['page_id'] ) ) { return; } // phpcs:ignore WordPress.Security.NonceVerification.Recommended

	$uri      = isset( $_SERVER['REQUEST_URI'] ) ? wp_unslash( $_SERVER['REQUEST_URI'] ) : '';
	$raw_path = (string) wp_parse_url( $uri, PHP_URL_PATH );
	$query    = (string) wp_parse_url( $uri, PHP_URL_QUERY );
	$path     = trim( $raw_path, '/' );
	$is_get   = isset( $_SERVER['REQUEST_METHOD'] ) && in_array( $_SERVER['REQUEST_METHOD'], array( 'GET', 'HEAD' ), true );

	// One address per page: no "www." copy.
	$host      = isset( $_SERVER['HTTP_HOST'] ) ? strtolower( sanitize_text_field( wp_unslash( $_SERVER['HTTP_HOST'] ) ) ) : '';
	$home_host = strtolower( (string) wp_parse_url( home_url(), PHP_URL_HOST ) );
	if ( $is_get && $home_host && 'www.' . $home_host === $host ) {
		wp_redirect( untrailingslashit( home_url() ) . $uri, 301 ); // phpcs:ignore WordPress.Security.SafeRedirect.wp_redirect_wp_redirect
		exit;
	}

	// Yoast's sitemaps list the previous site's pages; send them to ours.
	if ( $is_get && ( 'sitemap_index.xml' === $path || preg_match( '#^[a-z0-9_-]+-sitemap[0-9]*\\.xml$#', $path ) ) ) {
		wp_safe_redirect( home_url( '/sitemap.xml' ), 301 );
		exit;
	}

	// Addresses from the previous site.
	$moved = array( 'contact-us' => 'contact/', 'home' => '' );
	if ( isset( $moved[ $path ] ) ) {
		wp_safe_redirect( home_url( '/' . $moved[ $path ] ), 301 );
		exit;
	}

	if ( 'sitemap.xml' === $path ) {
		status_header( 200 );
		header( 'Content-Type: application/xml; charset=utf-8' );
		echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n" . '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' . "\n";
		foreach ( baba_page_paths() as $p => $file ) {
			echo '<url><loc>' . esc_url( home_url( '/' . $p ) ) . '</loc><lastmod>' . esc_html( gmdate( 'Y-m-d', filemtime( $file ) ) ) . '</lastmod></url>' . "\n";
		}
		echo '</urlset>';
		exit;
	}

	if ( '' === $path ) {
		if ( is_front_page() || is_home() ) {
			$file = baba_site_dir() . '/index.html';
			if ( file_exists( $file ) ) { baba_send_page( $file ); }
		}
		return;
	}
	if ( 'index' === $path || '404' === $path || ! preg_match( '#^[a-z0-9-]+(?:/[a-z0-9-]+)?$#', $path ) ) { return; }
	$file = baba_site_dir() . '/' . str_replace( '/', '-', $path ) . '.html';
	if ( file_exists( $file ) ) {
		// One address per page: always with the closing slash.
		if ( $is_get && '/' !== substr( $raw_path, -1 ) ) {
			wp_safe_redirect( home_url( '/' . $path . '/' ) . ( '' !== $query ? '?' . $query : '' ), 301 );
			exit;
		}
		baba_send_page( $file );
	}
}, 0 );

// Friendly "page not found" page.
add_action( 'template_redirect', function () {
	if ( ! is_404() ) { return; }
	$file = baba_site_dir() . '/404.html';
	if ( file_exists( $file ) ) { baba_send_page( $file, 404 ); }
}, 5 );

// One sitemap: ours.
add_filter( 'wp_sitemaps_enabled', '__return_false' );
add_filter( 'wpseo_sitemap_index_links', '__return_empty_array' );
add_filter( 'robots_txt', function ( $output, $public ) {
	$output = preg_replace( '#^Sitemap:.*sitemap_index\\.xml\\s*$#mi', '', $output );
	if ( $public && false === strpos( $output, '/sitemap.xml' ) ) { $output .= "\nSitemap: " . home_url( '/sitemap.xml' ) . "\n"; }
	return $output;
}, 99999, 2 );
