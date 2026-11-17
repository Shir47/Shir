#!/usr/bin/env python3
"""Builds the five static pages into site/ from shared header/footer parts."""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')
V = '5'

ICON = {
 'phone': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25c1.1.37 2.3.57 3.6.57a1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z" fill="currentColor"/></svg>',
 'mail': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18v12H3z M3 7l9 6 9-6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
 'clock': '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 7v5l3.5 2" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
 'pin': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.500C5 14.800 12 21 12 21z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><circle cx="12" cy="9.500" r="2.500" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>',
 'shield': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l8 3v6c0 4.500-3.300 8-8 9-4.700-1-8-4.500-8-9V6z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M8.500 12l2.500 2.500 4.500-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 'cal': '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.500" y="5" width="17" height="15" rx="1.500" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M3.500 10h17M8 3v4M16 3v4M8.500 15l2.300 2.200 4.700-4.700" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 'tool': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 17l8-8 4 4-8 8H3z M13 7l2-3 5 5-3 2z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
 'wall': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h18v14H3z M3 9.700h18M3 14.300h18M9 5v4.700M15 5v4.700M6 9.700v4.600M12 9.700v4.600M18 9.700v4.600M9 14.300V19M15 14.300V19" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
 'check': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.500l4.500 4.500L19 7.500" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
}

ICON.update({
 'garage': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 11l9-6 9 6v9H3z M7 20v-6h10v6 M7 17h10" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
 'fence': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 21V8l2-3 2 3v13 M10 21V8l2-3 2 3v13 M16 21V8l2-3 2 3v13 M3 12h18 M3 17h18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
 'hammer': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 4l6 6-3 3-6-6z M12.5 8.5L4 17l3 3 8.5-8.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
})
SVC_ICON = {'repairs': 'tool', 'garages': 'garage', 'fences': 'fence', 'retaining': 'wall', 'removal': 'hammer', 'maintenance': 'shield'}

NAV = [('Home', '/', 'home'), ('Services', '/services/', 'services'), ('Projects', '/projects/', 'projects'), ('About', '/about/', 'about'), ('Contact', '/contact/', 'contact')]

SERVICES = [
 ('repairs', 'Brick repairs and restorations', 'svc-repairs.jpg', 'Trowel repointing mortar joints in a red brick wall',
  'Cracked, loose or weathered brickwork brought back to sound condition and matched to the wall you already have.',
  ['Cracked and loose bricks replaced', 'Mortar joints raked out and repointed', 'Brick and mortar matched to the existing wall']),
 ('garages', 'Brick garages', 'svc-garages.jpg', 'Brick home with a wide double garage',
  'Attached or freestanding garages built in brick, designed to sit comfortably with the rest of the house.',
  ['Single and double garages', 'Attached or freestanding', 'Brick chosen to suit your home']),
 ('fences', 'Brick fences', 'svc-fences.jpg', 'Dark brick front fence with piers and steel infill panels',
  'Front fences, piers and letterboxes that add privacy, security and street appeal.',
  ['Front and boundary fences', 'Brick piers with infill panels', 'Letterboxes and gate piers']),
 ('retaining', 'Brick and block retaining walls', 'svc-retaining.jpg', 'Concrete block retaining wall under construction with steel reinforcing',
  'Reinforced brick and block walls that hold back the slope and turn a sloping block into usable space.',
  ['Brick and concrete block walls', 'Reinforced construction', 'Garden beds and level changes']),
 ('removal', 'Brick removal', 'svc-removal.jpg', 'Bricklayer in hi-vis working on a low brick wall',
  'Walls and brickwork taken down carefully when it is time to make way for something new.',
  ['Walls and brickwork taken down', 'Care around the rest of the structure', 'Ready for the next stage of your project']),
 ('maintenance', 'Brickwork maintenance', 'svc-maintenance.jpg', 'Gloved hands laying a course of red bricks',
  'Regular upkeep that catches small problems in mortar and brick before they turn into big ones.',
  ['Mortar and joint checks', 'Small repairs done early', 'Homes and commercial buildings']),
]

PROJECTS = [
 ('p5.jpg', 'Two-storey townhouses in red brick with cream panels', 'Red brick townhouses', 1100, 825),
 ('p4.jpg', 'Two-storey home in dark face brick with white upper level', 'Two-storey face brick home', 800, 600),
 ('svc-fences.jpg', 'Dark brick front fence with piers and steel infill panels', 'Brick and steel front fence', 1400, 1050),
 ('p7.jpg', 'Red brick home with grey rendered portico', 'Red brick and render home', 564, 376),
 ('p8.jpg', 'Two-storey home in light grey brick', 'Light grey brick home', 564, 423),
 ('hero.jpg', 'Single-storey brick home with a built-in garage at dusk', 'Brick home with garage', 1400, 1050),
 ('p1.jpg', 'Home with dark brick piers and a timber deck', 'Dark brick piers', 564, 376),
 ('p6.jpg', 'Two-storey home behind a limestone and steel front fence', 'Stone and steel front fence', 800, 622),
 ('p2.jpg', 'Entry of a home with brown brick and rendered piers', 'Brick entry', 564, 375),
 ('p3.jpg', 'Brick home with rendered entry and garage', 'Brick and render home', 550, 366),
 ('p12.jpg', 'Single-storey home with brick front and double garage', 'Brick-front home', 564, 282),
 ('svc-garages.jpg', 'Brick home with a wide double garage', 'Double garage', 564, 423),
]

FAQS = [
 ('What kinds of projects do you take on?', 'A wide range of masonry work: new construction, renovations, repairs and restoration, for residential, commercial and industrial properties.'),
 ('How experienced is your team?', 'Between us we have decades of experience in bricklaying and masonry, and we keep our training up to date.'),
 ('How do you keep the site safe?', 'We follow strict safety procedures, inspect the site regularly, keep the team trained and use well-maintained equipment, so the site stays safe for everyone on and around it.'),
 ('Can I see examples or references?', 'Yes. You can see photos on our <a href="/projects/">projects page</a>, and we can provide references when you ask.'),
 ('How long will my job take?', 'It depends on the size and complexity of the job. We give you an estimate and a timeline at the first consultation, then work to finish on time without cutting corners.'),
 ('How do I get a quote?', 'Fill in the <a href="/contact/">quote form</a> or call us on 0449 824 153. We will talk the job through and answer any questions.'),
]

WHY = [
 ('shield', 'Safety on every site', 'Strict safety standards protect our team, your family and your property from the first day to the last.'),
 ('cal', 'Finished on time', 'You get a clear timeline at the start, and steady, organised work to meet it.'),
 ('tool', 'Modern methods', 'Up-to-date tools and techniques, in the hands of people who have laid brick for decades.'),
 ('wall', 'Current designs', 'Bonds, bricks and finishes that suit the way homes and buildings are being built now.'),
]

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
<meta property="og:image" content="assets/img/crew.jpg">
<meta name="theme-color" content="#1d2125">
<link rel="icon" type="image/png" href="assets/img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600&family=Barlow+Condensed:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css?v={V}">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"HomeAndConstructionBusiness","name":"Baba Bricklayer","description":"Bricklaying services in Adelaide, South Australia.","telephone":"+61449824153","email":"bababricklayer@gmail.com","areaServed":{{"@type":"City","name":"Adelaide"}},"address":{{"@type":"PostalAddress","addressLocality":"Adelaide","addressRegion":"SA","addressCountry":"AU"}},"openingHoursSpecification":[{{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"08:00","closes":"17:30"}}]}}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''


def header(active):
    links = ''.join(f'<a href="{u}"{" aria-current=\"page\"" if k == active else ""}>{n}</a>' for n, u, k in NAV)
    return f'''<div class="topbar">
  <div class="wrap topbar-in">
    <p class="tb-item">{ICON['clock']}Mon to Sat, 8:00 am to 5:30 pm</p>
    <p class="tb-item tb-hide">{ICON['pin']}Adelaide, South Australia</p>
    <a class="tb-item tb-right" href="mailto:bababricklayer@gmail.com">{ICON['mail']}bababricklayer@gmail.com</a>
    <a class="tb-item" href="tel:+61449824153">{ICON['phone']}0449 824 153</a>
  </div>
</div>
<header class="header">
  <div class="wrap header-in">
    <a class="brand" href="/" aria-label="Baba Bricklayer, home">
      <img src="assets/img/logo.png" alt="" width="360" height="181">
      <span><strong>Baba Bricklayer</strong><small>Bricklaying, Adelaide</small></span>
    </a>
    <nav class="nav" id="nav" aria-label="Main">{links}</nav>
    <a class="btn btn-primary header-cta" href="/contact/">Get a quote</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
</header>
'''


def footer():
    svc = ''.join(f'<li><a href="/services/#{i}">{t}</a></li>' for i, t, *_ in SERVICES)
    nav = ''.join(f'<li><a href="{u}">{n}</a></li>' for n, u, _ in NAV)
    return f'''<footer class="footer">
  <div class="wrap footer-grid">
    <div class="f-about">
      <a class="f-brand" href="/"><span class="f-chip"><img src="assets/img/logo.png" alt="" width="360" height="181" loading="lazy"></span><strong>Baba Bricklayer</strong></a>
      <p>Adelaide bricklayers with more than 25 years of experience in new brickwork, repairs and restoration.</p>
    </div>
    <div><h2>Pages</h2><ul>{nav}</ul></div>
    <div><h2>Services</h2><ul>{svc}</ul></div>
    <div><h2>Contact</h2>
      <ul class="f-contact">
        <li>{ICON['phone']}<span><a href="tel:+61449824153">0449 824 153</a><br><a href="tel:+61424767153">0424 767 153</a></span></li>
        <li>{ICON['mail']}<a href="mailto:bababricklayer@gmail.com">bababricklayer@gmail.com</a></li>
        <li>{ICON['pin']}<span>Adelaide, South Australia</span></li>
        <li>{ICON['clock']}<span>Mon to Sat, 8:00 am to 5:30 pm<br>Sunday closed</span></li>
      </ul>
    </div>
  </div>
  <div class="footer-bot"><div class="wrap"><p>© <span id="yr">2026</span> Baba Bricklayer. All rights reserved.</p></div></div>
</footer>
<div class="callbar">
  <a class="btn btn-dark" href="tel:+61449824153">{ICON['phone']}Call now</a>
  <a class="btn btn-primary" href="/contact/">Get a quote</a>
</div>
<dialog class="lightbox" aria-label="Photo"><form method="dialog"><button class="lb-close">Close</button></form><img alt=""></dialog>
<script src="assets/site.js?v={V}" defer></script>
</body>
</html>
'''


def form(pid, compact=False):
    opts = ''.join(f'<option>{j}</option>' for j in JOBS)
    suburb = '' if compact else f'<div class="field"><label for="{pid}-suburb">Suburb</label><input id="{pid}-suburb" name="suburb" type="text" autocomplete="address-level2"></div>'
    return f'''<form class="qform" novalidate>
  <div class="field"><label for="{pid}-name">Your name</label><input id="{pid}-name" name="name" type="text" autocomplete="name" required></div>
  <div class="pair">
    <div class="field"><label for="{pid}-phone">Phone</label><input id="{pid}-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required></div>
    <div class="field"><label for="{pid}-email">Email</label><input id="{pid}-email" name="email" type="email" autocomplete="email" required></div>
  </div>
  <div class="pair{' single' if compact else ''}">
    {suburb}
    <div class="field"><label for="{pid}-job">Type of job</label><select id="{pid}-job" name="job"><option value="">Choose one</option>{opts}</select></div>
  </div>
  <div class="field"><label for="{pid}-msg">About the job</label><textarea id="{pid}-msg" name="message" rows="{2 if compact else 5}" required></textarea></div>
  <div class="hp" aria-hidden="true"><label for="{pid}-web">Website</label><input id="{pid}-web" name="website" type="text" tabindex="-1" autocomplete="off"></div>
  <button class="btn btn-primary btn-block" type="submit">Send quote request</button>
  <p class="form-msg" role="status" aria-live="polite"></p>
</form>'''


def banner(title, crumb, img):
    return f'''<section class="banner" style="background-image:linear-gradient(90deg,rgba(20,24,28,.92),rgba(20,24,28,.6)),url(assets/img/{img})">
  <div class="wrap">
    <h1>{title}</h1>
    <p class="crumb"><a href="/">Home</a><span aria-hidden="true">/</span>{crumb}</p>
  </div>
  <div class="stripe" aria-hidden="true"></div>
</section>'''


def cta():
    return f'''<section class="cta">
  <div class="wrap cta-in">
    <div><h2>Ready to start your project?</h2><p>Tell us what you need built, repaired or removed and we will get back to you with a quote.</p></div>
    <div class="cta-btns"><a class="cta-tel" href="tel:+61449824153">{ICON['phone']}<span><small>Call us now</small>0449 824 153</span></a><a class="btn btn-dark" href="/contact/">Request a quote</a></div>
  </div>
</section>'''


def why():
    items = ''.join(f'<li><span class="ico">{ICON[i]}</span><h3>{t}</h3><p>{p}</p></li>' for i, t, p in WHY)
    return f'''<section class="why">
  <div class="wrap">
    <div class="sec-head light"><p class="tag">Why choose us</p><h2>Built on safety, quality and reliability</h2></div>
    <ul class="why-grid">{items}</ul>
  </div>
</section>'''


def faq():
    items = ''.join(f'<details{" open" if n == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for n, (q, a) in enumerate(FAQS))
    return f'''<section class="sec faq">
  <div class="wrap faq-grid">
    <div class="sec-head"><p class="tag">Questions</p><h2>Frequently asked questions</h2><p>Can't see your question here? Call us on <a href="tel:+61449824153">0449 824 153</a> and we will be glad to help.</p></div>
    <div class="faq-list">{items}</div>
  </div>
</section>'''


def stats():
    return '''<ul class="stats">
  <li><strong><span data-count="25">25</span>+</strong><span>Years of experience</span></li>
  <li><strong><span data-count="800">800</span>+</strong><span>Projects completed</span></li>
  <li><strong>6</strong><span>Days a week, Monday to Saturday</span></li>
  <li><strong>100%</strong><span>Adelaide based</span></li>
</ul>'''


def page_home():
    cards = ''.join(f'''<li class="card"><a href="/services/#{i}"><div class="card-img"><img src="assets/img/{img}" alt="{alt}" loading="lazy"></div><div class="card-body"><span class="card-ico">{ICON[SVC_ICON[i]]}</span><h3>{t}</h3><p>{d}</p><span class="more">Learn more</span></div></a></li>''' for i, t, img, alt, d, _ in SERVICES)
    shots = ''.join(f'<li><button type="button" class="shot"><img src="assets/img/{f}" alt="{alt}" width="{w}" height="{h}" loading="lazy"><span>{cap}</span></button></li>' for f, alt, cap, w, h in PROJECTS[:8])
    checks = ''.join(f'<li>{ICON["check"]}{t}</li>' for t in ['Residential, commercial and industrial work', 'New brickwork, repairs and restoration', 'Clear estimates and timelines up front', 'Strict safety standards on every site'])
    steps = ''.join(f'<li><span class="num">{n}</span><h3>{t}</h3><p>{p}</p></li>' for n, t, p in [
        ('1', 'Get in touch', 'Call us or send the quote form with a few details about your job.'),
        ('2', 'Consultation and quote', 'We talk the job through and give you an estimate and a timeline.'),
        ('3', 'We get to work', 'Our team lays, repairs or removes the brickwork, safely and on schedule.'),
        ('4', 'Job complete', 'Solid, tidy brickwork, finished on time and built to last.')])
    return head('Baba Bricklayer | Bricklaying Services in Adelaide', 'Adelaide bricklayers with 25+ years of experience. Brick repairs and restoration, garages, fences, retaining walls and brick removal. Call 0449 824 153 for a quote.') + header('home') + f'''<main id="main">
<section class="hero">
  <div class="slides">
    <div class="slide on"><img src="assets/img/crew.jpg" alt="" width="1280" height="720" fetchpriority="high"></div>
    <div class="slide"><img src="assets/img/hero.jpg" alt="" width="1400" height="1050"></div>
    <div class="slide"><img src="assets/img/svc-fences.jpg" alt="" width="1400" height="1050"></div>
  </div>
  <div class="wrap hero-in">
    <div class="hero-copy">
      <p class="tag">Adelaide's bricklaying specialists</p>
      <h1><span class="mask"><span>Quality brickwork</span></span><span class="mask"><span><em>built to last</em></span></span></h1>
      <p class="hero-lede">For more than 25 years Baba Bricklayer has built, repaired and restored brickwork for homes and businesses across Adelaide.</p>
      <div class="hero-btns">
        <a class="btn btn-primary" href="/contact/">Get a quote</a>
        <a class="btn btn-outline" href="tel:+61449824153">{ICON['phone']}0449 824 153</a>
      </div>
      <ul class="trust"><li>{ICON['check']}25+ years experience</li><li>{ICON['check']}800+ projects completed</li><li>{ICON['check']}Homes and businesses</li></ul>
    </div>
    <div class="hero-form">
      <h2>Request a quote</h2>
      <p>Send us a few details and we will be in touch.</p>
      {form('h', True)}
    </div>
  </div>
  <div class="stripe" aria-hidden="true"></div>
</section>
<section class="statband"><div class="wrap">{stats()}</div></section>
<div class="ticker" aria-hidden="true"><div class="ticker-track"><span>Brick repairs</span><span>Restoration</span><span>Garages</span><span>Fences</span><span>Retaining walls</span><span>Brick removal</span><span>Maintenance</span><span>Brick repairs</span><span>Restoration</span><span>Garages</span><span>Fences</span><span>Retaining walls</span><span>Brick removal</span><span>Maintenance</span></div></div>

<section class="sec intro">
  <div class="wrap intro-grid">
    <div class="intro-imgs">
      <img class="i1" src="assets/img/hero.jpg" alt="Single-storey brick home with a built-in garage at dusk" width="1400" height="1050" loading="lazy">
      <img class="i2" src="assets/img/svc-repairs.jpg" alt="Trowel repointing mortar joints in a red brick wall" width="1200" height="1200" loading="lazy">
      <p class="badge"><strong>25+</strong>years on the trowel</p>
    </div>
    <div>
      <div class="sec-head"><p class="tag">About us</p><h2>Your trusted partner for quality brickwork</h2></div>
      <p>At Baba Bricklayer we turn plans into solid brick. With decades of experience in the craft, we take pride in workmanship that stands the test of time, from detailed face brickwork to essential structural repairs.</p>
      <ul class="checks">{checks}</ul>
      <a class="btn btn-dark" href="/about/">More about us</a>
    </div>
  </div>
</section>

<section class="sec services grey">
  <div class="wrap">
    <div class="sec-head center"><p class="tag">Our services</p><h2>Bricklaying services for every job</h2><p>If it is made of brick or block, we can lay it, repair it or remove it.</p></div>
    <ul class="cards">{cards}</ul>
  </div>
</section>

{why()}

<section class="sec projects">
  <div class="wrap">
    <div class="sec-head split"><div><p class="tag">Our projects</p><h2>Recent work</h2></div><a class="btn btn-dark" href="/projects/">View all projects</a></div>
    <ul class="shots four">{shots}</ul>
  </div>
</section>

<section class="sec process grey">
  <div class="wrap">
    <div class="sec-head center"><p class="tag">How it works</p><h2>From first call to finished wall</h2></div>
    <ol class="steps">{steps}</ol>
  </div>
</section>

{cta()}
{faq()}
</main>
''' + footer()


def page_services():
    rows = ''.join(f'''<article class="svc" id="{i}">
  <div class="svc-img"><img src="assets/img/{img}" alt="{alt}" loading="lazy"></div>
  <div class="svc-body"><h2>{t}</h2><p>{d}</p><ul class="checks">{''.join(f'<li>{ICON["check"]}{b}</li>' for b in bl)}</ul><a class="btn btn-primary" href="/contact/">Get a quote</a></div>
</article>''' for i, t, img, alt, d, bl in SERVICES)
    return head('Bricklaying Services in Adelaide | Baba Bricklayer', 'Brick repairs and restoration, brick garages, fences, retaining walls, brick removal and brickwork maintenance across Adelaide.') + header('services') + f'''<main id="main">
{banner('Our services', 'Services', 'svc-fences.jpg')}
<section class="sec">
  <div class="wrap">
    <div class="sec-head center"><p class="tag">What we do</p><h2>Brickwork for homes and businesses</h2><p>New construction, renovations, repairs and restoration for residential, commercial and industrial properties across Adelaide.</p></div>
    <div class="svc-list">{rows}</div>
  </div>
</section>
{why()}
{cta()}
</main>
''' + footer()


def page_projects():
    shots = ''.join(f'<li><button type="button" class="shot"><img src="assets/img/{f}" alt="{alt}" width="{w}" height="{h}" loading="lazy"><span>{cap}</span></button></li>' for f, alt, cap, w, h in PROJECTS)
    return head('Our Projects | Baba Bricklayer, Adelaide', 'Photos of residential brickwork in face brick, block and rendered finishes by Baba Bricklayer, Adelaide.') + header('projects') + f'''<main id="main">
{banner('Our projects', 'Projects', 'p5.jpg')}
<section class="sec">
  <div class="wrap">
    <div class="sec-head center"><p class="tag">Latest works</p><h2>Brickwork across Adelaide</h2><p>Residential brickwork in face brick, block and rendered finishes. Select a photo to see it larger.</p></div>
    <ul class="shots">{shots}</ul>
  </div>
</section>
{cta()}
</main>
''' + footer()


def page_about():
    return head('About Us | Baba Bricklayer, Adelaide', 'Baba Bricklayer has more than 25 years of bricklaying experience and over 800 completed projects across Adelaide.') + header('about') + f'''<main id="main">
{banner('About us', 'About', 'crew.jpg')}
<section class="sec intro">
  <div class="wrap intro-grid">
    <div class="intro-imgs">
      <img class="i1" src="assets/img/crew.jpg" alt="Three bricklayers in hi-vis laying a red brick wall" width="1280" height="720" loading="lazy">
      <img class="i2" src="assets/img/svc-maintenance.jpg" alt="Gloved hands laying a course of red bricks" width="802" height="360" loading="lazy">
      <p class="badge"><strong>800+</strong>projects completed</p>
    </div>
    <div>
      <div class="sec-head"><p class="tag">Who we are</p><h2>Adelaide's bricklaying experts</h2></div>
      <p>With decades of experience and a real pride in the craft, Baba Bricklayer is a trusted choice for bricklaying across Adelaide. From intricate face brickwork to essential structural repairs, our team delivers work that is plumb, level and built to last.</p>
      <p>More than 800 finished projects later, most of our work still comes from clients who were happy with the last job. When you choose us you get skill, reliability and a team that takes your project as seriously as you do.</p>
      <a class="btn btn-primary" href="/contact/">Get a quote</a>
    </div>
  </div>
</section>
<section class="statband"><div class="wrap">{stats()}</div></section>
<section class="sec safety">
  <div class="wrap safety-grid">
    <div>
      <div class="sec-head"><p class="tag">Health and safety</p><h2>Committed to keeping people safe</h2></div>
      <p>The wellbeing of our team and our clients comes first. We keep rigorous safety standards and procedures on every project, so your property is protected and the site stays secure at every stage of the work.</p>
    </div>
    <div>
      <div class="sec-head"><p class="tag">Best practice</p><h2>Careful planning, clean execution</h2></div>
      <p>We follow industry best practice with precision. From planning to the last course of bricks, every project reflects our commitment to quality, safety and professionalism.</p>
    </div>
  </div>
</section>
{why()}
{cta()}
</main>
''' + footer()


def page_contact():
    return head('Contact Us | Baba Bricklayer, Adelaide', 'Request a bricklaying quote in Adelaide. Call 0449 824 153 or send the quote form.') + header('contact') + f'''<main id="main">
{banner('Contact us', 'Contact', 'svc-retaining.jpg')}
<section class="sec">
  <div class="wrap contact-grid">
    <div>
      <div class="sec-head"><p class="tag">Get in touch</p><h2>Request a quote</h2><p>Tell us what you need built, repaired or removed. A rough size and a suburb is enough to get started.</p></div>
      <ul class="c-list">
        <li><span class="ico">{ICON['phone']}</span><div><h3>Phone</h3><a href="tel:+61449824153">0449 824 153</a><a href="tel:+61424767153">0424 767 153</a></div></li>
        <li><span class="ico">{ICON['mail']}</span><div><h3>Email</h3><a href="mailto:bababricklayer@gmail.com">bababricklayer@gmail.com</a></div></li>
        <li><span class="ico">{ICON['pin']}</span><div><h3>Service area</h3><p>Adelaide, South Australia</p></div></li>
        <li><span class="ico">{ICON['clock']}</span><div><h3>Hours</h3><p>Monday to Saturday, 8:00 am to 5:30 pm<br>Sunday closed</p></div></li>
      </ul>
    </div>
    <div class="form-card">
      <h2>Send us the details</h2>
      {form('c')}
    </div>
  </div>
</section>
<section class="map"><iframe title="Map of Adelaide, South Australia" src="https://www.google.com/maps?q=Adelaide+SA+Australia&z=11&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></section>
{faq()}
</main>
''' + footer()


PAGES = {'index.html': page_home, 'services.html': page_services, 'projects.html': page_projects, 'about.html': page_about, 'contact.html': page_contact}
for name, fn in PAGES.items():
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(fn())
    print('built', name)
