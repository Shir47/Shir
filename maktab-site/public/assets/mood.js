/* Seasons of the Shia calendar: the site celebrates around a birth or Eid and mourns around a martyrdom,
   for each of the Fourteen Masoomeen (AS). Needs people.js (MZP) and app.js (MZA).
   Preview with ?mood=<hijri month>-<day>, for example ?mood=6-3, or ?mood=off. */
(function(){
  var A=window.MZA,D=window.MZP;if(!A||!D)return;
  var fa=A.fa,fd=A.fd,now=A.now,EV=D.EV,P=D.P;
  function byKey(key){for(var i=0;i<EV.length;i++)if(EV[i][0]+'-'+EV[i][1]===key)return EV[i];return null}
  function find(){
    var ks=[0,1,-1,2,-2,3,4,5,6,7,8,9];
    for(var i=0;i<ks.length;i++){var k=ks[i],g=A.addDays(now.y,now.m,now.d,k),h=MZ.hijri(g.y,g.m,g.d),e=byKey(h.m+'-'+h.d);
      if(e&&e[4]&&k<=e[6]&&-k<=e[7])return {e:e,k:k}}
    return null}
  var q=(location.search.match(/[?&]mood=([a-z0-9-]+)/)||[])[1],cur;
  if(q==='off')return;
  var alias={mourn:'6-3',fatimah:'6-20',joy:'6-20',ali:'7-13',ashura:'1-10'};
  if(q){var e0=byKey(alias[q]||q);if(e0&&e0[4])cur={e:e0,k:0}}
  if(!cur)cur=find();
  if(!cur)return;
  var e=cur.e,k=cur.k,joy=e[4]==='j',name=fa?e[3]:e[2],p=e[5]>=0?P[e[5]]:null,html=document.documentElement;
  var big=p?p[4]:'عيد مبارك',salam=p?p[5]:'اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَآلِ مُحَمَّد',tone=p?p[6]:'gold';
  var eid=e[5]<0||(e[0]===12&&e[1]===18);
  html.classList.add(joy?'mood-joy':'mood-mourn');html.classList.add('tone-'+tone);
  if(!joy&&e[0]===1)html.classList.add('mood-muharram');
  var when=k>1?(fa?fd(k)+' روز دیگر':'in '+k+' days'):k===1?(fa?'فردا':'tomorrow'):k===0?(fa?'امروز':'today'):(fa?'این هفته':'this week');
  var title=joy?(fa?(eid?'عید مبارک':'میلاد مبارک'):(eid?'Eid Mubarak':'Wiladat Mubarak')):(fa?'تسلیت':'With sorrow we remember');
  var line=joy?(fa?'این روز خجسته بر شما و خانواده‌تان مبارک باد.':'Blessings to you and your family on this joyful occasion.')
              :(fa?'این مصیبت را به شما تسلیت می‌گوییم.':'Our condolences to you and your family.');
  var star='<svg width="14" height="14" viewBox="0 0 20 20"><path d="M10 0l2.6 6.2L19 7.4l-4.6 4.5 1.2 6.6L10 15.3 4.4 18.5l1.2-6.6L1 7.4l6.4-1.2z" fill="currentColor"/></svg>';
  var base=(document.querySelector('nav .l img')||{}).src||'';base=base.replace(/logo-288\.png.*$/,'');

  /* 1. a bar across the top of every page */
  var bar=document.createElement('a');bar.className='moodbar';bar.href='/'+(fa?'fa':'en')+'/masoomeen/';
  var nightTxt='';
  if(!joy&&e[0]===1&&e[1]===10&&k>0){var n=10-k;nightTxt=fa?('شب '+fd(n)+' محرم. '):('Night '+n+' of Muharram. ')}
  bar.innerHTML=(joy?star:'')+'<span>'+nightTxt+'<b>'+name+'</b>, '+when+'. '+(joy?title+'.':line)+'</span>'+(joy?star:'');
  document.body.insertBefore(bar,document.body.firstChild);

  /* in mourning, an embroidered banner band like the ones hung in a hussainiya: black cloth, crimson and green panels, gold thread */
  function band(){
    var w=440,h=58,s='<svg class="katibeh" width="100%" height="'+h+'" aria-hidden="true"><defs><pattern id="mzk" width="'+w+'" height="'+h+'" patternUnits="userSpaceOnUse">'
      +'<rect width="'+w+'" height="'+h+'" fill="#0b0607"/><path d="M0 4H'+w+'M0 '+(h-4)+'H'+w+'" stroke="#c9a24b" stroke-width="1.2" stroke-dasharray="1 5" stroke-linecap="round"/>';
    function cart(x,fill){return '<path d="M'+(x+22)+' 10h126q14 0 22 19q-8 19-22 19h-126q-14 0-22-19q8-19 22-19z" fill="'+fill+'" stroke="#c9a24b" stroke-width="1.4"/>'
      +'<text x="'+(x+85)+'" y="38" text-anchor="middle" font-family="Aref Ruqaa,Amiri,serif" font-size="25" fill="#fbf1dc" direction="rtl">'+big+'</text>'}
    function star(x){var pts='',i,a,r;for(i=0;i<16;i++){a=i*Math.PI/8;r=i%2?5.5:12;pts+=(x+r*Math.cos(a)).toFixed(1)+','+(29+r*Math.sin(a)).toFixed(1)+' '}
      return '<polygon points="'+pts+'" fill="none" stroke="#c9a24b" stroke-width="1.3"/><circle cx="'+x+'" cy="29" r="2.4" fill="#c9a24b"/>'}
    s+=cart(4,'var(--k1,#7d0f15)')+star(197)+cart(224,'var(--k2,#0d4a2c)')+star(417);
    return s+'</pattern></defs><rect width="100%" height="'+h+'" fill="url(#mzk)"/></svg>'}
  if(!joy){var kb=document.createElement('div');kb.className='katibehwrap';kb.innerHTML=band();bar.parentNode.insertBefore(kb,bar.nextSibling)}

  /* 2. the home page hero speaks about the occasion */
  var pill=document.querySelector('.hero .pill');
  if(pill){pill.textContent=(joy?title+': ':'')+name;pill.classList.add('moodpill')}
  var art=document.querySelector('.hero .art');
  if(art&&joy){var g=document.createElement('div');g.className='garland';g.innerHTML=new Array(12).join('<i></i>');art.appendChild(g)}
  if(art){var cg=document.createElement('div');cg.className='artname';cg.textContent=big;art.appendChild(cg)}

  /* 3. a full-screen greeting when you arrive, once per visit */
  var still=matchMedia('(prefers-reduced-motion:reduce)').matches,seen=false,key=e[0]+'-'+e[1];
  try{seen=sessionStorage.getItem('mz-mood')===key}catch(x){}
  if(location.search.indexOf('static')>-1)seen=true;else if(q)seen=false;
  var PAL={rose:['#f3c0cf','#e9c765','#fbe9ee','#f3dc98','#e59ab3'],gold:['#e9c765','#f3dc98','#fff3c9','#c9a24b','#ffe9a8'],green:['#bfe0cb','#e9c765','#f3dc98','#8fd0a8','#fff3c9']};
  function petals(host,ms){
    if(still)return;var c=document.createElement('canvas');c.className='petals';host.appendChild(c);
    var x=c.getContext('2d'),W=c.width=host.clientWidth,H=c.height=host.clientHeight,L=[],t0=Date.now(),cols=PAL[tone]||PAL.gold;
    for(var i=0;i<(W<700?46:90);i++)L.push({x:Math.random()*W,y:-Math.random()*H,r:5+Math.random()*8,s:1+Math.random()*2.2,a:Math.random()*6,w:.02+Math.random()*.04,c:cols[i%cols.length]});
    (function tick(){var t=Date.now()-t0,fade=t>ms-1200?Math.max(0,(ms-t)/1200):1;x.clearRect(0,0,W,H);x.globalAlpha=fade;
      L.forEach(function(o){o.y+=o.s;o.a+=o.w;o.x+=Math.sin(o.a)*1.2;if(o.y>H+20){o.y=-20;o.x=Math.random()*W}
        x.save();x.translate(o.x,o.y);x.rotate(o.a);x.fillStyle=o.c;x.beginPath();x.ellipse(0,0,o.r,o.r*.55,0,0,6.3);x.fill();x.restore()});
      if(t<ms)requestAnimationFrame(tick);else c.remove()})()}
  function candles(){
    var W=1440,s='<svg class="candles" viewBox="0 0 '+W+' 300" preserveAspectRatio="xMidYMax slice"><defs><radialGradient id="mzh"><stop offset="0" stop-color="rgba(255,196,96,.7)"/><stop offset=".4" stop-color="rgba(255,160,60,.22)"/><stop offset="1" stop-color="rgba(255,160,60,0)"/></radialGradient><linearGradient id="mzf" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#ff9a2e"/><stop offset=".5" stop-color="#ffd27a"/><stop offset="1" stop-color="#fff6dc"/></linearGradient><linearGradient id="mzw" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8f7a60"/><stop offset=".5" stop-color="#e9dcc4"/><stop offset="1" stop-color="#7d6a52"/></linearGradient></defs>',seed=7;
    var r=function(){seed=seed*16807%2147483647;return seed/2147483647};
    for(var i=0;i<34;i++){var x=20+i*42+r()*16,h=40+r()*100,w=15+r()*9,top=300-h,sc=.8+r()*.5,cx=x+w/2,fy=top-8;
      s+='<circle cx="'+cx+'" cy="'+(top-22)+'" r="'+(64*sc)+'" fill="url(#mzh)"/><rect x="'+x+'" y="'+top+'" width="'+w+'" height="'+(h+4)+'" rx="3" fill="url(#mzw)"/><rect x="'+(cx-1)+'" y="'+(top-7)+'" width="2" height="8" fill="#2a1702"/>'
        +'<path class="fl" style="animation-delay:'+(r()*2).toFixed(2)+'s" d="M'+cx+' '+(fy-30*sc)+' C '+(cx+9*sc)+' '+(fy-12*sc)+', '+(cx+7*sc)+' '+fy+', '+cx+' '+fy+' C '+(cx-7*sc)+' '+fy+', '+(cx-9*sc)+' '+(fy-12*sc)+', '+cx+' '+(fy-30*sc)+'Z" fill="url(#mzf)"/>'}
    return s+'</svg>'}
  if(!seen){
    try{sessionStorage.setItem('mz-mood',key)}catch(x){}
    var o=document.createElement('div');o.className='moodintro';
    o.innerHTML='<div class="mi-bg" style="background-image:url('+base+'cinematic-shrine.webp)"></div><div class="mi-sh"></div>'+(joy?'':candles())
      +'<div class="mi-in"><img src="'+base+'logo-288.png" alt=""><div class="mi-big">'+big+'</div><i class="mi-rule"></i><div class="mi-t">'+title+'</div><div class="mi-n">'+name+'</div>'
      +(p?'<div class="mi-s">'+(fa?p[3]:p[2])+'</div>':'')+'<div class="mi-ar">'+salam+'</div><div class="mi-w">'+when+'</div><p>'+line+'</p><button>'+(fa?'ورود به وب‌سایت':'Enter the website')+'</button></div>';
    document.body.appendChild(o);html.classList.add('menu-open');
    if(joy)petals(o,9000);
    var done=false,close=function(){if(done)return;done=true;o.classList.add('out');html.classList.remove('menu-open');setTimeout(function(){o.remove()},700);if(joy)petals(document.body,7000)};
    o.onclick=close;setTimeout(close,joy?6000:5500);
    requestAnimationFrame(function(){o.classList.add('on')});
  }
})();
