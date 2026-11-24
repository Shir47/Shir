/* Seasons of the Shia calendar: the site celebrates around a birth or Eid and mourns around a martyrdom.
   Needs app.js (window.MZA). Preview any mood with ?mood=fatimah, ?mood=ali, ?mood=mourn or ?mood=off. */
(function(){
  var A=window.MZA;if(!A)return;
  var fa=A.fa,fd=A.fd,now=A.now;
  /* Hijri month-day: [mood, days before, days after, Arabic salutation, petal colour] */
  var META={
    '1-10':['m',9,2,'السَّلَامُ عَلَيْكَ يَا أَبَا عَبْدِ اللَّهِ الْحُسَيْن'],
    '2-20':['m',3,1,'السَّلَامُ عَلَيْكَ يَا أَبَا عَبْدِ اللَّهِ الْحُسَيْن'],
    '2-28':['m',3,1,'السَّلَامُ عَلَيْكَ يَا رَسُولَ اللَّه'],
    '3-17':['j',7,1,'اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَآلِ مُحَمَّد'],
    '5-13':['m',3,1,'السَّلَامُ عَلَيْكِ يَا فَاطِمَةُ الزَّهْرَاء'],
    '6-3':['m',3,1,'السَّلَامُ عَلَيْكِ يَا فَاطِمَةُ الزَّهْرَاء'],
    '6-20':['j',7,1,'السَّلَامُ عَلَيْكِ يَا فَاطِمَةُ الزَّهْرَاء','rose'],
    '7-13':['j',7,1,'السَّلَامُ عَلَيْكَ يَا أَمِيرَ الْمُؤْمِنِين'],
    '7-27':['j',3,1,'اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَآلِ مُحَمَّد'],
    '8-3':['j',5,1,'السَّلَامُ عَلَيْكَ يَا أَبَا عَبْدِ اللَّهِ الْحُسَيْن'],
    '8-15':['j',7,1,'السَّلَامُ عَلَيْكَ يَا صَاحِبَ الزَّمَان'],
    '9-21':['m',3,1,'السَّلَامُ عَلَيْكَ يَا أَمِيرَ الْمُؤْمِنِين'],
    '10-1':['j',2,2,'عِيدٌ مُبَارَك'],
    '12-10':['j',2,2,'عِيدٌ مُبَارَك'],
    '12-18':['j',5,1,'السَّلَامُ عَلَيْكَ يَا أَمِيرَ الْمُؤْمِنِين']
  };
  function nameOf(key){for(var i=0;i<A.EV.length;i++)if(A.EV[i][0]+'-'+A.EV[i][1]===key)return fa?A.EV[i][3]:A.EV[i][2];return ''}
  function find(){
    var ks=[0,1,-1,2,-2,3,4,5,6,7,8,9];
    for(var i=0;i<ks.length;i++){var k=ks[i],g=A.addDays(now.y,now.m,now.d,k),h=MZ.hijri(g.y,g.m,g.d),key=h.m+'-'+h.d,m=META[key];
      if(m&&k<=m[1]&&-k<=m[2])return {key:key,k:k}}
    return null}
  var q=(location.search.match(/[?&]mood=([a-z]+)/)||[])[1],cur;
  if(q==='off')return;
  if(q==='mourn')cur={key:'6-3',k:0};else if(q==='ali')cur={key:'7-13',k:0};else if(q==='fatimah'||q==='joy')cur={key:'6-20',k:0};else cur=find();
  if(!cur)return;
  var m=META[cur.key],joy=m[0]==='j',name=nameOf(cur.key),k=cur.k,html=document.documentElement;
  html.classList.add(joy?'mood-joy':'mood-mourn');if(m[4])html.classList.add('mood-'+m[4]);
  var when=k>1?(fa?fd(k)+' روز دیگر':'in '+k+' days'):k===1?(fa?'فردا':'tomorrow'):k===0?(fa?'امروز':'today'):(fa?'این هفته':'this week');
  var title=joy?(fa?'میلاد مبارک':(cur.key==='10-1'||cur.key==='12-10'||cur.key==='12-18'?'Eid Mubarak':'Wiladat Mubarak')):(fa?'تسلیت':'With sorrow we remember');
  var line=joy?(fa?'این روز خجسته بر شما و خانواده‌تان مبارک باد.':'Blessings to you and your family on this joyful occasion.')
              :(fa?'این مصیبت را به شما تسلیت می‌گوییم.':'Our condolences to you and your family.');
  var star='<svg width="14" height="14" viewBox="0 0 20 20"><path d="M10 0l2.6 6.2L19 7.4l-4.6 4.5 1.2 6.6L10 15.3 4.4 18.5l1.2-6.6L1 7.4l6.4-1.2z" fill="currentColor"/></svg>';

  /* 1. a bar across the top of every page */
  var bar=document.createElement('a');bar.className='moodbar';bar.href='/'+(fa?'fa':'en')+'/calendar/';
  bar.innerHTML=(joy?star:'')+'<span><b>'+name+'</b>, '+when+'. '+(joy?title+'.':line)+'</span>'+(joy?star:'');
  document.body.insertBefore(bar,document.body.firstChild);

  /* 2. the home page hero speaks about the occasion */
  var pill=document.querySelector('.hero .pill');
  if(pill){pill.textContent=(joy?title+': ':'')+name;pill.classList.add('moodpill')}
  var art=document.querySelector('.hero .art');
  if(art&&joy){var g=document.createElement('div');g.className='garland';g.innerHTML=new Array(12).join('<i></i>');art.appendChild(g)}

  /* 3. a greeting when you arrive, once per visit */
  var still=matchMedia('(prefers-reduced-motion:reduce)').matches,seen=false;
  try{seen=sessionStorage.getItem('mz-mood')===cur.key+joy}catch(e){}
  if(location.search.indexOf('static')>-1)seen=true;
  if(q&&location.search.indexOf('static')<0)seen=false;
  function petals(host,ms){
    if(still)return;var c=document.createElement('canvas');c.className='petals';host.appendChild(c);
    var x=c.getContext('2d'),W,H,P=[],t0=Date.now(),cols=m[4]==='rose'?['#f3c0cf','#e9c765','#fbe9ee','#f3dc98','#e59ab3']:['#e9c765','#f3dc98','#fff3c9','#c9a24b','#bfe0cb'];
    function size(){W=c.width=host.clientWidth;H=c.height=host.clientHeight}size();
    for(var i=0;i<(W<700?46:90);i++)P.push({x:Math.random()*W,y:-Math.random()*H,r:5+Math.random()*8,s:1+Math.random()*2.2,a:Math.random()*6,w:.02+Math.random()*.04,c:cols[i%cols.length]});
    (function tick(){var e=Date.now()-t0,fade=e>ms-1200?Math.max(0,(ms-e)/1200):1;x.clearRect(0,0,W,H);x.globalAlpha=fade;
      P.forEach(function(p){p.y+=p.s;p.a+=p.w;p.x+=Math.sin(p.a)*1.2;if(p.y>H+20){p.y=-20;p.x=Math.random()*W}
        x.save();x.translate(p.x,p.y);x.rotate(p.a);x.fillStyle=p.c;x.beginPath();x.ellipse(0,0,p.r,p.r*.55,0,0,6.3);x.fill();x.restore()});
      if(e<ms)requestAnimationFrame(tick);else c.remove()})()}
  if(!seen){
    try{sessionStorage.setItem('mz-mood',cur.key+joy)}catch(e){}
    var o=document.createElement('div');o.className='moodintro';
    o.innerHTML='<div class="mi-in"><img src="'+(document.querySelector('nav .l img')||{}).src+'" alt=""><div class="mi-ar">'+m[3]+'</div><div class="mi-t">'+title+'</div><div class="mi-n">'+name+'</div><div class="mi-w">'+when+'</div><p>'+line+'</p><button>'+(fa?'ورود به وب‌سایت':'Enter the website')+'</button></div>';
    document.body.appendChild(o);html.classList.add('menu-open');
    if(joy)petals(o,9000);
    var done=false,close=function(){if(done)return;done=true;o.classList.add('out');html.classList.remove('menu-open');setTimeout(function(){o.remove()},700);if(joy)petals(document.body,7000)};
    o.onclick=close;setTimeout(close,joy?5200:4200);
    requestAnimationFrame(function(){o.classList.add('on')});
  }
})();
