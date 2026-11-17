# Baba Bricklayer site

One-page site served by the `baba-bricklayer` WordPress theme (its `front-page.php` outputs `site/index.html`).

- `site/` goes to `wp-content/themes/baba-bricklayer/site/`
- `baba-quote.php` is the quote form endpoint (`POST /wp-json/baba/v1/quote`); requests are saved under "Quote requests" in wp-admin and emailed to the site admin address
- `image-sources.json` lists where each photo came from on bababricklayer.com.au
