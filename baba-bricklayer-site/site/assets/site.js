(function () {
  var d = document;
  d.documentElement.classList.add('js');

  // Lay the headline wall once the page is ready.
  var wall = d.querySelector('.wall');
  if (wall) requestAnimationFrame(function () { requestAnimationFrame(function () { wall.classList.add('laid'); }); });

  var yr = d.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();

  // Mobile menu
  var btn = d.querySelector('.menu-btn'), nav = d.getElementById('nav');
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

  // Photo lightbox
  var lb = d.querySelector('.lightbox');
  if (lb && lb.showModal) {
    var lbImg = lb.querySelector('img');
    d.querySelectorAll('.shot').forEach(function (b) {
      b.addEventListener('click', function () {
        var i = b.querySelector('img');
        lbImg.src = i.currentSrc || i.src;
        lbImg.alt = i.alt;
        lb.showModal();
      });
    });
    lb.addEventListener('click', function (e) { if (e.target === lb) lb.close(); });
  }

  // Quote form
  var form = d.getElementById('quote-form');
  if (form) {
    var msg = form.querySelector('.form-msg'), send = form.querySelector('button[type=submit]');
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
      if (firstBad) {
        say('Add your name, phone, a valid email and a few words about the job.', 'err');
        firstBad.focus();
        return;
      }
      var data = {};
      new FormData(form).forEach(function (v, k) { data[k] = v; });
      send.disabled = true;
      say('Sending…');
      fetch('/wp-json/baba/v1/quote', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      }).then(function (r) {
        if (!r.ok) throw new Error(r.status);
        form.reset();
        say('Quote request sent. We will be in touch soon.', 'ok');
      }).catch(function () {
        say('Your request did not send. Try again, or call 0449 824 153.', 'err');
      }).then(function () { send.disabled = false; });
    });
  }
})();
