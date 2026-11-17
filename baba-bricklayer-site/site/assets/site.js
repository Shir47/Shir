(function () {
  window.__baba = true;
  var d = document, root = d.documentElement, w = window;
  var reduce = w.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = w.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var $ = function (s, c) { return (c || d).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); };
  var clamp = function (v, a, b) { return Math.min(b, Math.max(a, v)); };

  /* preloader */
  var hero = $('.hero [data-lines]');
  var start = function () { root.classList.add('ready'); if (hero) hero.classList.add('in'); };
  var pn = $('.pre-n'), pb = $('.pre-bar i');
  if (reduce || !pn) { start(); } else {
    var t0 = performance.now(), dur = 1500;
    (function tick(t) {
      var p = clamp((t - t0) / dur, 0, 1), e = 1 - Math.pow(1 - p, 3);
      pn.textContent = Math.round(e * 100);
      pb.style.width = (e * 100) + '%';
      if (p < 1) requestAnimationFrame(tick); else setTimeout(start, 180);
    })(t0);
  }

  /* reveal on view */
  var targets = $$('[data-lines],[data-clip]').filter(function (el) { return el !== hero; });
  if ('IntersectionObserver' in w) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -12% 0px' });
    targets.forEach(function (el) { io.observe(el); });
  } else { targets.forEach(function (el) { el.classList.add('in'); }); }

  /* statement: split to words */
  var st = $('[data-words]'), words = [];
  if (st && !reduce) {
    st.innerHTML = st.textContent.trim().split(/\s+/).map(function (x) { return '<span class="w">' + x + '</span>'; }).join(' ');
    words = $$('.w', st);
  }

  /* counters */
  var counted = false, counters = $$('[data-count]'), statsEl = $('.stats');
  var runCount = function () {
    counted = true;
    counters.forEach(function (el) {
      var to = +el.getAttribute('data-count'), s = performance.now();
      (function f(t) {
        var p = clamp((t - s) / 1600, 0, 1);
        el.textContent = Math.round((1 - Math.pow(1 - p, 4)) * to);
        if (p < 1) requestAnimationFrame(f);
      })(s);
    });
  };

  /* horizontal work */
  var work = $('.work'), track = $('.work-track'), workMax = 0;
  var pinOK = function () { return !reduce && w.innerWidth > 900 && w.innerHeight > 520; };
  var hint = $('.work-hint');
  var layout = function () {
    if (!work) return;
    if (hint) hint.textContent = pinOK() ? 'Keep scrolling' : 'Swipe across';
    if (pinOK()) {
      work.classList.add('pinned');
      workMax = Math.max(0, track.scrollWidth - w.innerWidth);
      work.style.height = (workMax + w.innerHeight) + 'px';
    } else {
      work.classList.remove('pinned');
      work.style.height = '';
      track.style.transform = '';
      workMax = 0;
    }
  };
  layout();
  w.addEventListener('resize', layout);
  w.addEventListener('load', layout);
  $$('img', track || d).forEach(function (i) { if (!i.complete) i.addEventListener('load', layout); });

  /* scroll-driven bits */
  var media = $('[data-expand]'), mimg = media && $('img', media), mq = $('.marquee-track');
  var bar = $('.bar'), callbar = $('.callbar'), wm = $('.wordmark'), foot = $('.foot');
  var lastY = w.scrollY, mx = 0, vel = 0, curX = 0, ticking = false;

  var frame = function () {
    ticking = false;
    var y = w.scrollY, vh = w.innerHeight, dy = y - lastY;
    lastY = y;

    if (bar && !$('.nav.open')) bar.classList.toggle('hide', dy > 4 && y > 300);
    if (callbar) callbar.classList.toggle('show', y > vh * 0.6);

    if (media && !reduce) {
      var r = media.getBoundingClientRect();
      var p = clamp((vh - r.top) / (vh * 0.9), 0, 1);
      media.style.setProperty('--inset', ((1 - p) * 7).toFixed(2) + '%');
      media.style.setProperty('--rad', ((1 - p) * 28).toFixed(1) + 'px');
      var q = clamp((vh - r.top) / (vh + r.height), 0, 1);
      mimg.style.setProperty('--py', (-q * 14).toFixed(2) + '%');
    }

    if (words.length) {
      var sr = st.getBoundingClientRect();
      var sp = clamp((vh * 0.82 - sr.top) / (sr.height + vh * 0.35), 0, 1);
      var n = Math.round(sp * words.length);
      for (var i = 0; i < words.length; i++) words[i].classList.toggle('on', i < n);
    }

    if (statsEl && !counted && !reduce && statsEl.getBoundingClientRect().top < vh * 0.9) runCount();

    if (work && workMax) {
      var wp = clamp((y - work.offsetTop) / workMax, 0, 1);
      track.style.transform = 'translate3d(' + (-wp * workMax).toFixed(1) + 'px,0,0)';
    }

    if (wm && !reduce) {
      var fr = foot.getBoundingClientRect();
      var fp = clamp((vh - fr.top) / fr.height, 0, 1);
      wm.style.setProperty('--wy', ((1 - fp) * 45).toFixed(1) + '%');
    }
    vel += dy;
  };
  var onScroll = function () { if (!ticking) { ticking = true; requestAnimationFrame(frame); } };
  w.addEventListener('scroll', onScroll, { passive: true });
  w.addEventListener('resize', onScroll);
  frame();

  /* marquee: drifts, speeds up with scroll */
  if (mq && !reduce) {
    var half = 0;
    var measure = function () { half = mq.scrollWidth / 2; };
    measure(); w.addEventListener('load', measure); w.addEventListener('resize', measure);
    (function loop() {
      vel *= 0.9;
      curX += 0.7 + Math.abs(vel) * 0.06;
      if (half && curX > half) curX -= half;
      mq.style.transform = 'translate3d(' + (-curX).toFixed(1) + 'px,0,0)';
      requestAnimationFrame(loop);
    })();
  }

  /* cursor + floating service image */
  if (fine && !reduce) {
    var cur = $('.cursor'), lab = $('span', cur), flo = $('.float'), fimg = flo && $('img', flo);
    var tx = -100, ty = -100, cx = -100, cy = -100, fx = 0, fy = 0, fr2 = 0;
    d.addEventListener('mousemove', function (e) { tx = e.clientX; ty = e.clientY; });
    (function follow() {
      cx += (tx - cx) * 0.22; cy += (ty - cy) * 0.22;
      cur.style.setProperty('--cx', cx.toFixed(1) + 'px');
      cur.style.setProperty('--cy', cy.toFixed(1) + 'px');
      if (flo) {
        var ox = fx; fx += (tx + 28 - fx) * 0.1; fy += (ty - flo.offsetHeight / 2 - fy) * 0.1;
        fr2 += (clamp((fx - ox) * 0.5, -10, 10) - fr2) * 0.12;
        flo.style.setProperty('--fx', fx.toFixed(1) + 'px');
        flo.style.setProperty('--fy', fy.toFixed(1) + 'px');
        flo.style.setProperty('--fr', fr2.toFixed(2) + 'deg');
      }
      requestAnimationFrame(follow);
    })();
    d.addEventListener('mouseover', function (e) {
      var big = e.target.closest('[data-cursor]'), link = e.target.closest('a,button,summary');
      cur.classList.toggle('big', !!big);
      cur.classList.toggle('link', !big && !!link);
      lab.textContent = big ? big.getAttribute('data-cursor') : '';
    });
    $$('.card').forEach(function (c) { c.setAttribute('data-cursor', 'Scroll'); });
    if (flo) {
      $$('.row').forEach(function (row) {
        row.addEventListener('mouseenter', function () { fimg.src = row.getAttribute('data-img'); flo.classList.add('on'); });
        row.addEventListener('mouseleave', function () { flo.classList.remove('on'); });
      });
    }
  }

  /* menu */
  var btn = $('.menu-btn'), nav = $('#nav');
  if (btn && nav) {
    var setMenu = function (open) {
      nav.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.textContent = open ? 'Close' : 'Menu';
    };
    btn.addEventListener('click', function () { setMenu(!nav.classList.contains('open')); });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
  }

  /* anchors: smooth unless reduced motion */
  d.addEventListener('click', function (e) {
    var a = e.target.closest('a[href^="#"]');
    if (!a) return;
    var el = d.getElementById(a.getAttribute('href').slice(1));
    if (!el) return;
    e.preventDefault();
    var top = el.id === 'top' ? 0 : el.getBoundingClientRect().top + w.scrollY - (el.id === 'work' ? 0 : 70);
    w.scrollTo({ top: top, behavior: reduce ? 'auto' : 'smooth' });
    history.replaceState(null, '', '#' + el.id);
  });

  /* footer clock + year */
  var yr = d.getElementById('yr'); if (yr) yr.textContent = new Date().getFullYear();
  var adl = d.getElementById('adl');
  if (adl) {
    var clock = function () {
      try { adl.textContent = new Date().toLocaleTimeString('en-AU', { timeZone: 'Australia/Adelaide', hour: 'numeric', minute: '2-digit' }); } catch (e) { adl.parentNode.style.display = 'none'; }
    };
    clock(); setInterval(clock, 30000);
  }

  /* quote form */
  var form = d.getElementById('quote-form');
  if (form) {
    var msg = $('.form-msg', form), send = $('button[type=submit]', form);
    var say = function (text, cls) { msg.textContent = text; msg.className = 'form-msg' + (cls ? ' ' + cls : ''); };
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var firstBad = null;
      ['name', 'phone', 'email', 'message'].forEach(function (n) {
        var el = form.elements[n], v = el.value.trim();
        var bad = !v || (n === 'email' && !/^\S+@\S+\.\S+$/.test(v));
        el.classList.toggle('bad', bad);
        el.setAttribute('aria-invalid', bad ? 'true' : 'false');
        if (bad && !firstBad) firstBad = el;
      });
      if (firstBad) { say('Add your name, phone, a valid email and a few words about the job.', 'err'); firstBad.focus(); return; }
      var data = {};
      new FormData(form).forEach(function (v, k) { data[k] = v; });
      send.disabled = true; say('Sending…');
      fetch('/wp-json/baba/v1/quote', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
        .then(function (r) { if (!r.ok) throw new Error(r.status); form.reset(); say('Quote request sent. We will be in touch soon.', 'ok'); })
        .catch(function () { say('Your request did not send. Try again, or call 0449 824 153.', 'err'); })
        .then(function () { send.disabled = false; });
    });
  }
})();
