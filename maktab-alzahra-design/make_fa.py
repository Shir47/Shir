# Builds the Dari (right-to-left) page from index.html
PH='<bdi dir="ltr">۰۴۱ ۴۰۱ ۲۹۶۴</bdi>'
ADDR='<bdi dir="ltr">20 Kylie Crescent, Ingle Farm</bdi>'
T=[
('<html lang="en">','<html lang="fa" dir="rtl">'),
('<a class="on" href="index.html">EN</a><a class="fa" href="index-fa.html">دری</a>','<a href="index.html">EN</a><a class="on fa" href="index-fa.html">دری</a>'),
('<b>Maktab Alzahra SA</b><span>Adelaide, South Australia</span>','<b>مکتب الزهرا</b><span>ادلاید، آسترالیای جنوبی</span>'),
('<a>About</a><a>Quran classes</a><a>Prayer times</a><a>Calendar</a><a>Questions</a><a>Contact</a>','<a>درباره ما</a><a>کلاس‌های قرآن</a><a>اوقات نماز</a><a>تقویم</a><a>پرسش‌ها</a><a>تماس</a>'),
('<a class="btn btn-gold">Call 041 401 2964</a>','<a class="btn btn-gold">تماس '+PH+'</a>'),
('<h1>Where faith<br>becomes light.</h1>','<h1>جایی که ایمان<br>نور می‌شود</h1>'),
('Free Quran classes for all ages in Adelaide, guided by the Quran and the Ahl al-Bayt (AS).','کلاس‌های رایگان قرآن برای همه سنین در ادلاید، در پرتو قرآن و اهل بیت (ع).'),
('<a class="btn btn-gold">See class details</a><a class="btn btn-ghost">Our story</a>','<a class="btn btn-gold">جزئیات کلاس‌ها</a><a class="btn btn-ghost">داستان ما</a>'),
('<div class="nast">مکتب الزهرا</div>\n        <div class="fa">کلاس‌های رایگان قرآن کریم برای همه سنین</div>\n        <small>Decorative imagined architecture</small>','<div class="lat">Maktab Alzahra SA</div>\n        <div class="lat2">Free Quran classes for all ages</div>\n        <small>معماری تزئینی خیالی</small>'),
('<span>Scroll to enter</span>','<span>برای ورود پایین بروید</span>'),
('<b>Prayer times <br>in Adelaide</b><span>Monday 23 November</span>','<b>اوقات نماز <br>در ادلاید</b><span>دوشنبه ۲۳ نوامبر</span>'),
('<div class="n">Fajr, next</div><div class="t">04:30</div>','<div class="n">صبح، بعدی</div><div class="t">۰۴:۳۰</div>'),
('<div class="n">Dhuhr</div><div class="t">13:02</div>','<div class="n">ظهر</div><div class="t">۱۳:۰۲</div>'),
('<div class="n">Asr</div><div class="t">16:48</div>','<div class="n">عصر</div><div class="t">۱۶:۴۸</div>'),
('<div class="n">Maghrib</div><div class="t">20:24</div>','<div class="n">مغرب</div><div class="t">۲۰:۲۴</div>'),
('<div class="n">Isha</div><div class="t">21:22</div>','<div class="n">عشا</div><div class="t">۲۱:۲۲</div>'),
('<div class="ar">١٢ جمادى الثانية ١٤٤٨</div><span>12 Jumada II 1448 AH</span>','<div class="ar">١٢ جمادى الثانية ١٤٤٨</div><span>۱۲ جمادی‌الثانی ۱۴۴۸ هجری قمری</span>'),
('Weekend Quran classes</div>','کلاس‌های قرآن آخر هفته</div>'),
('<h2>Every Saturday and Sunday morning, free for all ages.</h2>','<h2>هر شنبه و یکشنبه صبح، رایگان برای همه سنین</h2>'),
('Children, young people and adults learn the Quran together at our venue in Ingle Farm.','کودکان، نوجوانان و بزرگسالان در مکان ما در اینگل فارم با هم قرآن می‌آموزند.'),
('<dt>Arrive by</dt><dd>9:40 am</dd>','<dt>زمان حضور</dt><dd>۹:۴۰ صبح</dd>'),
('<dt>Doors close</dt><dd>10:00 am<small>Finishing times are awaiting confirmation.</small></dd>','<dt>بسته شدن دروازه</dt><dd>۱۰:۰۰ صبح<small>زمان پایان کلاس هنوز تأیید نشده است.</small></dd>'),
('<dt>Cost</dt><dd>Free</dd>','<dt>هزینه</dt><dd>رایگان</dd>'),
('<dt>Venue</dt><dd>20 Kylie Crescent, Ingle Farm<small><a class="textlink">View venue on map</a></small></dd>','<dt>مکان</dt><dd>'+ADDR+'<small><a class="textlink">دیدن مکان روی نقشه</a></small></dd>'),
('<a class="btn btn-blue">Registration information</a><a class="btn btn-line">Call about classes</a>','<a class="btn btn-blue">معلومات ثبت نام</a><a class="btn btn-line">تماس درباره کلاس‌ها</a>'),
('Online registration is not yet available. Registration requires Maktab staff approval.','ثبت نام آنلاین هنوز فعال نیست. ثبت نام نیاز به تأیید کارمندان مکتب دارد.'),
('<div class="cap">Decorative artwork</div>','<div class="cap">تصویر تزئینی</div>'),
('<h3>Your path to Quran classes</h3>','<h3>مسیر شما به کلاس‌های قرآن</h3>'),
('<h4>Read the class information</h4><p>Check the class notice and the materials list before you plan your visit.</p>','<h4>معلومات کلاس را بخوانید</h4><p>پیش از آمدن، اطلاعیه کلاس و فهرست لوازم را ببینید.</p>'),
('<h4>Ask your questions</h4><p>Call the Maktab on 041 401 2964, every day from 8 am to 8 pm.</p>','<h4>سؤال‌های خود را بپرسید</h4><p>هر روز از ۸ صبح تا ۸ شب با مکتب تماس بگیرید: '+PH+'</p>'),
('<h4>Follow staff guidance</h4><p>All registrations are subject to approval by Maktab staff.</p>','<h4>رهنمایی کارمندان را دنبال کنید</h4><p>همه ثبت نام‌ها نیاز به تأیید کارمندان مکتب دارد.</p>'),
('<h3>What to bring</h3>','<h3>چه چیزهایی با خود بیاورید</h3>'),
('</svg>Whiteboard</li>','</svg>تخته سفید</li>'),('</svg>Markers</li>','</svg>مارکر</li>'),('</svg>Notebooks and pencils</li>','</svg>کتابچه و پنسل</li>'),('</svg>Bag</li>','</svg>بکس</li>'),('</svg>Completed homework sheets</li>','</svg>برگه‌های کار خانگی تکمیل‌شده</li>'),
('Students must bring the required materials to attend class. Students without them will not be permitted to attend.','شاگردان باید لوازم لازم را با خود بیاورند. شاگردانی که لوازم نداشته باشند اجازه شرکت در کلاس را ندارند.'),
('“I leave among you two weighty things: the Book of Allah and my family, my Ahl al-Bayt.”','«من در میان شما دو چیز گران‌بها می‌گذارم: کتاب خدا و عترتم، اهل بیتم.»'),
('Hadith al-Thaqalayn, Prophet Muhammad (S)','حدیث ثقلین، پیامبر اکرم (ص)'),
('Madinah. Inspirational photograph, not Maktab premises','مدینه. عکس الهام‌بخش، نه ساختمان مکتب'),
('Our Maktab in Adelaide</div>','مکتب ما در ادلاید</div>'),
('<h2>Islamic education and community connection.</h2>','<h2>آموزش اسلامی و پیوند با جامعه</h2>'),
('Maktab Alzahra SA is an Islamic educational and community organisation in Adelaide, South Australia.','مکتب الزهرا یک نهاد آموزشی و اجتماعی اسلامی در ادلاید، آسترالیای جنوبی است.'),
('<b>Quran education.</b> Free classes for children, young people and adults.','<b>آموزش قرآن.</b> کلاس‌های رایگان برای کودکان، نوجوانان و بزرگسالان.'),
('<b>Our Adelaide community.</b> A place to remember Shia Islamic occasions together.','<b>جامعه ما در ادلاید.</b> جایی برای گرامی‌داشت مناسبت‌های اسلامی شیعی در کنار هم.'),
('<b>Ways to get involved.</b> Give your time, share your skills or donate.','<b>راه‌های همکاری.</b> وقت بگذارید، مهارت‌تان را شریک کنید یا کمک مالی کنید.'),
('>About the Maktab</a>','>درباره مکتب</a>'),
('Shia Islamic calendar</div>','تقویم اسلامی شیعی</div>'),
('<h2>Days of remembrance.</h2>','<h2>روزهای یادبود</h2>'),
('<b>Today is 12 Jumada II 1448</b><span class="ar">١٢ جمادى الثانية</span>','<b>امروز ۱۲ جمادی‌الثانی ۱۴۴۸ است</b>'),
('<b>1</b><span>December</span>','<b>۱</b><span>دسامبر</span>'),
('<h4>Birth of Lady Fatimah al-Zahra (AS)</h4><p>20 Jumada II 1448, the namesake of our Maktab</p>','<h4>ولادت حضرت فاطمه زهرا (س)</h4><p>۲۰ جمادی‌الثانی ۱۴۴۸، بانویی که مکتب ما به نام اوست</p>'),
('<b>8</b><span>days to go</span>','<b>۸</b><span>روز مانده</span>'),
('<b>23</b><span>December</span>','<b>۲۳</b><span>دسامبر</span>'),
('<h4>Birth of Imam Ali (AS)</h4><p>13 Rajab 1448</p>','<h4>ولادت امام علی (ع)</h4><p>۱۳ رجب ۱۴۴۸</p>'),
('<b>30</b><span>days to go</span>','<b>۳۰</b><span>روز مانده</span>'),
('Calculated Hijri dates are provisional and may vary with moon sightings. <a class="textlink">View the full calendar</a>','تاریخ‌های هجری محاسبه‌شده موقتی‌اند و ممکن است با رؤیت هلال تغییر کنند. <a class="textlink">دیدن تقویم کامل</a>'),
('<div class="k">Ayah of the day</div>','<div class="k">آیه روز</div>'),
('<div class="en">“My Lord, increase me in knowledge.”</div><div class="fa">پروردگارا، بر دانشم بیفزا</div><div class="src">Surah Taha 20:114</div>','<div class="en">«پروردگارا، بر دانشم بیفزا.»</div><div class="fa" dir="ltr">“My Lord, increase me in knowledge.”</div><div class="src">سوره طه، آیه ۱۱۴</div>'),
('<div class="k">Hadith of the day</div>','<div class="k">حدیث روز</div>'),
('<div class="en">“The worth of every person is in what they do well.”</div><div class="fa">ارزش هر کس به کاری است که نیکو انجام می‌دهد</div><div class="src">Imam Ali (AS), Nahj al-Balagha</div>','<div class="en">«ارزش هر کس به کاری است که نیکو انجام می‌دهد.»</div><div class="fa" dir="ltr">“The worth of every person is in what they do well.”</div><div class="src">امام علی (ع)، نهج‌البلاغه</div>'),
('From the Maktab’s Instagram</div>','از اینستاگرام مکتب</div>'),
('<h2>Moments from our Maktab.</h2>','<h2>لحظه‌هایی از مکتب ما</h2>'),
('<a class="btn btn-line">Follow @maktab.alzahra.sa</a>','<a class="btn btn-line">دنبال کنید <bdi dir="ltr">@maktab.alzahra.sa</bdi></a>'),
('<h4>Quran classes photo report</h4><span>View post</span>','<h4>گزارش تصویری کلاس‌های قرآن</h4><span>دیدن پست</span>'),
('<h4>Photo report, part 2</h4><span>View post</span>','<h4>گزارش تصویری، بخش دوم</h4><span>دیدن پست</span>'),
('<h4>Video report</h4><span>Watch</span>','<h4>گزارش ویدیویی</h4><span>تماشا</span>'),
('Support our work</div>','از کار ما حمایت کنید</div>'),
('Help us keep providing Islamic education to our community.</h2>','به ما کمک کنید آموزش اسلامی را برای جامعه‌مان ادامه دهیم</h2>'),
('<h3>Donate</h3><p>Support the Maktab by bank transfer.</p>','<h3>کمک مالی</h3><p>از طریق انتقال بانکی از مکتب حمایت کنید.</p>'),
('<span>Account name</span><b>Australian Youths Alliance inco</b>','<span>نام حساب</span><b dir="ltr">Australian Youths Alliance inco</b>'),
('<span>BSB</span><b>065-167</b>','<span dir="ltr">BSB</span><b dir="ltr">065-167</b>'),
('<span>Account number</span><b>10581185</b>','<span>شماره حساب</span><b dir="ltr">10581185</b>'),
('>Donation information</a><div class="soon">Monthly direct debit is coming soon.</div>','>معلومات کمک مالی</a><div class="soon">پرداخت ماهانه خودکار به‌زودی فعال می‌شود.</div>'),
('<h3>Volunteer</h3><p>Dedicate a day of your time, or contribute useful skills to the Maktab: community activities, practical support, or creative and digital skills.</p>','<h3>داوطلب شوید</h3><p>یک روز از وقت خود را بدهید یا مهارت‌های مفیدتان را در اختیار مکتب بگذارید: فعالیت‌های اجتماعی، کمک‌های عملی، یا مهارت‌های هنری و دیجیتال.</p>'),
('>Ways to help</a><div class="soon">Volunteer applications are not yet open.</div>','>راه‌های کمک</a><div class="soon">درخواست داوطلبی هنوز باز نشده است.</div>'),
('<h3>Islamic questions</h3><p>A space for Islamic religious enquiries, reviewed by an authorised religious representative. This website does not generate religious rulings.</p>','<h3>پرسش‌های دینی</h3><p>جایی برای پرسش‌های دینی اسلامی که نماینده مجاز دینی آن‌ها را بررسی می‌کند. این وب‌سایت حکم دینی صادر نمی‌کند.</p>'),
('>How enquiries work</a><div class="soon">Question submissions are not yet open.</div>','>روند پرسش‌ها</a><div class="soon">ارسال پرسش هنوز فعال نیست.</div>'),
('Quran class enquiries</div>','پرسش درباره کلاس‌های قرآن</div>'),
('<h2>Call the Maktab.</h2>','<h2>با مکتب تماس بگیرید</h2>'),
('<div class="bigphone">041 401 2964</div>','<div class="bigphone">'+PH+'</div>'),
('<div class="hours">Every day, 8 am to 8 pm</div>','<div class="hours">هر روز، ۸ صبح تا ۸ شب</div>'),
('<div class="k">Class venue</div><div class="v">20 Kylie Crescent,<br>Ingle Farm, SA</div><a>View address on map</a>','<div class="k">مکان کلاس</div><div class="v"><bdi dir="ltr">20 Kylie Crescent,</bdi><br><bdi dir="ltr">Ingle Farm, SA</bdi></div><a>دیدن آدرس روی نقشه</a>'),
('<div class="k">Class times</div><div class="v">Saturday and Sunday,<br>arrive by 9:40 am</div><div class="s">Confirm the class time before travelling.</div>','<div class="k">زمان کلاس</div><div class="v">شنبه و یکشنبه،<br>حضور تا ۹:۴۰ صبح</div><div class="s">پیش از حرکت، زمان کلاس را تأیید کنید.</div>'),
('<span>Instagram</span><span>YouTube</span><span>WhatsApp channel</span>','<span>اینستاگرام</span><span>یوتیوب</span><span>کانال واتساپ</span>'),
('Email is not yet published. No online contact form is active.','ایمیل هنوز منتشر نشده و فورم تماس آنلاین فعال نیست.'),
('<b>Maktab Alzahra SA</b><span>Australian Youths Alliance Incorporation</span>','<b>مکتب الزهرا</b><span dir="ltr">Australian Youths Alliance Incorporation</span>'),
('<h5>Visit</h5><ul><li>20 Kylie Crescent</li><li>Ingle Farm, SA</li><li>Saturday and Sunday, 9:40 am</li></ul>','<h5>آدرس</h5><ul><li><bdi dir="ltr">20 Kylie Crescent</bdi></li><li><bdi dir="ltr">Ingle Farm, SA</bdi></li><li>شنبه و یکشنبه، ۹:۴۰ صبح</li></ul>'),
('<h5>Explore</h5><ul><li>Quran classes</li><li>Prayer times</li><li>Islamic calendar</li><li>Donations</li><li>Volunteer</li></ul>','<h5>بخش‌ها</h5><ul><li>کلاس‌های قرآن</li><li>اوقات نماز</li><li>تقویم اسلامی</li><li>کمک مالی</li><li>داوطلبی</li></ul>'),
('<h5>Contact</h5><ul><li>041 401 2964</li><li>Every day, 8 am to 8 pm</li><li>Instagram, YouTube, WhatsApp</li></ul>','<h5>تماس</h5><ul><li>'+PH+'</li><li>هر روز، ۸ صبح تا ۸ شب</li><li>اینستاگرام، یوتیوب، واتساپ</li></ul>'),
('© 2026 Maktab Alzahra SA, Adelaide, South Australia','© ۲۰۲۶ مکتب الزهرا، ادلاید، آسترالیای جنوبی'),
("'Markazi Text',serif","Vazirmatn,sans-serif"),
]
RTL='''
/* ---------- Dari, right to left ---------- */
body{font-family:Vazirmatn,sans-serif;font-size:17px;line-height:1.85}
h1,h2{font-family:'Noto Nastaliq Urdu',serif;font-weight:700;letter-spacing:0}
h1{font-size:104px;line-height:1.75;margin-bottom:4px}
h2{font-size:50px;line-height:2.05;margin:0 0 -6px}
h3,h4{line-height:1.5;font-weight:700;letter-spacing:0}
.kicker{font-size:19px;margin-bottom:0}
.btn{font-family:Vazirmatn}
.hero .shade{background:linear-gradient(180deg,rgba(6,21,52,.82) 0%,rgba(6,21,52,.15) 24%,rgba(6,21,52,0) 42%,rgba(6,21,52,.55) 70%,rgba(6,21,52,.96) 100%),linear-gradient(270deg,rgba(6,21,52,.75) 0%,rgba(6,21,52,0) 55%)}
.hero > img{object-position:50% 38%;}
.bism{text-align:right}
.brand b{font-size:25px;line-height:1.4}
.hero-fa{text-align:left}
.hero-fa .lat{font-family:'Markazi Text',serif;font-weight:700;font-size:50px;line-height:1;color:var(--gold-2)}
.hero-fa .lat2{font-family:Figtree;font-size:19px;color:#e6edf8;margin-top:8px}
.katiba .where b{font-size:22px;line-height:1.5}
.katiba .hij{text-align:left}
.pt .t{font-size:29px;font-weight:700;line-height:1.3}
.fact dd{font-size:29px;font-weight:700;line-height:1.5}
.join h3{font-size:34px}.bring h3{font-size:30px}
.steps h4{font-size:23px;line-height:1.5}
.thaq .en{font-size:28px;line-height:1.9;font-weight:500}
.today b{font-size:28px}
.occ .date b{font-size:46px;line-height:1.2}.cd b{font-size:46px;line-height:1.2}
.occ h4{font-size:24px;line-height:1.5}
.cd{text-align:left}
.verse .k{font-size:17px}
.verse .ar{text-align:right}
.verse .en{font-size:22px;line-height:1.7;font-weight:500}
.verse .fa{text-align:right;direction:ltr;font-family:Figtree}
.mcap h4{font-size:20px}
.sup h3{font-size:31px}
.bigphone{font-size:100px;line-height:1.2}
.cbox{padding:24px 0 6px 28px}
.cbox + .cbox{padding-left:0;padding-right:28px;border-left:0;border-right:1px solid rgba(255,255,255,.22)}
.cbox .v{font-size:23px;line-height:1.6}
.foot h5{font-size:18px}
.foot .nast{text-align:right}
@media (max-width:760px){
  h1{font-size:58px}
  h2{font-size:34px;margin:0 0 -4px}
  .brand b{font-size:21px}
  .hero-fa{display:none}
  .katiba .where b{font-size:19px}
  .pt .t{font-size:20px}
  .fact dd{font-size:22px}
  .steps h4{font-size:20px}
  .thaq .en{font-size:21px}
  .today b{font-size:23px}
  .occ .date b{font-size:36px}.cd b{font-size:32px}.cd{text-align:right}
  .occ h4{font-size:21px}
  .verse .en{font-size:19px}
  .bigphone{font-size:54px}
  .cbox + .cbox{padding-right:0;border-right:0}
}
</style>'''
s=open('index.html',encoding='utf-8').read()
for a,b in T:
    assert a in s, a[:80]
    s=s.replace(a,b)
s=s.replace('family=Markazi+Text:wght@400;500;600;700','family=Markazi+Text:wght@700')
s=s.replace('</style>',RTL,1)
s=s.replace("document.getElementById('enter');","document.getElementById('enter');",1)
open('index-fa.html','w',encoding='utf-8').write(s)
print('ok')
