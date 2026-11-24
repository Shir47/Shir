/* Special days of the Shia calendar, for each of the Fourteen Masoomeen (AS).
   The website itself never changes colour. A special day adds only two things:
   a slim bar at the top of every page, and a greeting screen once per visit.
   Needs people.js (MZP) and app.js (MZA). Preview with ?mood=<hijri month>-<day>, e.g. ?mood=6-3, or ?mood=off. */
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
  var e=cur.e,k=cur.k,joy=e[4]==='j',name=fa?e[3]:e[2],p=e[5]>=0?P[e[5]]:null;
  var big=p?p[4]:'عِيدٌ مُبَارَك',salam=p?p[5]:'اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَآلِ مُحَمَّد';
  var eid=e[5]<0||(e[0]===12&&e[1]===18);
  var when=k>1?(fa?fd(k)+' روز دیگر':'in '+k+' days'):k===1?(fa?'فردا':'tomorrow'):k===0?(fa?'امروز':'today'):(fa?'این هفته':'this week');
  var title=joy?(fa?(eid?'عید مبارک':'میلاد مبارک'):(eid?'Eid Mubarak':'Wiladat Mubarak')):(fa?'تسلیت':'With sorrow we remember');
  var line=joy?(fa?'این روز خجسته بر شما و خانواده‌تان مبارک باد.':'Blessings to you and your family on this joyful occasion.')
              :(fa?'این مصیبت را به شما تسلیت می‌گوییم.':'Our condolences to you and your family.');
  var base=(document.querySelector('nav .l img')||{}).src||'';base=base.replace(/logo-160\.webp.*$/,'');
  var cls=joy?'joy':'mourn';

  /* 1. a slim bar at the top of every page */
  var bar=document.createElement('a');bar.className='moodbar '+cls;bar.href='/'+(fa?'fa':'en')+'/masoomeen/';
  var nightTxt='';
  if(!joy&&e[0]===1&&e[1]===10&&k>0){var n=10-k;nightTxt=fa?('شب '+fd(n)+' محرم. '):('Night '+n+' of Muharram. ')}
  bar.innerHTML='<i></i><span>'+nightTxt+'<b>'+name+'</b>, '+when+'. '+(joy?title+'.':line)+'</span><i></i>';
  document.body.insertBefore(bar,document.body.firstChild);

  /* 2. a greeting screen when you arrive, once per visit */
  var seen=false,key=e[0]+'-'+e[1];
  try{seen=sessionStorage.getItem('mz-mood')===key}catch(x){}
  if(location.search.indexOf('static')>-1)seen=true;else if(q)seen=false;
  if(seen)return;
  try{sessionStorage.setItem('mz-mood',key)}catch(x){}
  var o=document.createElement('div');o.className='moodintro '+cls;o.setAttribute('role','dialog');o.setAttribute('aria-label',name);
  o.innerHTML='<div class="mi-bg" style="background-image:url('+base+'shrine-1200.webp)"></div><div class="mi-sh"></div>'
    +'<div class="mi-in"><img src="'+base+'logo-160.webp" alt=""><div class="mi-k">'+title+'</div><div class="mi-big" lang="ar">'+big+'</div><i class="mi-rule"></i>'
    +'<div class="mi-n">'+name+'</div>'+(p?'<div class="mi-s">'+(fa?p[3]:p[2])+'</div>':'')
    +'<div class="mi-ar" lang="ar">'+salam+'</div><p>'+line+'</p><button>'+(fa?'ورود به وب‌سایت':'Enter the website')+'</button><div class="mi-w">'+when+'</div></div>';
  document.body.appendChild(o);
  var html=document.documentElement;html.classList.add('menu-open');
  var done=false,close=function(){if(done)return;done=true;o.classList.add('out');html.classList.remove('menu-open');setTimeout(function(){o.remove()},800)};
  o.onclick=close;setTimeout(close,6500);
  document.addEventListener('keydown',function(ev){if(ev.key==='Escape')close()});
  requestAnimationFrame(function(){o.classList.add('on')});
})();
