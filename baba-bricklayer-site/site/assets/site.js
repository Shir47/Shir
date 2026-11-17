(function () {
  var d = document, w = window, root = d.documentElement;
  var $ = function (s, c) { return (c || d).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); };
  var reduce = w.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var clamp = function (v, a, b) { return Math.min(b, Math.max(a, v)); };

  /* page veil: lift on load, drop on internal navigation */
  var lift = function () { root.classList.remove('leaving'); root.classList.add('loaded'); };
  if (d.readyState === 'complete') setTimeout(lift, 150); else { w.addEventListener('load', function () { setTimeout(lift, 150); }); setTimeout(lift, 2500); }
  w.addEventListener('pageshow', function (e) { if (e.persisted) lift(); });
  if (!reduce) {
    d.addEventListener('click', function (e) {
      var a = e.target.closest('a[href]');
      if (!a || e.defaultPrevented || e.button || e.metaKey || e.ctrlKey || e.shiftKey || a.target === '_blank') return;
      var href = a.getAttribute('href');
      if (!href || href.charAt(0) === '#' || /^(tel:|mailto:)/.test(href)) return;
      var u; try { u = new URL(a.href); } catch (x) { return; }
      if (u.origin !== location.origin || (u.pathname === location.pathname && u.hash)) return;
      e.preventDefault();
      root.classList.add('leaving');
      setTimeout(function () { location.href = a.href; }, 300);
    });
  }

  var yr = d.getElementById('yr'); if (yr) yr.textContent = new Date().getFullYear();

  /* mobile menu */
  var btn = $('.menu-btn'), nav = $('#nav');
  if (btn && nav) {
    var setMenu = function (open) { nav.classList.toggle('open', open); btn.setAttribute('aria-expanded', open ? 'true' : 'false'); };
    btn.addEventListener('click', function () { setMenu(!nav.classList.contains('open')); });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
  }

  /* hero slider */
  var slides = $$('.slide'), dots = $$('.dots button'), cur = 0, timer;
  var go = function (n) {
    slides[cur].classList.remove('on'); dots[cur] && dots[cur].classList.remove('on');
    cur = (n + slides.length) % slides.length;
    slides[cur].classList.add('on'); dots[cur] && dots[cur].classList.add('on');
  };
  var play = function () { clearInterval(timer); if (!reduce && slides.length > 1) timer = setInterval(function () { go(cur + 1); }, 6500); };
  if (slides.length) {
    dots.forEach(function (b, i) { b.addEventListener('click', function () { go(i); play(); }); });
    play();
    d.addEventListener('visibilitychange', function () { if (d.hidden) clearInterval(timer); else play(); });
  }

  /* set up reveals */
  $$('.sec-head h2,.svc-body h2,.cta h2,.form-card h2').forEach(function (h) {
    h.innerHTML = '<span>' + h.innerHTML + '</span>'; h.classList.add('hm');
  });
  $$('.card-img,.svc-img,.shots:not(.rail) .shot,.intro-imgs .i1').forEach(function (el) {
    if (el.tagName === 'IMG') { var s = d.createElement('div'); s.className = 'wipe i1w'; el.parentNode.insertBefore(s, el); s.appendChild(el); }
    else el.classList.add('wipe');
  });
  $$('.sec-head .tag,.sec-head>p:not(.tag),.card-body,.why-grid li,.steps li,.svc-body>p,.svc-body .checks,.svc-body .btn,.intro-grid>div:last-child>p,.intro-grid .checks,.intro-grid .link,.intro-grid .btn,.stats li,.c-list li,.qform,.safety-grid>div>p,.faq-list details,.cta-in>p,.cta-btns,.rail li,.rail-foot,.badge,.footer-grid>div').forEach(function (el) { el.classList.add('rv'); });

  var count = function (el) {
    var to = +el.getAttribute('data-count'), s = performance.now();
    (function f(t) { var p = Math.min(1, (t - s) / 1900); el.textContent = Math.round((1 - Math.pow(1 - p, 4)) * to); if (p < 1) requestAnimationFrame(f); })(s);
  };
  var targets = $$('.rv,.hm,.wipe');
  if ('IntersectionObserver' in w) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target, i = el.parentNode ? Array.prototype.indexOf.call(el.parentNode.children, el) : 0;
        var grid = el.matches('.card-body,.card-img') ? Array.prototype.indexOf.call(el.closest('.cards').children, el.closest('.card')) % 3 : i;
        el.style.transitionDelay = (Math.min(grid, 6) * 90) + 'ms';
        el.classList.add('in');
        setTimeout(function () { el.style.transitionDelay = ''; }, 1800);
        if (!reduce) $$('[data-count]', el).forEach(count);
        io.unobserve(el);
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    targets.forEach(function (el) { io.observe(el); });
  } else { targets.forEach(function (el) { el.classList.add('in'); }); }

  /* scroll: header hide/show + parallax */
  var header = $('.header'), heroSlides = $('.slides'), i2 = $('.intro-imgs .i2'), ctaImg = $('.cta-bg img'), banner = $('.banner');
  var lastY = w.scrollY, ticking = false;
  var frame = function () {
    ticking = false;
    var y = w.scrollY, vh = w.innerHeight, dy = y - lastY; lastY = y;
    if (header && !(nav && nav.classList.contains('open'))) {
      if (dy > 6 && y > 400) header.classList.add('hide'); else if (dy < -6 || y < 400) header.classList.remove('hide');
    }
    if (reduce) return;
    if (heroSlides && y < vh * 1.2) heroSlides.style.transform = 'translate3d(0,' + (y * 0.28).toFixed(1) + 'px,0)';
    if (banner && y < vh) banner.style.backgroundPositionY = 'calc(50% + ' + (y * 0.25).toFixed(1) + 'px)';
    if (i2) { var r = i2.parentNode.getBoundingClientRect(); var p = clamp((vh - r.top) / (vh + r.height), 0, 1); i2.style.transform = 'translate3d(0,' + ((0.5 - p) * 90).toFixed(1) + 'px,0)'; }
    if (ctaImg) { var c = ctaImg.parentNode.getBoundingClientRect(); var q = clamp((vh - c.top) / (vh + c.height), 0, 1); ctaImg.style.transform = 'translate3d(0,' + ((q - 0.5) * 16).toFixed(2) + '%,0)'; }
  };
  w.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(frame); } }, { passive: true });
  frame();

  /* project rail: arrows + drag */
  var rail = $('.rail');
  if (rail) {
    var step = function (dir) { var li = $('li', rail); rail.scrollBy({ left: dir * ((li ? li.offsetWidth : 400) + 24), behavior: reduce ? 'auto' : 'smooth' }); };
    var pv = $('.rail-prev'), nx = $('.rail-next');
    if (pv) pv.addEventListener('click', function () { step(-1); });
    if (nx) nx.addEventListener('click', function () { step(1); });
    var down = false, sx = 0, sl = 0, moved = 0;
    rail.addEventListener('pointerdown', function (e) { if (e.pointerType !== 'mouse') return; down = true; moved = 0; sx = e.clientX; sl = rail.scrollLeft; });
    w.addEventListener('pointermove', function (e) { if (!down) return; var dx = e.clientX - sx; moved = Math.max(moved, Math.abs(dx)); if (moved > 6) { rail.classList.add('drag'); rail.scrollLeft = sl - dx; } });
    w.addEventListener('pointerup', function () { if (!down) return; down = false; setTimeout(function () { rail.classList.remove('drag'); }, 0); });
    rail.addEventListener('click', function (e) { if (moved > 6) { e.stopPropagation(); e.preventDefault(); } }, true);
    rail.addEventListener('dragstart', function (e) { e.preventDefault(); });
  }

  /* lightbox */
  var lb = $('.lightbox');
  if (lb && lb.showModal) {
    var lbImg = $('img', lb);
    $$('.shot').forEach(function (b) {
      b.addEventListener('click', function () { var i = $('img', b); lbImg.src = i.currentSrc || i.src; lbImg.alt = i.alt; lb.showModal(); });
    });
    lb.addEventListener('click', function (e) { if (e.target === lb) lb.close(); });
  }

  /* quote forms */
  $$('.qform').forEach(function (form) {
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
  });
})();
