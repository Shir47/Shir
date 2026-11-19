<?php
/**
 * Baba Bricklayer theme.
 * The guards stop the code loading twice if a copy is also loaded from elsewhere.
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

if ( ! function_exists( 'baba_site_dir' ) ) {
	require get_template_directory() . '/inc/pages.php';
}
if ( ! function_exists( 'baba_quote_handle' ) ) {
	require get_template_directory() . '/inc/quote.php';
}

add_action( 'after_setup_theme', function () {
	add_theme_support( 'title-tag' );
} );
