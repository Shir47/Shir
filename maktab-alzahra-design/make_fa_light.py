# Builds the Dari (right-to-left) page home-light-fa.html from home-light.html
import re
PH='<bdi dir="ltr">۰۴۱ ۴۰۱ ۲۹۶۴</bdi>'
L=lambda t:'<bdi dir="ltr">'+t+'</bdi>'
T=[
('<html lang="en">','<html lang="fa" dir="rtl">'),
('<span class="on">EN</span><span class="fa">دری</span>','<span>EN</span><span class="on fa">دری</span>'),
('alt="Maktab Al-Zahra">Maktab Alzahra SA</a>','alt="Maktab Al-Zahra">مکتب الزهرا</a>'),
('<a class="on">Home</a><a>About</a><a>Quran classes</a><a>Prayer times</a><a>Calendar</a><a>Contact</a>','<a class="on">خانه</a><a>درباره ما</a><a>کلاس‌های قرآن</a><a>اوقات نماز</a><a>تقویم</a><a>تماس</a>'),
('<a class="btn b1">Call 041 401 2964</a>','<a class="btn b1">تماس&nbsp;&nbsp;'+PH+'</a>'),
('<span class="pill">Shia Islamic education in Adelaide</span>','<span class="pill">آموزش اسلامی شیعی در ادلاید</span>'),
('<h1>Where faith<br>becomes light.</h1>','<h1>جایی که ایمان<br>نور می‌شود</h1>'),
('Free Quran classes for all ages, guided by the Quran and the Ahl al-Bayt (AS).','کلاس‌های رایگان قرآن برای همه سنین، در پرتو قرآن و اهل بیت (ع).'),
('<a class="btn b1">See class details</a><a class="btn b2">Our story</a>','<a class="btn b1">جزئیات کلاس‌ها</a><a class="btn b2">داستان ما</a>'),
('<div><b>Free</b>for every family</div><div><b>All ages</b>children to adults</div><div><b>Sat and Sun</b>every weekend</div>','<div><b>رایگان</b>برای هر خانواده</div><div><b>همه سنین</b>از کودک تا بزرگسال</div><div><b>شنبه و یکشنبه</b>هر آخر هفته</div>'),
('>Decorative imagined architecture</div>','>معماری تزئینی خیالی</div>'),
('<span>Next prayer, Fajr</span><b>04:30</b>','<span>نماز بعدی، صبح</span><b>۰۴:۳۰</b>'),
('<h4>Weekend Quran classes</h4>','<h4>کلاس‌های قرآن آخر هفته</h4>'),
('<span>Arrive by</span><b>9:40 am</b></div><div class="row"><span>Doors close</span><b>10:00 am</b></div><div class="row"><span>Venue</span><b>Ingle Farm</b>','<span>زمان حضور</span><b>۹:۴۰ صبح</b></div><div class="row"><span>بسته شدن دروازه</span><b>۱۰:۰۰ صبح</b></div><div class="row"><span>مکان</span><b>اینگل فارم</b>'),
('<b>Prayer times <br>in Adelaide</b><span>Monday 23 November</span>','<b>اوقات نماز <br>در ادلاید</b><span>دوشنبه ۲۳ نوامبر</span>'),
('<span>Fajr, next</span><b>04:30</b>','<span>صبح، بعدی</span><b>۰۴:۳۰</b>'),
('<span>Dhuhr</span><b>13:02</b>','<span>ظهر</span><b>۱۳:۰۲</b>'),('<span>Asr</span><b>16:48</b>','<span>عصر</span><b>۱۶:۴۸</b>'),
('<span>Maghrib</span><b>20:24</b>','<span>مغرب</span><b>۲۰:۲۴</b>'),('<span>Isha</span><b>21:22</b>','<span>عشا</span><b>۲۱:۲۲</b>'),
('<span>12 Jumada II 1448 AH</span>','<span>۱۲ جمادی‌الثانی ۱۴۴۸ هجری قمری</span>'),
('<span class="pill g tag">Decorative artwork</span>','<span class="pill g tag">تصویر تزئینی</span>'),
('<span class="pill gr">Weekend Quran classes</span>','<span class="pill gr">کلاس‌های قرآن آخر هفته</span>'),
('>Every Saturday and Sunday morning.</h2>','>هر شنبه و یکشنبه صبح</h2>'),
('Children, young people and adults learn the Quran together at our venue in Ingle Farm.','کودکان، نوجوانان و بزرگسالان در مکان ما در اینگل فارم با هم قرآن می‌آموزند.'),
('<div class="fact"><span>Arrive by</span><b>9:40 am</b></div>','<div class="fact"><span>زمان حضور</span><b>۹:۴۰ صبح</b></div>'),
('<div class="fact"><span>Doors close</span><b>10:00 am</b></div>','<div class="fact"><span>بسته شدن دروازه</span><b>۱۰:۰۰ صبح</b></div>'),
('<div class="fact"><span>Cost</span><b>Free</b></div>','<div class="fact"><span>هزینه</span><b>رایگان</b></div>'),
('<div class="fact"><span>Ages</span><b>All ages</b></div>','<div class="fact"><span>سن</span><b>همه سنین</b></div>'),
('<span>Venue</span><b>20 Kylie Crescent, Ingle Farm</b></div><a>View on map</a>','<span>مکان</span><b>'+L('20 Kylie Crescent, Ingle Farm')+'</b></div><a>دیدن روی نقشه</a>'),
('<a class="btn b1">Registration information</a><a class="btn b2">Call about classes</a>','<a class="btn b1">معلومات ثبت نام</a><a class="btn b2">تماس درباره کلاس‌ها</a>'),
('Online registration is not yet available. Registration requires Maktab staff approval. Finishing times are awaiting confirmation.','ثبت نام آنلاین هنوز فعال نیست. ثبت نام نیاز به تأیید کارمندان مکتب دارد. زمان پایان کلاس هنوز تأیید نشده است.'),
('<h3>Your path to Quran classes</h3>','<h3>مسیر شما به کلاس‌های قرآن</h3>'),
('<i>1</i><div><h4>Read the class information</h4><p>Check the class notice and the materials list before you plan your visit.</p>','<i>۱</i><div><h4>معلومات کلاس را بخوانید</h4><p>پیش از آمدن، اطلاعیه کلاس و فهرست لوازم را ببینید.</p>'),
('<i>2</i><div><h4>Ask your questions</h4><p>Call the Maktab on 041 401 2964, every day from 8 am to 8 pm.</p>','<i>۲</i><div><h4>سؤال‌های خود را بپرسید</h4><p>هر روز از ۸ صبح تا ۸ شب با مکتب تماس بگیرید: '+PH+'</p>'),
('<i>3</i><div><h4>Follow staff guidance</h4><p>All registrations are subject to approval by Maktab staff.</p>','<i>۳</i><div><h4>رهنمایی کارمندان را دنبال کنید</h4><p>همه ثبت نام‌ها نیاز به تأیید کارمندان مکتب دارد.</p>'),
('<h3>What to bring</h3>','<h3>چه چیزهایی با خود بیاورید</h3>'),
('<li>Whiteboard</li><li>Markers</li><li>Notebooks and pencils</li><li>Bag</li><li>Completed homework sheets</li>','<li>تخته سفید</li><li>مارکر</li><li>کتابچه و پنسل</li><li>بکس</li><li>برگه‌های کار خانگی تکمیل‌شده</li>'),
('Students must bring the required materials to attend class. Students without them will not be permitted to attend.','شاگردان باید لوازم لازم را با خود بیاورند. شاگردانی که لوازم نداشته باشند اجازه شرکت در کلاس را ندارند.'),
('“I leave among you two weighty things: the Book of Allah and my family, my Ahl al-Bayt.”','«من در میان شما دو چیز گران‌بها می‌گذارم: کتاب خدا و عترتم، اهل بیتم.»'),
('Hadith al-Thaqalayn, Prophet Muhammad (S)','حدیث ثقلین، پیامبر اکرم (ص)'),
('Madinah. Inspirational photograph, not Maktab premises','مدینه. عکس الهام‌بخش، نه ساختمان مکتب'),
('<span class="pill">Our Maktab in Adelaide</span>','<span class="pill">مکتب ما در ادلاید</span>'),
('>Islamic education and community connection.</h2>','>آموزش اسلامی و پیوند با جامعه</h2>'),
('Maktab Alzahra SA is an Islamic educational and community organisation in Adelaide, South Australia.','مکتب الزهرا یک نهاد آموزشی و اجتماعی اسلامی در ادلاید، آسترالیای جنوبی است.'),
('<b>Quran education.</b> Free classes for children, young people and adults.','<b>آموزش قرآن.</b> کلاس‌های رایگان برای کودکان، نوجوانان و بزرگسالان.'),
('<b>Our Adelaide community.</b> A place to remember Shia Islamic occasions together.','<b>جامعه ما در ادلاید.</b> جایی برای گرامی‌داشت مناسبت‌های اسلامی شیعی در کنار هم.'),
('<b>Ways to get involved.</b> Give your time, share your skills or donate.','<b>راه‌های همکاری.</b> وقت بگذارید، مهارت‌تان را شریک کنید یا کمک مالی کنید.'),
('>About the Maktab</a>','>درباره مکتب</a>'),
('<span class="pill g">Shia Islamic calendar</span>','<span class="pill g">تقویم اسلامی شیعی</span>'),
('>Days of remembrance.</h2>','>روزهای یادبود</h2>'),
('<p class="lead">Today is 12 Jumada II 1448.</p>','<p class="lead">امروز ۱۲ جمادی‌الثانی ۱۴۴۸ است.</p>'),
('<b>1</b><span>December</span>','<b>۱</b><span>دسامبر</span>'),
('<h4>Birth of Lady Fatimah al-Zahra (AS)</h4><p>20 Jumada II 1448, the namesake of our Maktab</p>','<h4>ولادت حضرت فاطمه زهرا (س)</h4><p>۲۰ جمادی‌الثانی ۱۴۴۸، بانویی که مکتب ما به نام اوست</p>'),
('<b>8</b><span>days to go</span>','<b>۸</b><span>روز مانده</span>'),
('<b>23</b><span>December</span>','<b>۲۳</b><span>دسامبر</span>'),
('<h4>Birth of Imam Ali (AS)</h4><p>13 Rajab 1448</p>','<h4>ولادت امام علی (ع)</h4><p>۱۳ رجب ۱۴۴۸</p>'),
('<b>30</b><span>days to go</span>','<b>۳۰</b><span>روز مانده</span>'),
('Calculated Hijri dates are provisional and may vary with moon sightings. <a style="color:var(--green);font-weight:600">View the full calendar</a>','تاریخ‌های هجری محاسبه‌شده موقتی‌اند و ممکن است با رؤیت هلال تغییر کنند. <a style="color:var(--green);font-weight:600">دیدن تقویم کامل</a>'),
('>Ayah of the day</span>','>آیه روز</span>'),
('<div class="en">“My Lord, increase me in knowledge.”</div>\n      <div class="fa">پروردگارا، بر دانشم بیفزا</div>\n      <p class="small" style="margin-top:10px">Surah Taha 20:114</p>','<div class="en">«پروردگارا، بر دانشم بیفزا.»</div>\n      <div class="fa lat" dir="ltr">“My Lord, increase me in knowledge.”</div>\n      <p class="small" style="margin-top:10px">سوره طه، آیه ۱۱۴</p>'),
('<span class="pill gr">From the Maktab’s Instagram</span>','<span class="pill gr">از اینستاگرام مکتب</span>'),
('>Moments from our Maktab.</h2>','>لحظه‌هایی از مکتب ما</h2>'),
('<a class="btn b2">Follow @maktab.alzahra.sa</a>','<a class="btn b2">دنبال کنید&nbsp;'+L('@maktab.alzahra.sa')+'</a>'),
('<h4>Quran classes photo report</h4><span>View post</span>','<h4>گزارش تصویری کلاس‌های قرآن</h4><span>دیدن پست</span>'),
('<h4>Photo report, part 2</h4><span>View post</span>','<h4>گزارش تصویری، بخش دوم</h4><span>دیدن پست</span>'),
('<h4>Video report</h4><span>Watch</span>','<h4>گزارش ویدیویی</h4><span>تماشا</span>'),
('<span class="pill">Support our work</span>','<span class="pill">از کار ما حمایت کنید</span>'),
('>Help us keep providing Islamic education to our community.</h2>','>به ما کمک کنید آموزش اسلامی را برای جامعه‌مان ادامه دهیم</h2>'),
('<h3>Donate</h3><p>Support the Maktab by bank transfer.</p>','<h3>کمک مالی</h3><p>از طریق انتقال بانکی از مکتب حمایت کنید.</p>'),
('<span>Account name</span><b>Australian Youths Alliance inco</b>','<span>نام حساب</span><b dir="ltr">Australian Youths Alliance inco</b>'),
('<span>BSB</span><b>065-167</b>','<span dir="ltr">BSB</span><b dir="ltr">065-167</b>'),
('<span>Account number</span><b>10581185</b>','<span>شماره حساب</span><b dir="ltr">10581185</b>'),
('>Donation information</a><p class="small">Monthly direct debit is coming soon.</p>','>معلومات کمک مالی</a><p class="small">پرداخت ماهانه خودکار به‌زودی فعال می‌شود.</p>'),
('<h3>Volunteer</h3><p>Dedicate a day of your time, or contribute useful skills to the Maktab: community activities, practical support, or creative and digital skills.</p>','<h3>داوطلب شوید</h3><p>یک روز از وقت خود را بدهید یا مهارت‌های مفیدتان را در اختیار مکتب بگذارید: فعالیت‌های اجتماعی، کمک‌های عملی، یا مهارت‌های هنری و دیجیتال.</p>'),
('>Ways to help</a><p class="small">Volunteer applications are not yet open.</p>','>راه‌های کمک</a><p class="small">درخواست داوطلبی هنوز باز نشده است.</p>'),
('<h3>Islamic questions</h3><p>A space for Islamic religious enquiries, reviewed by an authorised religious representative. This website does not generate religious rulings.</p>','<h3>پرسش‌های دینی</h3><p>جایی برای پرسش‌های دینی اسلامی که نماینده مجاز دینی آن‌ها را بررسی می‌کند. این وب‌سایت حکم دینی صادر نمی‌کند.</p>'),
('>How enquiries work</a><p class="small">Question submissions are not yet open.</p>','>روند پرسش‌ها</a><p class="small">ارسال پرسش هنوز فعال نیست.</p>'),
('<span class="pill">Quran class enquiries</span>','<span class="pill">پرسش درباره کلاس‌های قرآن</span>'),
('<div class="phone">041 401 2964</div>','<div class="phone">'+PH+'</div>'),
('Call the Maktab every day, 8 am to 8 pm','هر روز از ۸ صبح تا ۸ شب با مکتب تماس بگیرید'),
('<span>Class venue</span><b>20 Kylie Crescent,<br>Ingle Farm, SA</b><small>View address on map</small>','<span>مکان کلاس</span><b>'+L('20 Kylie Crescent,')+'<br>'+L('Ingle Farm, SA')+'</b><small>دیدن آدرس روی نقشه</small>'),
('<span>Class times</span><b>Saturday and Sunday,<br>arrive by 9:40 am</b><small>Confirm the class time before travelling.</small>','<span>زمان کلاس</span><b>شنبه و یکشنبه،<br>حضور تا ۹:۴۰ صبح</b><small>پیش از حرکت، زمان کلاس را تأیید کنید.</small>'),
('<span>Instagram</span><span>YouTube</span><span>WhatsApp channel</span>','<span>اینستاگرام</span><span>یوتیوب</span><span>کانال واتساپ</span>'),
('Email is not yet published. No online contact form is active.','ایمیل هنوز منتشر نشده و فورم تماس آنلاین فعال نیست.'),
('alt="">Maktab Alzahra SA</div><p>An Islamic educational and community organisation in Adelaide. Australian Youths Alliance Incorporation.</p>','alt="">مکتب الزهرا</div><p>یک نهاد آموزشی و اجتماعی اسلامی در ادلاید. '+L('Australian Youths Alliance Incorporation')+'</p>'),
('<h5>Visit</h5><ul><li>20 Kylie Crescent</li><li>Ingle Farm, SA</li><li>Saturday and Sunday, 9:40 am</li></ul>','<h5>آدرس</h5><ul><li>'+L('20 Kylie Crescent')+'</li><li>'+L('Ingle Farm, SA')+'</li><li>شنبه و یکشنبه، ۹:۴۰ صبح</li></ul>'),
('<h5>Explore</h5><ul><li>Quran classes</li><li>Prayer times</li><li>Islamic calendar</li><li>Donations</li><li>Volunteer</li></ul>','<h5>بخش‌ها</h5><ul><li>کلاس‌های قرآن</li><li>اوقات نماز</li><li>تقویم اسلامی</li><li>کمک مالی</li><li>داوطلبی</li></ul>'),
('<h5>Contact</h5><ul><li>041 401 2964</li><li>Every day, 8 am to 8 pm</li><li>Instagram, YouTube, WhatsApp</li></ul>','<h5>تماس</h5><ul><li>'+PH+'</li><li>هر روز، ۸ صبح تا ۸ شب</li><li>اینستاگرام، یوتیوب، واتساپ</li></ul>'),
('© 2026 Maktab Alzahra SA, Adelaide, South Australia','© ۲۰۲۶ مکتب الزهرا، ادلاید، آسترالیای جنوبی'),
]
RTL='''
/* ---------- Dari, right to left ---------- */
body{font-family:Vazirmatn,sans-serif;font-size:17px;line-height:1.85}
h1,h2{font-family:'Noto Nastaliq Urdu',serif;font-weight:700;letter-spacing:0}
h1{font-size:76px;line-height:1.95;margin:6px 0 0;white-space:nowrap}
h2{font-size:46px;line-height:2.1;margin-bottom:-8px}
h3,h4,h5{font-weight:700;letter-spacing:0;line-height:1.5}
h3{font-size:25px}
.btn,.pill{font-family:Vazirmatn}
nav{padding:0 14px 0 12px}
.hero:before{right:auto;left:-180px}
.trust div+div{padding-left:0;border-left:0;padding-right:30px;border-right:1px solid #cfdcdc}
.trust b{font-size:24px;line-height:1.5}
.art .fl{left:auto;right:-70px}
.art .fl h4{font-size:20px}
.art .nx{right:auto;left:-26px}
.art .nx b{font-size:22px;line-height:1.3}
.art .cap{right:auto;left:22px}
.row b{text-align:left}
.pray .t0 b{font-size:21px;line-height:1.5}
.pt{border-left:0;border-right:1px solid var(--line)}
.pt.next,.pt.next + .pt{border-right:0}
.pt b{font-size:23px;line-height:1.3}
.pray .hij{text-align:left;border-left:0;padding-left:0;border-right:1px solid var(--line);padding-right:20px}
.cls .ph .tag{left:auto;right:22px}
.fact b{font-size:25px;line-height:1.5}.fact.w b{font-size:22px}
.step i{font-size:22px}
.step h4{font-size:20px}
.had .en{font-size:25px;line-height:1.9;font-weight:500}
.occ .d b,.cd b{font-size:28px;line-height:1.2}
.occ h4{font-size:20px}
.ayah .ar,.ayah .fa{text-align:right}
.ayah .en{font-size:22px;line-height:1.8;font-weight:600}
.ayah .lat{font-family:Figtree;text-align:right}
.mo h4{font-size:18px}
.contact:before{right:auto;left:-160px}
.phone{font-size:82px;line-height:1.2}
.ci b{font-size:19px;line-height:1.6}
.foot h5{font-size:17px}
@media (max-width:760px){
  h1{font-size:46px;white-space:normal}
  h2{font-size:32px}
  .trust div+div{padding-right:16px}
  .trust b{font-size:19px}
  .art .fl{left:12px;right:12px}
  .art .nx{left:8px;right:auto}
  .pt{border:0}
  .pt b{font-size:17px}
  .pray .hij{border:0;border-top:1px solid var(--line);padding:12px 6px 0}
  .fact b{font-size:20px}
  .had .en{font-size:20px}
  .ayah .en{font-size:19px}
  .phone{font-size:46px}
}
</style>'''
s=open('home-light.html',encoding='utf-8').read()
for a,b in T:
    assert a in s, a[:90]
    s=s.replace(a,b)
s=re.sub(r"font:400 ([^;']*)'DM Serif Display',\s*serif",r"font:700 \1Vazirmatn,sans-serif",s)
s=s.replace("font-family:'DM Serif Display',serif;font-weight:400","font-family:Vazirmatn,sans-serif;font-weight:700")
s=s.replace("'DM Serif Display',serif","Vazirmatn,sans-serif")
s=s.replace('family=DM+Serif+Display&','family=Noto+Nastaliq+Urdu:wght@700&')
s=s.replace('family=Vazirmatn:wght@400;500;600','family=Vazirmatn:wght@400;500;600;700')
s=s.replace('</style>',RTL,1)
open('home-light-fa.html','w',encoding='utf-8').write(s)
print('ok')
