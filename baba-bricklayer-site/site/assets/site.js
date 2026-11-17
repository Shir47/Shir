(function () {
  var d = document, w = window, root = d.documentElement;
  var $ = function (s, c) { return (c || d).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); };
  var reduce = w.matchMedia('(prefers-reduced-motion: reduce)').matches;

  requestAnimationFrame(function () { requestAnimationFrame(function () { root.classList.add('loaded'); }); });
  var yr = d.getElementById('yr'); if (yr) yr.textContent = new Date().getFullYear();

  /* greeting by time of day */
  var greet = d.getElementById('greet');
  if (greet) { var h = new Date().getHours(); greet.textContent = h < 12 ? 'Good morning.' : h < 18 ? 'Good afternoon.' : 'Good evening.'; }

  /* mobile menu */
  var btn = $('.menu-btn'), nav = $('#nav');
  if (btn && nav) {
    var setMenu = function (open) { nav.classList.toggle('open', open); btn.setAttribute('aria-expanded', open ? 'true' : 'false'); };
    btn.addEventListener('click', function () { setMenu(!nav.classList.contains('open')); });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
  }

  /* scroll progress + back to top */
  var bar = $('.progress i'), top = $('.float-top'), ticking = false;
  var onScroll = function () {
    ticking = false;
    var max = root.scrollHeight - w.innerHeight;
    if (bar) bar.style.width = (max > 0 ? Math.min(100, w.scrollY / max * 100) : 0) + '%';
    if (top) top.classList.toggle('show', w.scrollY > 700);
  };
  w.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();
  if (top) top.addEventListener('click', function () { w.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); });

  /* hero photo panel */
  var imgs = $$('.slides img'), dots = $$('.dots button'), cap = d.getElementById('cap'), capTop = d.getElementById('cap-top'), cur = 0, timer;
  var go = function (n) {
    imgs[cur].classList.remove('on'); dots[cur] && dots[cur].classList.remove('on');
    cur = (n + imgs.length) % imgs.length;
    imgs[cur].classList.add('on'); dots[cur] && dots[cur].classList.add('on');
    var c = imgs[cur].getAttribute('data-cap'); if (cap) cap.textContent = c; if (capTop) capTop.textContent = c;
  };
  var play = function () { clearInterval(timer); if (!reduce && imgs.length > 1) timer = setInterval(function () { if (!d.hidden) go(cur + 1); }, 4800); };
  if (imgs.length) { dots.forEach(function (b, i) { b.addEventListener('click', function () { go(i); play(); }); }); play(); }

  /* reveal on scroll */
  $$('.sec h2,.sec .lede,.rows li,.also-h,.slash,.feat-shot,.feat-info>div,.tiles li,.cream-grid>div,.sticky,.stats li,.score,.ticks li,.steps li,.faq details,.quote-grid>*,.svc>*,.why li,.two-col>div,.ft-grid>div,.ft-sign,.sub-h').forEach(function (el) { el.classList.add('rv'); });
  var count = function (el) {
    var to = +el.getAttribute('data-count'), s = performance.now();
    (function f(t) { var p = Math.min(1, (t - s) / 1600); el.textContent = Math.round((1 - Math.pow(1 - p, 3)) * to); if (p < 1) requestAnimationFrame(f); })(s);
  };
  var targets = $$('.rv,.notes,.hline');
  if ('IntersectionObserver' in w) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target, i = el.parentNode ? Array.prototype.indexOf.call(el.parentNode.children, el) : 0;
        if (el.classList.contains('rv')) { el.style.transitionDelay = (Math.min(i, 5) * 70) + 'ms'; setTimeout(function () { el.style.transitionDelay = ''; }, 1400); }
        el.classList.add('in');
        if (!reduce) $$('[data-count]', el).forEach(count);
        io.unobserve(el);
      });
    }, { rootMargin: '0px 0px -7% 0px' });
    targets.forEach(function (el) { io.observe(el); });
  } else { targets.forEach(function (el) { el.classList.add('in'); }); }

  /* checklist */
  var ticks = $$('.ticks input'), score = d.getElementById('score'), msg = d.getElementById('score-msg'), box = $('.score');
  if (ticks.length && score) {
    var update = function () {
      var n = ticks.filter(function (t) { return t.checked; }).length;
      score.textContent = n;
      msg.textContent = n === 0 ? 'Tick anything that sounds familiar.' : n < 3 ? 'Worth having it looked at before it gets worse.' : 'Time to have it checked. Send us a few details and we will take a look.';
      box.classList.toggle('hot', n > 0);
    };
    ticks.forEach(function (t) { t.addEventListener('change', update); });
  }

  /* lightbox */
  var lb = $('.lightbox');
  if (lb && lb.showModal) {
    var lbImg = $('img', lb);
    $$('.tile').forEach(function (b) {
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
