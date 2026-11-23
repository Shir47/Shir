# Maktab Alzahra SA website

A static website in English (`/en/`) and Dari (`/fa/`), nine pages each.

- `build.py` writes every page into `public/`. Each piece of text appears once as `L("English", "Dari")`.
- `src/style.css` is the design; `src/calc.js` calculates prayer times (Ja'fari method) and Hijri dates for Adelaide; `src/app.js` fills them into the pages.
- `src/images/` holds the logo and photos.

To rebuild after an edit:

```bash
python3 build.py
```

To put the site online, upload the contents of `public/` to the web root.
