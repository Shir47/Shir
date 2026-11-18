<?php
/**
 * Fallback template. Every public page is served by inc/pages.php before WordPress
 * reaches this file, so anything that lands here is not part of the site:
 * show the "page not found" page.
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

$baba_404 = function_exists( 'baba_site_dir' ) ? baba_site_dir() . '/404.html' : '';
if ( $baba_404 && file_exists( $baba_404 ) ) {
	baba_send_page( $baba_404, 404 );
}
status_header( 404 );
?><!doctype html>
<html <?php language_attributes(); ?>>
<head><meta charset="<?php bloginfo( 'charset' ); ?>"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Page not found</title></head>
<body><p>Page not found. <a href="<?php echo esc_url( home_url( '/' ) ); ?>">Back to home</a></p></body>
</html>
