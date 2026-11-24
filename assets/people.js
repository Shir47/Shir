/* The Fourteen Masoomeen (AS) and the days the site observes.
   Dates are the commonly cited Shia dates. Maktab staff should confirm them. */
var MZP=(function(){
  var S='السَّلَامُ عَلَيْكَ ';
  /* [English name, Dari name, title, Dari title, short calligraphy, salutation, petal colours] */
  var P=[
    ['Prophet Muhammad (S)','حضرت محمد (ص)','The Messenger of Allah','پیامبر خدا','يا رسول الله',S+'يَا رَسُولَ اللَّه','green'],
    ['Lady Fatimah al-Zahra (AS)','حضرت فاطمه زهرا (س)','Daughter of the Prophet (S)','دختر پیامبر (ص)','يا فاطمة الزهراء','السَّلَامُ عَلَيْكِ يَا فَاطِمَةُ الزَّهْرَاء','rose'],
    ['Imam Ali (AS)','امام علی (ع)','Amir al-Mu’minin, the 1st Imam','امیرالمؤمنین، امام اول','يا علي',S+'يَا أَمِيرَ الْمُؤْمِنِين','gold'],
    ['Imam Hasan (AS)','امام حسن مجتبی (ع)','Al-Mujtaba, the 2nd Imam','مجتبی، امام دوم','يا حسن',S+'يَا حَسَنَ بْنَ عَلِيٍّ الْمُجْتَبَى','green'],
    ['Imam Husayn (AS)','امام حسین (ع)','Sayyid al-Shuhada, the 3rd Imam','سیدالشهدا، امام سوم','يا حسين',S+'يَا أَبَا عَبْدِ اللَّهِ الْحُسَيْن','gold'],
    ['Imam Ali Zayn al-Abidin (AS)','امام سجاد (ع)','Al-Sajjad, the 4th Imam','زین‌العابدین، امام چهارم','يا سجاد',S+'يَا عَلِيَّ بْنَ الْحُسَيْنِ زَيْنَ الْعَابِدِين','green'],
    ['Imam Muhammad al-Baqir (AS)','امام محمد باقر (ع)','Al-Baqir, the 5th Imam','باقرالعلوم، امام پنجم','يا باقر',S+'يَا مُحَمَّدَ بْنَ عَلِيٍّ الْبَاقِر','gold'],
    ['Imam Ja‘far al-Sadiq (AS)','امام جعفر صادق (ع)','Al-Sadiq, the 6th Imam','صادق، امام ششم','يا صادق',S+'يَا جَعْفَرَ بْنَ مُحَمَّدٍ الصَّادِق','green'],
    ['Imam Musa al-Kazim (AS)','امام موسی کاظم (ع)','Al-Kazim, the 7th Imam','کاظم، امام هفتم','يا كاظم',S+'يَا مُوسَى بْنَ جَعْفَرٍ الْكَاظِم','gold'],
    ['Imam Ali al-Rida (AS)','امام رضا (ع)','Al-Rida, the 8th Imam','رضا، امام هشتم','يا رضا',S+'يَا عَلِيَّ بْنَ مُوسَى الرِّضَا','gold'],
    ['Imam Muhammad al-Jawad (AS)','امام جواد (ع)','Al-Jawad, the 9th Imam','جواد، امام نهم','يا جواد',S+'يَا مُحَمَّدَ بْنَ عَلِيٍّ الْجَوَاد','green'],
    ['Imam Ali al-Hadi (AS)','امام هادی (ع)','Al-Hadi, the 10th Imam','هادی، امام دهم','يا هادي',S+'يَا عَلِيَّ بْنَ مُحَمَّدٍ الْهَادِي','gold'],
    ['Imam Hasan al-Askari (AS)','امام حسن عسکری (ع)','Al-Askari, the 11th Imam','عسکری، امام یازدهم','يا عسكري',S+'يَا حَسَنَ بْنَ عَلِيٍّ الْعَسْكَرِي','green'],
    ['Imam al-Mahdi (AJ)','امام مهدی (عج)','Sahib al-Zaman, the 12th Imam','صاحب‌الزمان، امام دوازدهم','يا مهدي',S+'يَا صَاحِبَ الزَّمَان','green']
  ];
  /* [Hijri month, day, English, Dari, mood ('j' joy, 'm' mourning, '' none), person index, days before, days after, kind ('b' birth, 'm' martyrdom)] */
  var EV=[
    [1,1,'Islamic New Year, start of Muharram','آغاز سال نو هجری و ماه محرم','',-1,0,0,''],
    [1,10,'Ashura, martyrdom of Imam Husayn (AS)','عاشورا، شهادت امام حسین (ع)','m',4,9,2,'m'],
    [1,25,'Martyrdom of Imam Zayn al-Abidin (AS)','شهادت امام سجاد (ع)','m',5,2,1,'m'],
    [2,7,'Birth of Imam Musa al-Kazim (AS)','ولادت امام موسی کاظم (ع)','',8,0,0,'b'],
    [2,20,'Arbaeen of Imam Husayn (AS)','اربعین امام حسین (ع)','m',4,3,1,''],
    [2,28,'Passing of Prophet Muhammad (S) and martyrdom of Imam Hasan (AS)','رحلت پیامبر اکرم (ص) و شهادت امام حسن مجتبی (ع)','m',0,3,0,'m'],
    [2,29,'Martyrdom of Imam al-Rida (AS)','شهادت امام رضا (ع)','m',9,0,1,'m'],
    [3,8,'Martyrdom of Imam Hasan al-Askari (AS)','شهادت امام حسن عسکری (ع)','m',12,2,1,'m'],
    [3,17,'Birth of Prophet Muhammad (S) and Imam al-Sadiq (AS)','ولادت پیامبر اکرم (ص) و امام جعفر صادق (ع)','j',0,7,1,'b'],
    [4,8,'Birth of Imam Hasan al-Askari (AS)','ولادت امام حسن عسکری (ع)','j',12,3,1,'b'],
    [5,13,'Martyrdom of Lady Fatimah (AS), first narration','شهادت حضرت فاطمه (س)، روایت اول','m',1,3,1,''],
    [6,3,'Martyrdom of Lady Fatimah (AS), second narration','شهادت حضرت فاطمه (س)، روایت دوم','m',1,3,1,'m'],
    [6,20,'Birth of Lady Fatimah al-Zahra (AS)','ولادت حضرت فاطمه زهرا (س)','j',1,7,1,'b'],
    [7,1,'Birth of Imam Muhammad al-Baqir (AS)','ولادت امام محمد باقر (ع)','j',6,3,0,'b'],
    [7,3,'Martyrdom of Imam Ali al-Hadi (AS)','شهادت امام هادی (ع)','m',11,1,1,'m'],
    [7,10,'Birth of Imam Muhammad al-Jawad (AS)','ولادت امام جواد (ع)','j',10,3,1,'b'],
    [7,13,'Birth of Imam Ali (AS)','ولادت امام علی (ع)','j',2,2,1,'b'],
    [7,25,'Martyrdom of Imam Musa al-Kazim (AS)','شهادت امام موسی کاظم (ع)','m',8,2,1,'m'],
    [7,27,'Mab‘ath of Prophet Muhammad (S)','مبعث پیامبر اکرم (ص)','j',0,1,1,''],
    [8,3,'Birth of Imam Husayn (AS)','ولادت امام حسین (ع)','j',4,3,1,'b'],
    [8,5,'Birth of Imam Zayn al-Abidin (AS)','ولادت امام سجاد (ع)','j',5,0,1,'b'],
    [8,15,'Birth of Imam al-Mahdi (AJ)','ولادت امام مهدی (عج)','j',13,7,1,'b'],
    [9,1,'First day of Ramadan','آغاز ماه رمضان','',-1,0,0,''],
    [9,15,'Birth of Imam Hasan (AS)','ولادت امام حسن مجتبی (ع)','j',3,3,1,'b'],
    [9,21,'Martyrdom of Imam Ali (AS)','شهادت امام علی (ع)','m',2,2,1,'m'],
    [10,1,'Eid al-Fitr','عید فطر','j',-1,1,2,''],
    [10,25,'Martyrdom of Imam Ja‘far al-Sadiq (AS)','شهادت امام جعفر صادق (ع)','m',7,2,1,'m'],
    [11,11,'Birth of Imam al-Rida (AS)','ولادت امام رضا (ع)','j',9,5,1,'b'],
    [11,30,'Martyrdom of Imam Muhammad al-Jawad (AS)','شهادت امام جواد (ع)','m',10,2,1,'m'],
    [12,7,'Martyrdom of Imam Muhammad al-Baqir (AS)','شهادت امام محمد باقر (ع)','m',6,2,1,'m'],
    [12,10,'Eid al-Adha','عید قربان','j',-1,1,2,''],
    [12,15,'Birth of Imam Ali al-Hadi (AS)','ولادت امام هادی (ع)','j',11,2,1,'b'],
    [12,18,'Eid al-Ghadir','عید غدیر','j',2,2,1,'']
  ];
  return {P:P,EV:EV};
})();
