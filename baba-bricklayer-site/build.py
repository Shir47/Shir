#!/usr/bin/env python3
"""Builds the five static pages into site/. Design language follows afgweb.com.au."""
import os
from urllib.parse import quote

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')
V = '6'

LD = '{"@context":"https://schema.org","@type":"HomeAndConstructionBusiness","name":"Baba Bricklayer","description":"Bricklaying services in Adelaide, South Australia.","telephone":"+61449824153","email":"bababricklayer@gmail.com","areaServed":{"@type":"City","name":"Adelaide"},"address":{"@type":"PostalAddress","addressLocality":"Adelaide","addressRegion":"SA","addressCountry":"AU"},"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"08:00","closes":"17:30"}]}'

I_ARROW = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
I_PHONE = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h4l2 5-2.500 1.500a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>'
I_MAIL = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18v12H3zM3 7l9 6 9-6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>'
I_PIN = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s7-6.200 7-11.500A7 7 0 0 0 5 9.500C5 14.800 12 21 12 21z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><circle cx="12" cy="9.500" r="2.500" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>'
I_CLOCK = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 7v5l3.500 2" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>'
I_CHECK = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.500l4.500 4.500L19 7.500" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
I_UP = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 19V5M6 11l6-6 6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
I_BRICK = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18v12H3zM3 12h18M9 6v6M15 12v6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>'
# hand-drawn bits
H_UNDER = '<svg class="scribble" viewBox="0 0 300 16" preserveAspectRatio="none" aria-hidden="true"><path d="M3 10 C 50 3, 96 13, 150 7 S 250 4, 297 9" pathLength="1" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round"/></svg>'
H_ARROW = '<svg class="harrow" viewBox="0 0 44 44" aria-hidden="true"><path d="M38 6 C 20 7, 9 18, 8 36 M8 36 L3 26 M8 36 L17 30" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
H_LINE = '<svg class="hline" viewBox="0 0 1200 20" preserveAspectRatio="none" aria-hidden="true"><path d="M4 12 C 200 2, 420 18, 640 9 S 1040 4, 1196 11" pathLength="1" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg>'

NAV = [('Services', '/services/', 'services'), ('Our work', '/projects/', 'projects'), ('About', '/about/', 'about'), ('How we work', '/#process', ''), ('Questions', '/#faq', ''), ('Contact', '/contact/', 'contact')]

SERVICES = [
 ('repairs', 'Brick repairs', 'Brick repairs and restorations', 'svc-repairs.jpg', 'Trowel repointing mortar joints in a red brick wall',
  'Cracked, loose or weathered brickwork brought back to sound condition and matched to the wall you already have.',
  ['Cracked and loose bricks replaced', 'Mortar joints raked out and repointed', 'Brick and mortar matched to the existing wall']),
 ('garages', 'Brick garages', 'Brick garages', 'svc-garages.jpg', 'Brick home with a wide double garage',
  'Attached or freestanding garages built in brick, designed to sit comfortably with the rest of the house.',
  ['Single and double garages', 'Attached or freestanding', 'Brick chosen to suit your home']),
 ('fences', 'Brick fences', 'Brick fences', 'svc-fences.jpg', 'Dark brick front fence with piers and steel infill panels',
  'Front fences, piers and letterboxes that add privacy, security and street appeal.',
  ['Front and boundary fences', 'Brick piers with infill panels', 'Letterboxes and gate piers']),
 ('retaining', 'Retaining walls', 'Brick and block retaining walls', 'svc-retaining.jpg', 'Concrete block retaining wall under construction with steel reinforcing',
  'Reinforced brick and block walls that hold back the slope and turn a sloping block into usable space.',
  ['Brick and concrete block walls', 'Reinforced construction', 'Garden beds and level changes']),
 ('removal', 'Brick removal', 'Brick removal', 'svc-removal.jpg', 'Bricklayer in hi-vis working on a low brick wall',
  'Walls and brickwork taken down carefully when it is time to make way for something new.',
  ['Walls and brickwork taken down', 'Care around the rest of the structure', 'Ready for the next stage of your project']),
 ('maintenance', 'Maintenance', 'Brickwork maintenance', 'svc-maintenance.jpg', 'Gloved hands laying a course of red bricks',
  'Regular upkeep that catches small problems in mortar and brick before they turn into big ones.',
  ['Mortar and joint checks', 'Small repairs done early', 'Homes and commercial buildings']),
]

PROJECTS = [
 ('p5.jpg', 'Two-storey townhouses in red brick with cream panels', 'Red brick townhouses', 'Face brickwork'),
 ('p4.jpg', 'Two-storey home in dark face brick with white upper level', 'Two-storey face brick home', 'Face brickwork'),
 ('svc-fences.jpg', 'Dark brick front fence with piers and steel infill panels', 'Brick and steel front fence', 'Brick fences'),
 ('p7.jpg', 'Red brick home with grey rendered portico', 'Red brick and render home', 'Brick and render'),
 ('p8.jpg', 'Two-storey home in light grey brick', 'Light grey brick home', 'Face brickwork'),
 ('hero.jpg', 'Single-storey brick home with a built-in garage at dusk', 'Brick home with garage', 'Brick garages'),
 ('p1.jpg', 'Home with dark brick piers and a timber deck', 'Dark brick piers', 'Brick piers'),
 ('p6.jpg', 'Two-storey home behind a limestone and steel front fence', 'Stone and steel front fence', 'Front fences'),
 ('p2.jpg', 'Entry of a home with brown brick and rendered piers', 'Brick entry', 'Brick and render'),
 ('p3.jpg', 'Brick home with rendered entry and garage', 'Brick and render home', 'Brick and render'),
 ('p12.jpg', 'Single-storey home with brick front and double garage', 'Brick-front home', 'Brick garages'),
 ('svc-garages.jpg', 'Brick home with a wide double garage', 'Double garage', 'Brick garages'),
]

FAQS = [
 ('What kinds of projects do you take on?', 'A wide range of masonry work: new construction, renovations, repairs and restoration, for residential, commercial and industrial properties.'),
 ('How experienced is your team?', 'Between us we have decades of experience in bricklaying and masonry, and we keep our training up to date.'),
 ('How do you keep the site safe?', 'We follow strict safety procedures, inspect the site regularly, keep the team trained and use well-maintained equipment, so the site stays safe for everyone on and around it.'),
 ('Can I see examples or references?', 'Yes. You can see photos on <a href="/projects/">our work page</a>, and we can provide references when you ask.'),
 ('How long will my job take?', 'It depends on the size and complexity of the job. We give you an estimate and a timeline at the first consultation, then work to finish on time without cutting corners.'),
 ('How do I get a quote?', 'Fill in the <a href="/contact/">quote form</a> or call us on 0449 824 153. We will talk the job through and answer any questions.'),
]

STEPS = [('Get in touch', 'Call us or send the quote form with a few details about your job.'),
         ('Talk it through', 'We go over the job with you and give you an estimate and a timeline.'),
         ('We build', 'Our team lays, repairs or removes the brickwork, safely and on schedule.'),
         ('Job complete', 'Solid, tidy brickwork, finished on time and built to last.')]

WHY = [('Safety on every site', 'Strict safety standards protect our team, your family and your property from the first day to the last.'),
       ('Finished on time', 'You get a clear timeline at the start, and steady, organised work to meet it.'),
       ('Modern methods', 'Up-to-date tools and techniques, in the hands of people who have laid brick for decades.'),
       ('Current designs', 'Bonds, bricks and finishes that suit the way homes and buildings are being built now.')]

JOBS = ['Brick repairs and restoration', 'Brick garage', 'Brick fence', 'Retaining wall', 'Brick removal', 'Brickwork maintenance', 'New construction or renovation', 'Something else']


def head(title, desc):
    return f'''<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/img/hero.jpg">
<meta name="theme-color" content="#060913">
<link rel="icon" type="image/png" href="assets/img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600..800&family=Caveat:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css?v={V}">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">{LD}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''


def header(active):
    links = ''.join(f'<a href="{u}"{" aria-current=\"page\"" if k and k == active else ""}>{n}</a>' for n, u, k in NAV)
    return f'''<header class="hd">
  <div class="wrap hd-in">
    <a class="brand" href="/" aria-label="Baba Bricklayer, home"><img src="assets/img/logo-light.png" alt="" width="360" height="181"><span>Baba <b>Bricklayer</b></span></a>
    <nav class="nav" id="nav" aria-label="Main">{links}</nav>
    <a class="hd-tel" href="tel:+61449824153">{I_PHONE}0449 824 153</a>
    <a class="btn btn-pri btn-sm" href="/contact/">Request a quote</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
  <div class="progress" aria-hidden="true"><i></i></div>
</header>
'''


def footer():
    svc = ''.join(f'<li><a href="/services/#{i}">{t}</a></li>' for i, _, t, *_ in SERVICES)
    return f'''<footer class="ft">
  <div class="wrap ft-grid">
    <div class="ft-about">
      <a class="brand" href="/"><img src="assets/img/logo-light.png" alt="" width="360" height="181" loading="lazy"><span>Baba <b>Bricklayer</b></span></a>
      <p>Bricklaying, brick repairs and restoration for Adelaide homes and businesses.</p>
    </div>
    <div><h2>Services</h2><ul>{svc}</ul></div>
    <div><h2>Company</h2><ul><li><a href="/projects/">Our work</a></li><li><a href="/about/">About</a></li><li><a href="/#process">How we work</a></li><li><a href="/#faq">Questions</a></li><li><a href="/contact/">Contact</a></li></ul></div>
    <div><h2>Contact</h2><ul class="ft-contact">
      <li>{I_PIN}Adelaide, South Australia</li>
      <li>{I_PHONE}<a href="tel:+61449824153">0449 824 153</a></li>
      <li>{I_PHONE}<a href="tel:+61424767153">0424 767 153</a></li>
      <li>{I_MAIL}<a href="mailto:bababricklayer@gmail.com">bababricklayer@gmail.com</a></li>
      <li>{I_CLOCK}Mon to Sat, 8:00 am to 5:30 pm</li>
    </ul></div>
  </div>
  <div class="wrap"><p class="hand ft-sign">Built straight. Built to last. <span>Baba Bricklayer</span></p></div>
  <div class="wrap ft-bot"><p>© <span id="yr">2026</span> Baba Bricklayer</p><p>Bricklaying in Adelaide, South Australia</p></div>
</footer>
<div class="float">
  <a class="float-call" href="tel:+61449824153">{I_PHONE}<span>Call us</span></a>
  <a class="float-quote" href="/contact/">Request a quote</a>
  <button class="float-top" type="button" aria-label="Back to top">{I_UP}</button>
</div>
<dialog class="lightbox" aria-label="Photo"><form method="dialog"><button class="lb-close">Close</button></form><img alt=""></dialog>
<script src="assets/site.js?v={V}" defer></script>
</body>
</html>
'''


def form(pid):
    opts = ''.join(f'<option>{j}</option>' for j in JOBS)
    return f'''<form class="qform paper" novalidate>
  <div class="field"><label for="{pid}-name">Name <i>*</i></label><input id="{pid}-name" name="name" type="text" autocomplete="name" required></div>
  <div class="pair">
    <div class="field"><label for="{pid}-phone">Phone <i>*</i></label><input id="{pid}-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required></div>
    <div class="field"><label for="{pid}-email">Email <i>*</i></label><input id="{pid}-email" name="email" type="email" autocomplete="email" required></div>
  </div>
  <div class="pair">
    <div class="field"><label for="{pid}-suburb">Suburb</label><input id="{pid}-suburb" name="suburb" type="text" autocomplete="address-level2"></div>
    <div class="field"><label for="{pid}-job">Type of job</label><select id="{pid}-job" name="job"><option value="">Choose one</option>{opts}</select></div>
  </div>
  <div class="field"><label for="{pid}-msg">Job details <i>*</i></label><textarea id="{pid}-msg" name="message" rows="4" required></textarea></div>
  <div class="hp" aria-hidden="true"><label for="{pid}-web">Website</label><input id="{pid}-web" name="website" type="text" tabindex="-1" autocomplete="off"></div>
  <button class="btn btn-ink btn-block" type="submit">Request a quote</button>
  <p class="form-msg" role="status" aria-live="polite"></p>
</form>'''


def quote_section(pid, h='What would you like built?'):
    return f'''<section class="sec quote" id="quote">
  <div class="wrap quote-grid">
    <div>
      <h2>{h}</h2>
      <p class="lede">Tell us what you need built, repaired or removed. A rough size and a suburb is enough to get started.</p>
      <ul class="q-list">
        <li>{I_CHECK}<span>First we talk the job through. Then you get an estimate and a timeline.</span></li>
        <li>{I_PIN}<span>Adelaide, South Australia</span></li>
        <li>{I_PHONE}<span><a href="tel:+61449824153">0449 824 153</a> or <a href="tel:+61424767153">0424 767 153</a></span></li>
        <li>{I_MAIL}<span><a href="mailto:bababricklayer@gmail.com">bababricklayer@gmail.com</a></span></li>
        <li>{I_CLOCK}<span>Monday to Saturday, 8:00 am to 5:30 pm</span></li>
      </ul>
    </div>
    {form(pid)}
  </div>
</section>'''


def faq_section():
    items = ''.join(f'<details{" open" if n == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for n, (q, a) in enumerate(FAQS))
    return f'''<section class="sec" id="faq">
  <div class="wrap narrow">
    <h2>Before you get in touch.</h2>
    <div class="faq">{items}</div>
  </div>
</section>'''


def process_section():
    steps = ''.join(f'<li><span class="hand num">{n}</span><h3>{t}</h3><p>{p}</p></li>' for n, (t, p) in enumerate(STEPS, 1))
    return f'''<section class="sec" id="process">
  <div class="wrap">
    <h2>From the first call<br>to the finished wall.</h2>
    <p class="lede">You will know what we are doing, and when, at every stage.</p>
    {H_LINE}
    <ol class="steps">{steps}</ol>
  </div>
</section>'''


def page_head(title, lede, crumb):
    return f'''<section class="ph">
  <div class="wrap">
    <p class="crumb"><a href="/">Home</a><span aria-hidden="true">/</span>{crumb}</p>
    <h1>{title}</h1>
    <p class="lede">{lede}</p>
  </div>
</section>'''


def tile(f, alt, cap, kind, big=False):
    return f'<li><button type="button" class="tile"><span class="panel"><img src="assets/img/{f}" alt="{alt}" loading="lazy"></span><small>{kind}, Adelaide</small><strong>{cap}</strong></button></li>'


def cream_about(more=True):
    btn = f'<a class="btn btn-ink" href="/about/">More about us {I_ARROW}</a>' if more else f'<a class="btn btn-ink" href="/contact/">Request a quote {I_ARROW}</a>'
    return f'''<section class="cream" id="about">
  <div class="wrap cream-grid">
    <div>
      <h2>Every wall gets the same care, whatever the size of the job.</h2>
      <p>With decades of experience and real pride in the craft, Baba Bricklayer is a trusted choice for bricklaying across Adelaide. From detailed face brickwork to essential structural repairs, we deliver work that is plumb, level and built to last.</p>
      <p>More than 800 finished projects later, most of our work still comes from clients who were happy with the last job.</p>
      {btn}
    </div>
    <div class="pols">
      <figure class="pol p-a"><img src="assets/img/crew.jpg" alt="Three bricklayers in hi-vis laying a red brick wall" loading="lazy"><figcaption class="hand">On site</figcaption></figure>
      <figure class="pol p-b"><img src="assets/img/svc-repairs.jpg" alt="Trowel repointing mortar joints in a red brick wall" loading="lazy"><figcaption class="hand">Repointing</figcaption></figure>
      <figure class="pol p-c"><img src="assets/img/svc-maintenance.jpg" alt="Gloved hands laying a course of red bricks" loading="lazy"><figcaption class="hand">Laying</figcaption></figure>
    </div>
  </div>
  <div class="wrap cream-low">
    <div class="sticky"><p class="hand">Safety comes first on every job. For our team, for your family and for your property. A good wall means nothing if someone gets hurt building it.</p><p class="sticky-by"><b>Baba Bricklayer</b><span>Adelaide bricklayers, 25+ years</span></p></div>
    <ul class="stats">
      <li><strong><span data-count="25">25</span>+</strong><span>years of experience</span></li>
      <li><strong><span data-count="800">800</span>+</strong><span>projects completed</span></li>
      <li><strong>6</strong><span>days a week, Monday to Saturday</span></li>
    </ul>
  </div>
</section>'''


def why_section():
    items = ''.join(f'<li><h3>{t}</h3><p>{p}</p></li>' for t, p in WHY)
    return f'''<section class="sec">
  <div class="wrap">
    <h2>Safe. On time. Done properly.</h2>
    <p class="lede">Four things you can count on when we take on your job.</p>
    <ul class="why">{items}</ul>
  </div>
</section>'''


def page_home():
    rows = ''.join(f'<li><h3>{short}</h3><p>{d}</p><a class="more" href="/services/#{i}">More about {short.lower()} {I_ARROW}</a></li>' for i, short, t, img, alt, d, _ in SERVICES)
    chips = ''.join(f'<a class="chip" href="/contact/?job={quote(j)}">{t}</a>' for t, j in [('I need a wall repaired', 'Brick repairs and restoration'), ('I want a fence or garage', 'Brick fence'), ('I need a retaining wall', 'Retaining wall'), ('I need brick removed', 'Brick removal')])
    slides = [('hero.jpg', 'Single-storey brick home with a built-in garage at dusk', 'Brick home with garage'), ('svc-fences.jpg', 'Dark brick front fence with piers and steel infill panels', 'Brick and steel front fence'), ('p5.jpg', 'Two-storey townhouses in red brick with cream panels', 'Red brick townhouses'), ('p4.jpg', 'Two-storey home in dark face brick with white upper level', 'Two-storey face brick home')]
    sl = ''.join(f'<img src="assets/img/{f}" alt="{a}" data-cap="{c}"{" class=\"on\" fetchpriority=\"high\"" if n == 0 else " loading=\"lazy\""}>' for n, (f, a, c) in enumerate(slides))
    dots = ''.join(f'<button type="button" aria-label="Photo {n + 1}"{" class=\"on\"" if n == 0 else ""}></button>' for n in range(len(slides)))
    more = ''.join(tile(*PROJECTS[n]) for n in (1, 3, 5, 7))

    def feat(f, alt, kind, title, desc, notes, glow):
        ns = ''.join(f'<li>{H_ARROW}{n}</li>' for n in notes)
        return f'''<article class="feat">
      <button type="button" class="tile feat-shot"><span class="panel big {glow}"><span class="bar"><i></i><i></i><i></i><b>{title}</b></span><img src="assets/img/{f}" alt="{alt}" loading="lazy"></span></button>
      <div class="feat-info">
        <div><small>{kind}, Adelaide</small><h3>{title}</h3></div>
        <div><p>{desc}</p><a class="tlink" href="/projects/">See all our work</a></div>
        <ul class="hand notes">{ns}</ul>
      </div>
    </article>'''
    return head('Baba Bricklayer | Bricklaying Services in Adelaide', 'Adelaide bricklayers with 25+ years of experience. Brick repairs and restoration, garages, fences, retaining walls and brick removal. Call 0449 824 153 for a quote.') + header('home') + f'''<main id="main">
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-l">
      <div class="hello"><span class="ava"><img src="assets/img/logo.png" alt="" width="360" height="181"></span><p class="hand"><span id="greet">G'day.</span> We're Baba Bricklayer. We've laid brick around Adelaide for 25+ years.</p></div>
      <h1>Solid brickwork.<br><span class="ul">Built to last.{H_UNDER}</span></h1>
      <p class="lede">Brick repairs, garages, fences and retaining walls for Adelaide homes and businesses.</p>
      <div class="btns"><a class="btn btn-pri" href="/contact/">Request a quote {I_ARROW}</a><a class="btn btn-ghost" href="/projects/">See our work</a></div>
      <p class="ask">What do you need done?</p>
      <div class="chips">{chips}</div>
    </div>
    <div class="hero-r">
      <p class="hand note-top">straight courses, tight joints {H_ARROW}</p>
      <div class="panel big glow-o show">
        <span class="bar"><i></i><i></i><i></i><b id="cap-top">Brick home with garage</b></span>
        <div class="slides">{sl}</div>
        <span class="pill">{I_BRICK}<span><b id="cap">Brick home with garage</b><small>Recent brickwork, Adelaide</small></span></span>
      </div>
      <figure class="pol hero-pol"><img src="assets/img/crew.jpg" alt="Three bricklayers in hi-vis laying a red brick wall"><figcaption class="hand">On site</figcaption></figure>
      <div class="dots" role="group" aria-label="Choose a photo">{dots}</div>
    </div>
  </div>
</section>

<section class="sec" id="services">
  <div class="wrap">
    <h2>Lay it. Repair it.<br>Remove it.</h2>
    <p class="lede">If it is made of brick or block, we can help. Choose one job or combine several.</p>
    <ul class="rows">{rows}</ul>
    <p class="also-h">More ways we can help</p>
    <p class="slash">New construction <i>/</i> Renovations and remodelling <i>/</i> Brick restoration <i>/</i> Residential <i>/</i> Commercial <i>/</i> Industrial</p>
  </div>
</section>

<section class="sec" id="work">
  <div class="wrap">
    <h2>Brickwork that speaks<br>for itself.</h2>
    <p class="lede">A few recent jobs. Select any photo to see it larger.</p>
    {feat('svc-fences.jpg', 'Dark brick front fence with piers and steel infill panels', 'Brick fences', 'Brick and steel front fence', 'A front fence in dark brick with steel infill panels, giving the home privacy without closing it off from the street.', ['Piers set plumb and evenly spaced', 'Brick and steel working together', 'Privacy with street appeal'], 'glow-b')}
    {feat('p5.jpg', 'Two-storey townhouses in red brick with cream panels', 'Face brickwork', 'Red brick townhouses', 'Two storeys of face brick with clean lines and consistent joints, from the ground to the roofline.', ['Straight courses over two storeys', 'Consistent mortar joints', 'Crisp corners and openings'], 'glow-o')}
    <h3 class="sub-h">More recent work</h3>
    <ul class="tiles two">{more}</ul>
    <p class="center"><a class="btn btn-ghost" href="/projects/">See all our work {I_ARROW}</a></p>
  </div>
</section>

{cream_about()}

<section class="sec check">
  <div class="wrap check-grid">
    <div>
      <h2>Five signs your brickwork needs attention.</h2>
      <p class="lede">Tick the ones that sound familiar and see where you stand.</p>
      <div class="score"><strong><span id="score">0</span><small>of 5</small></strong><p id="score-msg">Tick anything that sounds familiar.</p></div>
      <a class="btn btn-pri" href="/contact/?job={quote('Brick repairs and restoration')}">Request a quote {I_ARROW}</a>
    </div>
    <ul class="ticks">
      <li><label><input type="checkbox"><span>Cracks in the bricks or the mortar</span></label></li>
      <li><label><input type="checkbox"><span>Mortar crumbling or missing from the joints</span></label></li>
      <li><label><input type="checkbox"><span>Loose or shifting bricks</span></label></li>
      <li><label><input type="checkbox"><span>A wall that leans or bulges</span></label></li>
      <li><label><input type="checkbox"><span>Damp patches or white salt stains</span></label></li>
    </ul>
  </div>
</section>

{process_section()}
{faq_section()}
{quote_section('h')}
</main>
''' + footer()


def page_services():
    rows = ''.join(f'''<article class="svc" id="{i}">
  <span class="panel big {'glow-o' if n % 2 == 0 else 'glow-b'}"><span class="bar"><i></i><i></i><i></i><b>{t}</b></span><img src="assets/img/{img}" alt="{alt}" loading="lazy"></span>
  <div><h2>{t}.</h2><p>{d}</p><ul class="q-list">{''.join(f'<li>{I_CHECK}<span>{b}</span></li>' for b in bl)}</ul><a class="btn btn-pri" href="/contact/?job={quote(JOBS[n] if n < 6 else JOBS[-1])}">Request a quote {I_ARROW}</a></div>
</article>''' for n, (i, short, t, img, alt, d, bl) in enumerate(SERVICES))
    return head('Bricklaying Services in Adelaide | Baba Bricklayer', 'Brick repairs and restoration, brick garages, fences, retaining walls, brick removal and brickwork maintenance across Adelaide.') + header('services') + f'''<main id="main">
{page_head('Lay it. Repair it. Remove it.', 'New construction, renovations, repairs and restoration for residential, commercial and industrial properties across Adelaide.', 'Services')}
<section class="sec tight"><div class="wrap svc-list">{rows}</div></section>
{why_section()}
{quote_section('s', 'Tell us about your job.')}
</main>
''' + footer()


def page_projects():
    tiles = ''.join(tile(*p) for p in PROJECTS)
    return head('Our Work | Baba Bricklayer, Adelaide', 'Photos of residential brickwork in face brick, block and rendered finishes by Baba Bricklayer, Adelaide.') + header('projects') + f'''<main id="main">
{page_head('Brickwork that speaks for itself.', 'Residential brickwork in face brick, block and rendered finishes. Select a photo to see it larger.', 'Our work')}
<section class="sec tight"><div class="wrap"><ul class="tiles three">{tiles}</ul></div></section>
{quote_section('p', 'Have a job like one of these?')}
</main>
''' + footer()


def page_about():
    return head('About Us | Baba Bricklayer, Adelaide', 'Baba Bricklayer has more than 25 years of bricklaying experience and over 800 completed projects across Adelaide.') + header('about') + f'''<main id="main">
{page_head("Adelaide's bricklayers for 25+ years.", 'Skill, reliability and a team that takes your project as seriously as you do.', 'About')}
{cream_about(False)}
<section class="sec">
  <div class="wrap two-col">
    <div><h2>Committed to keeping people safe.</h2><p class="lede">The wellbeing of our team and our clients comes first. We keep rigorous safety standards and procedures on every project, so your property is protected and the site stays secure at every stage of the work.</p></div>
    <div><h2>Careful planning, clean execution.</h2><p class="lede">We follow industry best practice with precision. From planning to the last course of bricks, every project reflects our commitment to quality, safety and professionalism.</p></div>
  </div>
</section>
{why_section()}
{quote_section('a')}
</main>
''' + footer()


def page_contact():
    return head('Contact Us | Baba Bricklayer, Adelaide', 'Request a bricklaying quote in Adelaide. Call 0449 824 153 or send the quote form.') + header('contact') + f'''<main id="main">
{quote_section('c', 'What would you like built?').replace('<section class="sec quote" id="quote">', '<section class="sec quote first" id="quote">').replace('<h2>', '<h1>', 1).replace('</h2>', '</h1>', 1)}
{faq_section()}
</main>
''' + footer()


PAGES = {'index.html': page_home, 'services.html': page_services, 'projects.html': page_projects, 'about.html': page_about, 'contact.html': page_contact}
for name, fn in PAGES.items():
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(fn())
    print('built', name)
