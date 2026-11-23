/* Maktab Alzahra SA: live prayer times, Hijri dates, countdowns, calendar. Needs calc.js (MZ). */
(function(){
  var fa=document.documentElement.lang==='fa';
  var $=function(s,c){return (c||document).querySelector(s)},$$=function(s,c){return [].slice.call((c||document).querySelectorAll(s))};
  var fd=function(v){v=String(v);return fa?v.replace(/[0-9]/g,function(d){return '۰۱۲۳۴۵۶۷۸۹'[d]}):v};
  var ad=function(v){return String(v).replace(/[0-9]/g,function(d){return '٠١٢٣٤٥٦٧٨٩'[d]})};
  var WD=fa?['یکشنبه','دوشنبه','سه‌شنبه','چهارشنبه','پنجشنبه','جمعه','شنبه']:['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
  var WDS=fa?['دو','سه','چهار','پنج','جمعه','شنبه','یک']:['Mon','Tue','Wed','Thu','Fri','Sat','Sun'];
  var MO=fa?['جنوری','فبروری','مارچ','اپریل','می','جون','جولای','اگست','سپتمبر','اکتوبر','نومبر','دسمبر']:['January','February','March','April','May','June','July','August','September','October','November','December'];
  var HM=fa?['محرم','صفر','ربیع‌الاول','ربیع‌الثانی','جمادی‌الاول','جمادی‌الثانی','رجب','شعبان','رمضان','شوال','ذی‌القعده','ذی‌الحجه']:['Muharram','Safar','Rabi I','Rabi II','Jumada I','Jumada II','Rajab','Sha‘ban','Ramadan','Shawwal','Dhu al-Qa‘dah','Dhu al-Hijjah'];
  var HMA=['محرم','صفر','ربيع الأول','ربيع الثاني','جمادى الأولى','جمادى الثانية','رجب','شعبان','رمضان','شوال','ذو القعدة','ذو الحجة'];
  var PN=fa?{fajr:'صبح',sunrise:'طلوع',dhuhr:'ظهر',asr:'عصر',sunset:'غروب',maghrib:'مغرب',isha:'عشا'}:{fajr:'Fajr',sunrise:'Sunrise',dhuhr:'Dhuhr',asr:'Asr',sunset:'Sunset',maghrib:'Maghrib',isha:'Isha'};
  var TX=fa?{next:'بعدی',nextPrayer:'نماز بعدی',tomorrow:'فردا',days:'روز مانده',today:'امروز',date:'تاریخ',copied:'کپی شد',ah:'هجری قمری',none:'در این ماه مناسبتی در این فهرست نیست.',prev:'ماه قبل',nextM:'ماه بعد'}
              :{next:'next',nextPrayer:'Next prayer',tomorrow:'tomorrow',days:'days to go',today:'Today',date:'Date',copied:'Copied',ah:'AH',none:'No observances from this selection fall in this month.',prev:'Previous',nextM:'Next'};
  /* Selected Shia observances by Hijri month and day. Dates are calculated and provisional. */
  var EV=[
    [1,1,'Islamic New Year','آغاز سال نو هجری'],[1,10,'Ashura, martyrdom of Imam Husayn (AS)','عاشورا، شهادت امام حسین (ع)'],
    [2,20,'Arbaeen of Imam Husayn (AS)','اربعین امام حسین (ع)'],[2,28,'Passing of Prophet Muhammad (S)','رحلت پیامبر اکرم (ص)'],
    [3,17,'Birth of Prophet Muhammad (S) and Imam al-Sadiq (AS)','ولادت پیامبر اکرم (ص) و امام صادق (ع)'],
    [5,13,'Martyrdom of Lady Fatimah (AS), first narration','شهادت حضرت فاطمه (س)، روایت اول'],
    [6,3,'Martyrdom of Lady Fatimah (AS), second narration','شهادت حضرت فاطمه (س)، روایت دوم'],
    [6,20,'Birth of Lady Fatimah al-Zahra (AS)','ولادت حضرت فاطمه زهرا (س)'],
    [7,13,'Birth of Imam Ali (AS)','ولادت امام علی (ع)'],[7,27,'Mab‘ath of Prophet Muhammad (S)','مبعث پیامبر اکرم (ص)'],
    [8,3,'Birth of Imam Husayn (AS)','ولادت امام حسین (ع)'],[8,15,'Birth of Imam al-Mahdi (AJ)','ولادت امام مهدی (عج)'],
    [9,1,'First day of Ramadan','آغاز ماه رمضان'],[9,21,'Martyrdom of Imam Ali (AS)','شهادت امام علی (ع)'],
    [10,1,'Eid al-Fitr','عید فطر'],[12,10,'Eid al-Adha','عید قربان'],[12,18,'Eid al-Ghadir','عید غدیر']
  ];
  var evOn=function(h){for(var i=0;i<EV.length;i++)if(EV[i][0]===h.m&&EV[i][1]===h.d)return fa?EV[i][3]:EV[i][2];return null};
  var addDays=function(y,m,d,n){var t=new Date(Date.UTC(y,m-1,d+n,12));return {y:t.getUTCFullYear(),m:t.getUTCMonth()+1,d:t.getUTCDate(),wd:t.getUTCDay()}};
  var hText=function(h){return fd(h.d)+' '+HM[h.m-1]+' '+fd(h.y)};

  var now=MZ.now(),T=MZ.times(now.y,now.m,now.d),nowMin=now.h*60+now.mi,H=MZ.hijri(now.y,now.m,now.d);
  var order=['fajr','dhuhr','asr','maghrib','isha'],nextKey=null;
  for(var i=0;i<order.length;i++)if(T[order[i]].min>nowMin){nextKey=order[i];break}
  var tomorrow=!nextKey,nextTime;
  if(tomorrow){var tm=addDays(now.y,now.m,now.d,1);nextKey='fajr';nextTime=MZ.times(tm.y,tm.m,tm.d).fajr.text}else nextTime=T[nextKey].text;

  $$('[data-pray]').forEach(function(e){var k=e.getAttribute('data-pray');e.textContent=fd(k===nextKey&&tomorrow?nextTime:T[k].text);
    var box=e.closest('.pt,.p');if(box){box.classList.toggle('next',k===nextKey);var lab=$('[data-label]',box);if(lab)lab.textContent=PN[k]+(k===nextKey?(fa?'، ':', ')+(tomorrow?TX.tomorrow:TX.next):'')}});
  $$('[data-next-name]').forEach(function(e){e.textContent=TX.nextPrayer+(fa?'، ':', ')+PN[nextKey]});
  $$('[data-next-time]').forEach(function(e){e.textContent=fd(nextTime)});
  $$('[data-today]').forEach(function(e){e.textContent=WD[now.wd]+(fa?' ':' ')+fd(now.d)+' '+MO[now.m-1]});
  $$('[data-hijri]').forEach(function(e){e.textContent=hText(H)+' '+TX.ah});
  $$('[data-hijri-ar]').forEach(function(e){e.textContent=ad(H.d)+' '+HMA[H.m-1]+' '+ad(H.y)});

  /* upcoming observances with countdowns */
  var up=$('[data-upcoming]');
  if(up){var n=+up.getAttribute('data-upcoming')||2,html='',found=0;
    for(var k=1;k<400&&found<n;k++){var g=addDays(now.y,now.m,now.d,k),h=MZ.hijri(g.y,g.m,g.d),nm=evOn(h);
      if(nm){found++;html+='<div class="occ'+(found>1?' n':'')+'"><div class="d"><b>'+fd(g.d)+'</b><span>'+MO[g.m-1]+'</span></div><div><h4>'+nm+'</h4><p>'+hText(h)+'</p></div><div class="cd"><b>'+fd(k)+'</b><span>'+TX.days+'</span></div></div>'}}
    up.innerHTML=html}

  /* ayah of the day (rotates through the week) */
  var AY=[['رَّبِّ زِدْنِي عِلْمًا','“My Lord, increase me in knowledge.”','«پروردگارا، بر دانشم بیفزا.»','Surah Taha 20:114','سوره طه، آیه ۱۱۴'],
    ['إِنَّ مَعَ الْعُسْرِ يُسْرًا','“Indeed, with hardship comes ease.”','«بی‌گمان با سختی آسانی است.»','Surah al-Sharh 94:6','سوره شرح، آیه ۶'],
    ['فَاذْكُرُونِي أَذْكُرْكُمْ','“So remember Me; I will remember you.”','«پس مرا یاد کنید تا شما را یاد کنم.»','Surah al-Baqarah 2:152','سوره بقره، آیه ۱۵۲'],
    ['أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ','“Surely in the remembrance of Allah do hearts find rest.”','«آگاه باشید، دل‌ها تنها با یاد خدا آرام می‌گیرد.»','Surah al-Ra‘d 13:28','سوره رعد، آیه ۲۸'],
    ['إِنَّ اللَّهَ مَعَ الصَّابِرِينَ','“Indeed, Allah is with the patient.”','«بی‌گمان خدا با شکیبایان است.»','Surah al-Baqarah 2:153','سوره بقره، آیه ۱۵۳'],
    ['اقْرَأْ بِاسْمِ رَبِّكَ الَّذِي خَلَقَ','“Read in the name of your Lord who created.”','«بخوان به نام پروردگارت که آفرید.»','Surah al-‘Alaq 96:1','سوره علق، آیه ۱'],
    ['هَلْ جَزَاءُ الْإِحْسَانِ إِلَّا الْإِحْسَانُ','“Is the reward for good anything but good?”','«آیا پاداش نیکی جز نیکی است؟»','Surah al-Rahman 55:60','سوره الرحمن، آیه ۶۰']];
  var ay=$('[data-ayah]');
  if(ay){var a=AY[now.wd];$('.ar',ay).textContent=a[0];$('.en',ay).textContent=fa?a[2]:a[1];$('.fa',ay).textContent=fa?a[1]:a[2].replace(/[«».]/g,'');$('.src',ay).textContent=fa?a[4]:a[3]}

  /* monthly timetable */
  var tt=$('[data-timetable]');
  if(tt){var xc=function(c){return (c==='sunrise'||c==='sunset')?' class="x"':''};var cols=['fajr','sunrise','dhuhr','asr','sunset','maghrib','isha'],dim=new Date(Date.UTC(now.y,now.m,0)).getUTCDate();
    var h='<table class="tt"><thead><tr><th>'+MO[now.m-1]+' '+fd(now.y)+'</th>'+cols.map(function(c){return '<th'+xc(c)+'>'+PN[c]+'</th>'}).join('')+'</tr></thead><tbody>';
    for(var d=1;d<=dim;d++){var t=MZ.times(now.y,now.m,d),w=new Date(Date.UTC(now.y,now.m-1,d,12)).getUTCDay();
      h+='<tr'+(d===now.d?' class="today"':'')+'><td>'+fd(d)+' <span class="wdn" style="font-weight:400;opacity:.7">'+WD[w]+'</span></td>'+cols.map(function(c){return '<td'+xc(c)+'>'+fd(t[c].text)+'</td>'}).join('')+'</tr>'}
    tt.innerHTML=h+'</tbody></table>'}

  /* month calendar with Hijri dates and observances */
  var cal=$('[data-calendar]');
  if(cal){var cy=now.y,cm=now.m;
    var draw=function(){var dim=new Date(Date.UTC(cy,cm,0)).getUTCDate(),first=(new Date(Date.UTC(cy,cm-1,1,12)).getUTCDay()+6)%7,list='';
      var h='<div class="calhead"><h3>'+MO[cm-1]+' '+fd(cy)+'</h3><div class="ctl"><button data-c="-1">'+TX.prev+'</button><button data-c="0">'+TX.today+'</button><button data-c="1">'+TX.nextM+'</button></div></div><div class="cal">'+WDS.map(function(w){return '<div class="wd">'+w+'</div>'}).join('');
      for(var i=0;i<first;i++)h+='<div class="c off"></div>';
      for(var d=1;d<=dim;d++){var hj=MZ.hijri(cy,cm,d),ev=evOn(hj),td=(cy===now.y&&cm===now.m&&d===now.d);
        h+='<div class="c'+(td?' today':'')+(ev?' ev':'')+'"><b>'+fd(d)+'</b>'+fd(hj.d)+'<span class="hm"> '+HM[hj.m-1]+'</span>'+(ev?'<em>'+ev+'</em>':'')+'</div>';
        if(ev)list+='<div class="occ" style="grid-template-columns:86px 1fr"><div class="d"><b>'+fd(d)+'</b><span>'+MO[cm-1]+'</span></div><div><h4>'+ev+'</h4><p>'+hText(hj)+'</p></div></div>'}
      cal.innerHTML=h+'</div><div class="evlist">'+(list||'<p class="small" style="padding:10px 0 16px">'+TX.none+'</p>')+'</div>';
      $$('button',cal).forEach(function(b){b.onclick=function(){var v=+b.getAttribute('data-c');if(v===0){cy=now.y;cm=now.m}else{cm+=v;if(cm<1){cm=12;cy--}if(cm>12){cm=1;cy++}}draw()}})};
    draw()}

  /* copy buttons and the mobile menu */
  $$('[data-copy]').forEach(function(b){b.onclick=function(){var v=b.getAttribute('data-copy'),o=b.textContent;if(navigator.clipboard)navigator.clipboard.writeText(v);b.textContent=TX.copied;setTimeout(function(){b.textContent=o},1500)}});
  var mm=$('.mmenu');if(mm){$$('[data-menu]').forEach(function(b){b.onclick=function(){mm.classList.toggle('open')}})}
})();
