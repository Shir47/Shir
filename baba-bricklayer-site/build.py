#!/usr/bin/env python3
"""Builds the five static pages into site/. Built by AFG Web."""
import os, re, json
from urllib.parse import quote

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')
V = '19'

LD = json.dumps({
 "@context": "https://schema.org", "@type": "HomeAndConstructionBusiness", "@id": "{{home}}/#business",
 "name": "Baba Bricklayer", "legalName": "Baba Bricklaying Pty Ltd", "taxID": "32649863838",
 "description": "Bricklaying, brick repairs and restoration for homes and businesses in Adelaide, South Australia.",
 "url": "{{home}}/", "image": "assets/img/share.jpg", "logo": "assets/img/icon-512.png",
 "telephone": "+61449824153", "email": "bababricklayer@gmail.com",
 "areaServed": [{"@type": "City", "name": "Adelaide"}, {"@type": "AdministrativeArea", "name": "Northern suburbs of Adelaide"}],
 "address": {"@type": "PostalAddress", "addressLocality": "Adelaide", "addressRegion": "SA", "addressCountry": "AU"},
 "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "opens": "07:00", "closes": "17:30"}],
 "sameAs": ["https://share.google/kLl9U1wGrtvDUYtTx", "https://www.tiktok.com/@_ahmad.313"],
 "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Bricklaying services", "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}} for n in ["Brick repairs and restorations", "Brick garages", "Brick fences", "Brick and block retaining walls", "Brick removal", "Brickwork maintenance"]]},
}, separators=(',', ':'))


def faq_ld(items):
    plain = lambda t: re.sub(r'<[^>]+>', '', t)
    data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in items]}
    return '<script type="application/ld+json">' + json.dumps(data, separators=(',', ':')) + '</script>'


GOOGLE = 'https://share.google/kLl9U1wGrtvDUYtTx'
ABN = '32 649 863 838'
TIKTOK = 'https://www.tiktok.com/@_ahmad.313'
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
 ('Do you work with builders?', 'Yes. We have been bricklayers for Fairmont Homes for the past 7 years and we work with other Adelaide builders too. If you are a builder, <a href="/contact/">get in touch</a> and tell us about your next job.'),
 ('Which areas do you cover?', 'Every suburb within about 20 km of Adelaide, and all of the northern suburbs, including Salisbury, Elizabeth, Mawson Lakes, Modbury, Golden Grove and Gawler. If you are not sure, call us and ask.'),
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


SLUG = {'repairs': 'brick-repairs', 'garages': 'brick-garages', 'fences': 'brick-fences', 'retaining': 'retaining-walls', 'removal': 'brick-removal', 'maintenance': 'brickwork-maintenance'}

# id: (headline a, headline b, second paragraph, included, when to call, faqs, photos)
MORE = {
 'repairs': ('Brick repairs', 'and restoration.',
  'Most damaged brickwork can be repaired without rebuilding the wall. We cut out what has failed, replace it with matching brick and mortar, and leave the repair as hard to spot as we can make it.',
  ['Cracked, broken and loose bricks cut out and replaced', 'Worn mortar raked out and repointed', 'Brick and mortar colour matched to the existing wall', 'Damaged corners, sills and window heads rebuilt', 'Older and heritage-style brickwork restored with care'],
  [('Cracks have appeared', 'Hairline or stepped cracks in the bricks or along the mortar joints.'), ('Mortar is falling out', 'Joints have worn back, or mortar is turning to sand when you touch it.'), ('Bricks are loose or flaking', 'Faces are breaking away, or bricks move in the wall.')],
  [('Can you match my existing bricks?', 'We match the brick and the mortar colour as closely as we can. With older bricks an exact match is not always possible, so we show you the options before we start.'), ('Does the whole wall need rebuilding?', 'Usually not. In most cases only the damaged section needs to be cut out and replaced. We will tell you honestly if a repair will not last.'), ('What causes brickwork to crack?', 'Common causes are ground movement, moisture and age. We look at the wall and tell you what we think is behind it, so the repair deals with the cause and not only the crack.')],
  [('p3.jpg', 'Brick home with rendered entry and garage'), ('svc-maintenance.jpg', 'Gloved hands laying a course of red bricks'), ('p7.jpg', 'Red brick home with grey rendered portico')]),
 'garages': ('Brick garages', 'built to match your home.',
  'A brick garage should look like it was always part of the house. We build to your plans, in a brick and bond that sits comfortably beside what is already there.',
  ['Single and double garages', 'Attached to the house or freestanding', 'Brick and mortar chosen to suit your home', 'Piers, door openings and lintels built to plan', 'Work for homeowners and for builders'],
  [('You are building new', 'A garage as part of a new home, with a builder or as an owner builder.'), ('You are adding on', 'An extra garage, or one to replace a carport or shed.'), ('You want it to match', 'Brickwork that ties in with the house instead of standing out.')],
  [('Do you build from my plans?', 'Yes. We work from your approved plans, whether they come from your builder, your designer or your engineer.'), ('Can the brick match my house?', 'We help you choose a brick and mortar as close as possible to the existing house, or one that deliberately contrasts if you prefer that.'), ('Do you organise council approval?', 'Approval is normally arranged by you or your builder before work starts. We can tell you what we need from the plans to give you a quote.')],
  [('p7.jpg', 'Red brick home with grey rendered portico'), ('hero.jpg', 'Single-storey brick home with a built-in garage at dusk'), ('p12.jpg', 'Single-storey home with brick front and double garage')]),
 'fences': ('Brick fences', 'that frame the home.',
  'A brick front fence gives you privacy and security, and it is the first thing people see from the street. We build fences, piers and letterboxes that suit the house behind them.',
  ['Front and boundary fences in brick', 'Brick piers with steel or timber infill panels', 'Letterboxes and gate piers', 'Capping and finishes to suit the house', 'Repairs to existing brick fences and piers'],
  [('You want more privacy', 'A solid or part-solid fence between the house and the street.'), ('You want street appeal', 'A fence that finishes off a new home or lifts an older one.'), ('Your old fence is failing', 'Leaning piers, cracked panels or missing capping.')],
  [('Can you combine brick with steel or timber?', 'Yes. Brick piers with steel or timber infill panels are one of the most common fences we build.'), ('Can the fence match my house?', 'We choose brick and mortar to suit the house, so the fence looks like part of the home.'), ('Do I need council approval?', 'It depends on the height and where the fence sits. Check with your council before work starts. We can tell you the fence height and details they are likely to ask about.')],
  [('p2.jpg', 'Entry of a home with brown brick and rendered piers'), ('p6.jpg', 'Two-storey home behind a limestone and steel front fence'), ('p1.jpg', 'Home with dark brick piers and a timber deck')]),
 'retaining': ('Retaining walls', 'in brick and block.',
  'A retaining wall has a job to do: hold the ground back for decades. We build reinforced brick and block walls that turn a sloping block into level, usable space.',
  ['Brick and concrete block retaining walls', 'Reinforced, core-filled construction', 'Garden beds, terraces and level changes', 'Walls built to your engineer\'s design where one is needed', 'Face brick or block ready for render'],
  [('Your block slopes', 'You want level lawn, parking or building space.'), ('You are landscaping', 'Raised garden beds, terraces and steps.'), ('An old wall is moving', 'A leaning, cracked or bulging retaining wall.')],
  [('Does my retaining wall need an engineer?', 'Taller walls and walls carrying extra load usually need an engineer\'s design and council approval. We will tell you early if we think yours does.'), ('Brick or block: which is better?', 'Concrete block is the usual choice for strength and cost. Brick, or block with a brick or render finish, suits walls that are on show.'), ('Can you replace a wall that is failing?', 'Yes. We take down the old wall and rebuild it properly, with the reinforcement it needs.')],
  [('p10.jpg', 'Charcoal brick home with a brick garden edge'), ('p9.jpg', 'Grey brick wall and corner of a new home'), ('p8.jpg', 'Two-storey home in light grey brick')]),
 'removal': ('Brick removal', 'done carefully.',
  'Taking brickwork down is a job for people who know how it was put up. We remove walls and brickwork cleanly, with care for everything that is staying.',
  ['Brick walls, fences and piers taken down', 'Openings cut for new doors and windows', 'Damaged sections removed ahead of repairs', 'Care around the rest of the structure', 'The area left ready for the next stage'],
  [('You are renovating', 'A wall has to come out, or a new opening has to go in.'), ('A wall is unsafe', 'Brickwork that is leaning, loose or beyond repair.'), ('You are starting again', 'An old fence or wall is making way for a new one.')],
  [('Can you remove part of a wall?', 'Yes. We often take out a section for a new opening or ahead of a repair, and leave the rest of the wall sound.'), ('Is the wall load-bearing?', 'It needs to be checked before anything is removed. If a wall is structural it needs proper support and usually an engineer\'s advice first.'), ('Can you rebuild after removing?', 'Yes. We can take down the old brickwork and build the new work, so one team handles the whole job.')],
  [('svc-repairs.jpg', 'Trowel repointing mortar joints in a red brick wall'), ('crew.jpg', 'Three bricklayers in hi-vis laying a red brick wall'), ('p2.jpg', 'Entry of a home with brown brick and rendered piers')]),
 'maintenance': ('Brickwork maintenance', 'that prevents bigger jobs.',
  'Brickwork lasts for generations when small problems are fixed early. A regular check and a few minor repairs cost far less than rebuilding a wall later.',
  ['Brickwork and mortar joints checked over', 'Small cracks and loose bricks fixed early', 'Worn joints repointed', 'Problem areas found before they spread', 'Homes, commercial and industrial buildings'],
  [('Your building is ageing', 'Older brickwork that has not been looked at for years.'), ('You manage a property', 'Commercial or rental buildings that need to be kept sound.'), ('You have spotted something small', 'A crack or a patch of worn mortar you would rather fix now.')],
  [('How often should brickwork be checked?', 'It depends on the age and exposure of the building. A look every few years, or whenever you notice a change, is a sensible rule.'), ('What does maintenance involve?', 'We look over the brickwork and joints, tell you what we find, and fix the small things before they grow.'), ('Do you look after commercial buildings?', 'Yes. We maintain brickwork on homes and on commercial and industrial properties.')],
  [('p4.jpg', 'Two-storey home in dark face brick with white upper level'), ('svc-repairs.jpg', 'Trowel repointing mortar joints in a red brick wall'), ('p5.jpg', 'Two-storey townhouses in red brick with cream panels')]),
}


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
<meta property="og:url" content="{{{{home}}}}{{{{path}}}}">
<link rel="canonical" href="{{{{home}}}}{{{{path}}}}">
<meta property="og:image" content="assets/img/share.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="Baba Bricklayer">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="assets/img/favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="assets/img/icon-192.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/archivo.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
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
    <a class="brand" href="/" aria-label="Baba Bricklayer, home"><img src="assets/img/logo.svg" alt="" width="360" height="181"><span>Baba Bricklayer<small>Adelaide</small></span></a>
    <nav class="nav" id="nav" aria-label="Main">{links}</nav>
    <a class="hd-tel" href="tel:+61449824153">{I_PHONE}0449 824 153</a>
    <a class="btn btn-pri btn-sm" href="/contact/">Get a quote</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
</header>
"""


def footer():
    svc = ''.join(f'<li><a href="/services/{SLUG[i]}/">{t}</a></li>' for i, _, t, *_ in SERVICES)
    return f"""<footer class="ft">
  <div class="wrap ft-grid">
    <div class="ft-about">
      <a class="ft-brand" href="/"><span><img src="assets/img/logo.svg" alt="" width="360" height="181" loading="lazy"></span>Baba Bricklayer</a>
      <p>Bricklaying, brick repairs and restoration for Adelaide homes and businesses.</p>
    </div>
    <div><h2>Services</h2><ul>{svc}</ul></div>
    <div><h2>Company</h2><ul><li><a href="/projects/">Our work</a></li><li><a href="/about/">About</a></li><li><a href="/contact/">Contact</a></li><li><a href="{GOOGLE}" target="_blank" rel="noopener">Google reviews</a></li><li><a href="{TIKTOK}" target="_blank" rel="noopener">TikTok</a></li></ul></div>
    <div><h2>Contact</h2><ul class="ft-contact">
      <li><a href="tel:+61449824153">0449 824 153</a></li>
      <li><a href="tel:+61424767153">0424 767 153</a></li>
      <li><a href="mailto:bababricklayer@gmail.com">bababricklayer@gmail.com</a></li>
      <li>Adelaide, South Australia</li>
      <li>Mon to Sat, 7:00 am to 5:30 pm</li>
    </ul></div>
  </div>
  <div class="wrap ft-bot"><p>© <span id="yr">2026</span> Baba Bricklaying Pty Ltd, trading as Baba Bricklayer. ABN {ABN}</p><p><a href="/privacy/">Privacy policy</a> · Website by <a href="https://afgweb.com.au/" rel="noopener">AFG Web</a></p></div>
</footer>
<a class="float-call" href="tel:+61449824153" aria-label="Call 0449 824 153">{I_PHONE}</a>
<dialog class="lightbox" aria-label="Photo"><form method="dialog"><button class="lb-close">Close</button></form><img alt=""></dialog>
<script src="assets/site.js?v={V}" defer></script>
</body>
</html>
"""


def form(pid, job=None):
    opts = ''.join(f'<option{" selected" if j == job else ""}>{j}</option>' for j in JOBS)
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
  <p class="form-note">We only use your details to reply to your request. See our <a href="/privacy/">privacy policy</a>.</p>
  <p class="form-msg" role="status" aria-live="polite"></p>
</form>"""


def h2(a, b, tag='h2'):
    return f'<{tag} class="h">{a}<span>{b}</span></{tag}>'


def quote_section(pid, a='Tell us about', b='your job.', tag='h2', job=None):
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
          <li>{I_CLOCK}<span><small>Hours</small>Monday to Saturday, 7:00 am to 5:30 pm</span></li>
          <li>{I_PIN}<span><small>Service area</small>Within about 20 km of Adelaide, and all northern suburbs</span></li>
          <li>{I_CHECK}<span><small>ABN</small>{ABN}</span></li>
        </ul>
      </div>
      <div class="quote-r">{form(pid, job)}</div>
    </div>
  </div>
</section>"""


STAR = '<svg class="star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.6l2.9 6.1 6.6.9-4.8 4.6 1.2 6.6L12 17.6l-5.900 3.200 1.200-6.600L2.500 9.600l6.600-.900z" fill="currentColor"/></svg>'
# Copied word for word from the Google Business page (November 2026). True = Google showed more text behind "More".
REVIEWS = [
 ('Salman Akhtar', 'Excellent quality brickwork and very professional service. Great communication from start to finish. Highly recommend.', False),
 ('Syed Arshad Ahmed', 'I was in contact with Ahmed, He and his team got the most professional work culture. They did their job in a very safe manner and no compromise on quality. The guys were efficient and completed the work as promised.', True),
 ('A B', 'Ahmad was very informative, communicated promptly and very professional. He was quick and careful, which we appreciated it so much.', False),
 ('Shaz Dave', 'Baba Bricklayer. Extremely happy with his communication, ethics and workmanship. He returned my call asap, organised quote and completed job within the week. He could have done it earlier but was done on Saturday to suits us.', True),
]


def reviews_section():
    stars = STAR * 5
    cards = ''.join(f"""<li class="rev"><span class="stars" role="img" aria-label="5 out of 5 stars">{stars}</span><blockquote>{t}{' …' if more else ''}</blockquote><p class="rev-by"><span class="rev-av" aria-hidden="true">{n[0]}</span><span><b>{n}</b><small>Google review</small></span></p></li>""" for n, t, more in REVIEWS)
    return f"""<section class="sec reviews" id="reviews">
  <div class="wrap">
    <div class="head">
      <div><p class="label">Reviews</p>{h2("Don't take our word for it.", 'Read what our customers say.')}</div>
      <div class="score"><strong>5.0</strong><div><span class="stars" role="img" aria-label="5 out of 5 stars">{stars}</span><p>from 5 Google reviews</p></div></div>
    </div>
    <ul class="revs">{cards}</ul>
    <div class="reviews-btns"><a class="btn btn-dark" href="{GOOGLE}" target="_blank" rel="noopener">Read all reviews on Google {I_ARROW}</a><a class="tlink" href="{GOOGLE}" target="_blank" rel="noopener">Leave a review {I_ARROW}</a><p class="fine">Rating and reviews as shown on Google, November 2026.</p></div>
  </div>
</section>"""


def builders_section():
    return f"""<section class="sec builders" id="builders">
  <div class="wrap builders-grid">
    <div>
      <p class="label">Builders we work with</p>
      {h2('Trusted on site', "by Adelaide's home builders.")}
      <p>Alongside our work for homeowners, we lay brick for home builders. For the past 7 years we have been bricklayers for Fairmont Homes, and we work with a range of other builders across Adelaide as well.</p>
      <p>Builders come back to us for the same reasons homeowners do: we turn up when we say we will, we work safely, and the walls are straight.</p>
      <a class="btn btn-dark" href="/contact/?job={quote('New construction or renovation')}">Builders, talk to us {I_ARROW}</a>
    </div>
    <ul class="b-cards">
      <li class="b-main"><strong><span data-count="7">7</span><small>years</small></strong><div><h3>Fairmont Homes</h3><p>Bricklaying for one of South Australia's home builders, year after year.</p><a class="tlink" href="https://fairmonthomes.com.au/" target="_blank" rel="noopener">fairmonthomes.com.au {I_ARROW}</a></div></li>
      <li>{I_CHECK}<div><h3>Other Adelaide builders</h3><p>We work with different builders on new homes and developments.</p></div></li>
      <li>{I_CHECK}<div><h3>Homeowners and businesses</h3><p>The same team and the same standard on repairs, fences and one-off jobs.</p></div></li>
    </ul>
  </div>
</section>"""


NORTH = ['Salisbury', 'Elizabeth', 'Mawson Lakes', 'Parafield Gardens', 'Paralowie', 'Para Hills', 'Ingle Farm', 'Pooraka', 'Modbury', 'Golden Grove', 'Tea Tree Gully', 'Munno Para', 'Smithfield', 'Craigmore', 'Angle Vale', 'Virginia', 'Gawler']
METRO = ['Adelaide CBD', 'North Adelaide', 'Prospect', 'Enfield', 'Norwood', 'Campbelltown', 'Burnside', 'Unley', 'Mitcham', 'Marion', 'Glenelg', 'Henley Beach', 'West Lakes', 'Port Adelaide']


def areas_section():
    north = ''.join(f'<li>{x}</li>' for x in NORTH)
    metro = ''.join(f'<li>{x}</li>' for x in METRO)
    return f"""<section class="sec areas" id="areas">
  <div class="wrap areas-grid">
    <div>
      <p class="label">Where we work</p>
      {h2('Across Adelaide,', 'and all through the north.')}
      <p>We work in every suburb within about 20 km of the city, and right across Adelaide's northern suburbs.</p>
      <p class="areas-note">{I_PIN}<span>Not sure if we come to you? Call <a href="tel:+61449824153">0449 824 153</a> and ask.</span></p>
    </div>
    <div class="areas-lists">
      <div><h3>Northern suburbs</h3><ul class="chips">{north}</ul><p class="fine">and every northern suburb in between.</p></div>
      <div><h3>Around Adelaide</h3><ul class="chips">{metro}</ul><p class="fine">and all suburbs within about 20 km of the city.</p></div>
    </div>
  </div>
</section>"""


I_TIKTOK = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M16.6 5.8a4.300 4.300 0 0 1-1-2.800h-3.100v12.400a2.600 2.600 0 1 1-2.600-2.600c.3 0 .5 0 .8.100V9.700a5.700 5.700 0 1 0 4.900 5.700V9a7.300 7.300 0 0 0 4.300 1.400V7.300a4.300 4.300 0 0 1-3.300-1.500z" fill="currentColor"/></svg>'


def tiktok_section():
    return f"""<section class="tt">
  <div class="wrap tt-in">
    <span class="tt-ic">{I_TIKTOK}</span>
    <div class="tt-text">
      <p class="label">On TikTok</p>
      <h2 class="h sm">See us on site.</h2>
      <p>Baba Bricklayer is on TikTok as <b>@_ahmad.313</b>. Follow along for videos from the team.</p>
    </div>
    <ul class="tt-stats"><li><strong>40+</strong>videos</li><li><strong>500+</strong>followers</li></ul>
    <a class="btn btn-dark" href="{TIKTOK}" target="_blank" rel="noopener">Watch on TikTok {I_ARROW}</a>
  </div>
</section>"""


def faq_section():
    items = ''.join(f'<details{" open" if n == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for n, (q, a) in enumerate(FAQS))
    return f"""<section class="sec" id="faq">
  <div class="wrap faq-grid">
    <div><p class="label">Questions</p>{h2('Good to know', 'before we start.')}<p class="lede">Can't see your question? Call us on <a href="tel:+61449824153">0449 824 153</a>.</p></div>
    <div class="faq">{items}</div>
  </div>
</section>{faq_ld(FAQS)}"""


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


GROUP = {'Face brickwork': 'Face brickwork', 'Brick and render': 'Brick and render', 'Brick garages': 'Garages', 'Brick fences': 'Fences and piers', 'Front fences': 'Fences and piers', 'Brick piers': 'Fences and piers'}


def shot(f, alt, cap, kind):
    return f'<li data-g="{GROUP[kind]}"><button type="button" class="shot"><img src="assets/img/{f}" alt="{alt}" loading="lazy"><span><small>{kind}</small>{cap}</span></button></li>'


def about_block(link=True):
    btn = f'<a class="btn btn-dark" href="/about/">More about us {I_ARROW}</a>' if link else f'<a class="btn btn-pri" href="/contact/">Request a quote {I_ARROW}</a>'
    return f"""<section class="sec" id="about">
  <div class="wrap about-grid">
    <div class="about-imgs">
      <img class="a1" src="assets/img/crew.jpg" alt="Three bricklayers in hi-vis laying a red brick wall" loading="lazy">
      <img class="a2" src="assets/img/svc-maintenance.jpg" alt="Gloved hands laying a course of red bricks" loading="lazy">
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
    cards = ''.join(f"""<li class="card"><a href="/services/{SLUG[i]}/"><span class="card-img"><img src="assets/img/{img}" alt="{alt}" loading="lazy"><b>{n:02d}</b></span><small>{CATS[i]}</small><strong>{short}</strong><em>Explore service {I_ARROW}</em></a></li>""" for n, (i, short, t, img, alt, d, _) in enumerate(SERVICES, 1))
    signs = ''.join(f'<li><span class="n">{n:02d}</span><div><h3>{t}</h3><p>{p}</p></div></li>' for n, (t, p) in enumerate(SIGNS, 1))
    shots = ''.join(shot(*PROJECTS[n]) for n in (0, 1, 2, 3, 5, 7))
    return head('Bricklayer Adelaide | Brick Repairs, Fences &amp; Walls | Baba Bricklayer', 'Adelaide bricklayers with 25+ years of experience. Brick repairs, fences, garages and retaining walls across Adelaide and the northern suburbs. Call 0449 824 153 for a quote.') + header('home') + f"""<main id="main">
<section class="hero">
  <div class="hero-bg"><img src="assets/img/hero.jpg" alt="" width="1400" height="1050" fetchpriority="high"></div>
  <div class="wrap hero-in">
    <h1 class="h"><small class="label">Bricklayer in Adelaide · Brick repairs and new brickwork</small>Quality brickwork,<span>built to last.</span></h1>
    <p class="hero-lede">New brickwork, repairs and restoration for Adelaide homes and businesses, from a team with more than 25 years on the trowel.</p>
    <div class="hero-btns"><a class="btn btn-pri" href="/contact/">Request a quote {I_ARROW}</a><a class="tlink light" href="/projects/">See our work {I_ARROW}</a></div>
  </div>
  <div class="trust">
    <ul class="wrap">
      <li>{I_CHECK}25+ years of experience</li>
      <li>{I_CHECK}800+ projects completed</li>
      <li>{I_CHECK}Trusted by home builders</li>
      <li>{I_CHECK}5.0 stars on Google</li>
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
{tiktok_section()}

{about_block()}
{builders_section()}
{reviews_section()}
{process_section()}
{why_section()}
{areas_section()}
{faq_section().replace('<section class="sec" id="faq">', '<section class="sec stone" id="faq">')}
{quote_section('h')}
</main>
""" + footer()


def page_services():
    rows = ''.join(f"""<article class="svc" id="{i}">
  <div class="svc-img"><img src="assets/img/{img}" alt="{alt}" loading="lazy"><b>{n + 1:02d}</b></div>
  <div><p class="label">{CATS[i]}</p><h2 class="h sm">{t}</h2><p>{d}</p><ul class="ticks">{''.join(f'<li>{I_CHECK}{b}</li>' for b in bl)}</ul><div class="svc-btns"><a class="btn btn-pri" href="/services/{SLUG[i]}/">More about {short.lower()} {I_ARROW}</a><a class="tlink" href="/contact/?job={quote(JOBS[n])}">Request a quote {I_ARROW}</a></div></div>
</article>""" for n, (i, short, t, img, alt, d, bl) in enumerate(SERVICES))
    return head('Bricklaying Services Adelaide | Repairs, Fences, Garages | Baba Bricklayer', 'Brick repairs and restoration, brick garages, fences, retaining walls, brick removal and brickwork maintenance across Adelaide and the northern suburbs.') + header('services') + f"""<main id="main">
{page_head('Brickwork for', 'every kind of job.', 'New construction, renovations, repairs and restoration for residential, commercial and industrial properties across Adelaide.', 'Services', 'svc-fences.jpg')}
<section class="sec"><div class="wrap svc-list">{rows}</div></section>
{process_section()}
{quote_section('s')}
</main>
""" + footer()


def page_projects():
    shots = ''.join(shot(*p) for p in PROJECTS)
    return head('Bricklaying Projects in Adelaide | Baba Bricklayer', 'Photos of brick homes, fences, garages and face brickwork by Baba Bricklayer, Adelaide.') + header('projects') + f"""<main id="main">
{page_head('Brickwork worth', 'a second look.', 'Residential brickwork in face brick, block and rendered finishes. Select a photo to see it larger.', 'Our work', 'p5.jpg')}
<section class="sec"><div class="wrap">
  <div class="filter" role="group" aria-label="Filter projects"><button type="button" class="on" data-f="">All work</button><button type="button" data-f="Face brickwork">Face brickwork</button><button type="button" data-f="Brick and render">Brick and render</button><button type="button" data-f="Garages">Garages</button><button type="button" data-f="Fences and piers">Fences and piers</button></div>
  <ul class="shots light">{shots}</ul>
</div></section>
{tiktok_section()}
{quote_section('p', 'Have a job like', 'one of these?')}
</main>
""" + footer()


def page_about():
    return head('About Baba Bricklayer | Adelaide Bricklayers for 25+ Years', 'Baba Bricklayer has more than 25 years of bricklaying experience, over 800 completed projects and 7 years working with Fairmont Homes in Adelaide.') + header('about') + f"""<main id="main">
{page_head("Adelaide's bricklayers", 'for more than 25 years.', 'Skill, reliability and a team that takes your project as seriously as you do.', 'About', 'crew.jpg')}
{about_block(False)}
{builders_section()}
{reviews_section()}
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
    return head('Get a Bricklaying Quote in Adelaide | Contact Baba Bricklayer', 'Request a bricklaying quote in Adelaide and the northern suburbs. Call 0449 824 153 or send the quote form. Open Monday to Saturday.') + header('contact') + f"""<main id="main">
{quote_section('c', 'Tell us about', 'your job.', 'h1').replace('<section class="quote" id="quote">', '<section class="quote first" id="quote">')}
{faq_section()}
</main>
""" + footer()


def page_service(n):
    i, short, t, img, alt, d, bl = SERVICES[n]
    a, b, p2, inc, when, faqs, photos = MORE[i]
    crumb = f'<a href="/services/">Services</a><span aria-hidden="true">/</span>{short}'
    incl = ''.join(f'<li>{I_CHECK}{x}</li>' for x in inc)
    whens = ''.join(f'<li><span class="n">{k:02d}</span><h3>{h}</h3><p>{x}</p></li>' for k, (h, x) in enumerate(when, 1))
    fq = ''.join(f'<details{" open" if k == 0 else ""}><summary>{q}</summary><p>{x}</p></details>' for k, (q, x) in enumerate(faqs))
    ph = ''.join(f'<li><button type="button" class="shot"><img src="assets/img/{f}" alt="{al}" loading="lazy"></button></li>' for f, al in photos)
    others = ''.join(f"""<li class="card"><a href="/services/{SLUG[oi]}/"><span class="card-img"><img src="assets/img/{oimg}" alt="{oalt}" loading="lazy"><b>{k + 1:02d}</b></span><small>{CATS[oi]}</small><strong>{oshort}</strong><em>Explore service {I_ARROW}</em></a></li>""" for k, (oi, oshort, ot, oimg, oalt, od, _) in enumerate(SERVICES) if oi != i)
    svc_ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "name": t, "serviceType": t, "description": d, "url": "{{home}}/services/" + SLUG[i] + "/", "areaServed": [{"@type": "City", "name": "Adelaide"}, {"@type": "AdministrativeArea", "name": "Northern suburbs of Adelaide"}], "provider": {"@id": "{{home}}/#business"}},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "{{home}}/"}, {"@type": "ListItem", "position": 2, "name": "Services", "item": "{{home}}/services/"}, {"@type": "ListItem", "position": 3, "name": short, "item": "{{home}}/services/" + SLUG[i] + "/"}]},
    ]}, separators=(',', ':')) + '</script>'
    return head(f'{t} Adelaide | Baba Bricklayer', f'{d} Adelaide and northern suburbs. Call Baba Bricklayer on 0449 824 153 for a quote.') + header('services') + f"""<main id="main">
{page_head(a, b, d, crumb, img)}
<section class="sec">
  <div class="wrap inc-grid">
    <div class="inc-img"><img src="assets/img/{img}" alt="{alt}" loading="lazy"></div>
    <div>
      <p class="label">What is included</p>
      <h2 class="h sm">{t}, done properly.</h2>
      <p>{p2}</p>
      <ul class="ticks">{incl}</ul>
      <a class="btn btn-pri" href="#quote">Request a quote {I_ARROW}</a>
    </div>
  </div>
</section>
<section class="sec stone">
  <div class="wrap">
    <div class="head"><div><p class="label">When to call us</p>{h2('Three good reasons', 'to pick up the phone.')}</div></div>
    <ol class="steps three">{whens}</ol>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="head"><div><p class="label">Our work</p>{h2('A closer look', 'at the brickwork.')}</div><a class="tlink" href="/projects/">View all projects {I_ARROW}</a></div>
    <ul class="shots light bare">{ph}</ul>
  </div>
</section>
<section class="sec stone">
  <div class="wrap faq-grid">
    <div><p class="label">Questions</p>{h2(f'About {short.lower()},', 'answered.')}<p class="lede">Something else on your mind? Call us on <a href="tel:+61449824153">0449 824 153</a>.</p></div>
    <div class="faq">{fq}</div>
  </div>
</section>{faq_ld(faqs)}
<section class="sec">
  <div class="wrap"><div class="head"><div><p class="label">More services</p>{h2('Other brickwork', 'we can help with.')}</div></div></div>
  <ul class="rail">{others}</ul>
</section>
{quote_section('v', 'Tell us about', 'your job.', 'h2', JOBS[n])}
</main>
{svc_ld}
""" + footer()


def page_privacy():
    return head('Privacy Policy | Baba Bricklayer', 'How Baba Bricklayer collects, uses and protects the personal information you send through this website.') + header('') + f"""<main id="main">
<section class="sec prose-sec">
  <div class="wrap prose">
    <p class="crumb on-light"><a href="/">Home</a><span aria-hidden="true">/</span>Privacy policy</p>
    <h1 class="h">Privacy policy</h1>
    <p class="fine">Last updated 18 November 2026</p>
    <p>This policy explains what personal information Baba Bricklaying Pty Ltd, trading as Baba Bricklayer (ABN {ABN}), collects through this website, why we collect it and what we do with it. We handle personal information in line with the Australian Privacy Principles.</p>
    <h2>What we collect</h2>
    <p>When you send a quote request we collect the details you type into the form: your name, phone number, email address, and, if you give them, your suburb, the type of job and a description of the work. If you phone or email us, we keep the details you give us so we can reply.</p>
    <h2>Why we collect it</h2>
    <p>We use your details to reply to your enquiry, prepare a quote, arrange and carry out the work, and contact you about that job. We do not use your details for advertising, and we do not sell or rent them to anyone.</p>
    <h2>Where it is kept</h2>
    <p>Quote requests are stored in this website's database and sent to our email inbox. The website is hosted by a third-party hosting company, and our email is provided by a third-party email service, so your details are held on their systems on our behalf. Some of these systems may be located outside Australia.</p>
    <h2>Who we share it with</h2>
    <p>We only share your details when it is needed to do the job, for example with a builder or supplier involved in your project, or when the law requires it.</p>
    <h2>Cookies and other services</h2>
    <p>This website does not use advertising or analytics cookies, and it does not load fonts or scripts from other companies. Links to other websites, including our Google reviews page, are covered by those sites' own privacy policies.</p>
    <h2>How long we keep it</h2>
    <p>We keep enquiry and job details for as long as we need them to do the work and to meet our legal and tax record-keeping obligations. You can ask us to delete an enquiry that did not go ahead.</p>
    <h2>Seeing or correcting your details</h2>
    <p>You can ask to see the personal information we hold about you, or ask us to correct or delete it. Contact us using the details below and we will respond within a reasonable time.</p>
    <h2>Complaints</h2>
    <p>If you are unhappy with how we have handled your information, please contact us first so we can put it right. If you are still not satisfied, you can contact the Office of the Australian Information Commissioner at <a href="https://www.oaic.gov.au/" target="_blank" rel="noopener">oaic.gov.au</a>.</p>
    <h2>Contact us</h2>
    <p>Baba Bricklayer, Adelaide, South Australia<br>Phone <a href="tel:+61449824153">0449 824 153</a><br>Email <a href="mailto:bababricklayer@gmail.com">bababricklayer@gmail.com</a></p>
    <p>We may update this policy from time to time. The latest version is always on this page.</p>
  </div>
</section>
</main>
""" + footer()


def page_404():
    return head('Page not found | Baba Bricklayer', 'That page could not be found.').replace('<meta name="viewport"', '<meta name="robots" content="noindex">\n<meta name="viewport"') + header('') + f"""<main id="main">
<section class="sec nf">
  <div class="wrap">
    <p class="label">Page not found</p>
    {h2('That page has moved', 'or was never built.', 'h1')}
    <p class="lede">The link you followed does not lead anywhere. These will get you back on track.</p>
    <div class="nf-btns"><a class="btn btn-pri" href="/">Back to home {I_ARROW}</a><a class="tlink" href="/services/">Our services {I_ARROW}</a><a class="tlink" href="/contact/">Request a quote {I_ARROW}</a></div>
  </div>
</section>
</main>
""" + footer()


PAGES = {'index.html': page_home, 'services.html': page_services, 'projects.html': page_projects, 'about.html': page_about, 'contact.html': page_contact, 'privacy.html': page_privacy, '404.html': page_404}
for _n, _svc in enumerate(SERVICES):
    PAGES['services-' + SLUG[_svc[0]] + '.html'] = (lambda k: (lambda: page_service(k)))(_n)
BIG = dict(l.split() for l in open(os.path.join(OUT, 'assets', 'img', 'sizes.txt')).read().split('\n') if l.strip())


def responsive(m):
    tag, f = m.group(0), m.group(1)
    if f not in BIG or 'srcset' in tag:
        return tag
    sizes = '100vw' if 'fetchpriority' in tag else '(max-width: 900px) 92vw, 46vw'
    return tag.replace(f'src="assets/img/{f}"', f'src="assets/img/{f}" srcset="assets/img/{f[:-4]}-800.jpg 800w, assets/img/{f} {BIG[f]}w" sizes="{sizes}"')


for name, fn in PAGES.items():
    stem = name[:-5]
    path = '/' if stem == 'index' else '/services/' + stem[9:] + '/' if stem.startswith('services-') else '/' + stem + '/'
    html = fn().replace('{{path}}', path)
    html = re.sub(r'<img src="assets/img/([a-z0-9-]+\.jpg)"[^>]*>', responsive, html)
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(html)
    print('built', name)
