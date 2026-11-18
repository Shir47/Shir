<?php
/**
 * Baba Bricklayer: serves the inner pages from the theme's site/ folder,
 * the same way front-page.php serves the home page.
 * /about/ -> site/about.html, /services/brick-fences/ -> site/services-brick-fences.html
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

add_action( 'template_redirect', function () {
	$path = trim( (string) wp_parse_url( isset( $_SERVER['REQUEST_URI'] ) ? wp_unslash( $_SERVER['REQUEST_URI'] ) : '', PHP_URL_PATH ), '/' );
	if ( '' === $path || 'index' === $path || ! preg_match( '#^[a-z0-9-]+(?:/[a-z0-9-]+)?$#', $path ) ) { return; }
	$file = get_theme_file_path( 'site/' . str_replace( '/', '-', $path ) . '.html' );
	if ( ! file_exists( $file ) ) { return; }
	$html = file_get_contents( $file );
	$base = trailingslashit( get_theme_file_uri( 'site' ) );
	$html = str_replace( 'assets/', $base . 'assets/', $html );
	if ( ! get_option( 'blog_public' ) ) {
		$html = str_replace( '<meta charset="utf-8">', '<meta charset="utf-8">' . "\n" . '<meta name="robots" content="noindex, nofollow">', $html );
	}
	status_header( 200 );
	header( 'Content-Type: text/html; charset=utf-8' );
	echo $html; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
	exit;
}, 0 );
