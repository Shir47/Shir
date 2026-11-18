<?php
/**
 * Baba Bricklayer: serves the static pages from the theme's site/ folder.
 * /  -> site/index.html, /about/ -> site/about.html,
 * /services/brick-fences/ -> site/services-brick-fences.html
 * Also provides /sitemap.xml and the "page not found" page.
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

function baba_send_page( $file, $status = 200 ) {
	$html = file_get_contents( $file );
	$base = trailingslashit( get_theme_file_uri( 'site' ) );
	$html = str_replace( array( 'assets/', '{{home}}' ), array( $base . 'assets/', untrailingslashit( home_url() ) ), $html );
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
	foreach ( (array) glob( get_theme_file_path( 'site/*.html' ) ) as $file ) {
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
	$path = trim( (string) wp_parse_url( isset( $_SERVER['REQUEST_URI'] ) ? wp_unslash( $_SERVER['REQUEST_URI'] ) : '', PHP_URL_PATH ), '/' );

	if ( 'sitemap.xml' === $path ) {
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
			$file = get_theme_file_path( 'site/index.html' );
			if ( file_exists( $file ) ) { baba_send_page( $file ); }
		}
		return;
	}
	if ( 'index' === $path || '404' === $path || ! preg_match( '#^[a-z0-9-]+(?:/[a-z0-9-]+)?$#', $path ) ) { return; }
	$file = get_theme_file_path( 'site/' . str_replace( '/', '-', $path ) . '.html' );
	if ( file_exists( $file ) ) { baba_send_page( $file ); }
}, 0 );

// Friendly "page not found" page.
add_action( 'template_redirect', function () {
	if ( ! is_404() ) { return; }
	$file = get_theme_file_path( 'site/404.html' );
	if ( file_exists( $file ) ) { baba_send_page( $file, 404 ); }
}, 5 );

// One sitemap: ours.
add_filter( 'wp_sitemaps_enabled', '__return_false' );
add_filter( 'robots_txt', function ( $output, $public ) {
	if ( $public ) { $output .= "\nSitemap: " . home_url( '/sitemap.xml' ) . "\n"; }
	return $output;
}, 10, 2 );
