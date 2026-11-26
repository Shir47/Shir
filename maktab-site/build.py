#!/usr/bin/env python3
"""Builds the Maktab Alzahra SA website (English and Dari) into ./public.

Run:  python3 build.py
Every piece of text is written once as L("English", "Dari"), so the two languages stay in step.
"""
import os, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "public")
LANG = "en"
LEGAL = "Australian Youths Alliance inco"
BASE = "https://maktabalzahra.org.au"
MAPSVG = '<svg viewBox="0 0 700 330" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="700" height="330" fill="#e3ece9"/><g fill="none" stroke="#fff" stroke-width="14" stroke-linecap="round"><path d="M-20 90 L720 140"/><path d="M180 -20 L250 350"/><path d="M460 -20 Q420 160 520 350"/><path d="M-20 250 Q300 200 720 270"/></g><g fill="none" stroke="#f6f9f8" stroke-width="7"><path d="M60 -20 L90 350"/><path d="M-20 180 L720 200"/><path d="M600 -20 L640 350"/><path d="M330 -20 L340 350"/></g><rect x="380" y="20" width="120" height="70" rx="10" fill="#cfe5d6"/><rect x="40" y="210" width="110" height="80" rx="10" fill="#cfe5d6"/><circle cx="350" cy="152" r="34" fill="#0f5a33" opacity=".12"/></svg>'
TEL = "tel:+61414012964"
MAP = "https://www.google.com/maps/search/?api=1&query=20%20Kylie%20Crescent%2C%20Ingle%20Farm%2C%20SA"
IG = "https://www.instagram.com/maktab.alzahra.sa/"
YT = "https://www.youtube.com/@MaktabAlzahraSA"
WA = "https://whatsapp.com/channel/0029Vb8WEWSCMY0P63lpM80x"
IG1 = "https://www.instagram.com/maktab.alzahra.sa/p/DdiNljVFKVu/"
IG2 = "https://www.instagram.com/maktab.alzahra.sa/p/DdiRM4GFIWL/"
IG3 = "https://www.instagram.com/maktab.alzahra.sa/reel/DdigeWDB7_8/"


def L(en, fa):
    return fa if LANG == "fa" else en


def ltr(text):
    return f'<bdi dir="ltr">{text}</bdi>'


def phone():
    return L("041 401 2964", ltr("۰۴۱ ۴۰۱ ۲۹۶۴"))


def url(slug=""):
    return f"/{LANG}/{slug}"


def notice(title, text):
    return f'<div class="notice"><div><b>{title}</b><p>{text}</p></div></div>'


NOT_PREMISES = lambda: L("Madinah al-Munawwarah", "مدینه منوره")
DECOR = lambda: ""


def phead(pill, h1, lead, img, cap, extra=""):
    return f'''<header class="phead"><div class="wrap"><div class="phead-g">
  <div><span class="pill">{pill}</span><h1>{h1}</h1><p class="lead">{lead}</p>{extra}</div>
  <div><div class="ph"><img src="{{A}}/{img}" alt=""></div>{f'<p class="small" style="text-align:center;margin-top:10px">{cap}</p>' if cap else ''}</div>
</div></div></header>'''


def moments():
    return f'''<div class="moments">
    <a class="mo" href="{IG1}"><div class="im"><img src="{{A}}/quran-photo-report-1.webp" alt=""></div><div class="c"><h4>{L("Quran classes photo report", "گزارش تصویری کلاس‌های قرآن")}</h4><span>{L("View post", "دیدن پست")}</span></div></a>
    <a class="mo" href="{IG2}"><div class="im"><img src="{{A}}/quran-photo-report-2.webp" alt=""></div><div class="c"><h4>{L("Photo report, part 2", "گزارش تصویری، بخش دوم")}</h4><span>{L("View post", "دیدن پست")}</span></div></a>
    <a class="mo reel" href="{IG3}"><div class="im"><img src="{{A}}/quran-reel-cover.webp" alt=""></div><div class="c"><h4>{L("Video report", "گزارش ویدیویی")}</h4><span>{L("Watch", "تماشا")}</span></div></a>
  </div>'''


SKY = {"imsak": "linear-gradient(180deg,#040f2a,#1d3f8a)", "fajr": "linear-gradient(180deg,#2a3f7a,#c98ba0 60%,#f6c79b)",
       "sunrise": "linear-gradient(180deg,#8cc3ea,#ffe2a8)", "dhuhr": "linear-gradient(180deg,#4fa7e0,#cfeefa)",
       "sunset": "linear-gradient(180deg,#5a7fc0,#f39c55)", "maghrib": "linear-gradient(180deg,#22306b,#b0497a 60%,#f39c55)"}


def pnames():
    return {"imsak": L("Imsak", "امساک"), "fajr": L("Fajr", "صبح"), "sunrise": L("Sunrise", "طلوع آفتاب"),
            "dhuhr": L("Dhuhr", "ظهر"), "sunset": L("Sunset", "غروب آفتاب"), "maghrib": L("Maghrib", "مغرب")}


def prayer_strip():
    names = pnames()
    cells = "".join(f'<div class="pt"><span><i style="background:{SKY[k]}"></i>{names[k]}</span><b data-pray="{k}">--:--</b></div>' for k in SKY)
    return f'''<div class="wrap"><div class="card pray">
  <div class="t0"><b>{L("Prayer times <br>in Adelaide", "اوقات نماز <br>در ادلاید")}</b><span data-today></span></div>
  {cells}
  <div class="hij"><div class="ar" data-hijri-ar></div><span data-hijri></span></div>
</div></div>'''


def steps_card():
    return f'''<div class="card steps"><h3>{L("Your path to Quran classes", "مسیر شما به کلاس‌های قرآن")}</h3>
      <div class="step" style="margin-top:8px"><i>{L("1", "۱")}</i><div><h4>{L("Read the class information", "معلومات کلاس را بخوانید")}</h4><p>{L("Check the class notice and the materials list before you plan your visit.", "پیش از آمدن، اطلاعیه کلاس و فهرست لوازم را ببینید.")}</p></div></div>
      <div class="step"><i>{L("2", "۲")}</i><div><h4>{L("Ask your questions", "سؤال‌های خود را بپرسید")}</h4><p>{L("Call the Maktab on", "با مکتب تماس بگیرید:")} <a class="textlink" href="{TEL}">{phone()}</a>{L(", every day from 8 am to 8 pm.", "، هر روز از ۸ صبح تا ۸ شب.")}</p></div></div>
      <div class="step"><i>{L("3", "۳")}</i><div><h4>{L("Follow staff guidance", "رهنمایی کارمندان را دنبال کنید")}</h4><p>{L("All registrations are subject to approval by Maktab staff.", "همه ثبت نام‌ها نیاز به تأیید کارمندان مکتب دارد.")}</p></div></div>
    </div>'''


def bring_card():
    items = [L("Whiteboard", "تخته سفید"), L("Markers", "مارکر"), L("Notebooks and pencils", "کتابچه و پنسل"), L("Bag", "بکس"), L("Completed homework sheets", "برگه‌های کار خانگی تکمیل‌شده")]
    return f'''<div class="bring"><h3>{L("What to bring", "چه چیزهایی با خود بیاورید")}</h3>
      <ul>{"".join(f"<li>{i}</li>" for i in items)}</ul>
      <p>{L("Students must bring the required materials to attend class. Students without them will not be permitted to attend.", "شاگردان باید لوازم لازم را با خود بیاورند. شاگردانی که لوازم نداشته باشند اجازه شرکت در کلاس را ندارند.")}</p></div>'''


def facts():
    return f'''<div class="facts">
        <div class="fact"><span>{L("Arrive by", "زمان حضور")}</span><b>{L("9:40 am", "۹:۴۰ صبح")}</b></div>
        <div class="fact"><span>{L("Doors close", "بسته شدن دروازه")}</span><b>{L("10:00 am", "۱۰:۰۰ صبح")}</b></div>
        <div class="fact"><span>{L("Cost", "هزینه")}</span><b>{L("Free", "رایگان")}</b></div>
        <div class="fact"><span>{L("Ages", "سن")}</span><b>{L("All ages", "همه سنین")}</b></div>
        <div class="fact w"><div><span>{L("Venue", "مکان")}</span><b>{ltr("20 Kylie Crescent, Ingle Farm")}</b></div><a href="{MAP}">{L("View on map", "دیدن روی نقشه")}</a></div>
      </div>'''


def contact_panel():
    return f'''<div class="wrap"><div class="contact">
  <div>
    <span class="pill">{L("Quran class enquiries", "پرسش درباره کلاس‌های قرآن")}</span>
    <a class="phone" href="{TEL}" style="display:block">{phone()}</a>
    <div class="hrs">{L("Call the Maktab every day, 8 am to 8 pm", "هر روز از ۸ صبح تا ۸ شب با مکتب تماس بگیرید")}</div>
    <div class="ci"><div><span>{L("Class venue", "مکان کلاس")}</span><b>{ltr("20 Kylie Crescent,")}<br>{ltr("Ingle Farm, SA")}</b><small><a href="{MAP}">{L("View address on map", "دیدن آدرس روی نقشه")}</a></small></div><div><span>{L("Class times", "زمان کلاس")}</span><b>{L("Saturday and Sunday,<br>arrive by 9:40 am", "شنبه و یکشنبه،<br>حضور تا ۹:۴۰ صبح")}</b><small>{L("Confirm the class time before travelling.", "پیش از حرکت، زمان کلاس را تأیید کنید.")}</small></div></div>
    <div class="soc"><a href="{IG}"><span>{L("Instagram", "اینستاگرام")}</span></a><a href="{YT}"><span>{L("YouTube", "یوتیوب")}</span></a><a href="{WA}"><span>{L("WhatsApp channel", "کانال واتساپ")}</span></a></div>
    
  </div>
  <div><div class="ph"><img src="{{A}}/madinah-green-dome-736.webp" alt=""></div><p class="small" style="text-align:center;margin-top:10px">{NOT_PREMISES()}</p></div>
</div></div>'''


# ---------------------------------------------------------------- pages

def home():
    return f'''
<header class="hero"><div class="wrap"><div class="hero-g">
  <div>
    <span class="pill">{L("Shia Islamic education in Adelaide", "آموزش اسلامی شیعی در ادلاید")}</span>
    <h1>{L("Where faith<br>becomes light.", "جایی که ایمان<br>نور می‌شود")}</h1>
    <p class="lead">{L("Free Quran classes for all ages, guided by the Quran and the Ahl al-Bayt (AS).", "کلاس‌های رایگان قرآن برای همه سنین، در پرتو قرآن و اهل بیت (ع).")}</p>
    <div class="cta"><a class="btn b1" href="{url("registration/")}">{L("See class details", "جزئیات کلاس‌ها")}</a><a class="btn b2" href="{url("about/")}">{L("Our story", "داستان ما")}</a></div>
    <div class="trust"><div><b>{L("Free", "رایگان")}</b>{L("for every family", "برای هر خانواده")}</div><div><b>{L("All ages", "همه سنین")}</b>{L("children to adults", "از کودک تا بزرگسال")}</div><div><b>{L("Sat and Sun", "شنبه و یکشنبه")}</b>{L("every weekend", "هر آخر هفته")}</div></div>
  </div>
  <div class="art">
    <div class="ring"></div>
    <div class="ph"><img src="{{A}}/shrine-1200.webp" alt=""></div>
    <div class="card nx"><i></i><div><span data-next-name>{L("Next prayer", "نماز بعدی")}</span><b data-next-time>--:--</b></div></div>
    <div class="card fl"><h4>{L("Weekend Quran classes", "کلاس‌های قرآن آخر هفته")}</h4>
      <div class="row" style="margin-top:6px"><span>{L("Arrive by", "زمان حضور")}</span><b>{L("9:40 am", "۹:۴۰ صبح")}</b></div><div class="row"><span>{L("Doors close", "بسته شدن دروازه")}</span><b>{L("10:00 am", "۱۰:۰۰ صبح")}</b></div><div class="row"><span>{L("Venue", "مکان")}</span><b>{L("Ingle Farm", "اینگل فارم")}</b></div></div>
  </div>
</div></div></header>

{prayer_strip()}

<section class="sec"><div class="wrap">
  <div class="cls">
    <div class="ph"><img src="{{A}}/premium-quran.webp" alt=""></div>
    <div>
      <span class="pill gr">{L("Weekend Quran classes", "کلاس‌های قرآن آخر هفته")}</span>
      <h2 style="margin-top:18px">{L("Every Saturday and Sunday morning.", "هر شنبه و یکشنبه صبح")}</h2>
      <p class="lead">{L("Children, young people and adults learn the Quran together at our venue in Ingle Farm.", "کودکان، نوجوانان و بزرگسالان در مکان ما در اینگل فارم با هم قرآن می‌آموزند.")}</p>
      {facts()}
      <div class="cta"><a class="btn b1" href="{url("registration/")}">{L("Registration information", "معلومات ثبت نام")}</a><a class="btn b2" href="{TEL}">{L("Call about classes", "تماس درباره کلاس‌ها")}</a></div>
      <p class="small" style="margin-top:16px">{L("Register by phone. Every place is confirmed by Maktab staff.", "ثبت نام از طریق تلفن انجام می‌شود. هر ثبت نام توسط کارمندان مکتب تأیید می‌شود.")}</p>
    </div>
  </div>
  <div class="two">{steps_card()}{bring_card()}</div>
</div></section>

<div class="wrap"><div class="had">
  <div class="q ar">إِنِّي تَارِكٌ فِيكُمُ الثَّقَلَيْنِ<br>كِتَابَ اللَّهِ وَعِتْرَتِي أَهْلَ بَيْتِي</div>
  <div class="en">{L("“I leave among you two weighty things: the Book of Allah and my family, my Ahl al-Bayt.”", "«من در میان شما دو چیز گران‌بها می‌گذارم: کتاب خدا و عترتم، اهل بیتم.»")}</div>
  <div class="src">{L("Hadith al-Thaqalayn, Prophet Muhammad (S)", "حدیث ثقلین، پیامبر اکرم (ص)")}</div>
</div></div>

<section class="sec"><div class="wrap about">
  <div><div class="ph"><img src="{{A}}/madinah-arch-736.webp" alt=""></div><p class="small" style="text-align:center;margin-top:10px">{NOT_PREMISES()}</p></div>
  <div>
    <span class="pill">{L("Our Maktab in Adelaide", "مکتب ما در ادلاید")}</span>
    <h2 style="margin-top:18px">{L("Islamic education and community connection.", "آموزش اسلامی و پیوند با جامعه")}</h2>
    <p class="lead">{L("Maktab Alzahra SA is an Islamic educational and community organisation in Adelaide, South Australia.", "مکتب الزهرا یک نهاد آموزشی و اجتماعی اسلامی در ادلاید، آسترالیای جنوبی است.")}</p>
    <ul>
      <li><span>{L("<b>Quran education.</b> Free classes for children, young people and adults.", "<b>آموزش قرآن.</b> کلاس‌های رایگان برای کودکان، نوجوانان و بزرگسالان.")}</span></li>
      <li><span>{L("<b>Our Adelaide community.</b> A place to remember Shia Islamic occasions together.", "<b>جامعه ما در ادلاید.</b> جایی برای گرامی‌داشت مناسبت‌های اسلامی شیعی در کنار هم.")}</span></li>
      <li><span>{L("<b>Ways to get involved.</b> Give your time, share your skills or donate.", "<b>راه‌های همکاری.</b> وقت بگذارید، مهارت‌تان را شریک کنید یا کمک مالی کنید.")}</span></li>
    </ul>
    <a class="btn b1" style="margin-top:30px" href="{url("about/")}">{L("About the Maktab", "درباره مکتب")}</a>
  </div>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap">
  <span class="pill g">{L("Shia Islamic calendar", "تقویم اسلامی شیعی")}</span>
  <h2 style="margin-top:18px">{L("Days of remembrance.", "روزهای یادبود")}</h2>
  <p class="lead">{L("Today is", "امروز")} <span data-hijri></span>.</p>
  <div class="days">
    <div class="card occs">
      <div data-upcoming="2"></div>
      <div class="occ" style="display:block"><p class="small">{L("Calculated Hijri dates are provisional and may vary with moon sightings.", "تاریخ‌های هجری محاسبه‌شده موقتی‌اند و ممکن است با رؤیت هلال تغییر کنند.")} <a class="textlink" href="{url("calendar/")}">{L("View the full calendar", "دیدن تقویم کامل")}</a></p></div>
    </div>
    <div class="ayah" data-ayah>
      <span class="pill" style="background:#fff">{L("Ayah of the day", "آیه روز")}</span>
      <div class="ar"></div><div class="en"></div><div class="fa{L("", " lat")}"></div>
      <p class="small src" style="margin-top:10px"></p>
    </div>
  </div>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap">
  <div class="head"><div><span class="pill gr">{L("From the Maktab’s Instagram", "از اینستاگرام مکتب")}</span><h2 style="margin-top:18px">{L("Moments from our Maktab.", "لحظه‌هایی از مکتب ما")}</h2></div><a class="btn b2" href="{IG}">{L("Follow", "دنبال کنید")}&nbsp;{ltr("@maktab.alzahra.sa")}</a></div>
  {moments()}
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap">
  <span class="pill">{L("Support our work", "از کار ما حمایت کنید")}</span>
  <h2 style="margin-top:18px;max-width:800px">{L("Help us keep providing Islamic education to our community.", "به ما کمک کنید آموزش اسلامی را برای جامعه‌مان ادامه دهیم")}</h2>
  <div class="sup-g">
    <div class="card sup"><div class="im"><img src="{{A}}/premium-giving.webp" alt=""></div><div class="in"><h3>{L("Donate", "کمک مالی")}</h3><p>{L("Support the Maktab by bank transfer.", "از طریق انتقال بانکی از مکتب حمایت کنید.")}</p>
      <div class="bank"><div><span>{L("Account name", "نام حساب")}</span><b dir="ltr">{LEGAL}</b></div><div><span dir="ltr">BSB</span><b dir="ltr">065-167</b></div><div><span>{L("Account number", "شماره حساب")}</span><b dir="ltr">10581185</b></div></div>
      <div class="sp"></div><a class="btn b1" href="{url("donations/")}">{L("Donation information", "معلومات کمک مالی")}</a><p class="small">{L("Any amount, by bank transfer.", "هر مبلغ، از طریق انتقال بانکی.")}</p></div></div>
    <div class="card sup"><div class="im"><img src="{{A}}/premium-volunteer.webp" alt=""></div><div class="in"><h3>{L("Volunteer", "داوطلب شوید")}</h3><p>{L("Dedicate a day of your time, or contribute useful skills to the Maktab: community activities, practical support, or creative and digital skills.", "یک روز از وقت خود را بدهید یا مهارت‌های مفیدتان را در اختیار مکتب بگذارید: فعالیت‌های اجتماعی، کمک‌های عملی، یا مهارت‌های هنری و دیجیتال.")}</p>
      <div class="sp"></div><a class="btn b2" href="{url("volunteer/")}">{L("Ways to help", "راه‌های کمک")}</a><p class="small">{L("Give a day, or share a skill.", "یک روز وقت بدهید یا مهارتی شریک کنید.")}</p></div></div>
    <div class="card sup"><div class="im"><img src="{{A}}/courtyard-800.webp" alt=""></div><div class="in"><h3>{L("Islamic questions", "پرسش‌های دینی")}</h3><p>{L("A space for Islamic religious enquiries, reviewed by an authorised religious representative. This website does not generate religious rulings.", "جایی برای پرسش‌های دینی اسلامی که نماینده مجاز دینی آن‌ها را بررسی می‌کند. این وب‌سایت حکم دینی صادر نمی‌کند.")}</p>
      <div class="sp"></div><a class="btn b2" href="{url("questions/")}">{L("How enquiries work", "روند پرسش‌ها")}</a><p class="small">{L("Answered by an authorised representative.", "پاسخ توسط نماینده مجاز دینی.")}</p></div></div>
  </div>
</div></section>

{contact_panel()}
'''


def about():
    return phead(L("Faith, learning, community", "ایمان، دانش، جامعه"), L("About us", "درباره ما"),
                 L("Maktab Alzahra SA is an Islamic educational and community organisation in Adelaide, South Australia. We offer free Quran classes for all ages, with registration subject to Maktab staff approval.",
                   "مکتب الزهرا یک نهاد آموزشی و اجتماعی اسلامی در ادلاید، آسترالیای جنوبی است. ما کلاس‌های رایگان قرآن برای همه سنین داریم و ثبت نام نیاز به تأیید کارمندان مکتب دارد."),
                 "madinah-arch-736.webp", NOT_PREMISES()) + f'''
<section class="secs"><div class="wrap">
  <div class="grid3">
    <div class="card pad"><h3>{L("Quran education", "آموزش قرآن")}</h3><p>{L("Quran classes are free for all ages. All registrations require approval by Maktab staff. Classes are on Saturday and Sunday; students should arrive by 9:40 am and classroom doors close at 10:00 am.", "کلاس‌های قرآن برای همه سنین رایگان است. همه ثبت نام‌ها نیاز به تأیید کارمندان مکتب دارد. کلاس‌ها شنبه و یکشنبه برگزار می‌شود؛ شاگردان باید تا ۹:۴۰ صبح حاضر باشند و دروازه صنف ساعت ۱۰:۰۰ صبح بسته می‌شود.")}</p></div>
    <div class="card pad"><h3>{L("Our Adelaide community", "جامعه ما در ادلاید")}</h3><p>{L("Maktab Alzahra SA is based in Adelaide, South Australia. This website brings together information about Quran education and ways to support the Maktab.", "مکتب الزهرا در ادلاید، آسترالیای جنوبی فعالیت می‌کند. این وب‌سایت معلومات درباره آموزش قرآن و راه‌های حمایت از مکتب را یکجا فراهم می‌کند.")}</p></div>
    <div class="card pad"><h3>{L("Ways to get involved", "راه‌های همکاری")}</h3><p>{L("You can read about volunteering and financial support on this website. Volunteer applications are not currently open; donations are accepted by bank transfer.", "در این وب‌سایت می‌توانید درباره داوطلبی و حمایت مالی بخوانید. درخواست داوطلبی فعلاً باز نیست؛ کمک مالی از طریق انتقال بانکی پذیرفته می‌شود.")}</p></div>
  </div>
  <div class="card pad legal"><div><span class="pill gr">{L("Legal name", "نام قانونی")}</span><h3 style="margin-top:12px" dir="ltr">{LEGAL}</h3></div><p>{L("Maktab Alzahra SA is the name our community knows us by. Our legal name, which you will see on bank transfers and official documents, is", "مکتب الزهرا نامی است که جامعه ما را با آن می‌شناسد. نام قانونی ما که در انتقال‌های بانکی و اسناد رسمی می‌بینید این است:")} {ltr(LEGAL)}.</p></div>
  
  <div class="cta"><a class="btn b1" href="{url("registration/")}">{L("Quran class registration", "ثبت نام کلاس قرآن")}</a><a class="btn b2" href="{url("volunteer/")}">{L("Explore volunteering", "درباره داوطلبی")}</a></div>
</div></section>
{contact_panel()}'''


def registration():
    prev = [L("Student’s name", "نام شاگرد"), L("Student’s age or date of birth", "سن یا تاریخ تولد شاگرد"),
            L("School year level, for example Year 4", "صنف مکتب، مثلاً صنف ۴"), L("Address", "آدرس"),
            L("Parent or guardian’s name (for children)", "نام والدین یا سرپرست (برای کودکان)"), L("Parent or guardian’s contact details (for children)", "شماره تماس والدین یا سرپرست (برای کودکان)")]
    return phead(L("Weekend Quran classes", "کلاس‌های قرآن آخر هفته"), L("Quran class registration", "ثبت نام کلاس قرآن"),
                 L("Maktab Alzahra SA offers free Quran classes for all ages, every Saturday and Sunday, insha’Allah.", "مکتب الزهرا هر شنبه و یکشنبه، ان‌شاءالله، کلاس‌های رایگان قرآن برای همه سنین برگزار می‌کند."),
                 "premium-quran.webp", DECOR(),
                 f'<div class="cta"><a class="btn b1" href="{TEL}">{L("Call about classes", "تماس درباره کلاس‌ها")}</a><a class="btn b2" href="{MAP}">{L("View venue on map", "دیدن مکان روی نقشه")}</a></div>') + f'''
<section class="secs"><div class="wrap">
  {notice(L("Register by phone", "ثبت نام از طریق تلفن"), L("Call the Maktab every day, 8 am to 8 pm, to register. Every place is confirmed by Maktab staff.", "برای ثبت نام هر روز از ۸ صبح تا ۸ شب با مکتب تماس بگیرید. هر ثبت نام توسط کارمندان مکتب تأیید می‌شود."))}
  <h2 class="stitle">{L("Before you visit", "پیش از آمدن")}</h2>
  {facts()}
  <p class="small">{L("Questions about classes? Call the Maktab every day, 8 am to 8 pm:", "سؤالی درباره کلاس‌ها دارید؟ هر روز از ۸ صبح تا ۸ شب با مکتب تماس بگیرید:")} <a class="textlink" href="{TEL}">{phone()}</a></p>
  <div class="two" style="margin-top:26px">{steps_card()}{bring_card()}</div>
  <h2 class="stitle">{L("Registration information preview", "پیش‌نمایش معلومات ثبت نام")}</h2>
  <div class="card pad"><p>{L("The Maktab has confirmed that future registration will include school year level, address and parent or guardian information. The list below is a proposed preview, not a final list of required fields.", "مکتب تأیید کرده است که ثبت نام آینده شامل صنف مکتب، آدرس و معلومات والدین یا سرپرست خواهد بود. فهرست زیر یک پیش‌نمایش پیشنهادی است، نه فهرست نهایی.")}</p>
    <ul class="ticks">{"".join(f"<li>{i}</li>" for i in prev)}</ul></div>
  <h2 class="stitle">{L("Moments from our Maktab", "لحظه‌هایی از مکتب ما")}</h2>
  {moments()}
</div></section>
{contact_panel()}'''


def prayer_times():
    names = pnames()
    rows = "".join(f'<tr><th><i style="background:{SKY[k]}"></i>{names[k]}</th><td><b data-pray="{k}">--:--</b></td><td data-pray-tom="{k}">--:--</td></tr>' for k in SKY)
    return phead(L("Adelaide, Shia Ja‘fari method", "ادلاید، روش شیعه جعفری"), L("Prayer times", "اوقات نماز"),
                 L("A moment to pause. A day guided by prayer.", "لحظه‌ای برای درنگ. روزی در پرتو نماز."),
                 "shrine-1200.webp", "") + f'''
<section class="secs"><div class="wrap">
  <div class="head" style="align-items:center"><h2 class="stitle" style="margin:0"><span data-today></span></h2><span class="pill g" data-hijri></span></div>
  <div class="card ptwrap"><table class="pt2">
    <thead><tr><th></th><th>{L("Today", "امروز")}</th><th>{L("Tomorrow", "فردا")}</th></tr></thead>
    <tbody>{rows}</tbody></table></div>
  <h2 class="stitle">{L("Monthly timetable", "جدول ماهانه")}</h2>
  <div class="card ttwrap" data-timetable></div>
  {notice(L("How these times are calculated", "این اوقات چگونه محاسبه شده‌اند"), L("Shia Ja‘fari (Ithna-Ashari) method, Leva Institute, Qum: Fajr at 16°, Maghrib at 4° after sunset. Imsak is shown 10 minutes before Fajr as a precaution. Asr follows Dhuhr and Isha follows Maghrib; follow your marja‘s guidance on combining prayers. All times are Adelaide local time, including daylight saving.", "روش شیعه جعفری (اثنی‌عشری)، مؤسسه لواء، قم: صبح ۱۶ درجه، مغرب ۴ درجه پس از غروب. امساک برای احتیاط ۱۰ دقیقه پیش از اذان صبح نشان داده شده است. نماز عصر پس از ظهر و نماز عشا پس از مغرب خوانده می‌شود؛ درباره جمع خواندن نمازها از مرجع خود پیروی کنید. همه اوقات به وقت محلی ادلاید است."))}
</div></section>'''


def calendar():
    return phead(L("A rhythm of remembrance", "آهنگ یادآوری"), L("Shia Islamic calendar", "تقویم اسلامی شیعی"),
                 L("Explore selected Shia Islamic observances and calculated Hijri dates.", "مناسبت‌های منتخب اسلامی شیعی و تاریخ‌های هجری محاسبه‌شده را ببینید."),
                 "courtyard-800.webp", DECOR(),
                 f'<p class="lead" style="margin-top:10px"><b>{L("Today:", "امروز:")}</b> <span data-today></span>, <span data-hijri></span></p>') + f'''
<section class="secs"><div class="wrap">
  <h2 class="stitle" style="margin-top:0">{L("Coming up", "مناسبت‌های پیش رو")}</h2>
  <div class="card occs"><div data-upcoming="4"></div></div>
  <p class="small"><a class="textlink" href="{url("masoomeen/")}">{L("See all Fourteen Masoomeen and their days", "دیدن چهارده معصوم و روزهای ایشان")}</a></p>
  <h2 class="stitle">{L("Month by month", "ماه به ماه")}</h2>
  <div class="card" data-calendar></div>
  {notice(L("About these dates", "درباره این تاریخ‌ها"), L("Calculated Hijri dates are provisional. Confirm religious observances with your local Shia authority; dates may vary with moon sightings. Dates refer to the daytime; Islamic nights begin at the preceding sunset.", "تاریخ‌های هجری محاسبه‌شده موقتی‌اند. مناسبت‌های دینی را با مرجع شیعی محلی خود تأیید کنید؛ تاریخ‌ها ممکن است با رؤیت هلال تغییر کنند. تاریخ‌ها به روز اشاره دارند؛ شب‌های اسلامی از غروب روز قبل آغاز می‌شوند."))}
</div></section>'''


def donations():
    def row(label, value, lab_ltr=False):
        lab = f'<span dir="ltr">{label}</span>' if lab_ltr else f"<span>{label}</span>"
        return f'<div>{lab}<span class="v"><b dir="ltr">{value}</b><button class="copy" data-copy="{value}">{L("Copy", "کپی")}</button></span></div>'
    amts = "".join(f'<span>{ltr(a)}<small>{L("per month", "در ماه")}</small></span>' for a in ["$10", "$20", "$50", "$100"])
    return phead(L("Support our work", "از کار ما حمایت کنید"), L("Financial donations", "کمک‌های مالی"),
                 L("Support the Maktab by bank transfer using the details below.", "با استفاده از معلومات زیر، از طریق انتقال بانکی از مکتب حمایت کنید."),
                 "premium-giving.webp", DECOR()) + f'''
<section class="secs"><div class="wrap">
  <h2 class="stitle" style="margin-top:0">{L("Donate by bank transfer", "کمک از طریق انتقال بانکی")}</h2>
  <p class="lead" style="max-width:760px">{L("Copy the details below. In your banking app, start a bank transfer, enter your donation amount and check the recipient before confirming.", "معلومات زیر را کپی کنید. در اپلیکیشن بانک خود انتقال بانکی را آغاز کنید، مبلغ کمک را وارد کنید و پیش از تأیید، گیرنده را بررسی کنید.")}</p>
  <div class="bank big card">{row(L("Account name", "نام حساب"), LEGAL)}{row("BSB", "065-167", True)}{row(L("Account number", "شماره حساب"), "10581185")}</div>
  <p class="small">{L("The account is in the Maktab’s legal name,", "حساب به نام قانونی مکتب است:")} <b>{ltr(LEGAL)}</b>{L(". Your bank will show this name as the recipient.", ". بانک شما این نام را به عنوان گیرنده نشان می‌دهد.")}</p>
  <div class="grid2">
    <div class="card pad"><h3>{L("One-off giving", "کمک یک‌باره")}</h3><p>{L("A single contribution made on one occasion, without an ongoing payment commitment.", "کمکی که یک بار پرداخت می‌شود، بدون تعهد پرداخت دوامدار.")}</p></div>
    <div class="card pad"><h3>{L("Donate monthly", "کمک ماهانه")}</h3><p>{L("Set up a recurring transfer in your banking app with the details above, for example:", "با همین معلومات در اپ بانکی خود یک انتقال ماهانه تنظیم کنید، برای مثال:")}</p><div class="amts">{amts}</div></div>
  </div>
  {notice(L("Questions about donating?", "سؤالی درباره کمک مالی دارید؟"), L("Contact the Maktab if you have a question about your transfer:", "اگر درباره انتقال خود سؤالی دارید با مکتب تماس بگیرید:") + f' <a class="textlink" href="{TEL}">{phone()}</a>')}
  <div class="cta"><a class="btn b2" href="{url("volunteer/")}">{L("Give your time or skills", "وقت یا مهارت خود را بدهید")}</a></div>
</div></section>'''


def volunteer():
    asks = [L("Your name and preferred contact method", "نام شما و روش تماس دلخواه"), L("Whether you would like to offer a day of your time or share skills", "اینکه می‌خواهید یک روز وقت بگذارید یا مهارت‌تان را شریک کنید"),
            L("Activities that interest you and skills you would like to contribute", "فعالیت‌هایی که به آن علاقه دارید و مهارت‌هایی که می‌خواهید ارائه کنید"), L("Your general availability", "زمان‌هایی که معمولاً وقت دارید")]
    return phead(L("Give time, share skills", "وقت بگذارید، مهارت شریک کنید"), L("Volunteer opportunities", "فرصت‌های داوطلبی"),
                 L("Dedicate a day of your time or contribute useful skills to the Maktab.", "یک روز از وقت خود را بدهید یا مهارت‌های مفیدتان را در اختیار مکتب بگذارید."),
                 "premium-volunteer.webp", DECOR()) + f'''
<section class="secs"><div class="wrap">
  {notice(L("Want to help?", "می‌خواهید کمک کنید؟"), L("Call the Maktab every day, 8 am to 8 pm, and tell us how you would like to help.", "هر روز از ۸ صبح تا ۸ شب با مکتب تماس بگیرید و بگویید چگونه می‌خواهید کمک کنید."))}
  <div class="grid2">
    <div class="card pad"><h3>{L("Dedicate a day", "یک روز وقت بگذارید")}</h3><p>{L("Offer a day of your time to help with an agreed activity. We agree the date and the task with you.", "یک روز از وقت خود را برای کمک در یک فعالیت توافق‌شده بدهید. تاریخ و کار با شما هماهنگ می‌شود.")}</p></div>
    <div class="card pad"><h3>{L("Contribute your skills", "مهارت خود را ارائه کنید")}</h3><p>{L("Share useful practical, organisational or creative skills. We match you with what the Maktab needs.", "مهارت‌های عملی، سازماندهی یا هنری خود را شریک کنید. ما شما را با نیازهای مکتب هماهنگ می‌کنیم.")}</p></div>
  </div>
  <h2 class="stitle">{L("Ways you could help", "راه‌هایی که می‌توانید کمک کنید")}</h2>
  
  <div class="grid3">
    <div class="card pad"><h3>{L("Community activities", "فعالیت‌های اجتماعی")}</h3><p>{L("For example, helping prepare a space or organise materials for an activity.", "مثلاً کمک در آماده کردن مکان یا منظم کردن لوازم یک برنامه.")}</p></div>
    <div class="card pad"><h3>{L("Practical support", "کمک‌های عملی")}</h3><p>{L("For example, helping organise resources or contributing useful practical skills.", "مثلاً کمک در منظم کردن منابع یا ارائه مهارت‌های عملی مفید.")}</p></div>
    <div class="card pad"><h3>{L("Creative and digital skills", "مهارت‌های هنری و دیجیتال")}</h3><p>{L("For example, contributing design, translation or technology skills.", "مثلاً مهارت در دیزاین، ترجمه یا تکنالوژی.")}</p></div>
  </div>
  <h2 class="stitle">{L("When you call, we may ask about", "وقتی تماس می‌گیرید، ممکن است بپرسیم")}</h2>
  <div class="card pad"><ul class="ticks">{"".join(f"<li>{i}</li>" for i in asks)}</ul></div>
  <div class="cta"><a class="btn b1" href="{url("donations/")}">{L("Learn about donations", "درباره کمک مالی")}</a><a class="btn b2" href="{url("contact/")}">{L("Contact us", "تماس با ما")}</a></div>
</div></section>'''


def questions():
    def st(n, title, text):
        return f'<div class="card pad"><div class="num">{n}</div><h3>{title}</h3><p>{text}</p></div>'
    return phead(L("Faith, learning, community", "ایمان، دانش، جامعه"), L("Islamic religious questions", "پرسش‌های دینی اسلامی"),
                 L("A space for Islamic religious enquiries, reviewed by an authorised religious representative.", "جایی برای پرسش‌های دینی اسلامی که نماینده مجاز دینی آن‌ها را بررسی می‌کند."),
                 "courtyard-800.webp", DECOR()) + f'''
<section class="secs"><div class="wrap">
  {notice(L("Coming soon", "به‌زودی"), L("A way to send your questions is being prepared. Until then, please contact the Maktab.", "راهی برای فرستادن پرسش‌ها در حال آماده شدن است. تا آن زمان لطفاً با مکتب تماس بگیرید."))}
  <h2 class="stitle">{L("How it will work", "روند کار")}</h2>
  
  <div class="grid3">
    {st(L("1", "۱"), L("Read the service information", "معلومات خدمت را بخوانید"), L("Review the service scope, privacy information and instructions before sending an enquiry.", "پیش از ارسال پرسش، محدوده خدمت، معلومات حریم خصوصی و رهنمودها را بخوانید."))}
    {st(L("2", "۲"), L("Prepare your question", "پرسش خود را آماده کنید"), L("Write your question clearly and include a way for us to reply.", "پرسش خود را روشن بنویسید و راهی برای پاسخ دادن بگذارید."))}
    {st(L("3", "۳"), L("Review by an authorised representative", "بررسی توسط نماینده مجاز"), L("The authorised religious representative would review the enquiry and determine an appropriate response.", "نماینده مجاز دینی پرسش را بررسی کرده و پاسخ مناسب را تعیین می‌کند."))}
  </div>
  <div class="card pad"><h3>{L("Human guidance", "رهنمایی انسانی")}</h3><p>{L("This website does not generate religious rulings or automatically answer religious questions.", "این وب‌سایت حکم دینی صادر نمی‌کند و به پرسش‌های دینی به‌طور خودکار پاسخ نمی‌دهد.")}</p></div>
</div></section>'''


def contact():
    return phead(L("Get in touch", "تماس با ما"), L("Contact us", "تماس با ما"),
                 L("Find our class venue in Ingle Farm, South Australia, and the phone number for Quran class enquiries.", "مکان کلاس ما در اینگل فارم، آسترالیای جنوبی، و شماره تماس برای پرسش درباره کلاس‌های قرآن."),
                 "madinah-green-dome-736.webp", NOT_PREMISES(),
                 f'<div class="cta"><a class="btn b1" href="{TEL}">{L("Call", "تماس")}&nbsp;&nbsp;{phone()}</a><a class="btn b2" href="{MAP}">{L("View address on map", "دیدن آدرس روی نقشه")}</a></div>') + f'''
<section class="secs"><div class="wrap">
  <div class="grid2">
    <div class="card pad"><span class="pill gr">{L("Quran class enquiries", "پرسش درباره کلاس‌های قرآن")}</span><h3 style="margin-top:14px">{L("Call the Maktab", "با مکتب تماس بگیرید")}</h3>
      <a href="{TEL}" style="display:block;font:var(--dw) 54px/1.2 var(--display);color:var(--green);margin:6px 0">{phone()}</a>
      <p>{L("Every day, 8 am to 8 pm.", "هر روز، ۸ صبح تا ۸ شب.")}</p><p style="margin-top:10px">{L("Classes are on Saturday and Sunday. Please arrive by 9:40 am; classroom doors close at 10:00 am.", "کلاس‌ها شنبه و یکشنبه است. لطفاً تا ۹:۴۰ صبح حاضر باشید؛ دروازه صنف ساعت ۱۰:۰۰ صبح بسته می‌شود.")}</p></div>
    <div class="card pad"><span class="pill">{L("Class venue", "مکان کلاس")}</span><h3 style="margin-top:14px">{L("Find us", "ما را پیدا کنید")}</h3>
      <p style="font:var(--dw) 30px/1.3 var(--display);color:var(--ink);margin:6px 0">{ltr("20 Kylie Crescent,")}<br>{ltr("Ingle Farm, SA")}</p>
      <p>{L("Confirm the class time before travelling.", "پیش از حرکت، زمان کلاس را تأیید کنید.")}</p><a class="btn b2" style="margin-top:18px" href="{MAP}">{L("View address on map", "دیدن آدرس روی نقشه")}</a></div>
  </div>
  <div class="card pad"><h3>{L("Social media", "شبکه‌های اجتماعی")}</h3><p>{L("Follow Maktab Alzahra SA on Instagram and YouTube, or join our WhatsApp channel for updates.", "مکتب الزهرا را در اینستاگرام و یوتیوب دنبال کنید، یا برای تازه‌ترین خبرها به کانال واتساپ ما بپیوندید.")}</p>
    <div class="cta" style="margin-top:18px"><a class="btn b2" href="{IG}">{L("Instagram", "اینستاگرام")}</a><a class="btn b2" href="{YT}">{L("YouTube", "یوتیوب")}</a><a class="btn b2" href="{WA}">{L("WhatsApp channel", "کانال واتساپ")}</a></div></div>
  <div class="card pad legal"><div><span class="pill gr">{L("Legal name", "نام قانونی")}</span><h3 style="margin-top:12px" dir="ltr">{LEGAL}</h3></div><p>{L("Use this name for bank transfers and official correspondence with Maktab Alzahra SA.", "برای انتقال بانکی و مکاتبات رسمی با مکتب الزهرا از این نام استفاده کنید.")}</p></div>
</div></section>'''


def masoomeen():
    return phead(L("The Ahl al-Bayt (AS)", "اهل بیت (ع)"), L("The Fourteen Masoomeen", "چهارده معصوم"),
                 L("The Prophet (S), his daughter and the twelve Imams (AS). This website celebrates each of their births and mourns each of their martyrdoms, following the Shia calendar.", "پیامبر اکرم (ص)، دختر گرامی‌اش و دوازده امام (ع). این وب‌سایت طبق تقویم شیعی، ولادت هر یک را جشن می‌گیرد و در شهادت هر یک عزادار می‌شود."),
                 "madinah-green-dome-736.webp", NOT_PREMISES()) + f'''
<section class="secs"><div class="wrap">
  <div class="mzgrid" data-masoomeen></div>
  {notice(L("About these dates", "درباره این تاریخ‌ها"), L("These are commonly cited Shia dates, and some differ between narrations. The Gregorian dates are calculated and may vary by a day with the moon sighting.", "این‌ها تاریخ‌های مشهور شیعی‌اند و برخی در روایات مختلف فرق دارند. تاریخ‌های میلادی محاسبه‌شده‌اند و ممکن است با رؤیت هلال یک روز تفاوت کنند."))}
  <div class="cta"><a class="btn b1" href="{url("calendar/")}">{L("View the calendar", "دیدن تقویم")}</a></div>
</div></section>'''


PAGES = [  # slug, builder, (title en, title fa)
    ("", home, ("Quran classes in Adelaide", "کلاس‌های قرآن در ادلاید")),
    ("about/", about, ("About us", "درباره ما")),
    ("registration/", registration, ("Quran class registration", "ثبت نام کلاس قرآن")),
    ("prayer-times/", prayer_times, ("Prayer times in Adelaide", "اوقات نماز در ادلاید")),
    ("calendar/", calendar, ("Shia Islamic calendar", "تقویم اسلامی شیعی")),
    ("donations/", donations, ("Financial donations", "کمک‌های مالی")),
    ("volunteer/", volunteer, ("Volunteer opportunities", "فرصت‌های داوطلبی")),
    ("questions/", questions, ("Islamic religious questions", "پرسش‌های دینی اسلامی")),
    ("contact/", contact, ("Contact us", "تماس با ما")),
    ("masoomeen/", masoomeen, ("The Fourteen Masoomeen", "چهارده معصوم")),
]


def layout(slug, title, body):
    A = "../" * (2 if slug else 1) + "assets"
    other = "fa" if LANG == "en" else "en"
    name = L("Maktab Alzahra SA", "مکتب الزهرا")
    nav = [("", L("Home", "خانه")), ("about/", L("About", "درباره ما")), ("registration/", L("Quran classes", "کلاس‌های قرآن")),
           ("prayer-times/", L("Prayer times", "اوقات نماز")), ("calendar/", L("Calendar", "تقویم")), ("contact/", L("Contact", "تماس"))]
    more = [("masoomeen/", L("14 Masoomeen", "چهارده معصوم")), ("donations/", L("Donations", "کمک مالی")), ("volunteer/", L("Volunteer", "داوطلبی")), ("questions/", L("Questions", "پرسش‌ها"))]
    links = "".join(f'<a href="{url(s)}"{" class=on" if s == slug else ""}>{t}</a>' for s, t in nav)
    mlinks = "".join(f'<a href="{url(s)}"{" class=on" if s == slug else ""}><span>{t}</span><i></i></a>' for s, t in nav + more)
    en_cls, fa_cls = ("on", "fa") if LANG == "en" else ("", "on fa")
    desc = L("Free Quran classes for all ages in Adelaide. Maktab Alzahra SA is a place for Islamic education and community.", "کلاس‌های رایگان قرآن برای همه سنین در ادلاید. مکتب الزهرا جایی برای آموزش اسلامی و جامعه است.")
    ld = ""
    if not slug:
        import json
        ld = '<script type="application/ld+json">' + json.dumps({
            "@context": "https://schema.org", "@type": "EducationalOrganization", "name": "Maktab Alzahra SA", "legalName": LEGAL,
            "url": BASE + "/" + LANG + "/", "logo": BASE + "/assets/logo-288.png", "image": BASE + "/assets/share.jpg",
            "description": desc, "telephone": "+61414012964",
            "address": {"@type": "PostalAddress", "streetAddress": "20 Kylie Crescent", "addressLocality": "Ingle Farm", "addressRegion": "SA", "addressCountry": "AU"},
            "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Saturday", "Sunday"], "opens": "09:40"}],
            "sameAs": [IG, YT, WA]}, ensure_ascii=False) + "</script>"
    html = f'''<!doctype html>
<html lang="{LANG}" dir="{L("ltr", "rtl")}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | {name}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}/{LANG}/{slug}">
<link rel="alternate" hreflang="en" href="{BASE}/en/{slug}">
<link rel="alternate" hreflang="fa" href="{BASE}/fa/{slug}">
<link rel="alternate" hreflang="x-default" href="{BASE}/en/{slug}">
<meta name="theme-color" content="#0f5a33">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Maktab Alzahra SA">
<meta property="og:title" content="{title} | {name}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{BASE}/{LANG}/{slug}">
<meta property="og:image" content="{BASE}/assets/share.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{L("en_AU", "fa_AF")}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{{A}}/logo-288.png">
<link rel="apple-touch-icon" href="{{A}}/logo-288.png">
{ld}
<link rel="stylesheet" href="{{A}}/style.css?v=15">
</head>
<body>
<a class="skip" href="#main">{L("Skip to content", "رفتن به محتوا")}</a>
<div class="navwrap"><div class="wrap">
  <nav>
    <a class="l" href="{url()}"><img src="{{A}}/logo-160.webp" alt="Maktab Al-Zahra"><span class="bn"><b>{name}</b><small dir="ltr">{LEGAL}</small></span></a>
    <div class="m">{links}</div>
    <div class="r"><div class="lang"><a class="{en_cls}" href="/en/{slug}">EN</a><a class="{fa_cls}" href="/fa/{slug}">دری</a></div><a class="btn b1" href="{TEL}">{L("Call", "تماس")}&nbsp;&nbsp;{phone()}</a>
      <button class="burger" data-menu aria-label="{L("Menu", "منو")}"><svg width="18" height="12" viewBox="0 0 18 12" stroke="#fff" stroke-width="2" stroke-linecap="round"><path d="M1 1h16M1 6h16M1 11h16"/></svg></button></div>
  </nav>
</div></div>
<div class="mmenu" aria-hidden="true" role="dialog" aria-label="{L("Menu", "منو")}">
  <div class="mm-top"><a class="l" href="{url()}"><img src="{{A}}/logo-160.webp" alt=""><span class="bn"><b>{name}</b><small dir="ltr">{LEGAL}</small></span></a><button class="x" data-menu aria-label="{L("Close", "بستن")}"><svg width="16" height="16" viewBox="0 0 16 16" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M2 2l12 12M14 2L2 14"/></svg></button></div>
  <div class="mm-links">{mlinks}</div>
  <div class="mm-foot">
    <a class="btn mm-call" href="{TEL}">{L("Call", "تماس")}&nbsp;&nbsp;{phone()}</a>
    <div class="mm-row"><div class="lang"><a class="{en_cls}" href="/en/{slug}">English</a><a class="{fa_cls}" href="/fa/{slug}">دری</a></div>
    <div class="mm-soc"><a href="{IG}">{L("Instagram", "اینستاگرام")}</a><a href="{YT}">{L("YouTube", "یوتیوب")}</a><a href="{WA}">{L("WhatsApp", "واتساپ")}</a></div></div>
  </div>
</div>
<main id="main">{body}</main>
<footer><div class="wrap">
  <div class="ftop">
    <a class="mapc" href="{MAP}" aria-label="{L("Directions to 20 Kylie Crescent, Ingle Farm", "مسیریابی به آدرس مکتب")}">{MAPSVG}<span class="pin">{name}</span>
      <span class="addr"><span><b>{ltr("20 Kylie Crescent, Ingle Farm")}</b><small>{L("Saturday and Sunday, arrive by 9:40 am", "شنبه و یکشنبه، حضور تا ۹:۴۰ صبح")}</small></span><span class="btn b1">{L("Directions", "مسیریابی")}</span></span></a>
    <div class="prc"><div class="h"><b>{L("Today in Adelaide", "امروز در ادلاید")}</b><span data-hijri></span></div>
      <div class="g">{"".join(f'<div class="p"><span data-label>{v}</span><b data-pray="{k}">--:--</b></div>' for k, v in pnames().items())}</div>
      <div class="sal" lang="ar">اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَآلِ مُحَمَّد</div></div>
  </div>
  <div class="foot">
    <div><div class="l"><img src="{{A}}/logo-160.webp" alt=""><span class="bn"><b>{name}</b><small dir="ltr">{LEGAL}</small></span></div><p>{L("An Islamic educational and community organisation in Adelaide.", "یک نهاد آموزشی و اجتماعی اسلامی در ادلاید.")}</p></div>
    <div><h5>{L("Learn", "آموزش")}</h5><ul>{"".join(f'<li><a href="{url(s2)}">{t}</a></li>' for s2, t in [("registration/", L("Quran classes", "کلاس‌های قرآن")), ("prayer-times/", L("Prayer times", "اوقات نماز")), ("calendar/", L("Islamic calendar", "تقویم اسلامی")), ("masoomeen/", L("14 Masoomeen", "چهارده معصوم"))])}</ul></div>
    <div><h5>{L("Support", "حمایت")}</h5><ul>{"".join(f'<li><a href="{url(s2)}">{t}</a></li>' for s2, t in [("donations/", L("Donations", "کمک مالی")), ("volunteer/", L("Volunteer", "داوطلبی")), ("questions/", L("Islamic questions", "پرسش‌های دینی")), ("about/", L("About us", "درباره ما"))])}</ul></div>
    <div class="fcon"><h5>{L("Contact", "تماس")}</h5><a class="fcall" href="{TEL}">{phone()}</a><p class="fhrs">{L("Every day, 8 am to 8 pm", "هر روز، ۸ صبح تا ۸ شب")}</p><div class="fsoc"><a href="{IG}">{L("Instagram", "اینستاگرام")}</a><a href="{YT}">{L("YouTube", "یوتیوب")}</a><a href="{WA}">{L("WhatsApp", "واتساپ")}</a></div></div>
  </div>
  <div class="fb"><span>{L("© 2026 Maktab Alzahra SA", "© ۲۰۲۶ مکتب الزهرا")} ({ltr(LEGAL)}){L(", Adelaide, South Australia", "، ادلاید، آسترالیای جنوبی")}</span><span><a href="/en/{slug}">English</a> | <a class="fa" href="/fa/{slug}">دری</a></span></div>
</div></footer>
<script src="{{A}}/calc.js?v=3"></script>
<script src="{{A}}/people.js?v=2"></script>
<script src="{{A}}/app.js?v=6"></script>
<script src="{{A}}/mood.js?v=9"></script>
</body>
</html>
'''
    html = html.replace(' class=on>', ' class=on aria-current="page">')
    html = html.replace(' ar"', ' ar" lang="ar"').replace('class="ar"', 'class="ar" lang="ar"')
    head, sep, rest = html.partition('<main id="main">')
    rest = rest.replace('<img src=', '<img loading="lazy" decoding="async" src=')
    rest = rest.replace('<img loading="lazy" decoding="async" src=', '<img fetchpriority="high" decoding="async" src=', 1)
    return (head + sep + rest).replace("{A}", A)


def notfound():
    return f'''<header class="phead"><div class="wrap"><div class="phead-g">
  <div><span class="pill">{L("Page not found", "صفحه پیدا نشد")}</span><h1>{L("This page isn’t here.", "این صفحه اینجا نیست")}</h1>
    <p class="lead">{L("The link may be old, or the address may have a typo. These pages can help you find what you need.", "ممکن است لینک قدیمی باشد یا آدرس اشتباه نوشته شده باشد. این صفحه‌ها می‌توانند کمک کنند.")}</p>
    <div class="cta"><a class="btn b1" href="{url()}">{L("Go to the home page", "رفتن به صفحه اصلی")}</a><a class="btn b2" href="{url("registration/")}">{L("Quran classes", "کلاس‌های قرآن")}</a><a class="btn b2" href="{url("contact/")}">{L("Contact us", "تماس با ما")}</a></div></div>
  <div><div class="ph"><img src="{{A}}/madinah-arch-736.webp" alt=""></div></div>
</div></div></header>'''


def build():
    global LANG
    assets = os.path.join(OUT, "assets")
    os.makedirs(os.path.join(assets, "fonts"), exist_ok=True)
    for f in ("app.js", "calc.js", "mood.js", "people.js"):
        shutil.copy(os.path.join(ROOT, "src", f), assets)
    fonts = os.path.join(ROOT, "src", "fonts")
    for f in os.listdir(fonts):
        if f.endswith(".woff2"):
            shutil.copy(os.path.join(fonts, f), os.path.join(assets, "fonts"))
    with open(os.path.join(assets, "style.css"), "w", encoding="utf-8") as fh:  # the fonts and the design in one file
        fh.write(open(os.path.join(fonts, "fonts.css"), encoding="utf-8").read() + open(os.path.join(ROOT, "src", "style.css"), encoding="utf-8").read())
    for f in os.listdir(os.path.join(ROOT, "src", "images")):
        shutil.copy(os.path.join(ROOT, "src", "images", f), assets)
    urls = []
    for LANG in ("en", "fa"):
        for slug, fn, titles in PAGES:
            d = os.path.join(OUT, LANG, slug)
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
                fh.write(layout(slug, L(*titles), fn()))
            urls.append(f"{BASE}/{LANG}/{slug}")
    LANG = "en"
    page = layout("404/", "Page not found", notfound()).replace("../../assets", "/assets").replace('<link rel="canonical" href="' + BASE + '/en/404/">', '<meta name="robots" content="noindex">')
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as fh:
        fh.write(page)
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as fh:
        fh.write('<!doctype html><meta charset="utf-8"><title>Maktab Alzahra SA</title><meta http-equiv="refresh" content="0; url=/en/"><link rel="canonical" href="' + BASE + '/en/"><a href="/en/">Maktab Alzahra SA</a>\n')
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    with open(os.path.join(OUT, ".htaccess"), "w", encoding="utf-8") as fh:
        fh.write("ErrorDocument 404 /404.html\n<IfModule mod_expires.c>\nExpiresActive On\nExpiresByType font/woff2 \"access plus 1 year\"\nExpiresByType image/webp \"access plus 1 month\"\nExpiresByType image/png \"access plus 1 month\"\nExpiresByType image/jpeg \"access plus 1 month\"\n</IfModule>\n")
    print("built", len(PAGES) * 2, "pages into", OUT)


if __name__ == "__main__":
    build()
