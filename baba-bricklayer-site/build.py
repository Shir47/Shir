#!/usr/bin/env python3
"""Builds the five static pages into site/. Built by AFG Web."""
import os
from urllib.parse import quote

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')
V = '7'

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

NAV = [('Services', '/services/', 'services'), ('Our work', '/projects/', 'projects'), ('About', '/about/', 'about'), ('Contact', '/contact/', 'contact')]

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


SIGNS = [('Cracks in the bricks or mortar', 'Hairline or stepped cracks let water in and tend to grow over time.'),
         ('Crumbling or missing mortar', 'Joints that have worn back leave the bricks without proper support.'),
         ('Loose or shifting bricks', 'Bricks that move when touched are no longer bonded to the wall.'),
         ('A wall that leans or bulges', 'Movement in the wall itself should be looked at sooner rather than later.'),
         ('Damp patches or white salt stains', 'Moisture is getting into the brickwork and bringing salts to the surface.')]
CATS = {'repairs': 'Repairs', 'garages': 'New builds', 'fences': 'Outdoor', 'retaining': 'Landscaping', 'removal': 'Demolition', 'maintenance': 'Upkeep'}


def head(title, desc):
    return f"""<!doctype html>
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
<meta name="theme-color" content="#ffffff">
<link rel="icon" type="image/png" href="assets/img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css?v={V}">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">{LD}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(active):
    links = ''.join(f'<a href="{u}"{" aria-current=\"page\"" if k == active else ""}>{n}</a>' for n, u, k in NAV)
    return f"""<header class="hd">
  <div class="wrap hd-in">
    <a class="brand" href="/" aria-label="Baba Bricklayer, home"><img src="assets/img/logo.png" alt="" width="360" height="181"><span>Baba Bricklayer<small>Adelaide</small></span></a>
    <nav class="nav" id="nav" aria-label="Main">{links}</nav>
    <a class="hd-tel" href="tel:+61449824153">{I_PHONE}0449 824 153</a>
    <a class="btn btn-pri btn-sm" href="/contact/">Get a quote</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
</header>
"""


def footer():
    svc = ''.join(f'<li><a href="/services/#{i}">{t}</a></li>' for i, _, t, *_ in SERVICES)
    return f"""<footer class="ft">
  <div class="wrap ft-grid">
    <div class="ft-about">
      <a class="ft-brand" href="/"><span><img src="assets/img/logo.png" alt="" width="360" height="181" loading="lazy"></span>Baba Bricklayer</a>
      <p>Bricklaying, brick repairs and restoration for Adelaide homes and businesses.</p>
    </div>
    <div><h2>Services</h2><ul>{svc}</ul></div>
    <div><h2>Company</h2><ul><li><a href="/projects/">Our work</a></li><li><a href="/about/">About</a></li><li><a href="/contact/">Contact</a></li></ul></div>
    <div><h2>Contact</h2><ul class="ft-contact">
      <li><a href="tel:+61449824153">0449 824 153</a></li>
      <li><a href="tel:+61424767153">0424 767 153</a></li>
      <li><a href="mailto:bababricklayer@gmail.com">bababricklayer@gmail.com</a></li>
      <li>Adelaide, South Australia</li>
      <li>Mon to Sat, 8:00 am to 5:30 pm</li>
    </ul></div>
  </div>
  <div class="wrap ft-bot"><p>© <span id="yr">2026</span> Baba Bricklayer. All rights reserved.</p><p>Website by <a href="https://afgweb.com.au/" rel="noopener">AFG Web</a></p></div>
</footer>
<a class="float-call" href="tel:+61449824153" aria-label="Call 0449 824 153">{I_PHONE}</a>
<dialog class="lightbox" aria-label="Photo"><form method="dialog"><button class="lb-close">Close</button></form><img alt=""></dialog>
<script src="assets/site.js?v={V}" defer></script>
</body>
</html>
"""


def form(pid):
    opts = ''.join(f'<option>{j}</option>' for j in JOBS)
    return f"""<form class="qform" novalidate>
  <div class="field"><label for="{pid}-name">Name</label><input id="{pid}-name" name="name" type="text" autocomplete="name" required></div>
  <div class="pair">
    <div class="field"><label for="{pid}-phone">Phone</label><input id="{pid}-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required></div>
    <div class="field"><label for="{pid}-email">Email</label><input id="{pid}-email" name="email" type="email" autocomplete="email" required></div>
  </div>
  <div class="pair">
    <div class="field"><label for="{pid}-suburb">Suburb <i>(optional)</i></label><input id="{pid}-suburb" name="suburb" type="text" autocomplete="address-level2"></div>
    <div class="field"><label for="{pid}-job">Type of job <i>(optional)</i></label><select id="{pid}-job" name="job"><option value="">Choose one</option>{opts}</select></div>
  </div>
  <div class="field"><label for="{pid}-msg">Tell us about the job</label><textarea id="{pid}-msg" name="message" rows="4" required></textarea></div>
  <div class="hp" aria-hidden="true"><label for="{pid}-web">Website</label><input id="{pid}-web" name="website" type="text" tabindex="-1" autocomplete="off"></div>
  <button class="btn btn-pri btn-block" type="submit">Request a quote {I_ARROW}</button>
  <p class="form-msg" role="status" aria-live="polite"></p>
</form>"""


def h2(a, b, tag='h2'):
    return f'<{tag} class="h">{a}<span>{b}</span></{tag}>'


def quote_section(pid, a='Tell us about', b='your job.', tag='h2'):
    return f"""<section class="quote" id="quote">
  <div class="wrap">
    <div class="quote-box">
      <div class="quote-l">
        <p class="label">Request a quote</p>
        {h2(a, b, tag)}
        <p>Tell us what you need built, repaired or removed. A rough size and a suburb is enough to get started.</p>
        <ul class="q-list">
          <li>{I_PHONE}<span><small>Call us</small><a href="tel:+61449824153">0449 824 153</a><a href="tel:+61424767153">0424 767 153</a></span></li>
          <li>{I_MAIL}<span><small>Email</small><a href="mailto:bababricklayer@gmail.com">bababricklayer@gmail.com</a></span></li>
          <li>{I_CLOCK}<span><small>Hours</small>Monday to Saturday, 8:00 am to 5:30 pm</span></li>
          <li>{I_PIN}<span><small>Service area</small>Adelaide, South Australia</span></li>
        </ul>
      </div>
      <div class="quote-r">{form(pid)}</div>
    </div>
  </div>
</section>"""


def faq_section():
    items = ''.join(f'<details{" open" if n == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for n, (q, a) in enumerate(FAQS))
    return f"""<section class="sec" id="faq">
  <div class="wrap faq-grid">
    <div><p class="label">Questions</p>{h2('Good to know', 'before we start.')}<p class="lede">Can't see your question? Call us on <a href="tel:+61449824153">0449 824 153</a>.</p></div>
    <div class="faq">{items}</div>
  </div>
</section>"""


def process_section():
    steps = ''.join(f'<li><span class="n">{n:02d}</span><h3>{t}</h3><p>{p}</p></li>' for n, (t, p) in enumerate(STEPS, 1))
    return f"""<section class="sec stone" id="process">
  <div class="wrap">
    <div class="head"><div><p class="label">How it works</p>{h2('A clear path', 'to a finished wall.')}</div><p class="lede">From the first call to the last brick, you will know what we are doing and when.</p></div>
    <ol class="steps">{steps}</ol>
  </div>
</section>"""


def why_section():
    icons = [I_CHECK, I_CLOCK, I_BRICK, I_PIN]
    items = ''.join(f'<li><span class="ic">{icons[n]}</span><h3>{t}</h3><p>{p}</p></li>' for n, (t, p) in enumerate(WHY))
    return f"""<section class="sec">
  <div class="wrap">
    <div class="head"><div><p class="label">Why Baba Bricklayer</p>{h2('Safe. On time.', 'Done properly.')}</div><p class="lede">Four things you can count on when we take on your job.</p></div>
    <ul class="why">{items}</ul>
  </div>
</section>"""


def page_head(a, b, lede, crumb, img):
    return f"""<section class="ph">
  <img src="assets/img/{img}" alt="" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="/">Home</a><span aria-hidden="true">/</span>{crumb}</p>
    {h2(a, b, 'h1')}
    <p class="lede">{lede}</p>
  </div>
</section>"""


def shot(f, alt, cap, kind):
    return f'<li><button type="button" class="shot"><img src="assets/img/{f}" alt="{alt}" loading="lazy"><span><small>{kind}</small>{cap}</span></button></li>'


def about_block(link=True):
    btn = f'<a class="btn btn-dark" href="/about/">More about us {I_ARROW}</a>' if link else f'<a class="btn btn-pri" href="/contact/">Request a quote {I_ARROW}</a>'
    return f"""<section class="sec" id="about">
  <div class="wrap about-grid">
    <div class="about-imgs">
      <img class="a1" src="assets/img/crew.jpg" alt="Three bricklayers in hi-vis laying a red brick wall" loading="lazy">
      <img class="a2" src="assets/img/svc-repairs.jpg" alt="Trowel repointing mortar joints in a red brick wall" loading="lazy">
    </div>
    <div>
      <p class="label">About us</p>
      {h2('25 years on the trowel.', 'More than 800 jobs behind us.')}
      <p>With decades of experience and real pride in the craft, Baba Bricklayer is a trusted choice for bricklaying across Adelaide. From detailed face brickwork to essential structural repairs, we deliver work that is plumb, level and built to last.</p>
      <p>Most of our work still comes from clients who were happy with the last job.</p>
      <ul class="stats">
        <li><strong><span data-count="25">25</span>+</strong>years of experience</li>
        <li><strong><span data-count="800">800</span>+</strong>projects completed</li>
        <li><strong>6</strong>days a week on site</li>
      </ul>
      {btn}
    </div>
  </div>
</section>"""


def page_home():
    cards = ''.join(f"""<li class="card"><a href="/services/#{i}"><span class="card-img"><img src="assets/img/{img}" alt="{alt}" loading="lazy"><b>{n:02d}</b></span><small>{CATS[i]}</small><strong>{short}</strong><em>Explore service {I_ARROW}</em></a></li>""" for n, (i, short, t, img, alt, d, _) in enumerate(SERVICES, 1))
    signs = ''.join(f'<li><span class="n">{n:02d}</span><div><h3>{t}</h3><p>{p}</p></div></li>' for n, (t, p) in enumerate(SIGNS, 1))
    shots = ''.join(shot(*PROJECTS[n]) for n in (0, 1, 2, 3, 5, 7))
    return head('Baba Bricklayer | Bricklaying Services in Adelaide', 'Adelaide bricklayers with 25+ years of experience. Brick repairs and restoration, garages, fences, retaining walls and brick removal. Call 0449 824 153 for a quote.') + header('home') + f"""<main id="main">
<section class="hero">
  <div class="hero-bg"><img src="assets/img/hero.jpg" alt="" width="1400" height="1050" fetchpriority="high"></div>
  <div class="wrap hero-in">
    <p class="label">Adelaide · Bricklaying and brick repairs</p>
    <h1 class="h">Quality brickwork,<span>built to last.</span></h1>
    <p class="hero-lede">New brickwork, repairs and restoration for Adelaide homes and businesses, from a team with more than 25 years on the trowel.</p>
    <div class="hero-btns"><a class="btn btn-pri" href="/contact/">Request a quote {I_ARROW}</a><a class="tlink light" href="/projects/">See our work {I_ARROW}</a></div>
  </div>
  <div class="trust">
    <ul class="wrap">
      <li>{I_CHECK}25+ years of experience</li>
      <li>{I_CHECK}800+ projects completed</li>
      <li>{I_CHECK}Homes and businesses</li>
      <li>{I_CHECK}Open Monday to Saturday</li>
    </ul>
  </div>
</section>

<section class="sec" id="services">
  <div class="wrap">
    <div class="head"><div><p class="label">What we do</p>{h2('Brickwork for', 'every kind of job.')}</div>
      <div class="rail-nav"><button type="button" class="rail-prev" aria-label="Previous services">{I_ARROW}</button><button type="button" class="rail-next" aria-label="Next services">{I_ARROW}</button></div></div>
  </div>
  <ul class="rail">{cards}</ul>
  <div class="wrap"><p class="rail-foot">New construction, renovations and remodelling too. <a href="/services/">See all services</a></p></div>
</section>

<section class="sec stone">
  <div class="wrap signs-grid">
    <div class="signs-l">
      <p class="label">Know the signs</p>
      {h2('Small cracks.', 'Worth a closer look.')}
      <p class="lede">Brickwork usually gives a warning before it becomes a bigger job. These are the common ones.</p>
      <img src="assets/img/svc-repairs.jpg" alt="Trowel repointing mortar joints in a red brick wall" loading="lazy">
      <p class="fine">A general guide only. Have a bricklayer look at the wall before deciding on repairs.</p>
    </div>
    <div>
      <ol class="signs">{signs}</ol>
      <a class="btn btn-dark" href="/contact/?job={quote('Brick repairs and restoration')}">Have it looked at {I_ARROW}</a>
    </div>
  </div>
</section>

<section class="sec dark" id="work">
  <div class="wrap">
    <div class="head"><div><p class="label">Our work</p>{h2('Brickwork worth', 'a second look.')}</div><p class="lede">Residential brickwork in face brick, block and rendered finishes around Adelaide.</p></div>
    <ul class="shots">{shots}</ul>
    <p class="after"><a class="tlink light" href="/projects/">View all projects {I_ARROW}</a></p>
  </div>
</section>

{about_block()}
{process_section()}
{why_section()}
{faq_section().replace('<section class="sec" id="faq">', '<section class="sec stone" id="faq">')}
{quote_section('h')}
</main>
""" + footer()


def page_services():
    rows = ''.join(f"""<article class="svc" id="{i}">
  <div class="svc-img"><img src="assets/img/{img}" alt="{alt}" loading="lazy"><b>{n + 1:02d}</b></div>
  <div><p class="label">{CATS[i]}</p><h2 class="h sm">{t}</h2><p>{d}</p><ul class="ticks">{''.join(f'<li>{I_CHECK}{b}</li>' for b in bl)}</ul><a class="btn btn-pri" href="/contact/?job={quote(JOBS[n])}">Request a quote {I_ARROW}</a></div>
</article>""" for n, (i, short, t, img, alt, d, bl) in enumerate(SERVICES))
    return head('Bricklaying Services in Adelaide | Baba Bricklayer', 'Brick repairs and restoration, brick garages, fences, retaining walls, brick removal and brickwork maintenance across Adelaide.') + header('services') + f"""<main id="main">
{page_head('Brickwork for', 'every kind of job.', 'New construction, renovations, repairs and restoration for residential, commercial and industrial properties across Adelaide.', 'Services', 'svc-fences.jpg')}
<section class="sec"><div class="wrap svc-list">{rows}</div></section>
{process_section()}
{quote_section('s')}
</main>
""" + footer()


def page_projects():
    shots = ''.join(shot(*p) for p in PROJECTS)
    return head('Our Work | Baba Bricklayer, Adelaide', 'Photos of residential brickwork in face brick, block and rendered finishes by Baba Bricklayer, Adelaide.') + header('projects') + f"""<main id="main">
{page_head('Brickwork worth', 'a second look.', 'Residential brickwork in face brick, block and rendered finishes. Select a photo to see it larger.', 'Our work', 'p5.jpg')}
<section class="sec"><div class="wrap"><ul class="shots light">{shots}</ul></div></section>
{quote_section('p', 'Have a job like', 'one of these?')}
</main>
""" + footer()


def page_about():
    return head('About Us | Baba Bricklayer, Adelaide', 'Baba Bricklayer has more than 25 years of bricklaying experience and over 800 completed projects across Adelaide.') + header('about') + f"""<main id="main">
{page_head("Adelaide's bricklayers", 'for more than 25 years.', 'Skill, reliability and a team that takes your project as seriously as you do.', 'About', 'crew.jpg')}
{about_block(False)}
<section class="sec stone">
  <div class="wrap two-col">
    <div><p class="label">Health and safety</p><h2 class="h sm">Committed to keeping people safe.</h2><p>The wellbeing of our team and our clients comes first. We keep rigorous safety standards and procedures on every project, so your property is protected and the site stays secure at every stage of the work.</p></div>
    <div><p class="label">Best practice</p><h2 class="h sm">Careful planning, clean execution.</h2><p>We follow industry best practice with precision. From planning to the last course of bricks, every project reflects our commitment to quality, safety and professionalism.</p></div>
  </div>
</section>
{why_section()}
{quote_section('a')}
</main>
""" + footer()


def page_contact():
    return head('Contact Us | Baba Bricklayer, Adelaide', 'Request a bricklaying quote in Adelaide. Call 0449 824 153 or send the quote form.') + header('contact') + f"""<main id="main">
{quote_section('c', 'Tell us about', 'your job.', 'h1').replace('<section class="quote" id="quote">', '<section class="quote first" id="quote">')}
{faq_section()}
</main>
""" + footer()


PAGES = {'index.html': page_home, 'services.html': page_services, 'projects.html': page_projects, 'about.html': page_about, 'contact.html': page_contact}
for name, fn in PAGES.items():
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(fn())
    print('built', name)
