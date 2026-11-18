(function () {
  var d = document, w = window, root = d.documentElement;
  var $ = function (s, c) { return (c || d).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); };
  var reduce = w.matchMedia('(prefers-reduced-motion: reduce)').matches;

  requestAnimationFrame(function () { requestAnimationFrame(function () { root.classList.add('loaded'); }); });
  var yr = d.getElementById('yr'); if (yr) yr.textContent = new Date().getFullYear();

  /* header */
  var hd = $('.hd');
  var onScroll = function () { if (hd) hd.classList.toggle('stuck', w.scrollY > 20); };
  w.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* mobile menu */
  var btn = $('.menu-btn'), nav = $('#nav');
  if (btn && nav) {
    var setMenu = function (open) { nav.classList.toggle('open', open); btn.setAttribute('aria-expanded', open ? 'true' : 'false'); };
    btn.addEventListener('click', function () { setMenu(!nav.classList.contains('open')); });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
  }

  /* services rail */
  var rail = $('.rail');
  if (rail) {
    var step = function (dir) { var c = $('.card', rail); rail.scrollBy({ left: dir * ((c ? c.offsetWidth : 280) + 24), behavior: reduce ? 'auto' : 'smooth' }); };
    var pv = $('.rail-prev'), nx = $('.rail-next');
    if (pv) pv.addEventListener('click', function () { step(-1); });
    if (nx) nx.addEventListener('click', function () { step(1); });
  }

  /* reveal on scroll + counters */
  $$('.head,.card,.signs-l,.signs li,.shots li,.about-grid>div,.steps li,.why li,.faq-grid>div,.quote-box,.svc>*,.two-col>div,.rail-foot,.after,.reviews-in>div').forEach(function (el) { el.classList.add('rv'); });
  var count = function (el) {
    var to = +el.getAttribute('data-count'), s = performance.now();
    (function f(t) { var p = Math.min(1, (t - s) / 1600); el.textContent = Math.round((1 - Math.pow(1 - p, 3)) * to); if (p < 1) requestAnimationFrame(f); })(s);
  };
  var targets = $$('.rv');
  if ('IntersectionObserver' in w) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target, i = el.parentNode ? Array.prototype.indexOf.call(el.parentNode.children, el) : 0;
        el.style.transitionDelay = (Math.min(i, 5) * 70) + 'ms';
        setTimeout(function () { el.style.transitionDelay = ''; }, 1400);
        el.classList.add('in');
        if (!reduce) $$('[data-count]', el).forEach(count);
        io.unobserve(el);
      });
    }, { rootMargin: '0px 0px -6% 0px' });
    targets.forEach(function (el) { io.observe(el); });
  } else { targets.forEach(function (el) { el.classList.add('in'); }); }

  /* project filter */
  var fbtns = $$('.filter button');
  fbtns.forEach(function (b) {
    b.addEventListener('click', function () {
      var f = b.getAttribute('data-f');
      fbtns.forEach(function (x) { x.classList.toggle('on', x === b); x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      $$('.shots li').forEach(function (li) { li.hidden = !!f && li.getAttribute('data-g') !== f; li.classList.add('in'); });
    });
  });

  /* lightbox */
  var lb = $('.lightbox');
  if (lb && lb.showModal) {
    var lbImg = $('img', lb);
    $$('.shot').forEach(function (b) {
      b.addEventListener('click', function () { var i = $('img', b); lbImg.src = i.currentSrc || i.src; lbImg.alt = i.alt; lb.showModal(); });
    });
    lb.addEventListener('click', function (e) { if (e.target === lb) lb.close(); });
  }

  /* quote forms: preselect job from ?job=, then submit */
  var want = new URLSearchParams(location.search).get('job');
  $$('.qform').forEach(function (form) {
    if (want) { var sel = form.elements.job; Array.prototype.forEach.call(sel.options, function (o) { if (o.text === want) sel.value = o.value || o.text; }); }
    var msgEl = $('.form-msg', form), send = $('button[type=submit]', form);
    var say = function (text, cls) { msgEl.textContent = text; msgEl.className = 'form-msg' + (cls ? ' ' + cls : ''); };
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
