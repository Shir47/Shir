/* Prayer times (Ja'fari: Fajr 16, Maghrib 4, Isha 14) and Hijri dates for Adelaide. */
var MZ=(function(){
  var LAT=-34.9285,LNG=138.6007,TZ='Australia/Adelaide',HCAL='islamic-civil';
  var r=Math.PI/180,sin=function(d){return Math.sin(d*r)},cos=function(d){return Math.cos(d*r)},tan=function(d){return Math.tan(d*r)};
  var asin=function(x){return Math.asin(x)/r},acos=function(x){return Math.acos(x)/r},atan2=function(y,x){return Math.atan2(y,x)/r},acot=function(x){return Math.atan(1/x)/r};
  var fix=function(a,b){a=a-b*Math.floor(a/b);return a<0?a+b:a};
  function jd(y,m,d){if(m<=2){y-=1;m+=12}var A=Math.floor(y/100),B=2-A+Math.floor(A/4);return Math.floor(365.25*(y+4716))+Math.floor(30.6001*(m+1))+d+B-1524.5}
  function sun(j){var D=j-2451545,g=fix(357.529+0.98560028*D,360),q=fix(280.459+0.98564736*D,360),L=fix(q+1.915*sin(g)+0.020*sin(2*g),360),e=23.439-0.00000036*D;
    return {decl:asin(sin(e)*sin(L)),eqt:q/15-fix(atan2(cos(e)*sin(L),cos(L))/15,24)}}
  function tzOffset(y,m,d){var u=new Date(Date.UTC(y,m-1,d,12));var p=parts(u);return (Date.UTC(p.y,p.m-1,p.d,p.h,p.mi)-u.getTime())/36e5}
  function parts(date){var f=new Intl.DateTimeFormat('en-GB',{timeZone:TZ,year:'numeric',month:'numeric',day:'numeric',hour:'numeric',minute:'numeric',weekday:'short',hourCycle:'h23'}).formatToParts(date),o={};
    f.forEach(function(x){o[x.type]=x.value});return {y:+o.year,m:+o.month,d:+o.day,h:+o.hour,mi:+o.minute,wd:['Sun','Mon','Tue','Wed','Thu','Fri','Sat'].indexOf(o.weekday)}}
  function times(y,m,d){
    var J=jd(y,m,d)-LNG/(15*24),tz=tzOffset(y,m,d);
    function mid(t){return fix(12-sun(J+t).eqt,24)}
    function ang(a,t,ccw){var dc=sun(J+t).decl,n=mid(t),T=acos((-sin(a)-sin(dc)*sin(LAT))/(cos(dc)*cos(LAT)))/15;return n+(ccw?-T:T)}
    function asr(f,t){var dc=sun(J+t).decl;return ang(-acot(f+tan(Math.abs(LAT-dc))),t)}
    var t={fajr:5,sunrise:6,dhuhr:12,asr:13,sunset:18,maghrib:18,isha:18};
    for(var i=0;i<2;i++){t={fajr:ang(16,t.fajr/24,1),sunrise:ang(0.833,t.sunrise/24,1),dhuhr:mid(t.dhuhr/24),asr:asr(1,t.asr/24),sunset:ang(0.833,t.sunset/24),maghrib:ang(4,t.maghrib/24),isha:ang(14,t.isha/24)}}
    var o={};for(var k in t){var v=fix(t[k]+tz-LNG/15,24),mins=Math.round(v*60);o[k]={min:mins,text:('0'+Math.floor(mins/60)%24).slice(-2)+':'+('0'+mins%60).slice(-2)}}
    return o}
  function hijri(y,m,d){var f=new Intl.DateTimeFormat('en-u-ca-'+HCAL+'-nu-latn',{timeZone:'UTC',day:'numeric',month:'numeric',year:'numeric'}).formatToParts(new Date(Date.UTC(y,m-1,d,12))),o={};
    f.forEach(function(x){o[x.type]=x.value});return {d:+o.day,m:+o.month,y:parseInt(o.year,10)}}
  return {times:times,hijri:hijri,now:function(){return parts(new Date())},tzOffset:tzOffset,setCal:function(c){HCAL=c}};
})();
if(typeof module!=='undefined')module.exports=MZ;
