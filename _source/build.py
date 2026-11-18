import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PHONE_DISPLAY = "+65 9850 5804"
PHONE_TEL = "+6598505804"
WA = "https://wa.me/6598505804"
EMAIL = "sripoojaservices@gmail.com"
FB = "https://www.facebook.com/sripoojaservices/"
GMAPS = "https://www.google.com/maps?cid=2605221990443303164"
NAME = "Sri Rajarajeswari Divine Services"

WA_SVG = '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3C9 3 3.3 8.6 3.3 15.6c0 2.5.7 4.9 2 7L3 29l6.6-2.2c2 1.1 4.2 1.7 6.4 1.7 7 0 12.7-5.6 12.7-12.6S23 3 16 3zm0 23.2c-2 0-4-.6-5.7-1.6l-.4-.2-3.9 1.3 1.3-3.8-.3-.4c-1.1-1.7-1.7-3.8-1.7-5.9C5.3 9.8 10.1 5.1 16 5.1s10.7 4.7 10.7 10.5S21.9 26.2 16 26.2zm5.9-7.9c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.4.3-.6.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.7s1.2 3.2 1.4 3.4c.2.2 2.4 3.6 5.7 5 .8.3 1.4.5 1.9.7.8.3 1.5.2 2.1.1.6-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.3-.3-.4-.6-.5z"/></svg>'

NAV = [("index.htm","Home"),("service.htm","Services"),("extra_mile.htm","About Us"),("reviews.htm","Reviews"),("photo.htm","Photos"),("faq.htm","FAQ")]

def head(title, desc, extra=""):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="sri, rajarajeswari, divine, services, pooja, poojas, homam, homas, hindu, priest, singapore, agamas, shastras, griha pravesam, house warming">
{extra}<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Tiro+Devanagari+Hindi&family=Noto+Serif+Devanagari:wght@700;900&family=Mulish:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css?v=102">
</head>
<body>
'''

def header(active):
    act = ' class="active"'
    links = "\n".join(
        f'      <li><a href="{h}"{act if h==active else ""}>{t}</a></li>' for h,t in NAV)
    cta_active = ' active' if active=="contact.htm" else ''
    return f'''<div class="site-head">
<div class="bija" lang="sa" aria-hidden="true">श्रीं</div>
<header class="site"><div class="wrap">
  <a class="brand" href="index.htm">
    <img class="logo" src="image/srds_logo_gold.png" alt="Sri Rajarajeswari Divine Services logo">
    <span class="brand-text"><span class="name">Sri Rajarajeswari <span class="name2">Divine Services</span><small class="tag">Your trusted partner for pooja services in <b>Singapore</b></small></span></span>
  </a>
</div></header>
<nav class="main"><div class="wrap">
  <ul>
{links}
    <li><a href="contact.htm" class="cta{cta_active}">Contact Us</a></li>
  </ul>
</div></nav>
<div class="wrap">
  <div class="head-contact">
    <a href="tel:{PHONE_TEL}"><svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.46.57 3.6a1 1 0 0 1-.25 1z"/></svg> {PHONE_DISPLAY}</a>
    <a href="mailto:{EMAIL}">✉ {EMAIL}</a>
    <a href="reviews.htm" class="tb-rev"><span class="tw">★</span> Reviews</a>
  </div>
</div>
</div>

'''

CTA = f'''<section class="cta-band"><div class="wrap">
  <img class="lotus-div" src="image/lotus_divider.svg" alt="" aria-hidden="true">
  <p>Feel free to reach out to us and know more.</p>
</div></section>
'''

def footer():
    return f'''<footer class="site slim"><div class="wrap">
  <p class="copy">© {NAME}<br>Registered in Singapore since 2009 · UEN 53144294B</p>
</div></footer>
<script>document.addEventListener('contextmenu',function(e){{e.preventDefault();}});document.addEventListener('dragstart',function(e){{if(e.target.tagName==='IMG')e.preventDefault();}});</script>
<a class="wa-float" href="{WA}" aria-label="Chat with us on WhatsApp" title="Chat with us on WhatsApp">{WA_SVG}<span class="wa-tip">Chat with us on WhatsApp</span></a>
</body>
</html>
'''

SITE = "https://sripoojaservices.com.sg"
SVC_LINK = {"Graha Pravesam":"graha-pravesam.htm","Maha Ganapati Homam":"ganapati-homam.htm","Navagraha Shanti Homam":"navagraha-shanti-homam.htm","Mrityunjaya Homam":"mrityunjaya-homam.htm","Naamakaranam":"naamakaranam.htm","Business Inauguration Pooja":"business-inauguration-pooja.htm"}
ALL_PAGES = []
def seo_head(slug, title, desc, img="image/srds_logo.png"):
    url = SITE + "/" + ("" if slug=="index.htm" else slug)
    return (f'<link rel="canonical" href="{url}">\n'
            f'<meta property="og:type" content="website">\n<meta property="og:title" content="{title}">\n'
            f'<meta property="og:description" content="{desc}">\n<meta property="og:url" content="{url}">\n'
            f'<meta property="og:image" content="{SITE}/{img}">\n')

FRAME_PAGES = None  # None = every page
CORNERS = ''.join(f'<img class="gf-c gf-{c}" src="image/corner_gold.svg" alt="" aria-hidden="true">' for c in ("tl","tr","bl","br"))
def page(fname, title, desc, active, body, extra_head="", img="image/srds_logo.png"):
    ALL_PAGES.append(fname)
    if FRAME_PAGES is None or fname in FRAME_PAGES:
        body = (f'<div class="gold-frame">{CORNERS}<div class="gf-scroll">' + body + '</div><div class="gf-hint" aria-hidden="true">▾ scroll ▾</div></div>\n'
                '<script>(function(){var f=document.querySelector(".gold-frame");if(!f)return;'
                'function fit(){if(window.innerWidth<=560){f.style.height="";document.documentElement.classList.remove("gf-fixed");return;}'
                'var h=document.querySelector(".site-head"),ft=document.querySelector("footer.site");'
                'var avail=window.innerHeight-(h?h.offsetHeight:0)-(ft?ft.offsetHeight:0)-36;'
                'f.style.height=Math.max(320,avail)+"px";document.documentElement.classList.add("gf-fixed");}'
                'window.addEventListener("resize",fit);window.addEventListener("load",fit);fit();'
                'var sc=f.querySelector(".gf-scroll"),hint=f.querySelector(".gf-hint");'
                'if(sc&&hint){var upd=function(){var end=sc.scrollTop+sc.clientHeight>=sc.scrollHeight-8;'
                'if(end){hint.textContent="\u25B4 back to top \u25B4";hint.classList.add("up");}else{hint.textContent="\u25BE scroll \u25BE";hint.classList.remove("up");}};'
                'sc.addEventListener("scroll",upd);hint.addEventListener("click",function(){if(hint.classList.contains("up"))sc.scrollTo({top:0,behavior:"smooth"});else sc.scrollBy({top:sc.clientHeight*0.8,behavior:"smooth"});});}'
                '})();</script>\n')

    with open(fname, "w", encoding="utf-8") as f:
        f.write(head(title, desc, seo_head(fname, title, desc, img) + extra_head) + header(active) + body + footer())

BIZ_SCHEMA = '<script type="application/ld+json">' + __import__("json").dumps({
  "@context":"https://schema.org","@type":"LocalBusiness","name":NAME,"url":SITE+"/",
  "logo":SITE+"/image/srds_logo.png","image":SITE+"/image/srds_logo.png",
  "description":"Hindu priest services in Singapore: poojas and homams conducted according to the Agamas and Shastras.",
  "telephone":"+65 9850 5804","email":EMAIL,"foundingDate":"2009",
  "areaServed":{"@type":"Country","name":"Singapore"},
  "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"11:00","closes":"17:00"}],
  "sameAs":[FB, GMAPS]}) + '</script>\n'

# ---------- HOME ----------
home = f'''<section class="hero home-intro"><div class="wrap">
  <div>
    <h1>Authentic Vedic rituals for your family's blessings</h1>
    <p class="lead">From welcoming a newborn to blessing a new home or business, we conduct genuine poojas and homams drawn from the ancient scriptures, for all Hindu families.</p>
    <p class="lead">Each new stage of life deserves God's blessings. At <strong>{NAME}</strong>, every ceremony is performed as laid down in the scriptures, because every family deserves pure and authentic worship.</p>
    <p class="lead">Our Rishis have laid down the scriptures to guide us to follow certain principles and perform the right poojas and vratas for each occasion.</p>
    <p class="lead">To know more about our services and the care we bring to every ceremony, please visit our <a href="service.htm">Services</a> and <a href="reviews.htm">Reviews</a> pages.</p>
  </div>
</div></section>

<section class="reviews"><div class="wrap">
  <div class="rv-head">
    <p class="eyebrow">In their words</p>
    <h2>What families say</h2>
  </div>
  <div class="rv-grid">
    <figure class="rv"><span class="stars" aria-hidden="true">★★★★★</span><blockquote>“The entire ceremony was performed with care and attention to detail, creating a peaceful and spiritual atmosphere for our family.”</blockquote><figcaption><strong>Vicki M.</strong> · Mrityunjaya Homam</figcaption></figure>
    <figure class="rv"><span class="stars" aria-hidden="true">★★★★★</span><blockquote>“From the first time I spoke to him about my plans for the grihapravesam to the day of the prayers, he has been a guiding light in ensuring my first home is thoroughly blessed. I really appreciated how his list of pooja items was clear and included alternatives and supplementary notes.”</blockquote><figcaption><strong>Vasellia S.</strong> · Graha Pravesam</figcaption></figure>
    <figure class="rv"><span class="stars" aria-hidden="true">★★★★★</span><blockquote lang="hi" class="hi">“अगर अच्छे से पूजा हो तो उसका इतना बेहतरीन रिज़ल्ट आता है, यह पंडितजी से पूजा कराने के बाद पता चला।”</blockquote><p class="rv-tr">“After having Panditji perform the puja, I realised how excellent the results are when puja is done properly.”</p><figcaption><strong>Priya S.</strong> · Poojas &amp; homams at home</figcaption></figure>
  </div>
</div></section>
''' + CTA

page("index.htm", f"Hindu Priest & Pooja Services in Singapore | {NAME}",
     "Experienced Hindu priest in Singapore for Graha Pravesam, homams and poojas, conducted strictly according to the Agamas. WhatsApp +65 9850 5804.",
     "index.htm", home,
     extra_head='<meta name="google-site-verification" content="7lQvcw224-vS7JU3_tW4DSMfaEhSHULiIyVkj0b1O1Q">\n' + BIZ_SCHEMA)

# ---------- SERVICES ----------
def grid(items):
    out = []
    for i,(n,s) in enumerate(items,1):
        sub = f"<small>{s}</small>" if s else ""
        nm = f'<a href="{SVC_LINK[n]}">{n} →</a>' if n in SVC_LINK else n
        out.append(f'<div class="svc"><div><strong>{nm}</strong>{sub}</div></div>')
    return '<div class="svc-grid">' + "\n".join(out) + '</div>'

homams = [("Maha Ganapati Homam","Removing obstacles before new beginnings"),("Sahasra Modaka Homam","Offering a thousand modakas to Lord Ganapati in the sacred fire"),("Ayushya Homam","For long life and good health"),("Nakshathra Homam","Honouring one's birth star"),("Sri Suktam Homam","Invoking Goddess Lakshmi for prosperity"),("Sri Vidya Homam","Worship of the Divine Mother as Sri Lalitha"),("Chandi Homam","Invoking Goddess Chandi for protection and strength"),("Dasa Maha Vidya Homam","Worship of the ten great wisdom forms of the Divine Mother"),("Sudarshana Homam","Protection from negative influences"),("Dhanvantari Homam","For healing and wellbeing"),("Mrityunjaya Homam","For health and protection"),("Lalitha Sahasranaama Homam","Thousand-name worship of the Divine Mother"),("Navagraha Shanti Homam","Pacifying the nine planets"),("Vastu Shanti Homam","Harmony for a home or premises")]
poojas = [("Shubha Punyaahavaachanam","Purification ceremony"),("Varalakshmi Vratha Pooja","Worship of Goddess Varalakshmi for the family's wellbeing"),("Navarathri Pooja","Nine nights of worship of the Divine Mother"),("Devata Pratishta","Installation of deities"),("Business Inauguration Pooja","For a new business or office"),("Devata Sahasranaama Pooja","Thousand-name worship of a chosen deity")]
sams = [("Naamakaranam","Naming ceremony"),("Annaprasanam","Child's first feeding ceremony"),("Aksharabhyasam","Initiation into the world of learning"),("Graha Pravesam","Housewarming")]


def L(name, href=None, info=None):
    if href: name = f'<a href="{href}">{name} →</a>'
    if info: name += f' <a class="svc-info" href="{info}">please read ⓘ</a>'
    return name
SVC_GROUPS = [
 ("Life occasions", "", "occ", [
   ("", [L("Graha Pravesam (housewarming)","graha-pravesam.htm"), L("Business premises opening","business-inauguration-pooja.htm"),
         "Shubha Punyaahavaachanam", "Naamakaranam (naming)", "Annaprasanam (first feeding)",
         "Aksharabhyasam (initiation into learning)", "Ayushya Homam", "Chanting session during palliative care"])]),
 ("Worship by deity", "", "deity", [
   ("Sri Maha Ganapati", ["Caturaavrutti Tarpanam", "Sri Maha Ganapati Sahasranaama Archana", "Sri Maha Ganapati Aavarana Pooja", L("Sri Maha Ganapati Homam","ganapati-homam.htm"),
                      "Ashta Dravya Sri Maha Ganapati Homam", "Sahasra Modaka Homam"]),
   ("Devi", ["Sri Vidya Homam", "Devi Navaavarana Pooja", "Sri Lalitha Sahasranaama Archana", "Kunkuma Archana and Suvaasini Pooja (by Suvaasinis)",
             "Sri Sukta Homam", "Abirami Andhathi Paraayanam with Pancha Upachaara Pooja at each of the 100 verses", L("Sri Varalakshmi Pooja", info="varalakshmi-pooja.htm"),
             "Aishwarya Deepa Pooja with Suvaasini Pooja", L("Bagavathi Seva", info="bagavathi-seva.htm"),
             "Sri Lalitha Sahasranaama Homam", "Navarathri Pooja", "Deepavali Sri Lakshmi Pooja", "Dhanteras Sri Lakshmi Pooja", "Dasa Maha Vidya Homam",
             "Durga Saptasati Paraayanam (also Samputikarana)", "Chandi Homam (also Samputikarana)"]),
   ("Sri Maha Vishnu", ["Sri Maha Vishnu Sahasranaama Archana", "Sri Maha Vishnu Homam", "Sri Sudarshana Homam", "Sri Dhanvantari Homam", L("Sri Sathyanarayana Pooja", info="sathyanarayana-pooja.htm")]),
   ("Sri Shiva", ["Sri Shiva Sahasranaama Archana", L("Sri Maha Mrityunjaya Homam","mrityunjaya-homam.htm"), "Sri Shiva Panchakshara Homam"]),
   ("Sri Subramanya", ["Sri Skanda Homam", "Shatru Samhaara Trisati Maha Pooja"]),
   ("Navagraha and birth star", [L("Navagraha Shanti Homam","navagraha-shanti-homam.htm"), "Laghu Navagraha Pooja", "Nakshathra Homam"]),
   ("Any chosen deity", ["Devata Sahasranaama Archana (thousand-name worship for any chosen deity)"])]),
 ("Praanapratishta (installation)", "", "inst", [
   ("", ["Sri Mahameru Praanapratishta", "Sri Chakra Yantra Praanapratishta", "Devata Vigraha Pratishta (idol installation)", "Yantra Pratishta for a chosen deity (please check with us)"])]),
]
def svc_list():
    out=[]
    for title, sub, gid, rows in SVC_GROUPS:
        out.append(f'  <div class="svc-group" id="{gid}"><header class="svc-sub"><h2>{title}</h2></header>')
        for deity, items in rows:
            lis = "".join(f"<li>{i}</li>" for i in items)
            if deity:
                out.append(f'    <div class="deity-row"><h3>{deity}</h3><ul class="svc-list">{lis}</ul></div>')
            else:
                out.append(f'    <ul class="svc-list">{lis}</ul>')
        out.append('  </div>')
    out.append('  <p class="svc-combine">Some of these can be combined. Please <a href="contact.htm">give us a call</a> and we will be happy to clarify.</p>')
    return "\n".join(out)
SVC_LIST = svc_list()

services = f'''<section class="page-hero svc-hero"><div class="wrap">
  <p class="eyebrow">Our services</p>
  <h1>Poojas, Homams &amp; Ceremonies</h1>
  <p>We offer the following services, performed as laid down in the scriptures.</p>
  <p>We conduct poojas, homams and ceremonies offered in worship of the Divine to seek blessings and grace. Larger events with additional priests can also be arranged on request. Don't see what you need? <a href="contact.htm">Contact us</a> with your occasion and preferred date and we will let you know if we can arrange it.</p>
  <p>We do not conduct weddings, as customs differ from one community to another, or ancestral rituals.</p>
</div></section>
<section><div class="wrap">
{SVC_LIST}
</div></section>
''' + CTA
page("service.htm", f"Poojas & Homams in Singapore | {NAME}", "Full list of poojas and homams conducted in Singapore, including Graha Pravesam, Ganapati Homam, Navagraha Shanti and Naamakaranam.", "service.htm", services)

INFO_PAGES = [
 ("varalakshmi-pooja.htm","Sri Varalakshmi Pooja",
  ["Sri Varalakshmi Pooja is conducted over two days. On the day of the pooja, Goddess Lakshmi is invoked and welcomed into the home. She is not sent off (udvasanam) on the same day, so a Punar Pooja is performed the following day.",
   "According to the scriptures, the priest who begins the pooja must return to complete it. The Punar Pooja cannot be left to the family to perform on their own to save cost. Our arrangement therefore always covers both days.",
   "If a one-day arrangement is preferred, we would not be able to take up the booking."]),
 ("sathyanarayana-pooja.htm","Sri Sathyanarayana Pooja",
  ["We perform Sri Sathyanarayana Pooja in full, as laid down in the scriptures, ideally on a full moon day. It is an elaborate pooja that takes several hours, and it is followed by a Punar Pooja.",
   "There is no shortened or simplified version of this pooja in the scriptures, so we do not offer one.",
   "If the full pooja suits your family, we would be glad to conduct it."]),
 ("bagavathi-seva.htm","Bagavathi Seva",
  ["For Bagavathi Seva, the mandalam needs to be made ready before we arrive to perform the Seva.",
   "If you are unfamiliar with it, we can guide you, and a template is available for you to collect from us.",
   "We do not offer the service of creating the mandalam."]),
]
for slug, title, paras in INFO_PAGES:
    ptxt = "".join(f"<p>{x}</p>" for x in paras)
    body = f'''<section class="page-hero svc-hero"><div class="wrap">
  <p class="back-link"><a href="service.htm">← Back to Services</a></p>
  <p class="eyebrow">Please read before booking</p>
  <h1>{title}</h1>
  {ptxt}
  <p class="back-link" style="margin-top:24px"><a href="service.htm">← Back to Services</a></p>
</div></section>
''' + CTA
    page(slug, f"{title} in Singapore | {NAME}", f"How we conduct {title} in Singapore, as laid down in the scriptures.", "service.htm", body)

# ---------- WHY US ----------
why = f'''<section class="page-hero"><div class="wrap">
  <p class="eyebrow">About us</p>
  <h1>Serving Singapore's Hindu families since 2009</h1>
  <p>For nearly two decades, families across our island have engaged us for poojas and homams in their homes. Many engage us again for subsequent prayers, and recommend us to their relatives and friends.</p>
</div></section>
<section class="alt about-flow"><div class="wrap">
  <div class="about-centre">
    <div>
      <p>We guide you and your family through every step, explaining as we go, so your prayers are offered to God just as you intend. Every ritual follows the scriptures given by our Rishis, and families feel its positive effects in their lives and homes.</p>
      <p style="margin-top:1rem"><strong>Our approach:</strong> the rituals and procedures of every pooja and homam we conduct will not be altered or simplified. <strong>They are followed strictly as laid down in the scriptures by our Rishis, for this is the duty of everyone who performs a prayer.</strong> On the other hand, as Lord Krishna tells Arjuna in the Bhagavad Gita (9.26), even a leaf, a flower, a fruit or a little water, offered with devotion, is accepted. So choose the prayer that suits your means: a Sahasranama Archana needs only flowers, fruits and a tambulam. But once you choose a bigger prayer such as a homam, please gather its items in full, just as you would not invite a guest to a feast and then serve less. If you have constraints with any item, tell us openly and we will suggest a respectful alternative (lotus-leaf plates, yes; plastic plates, no). Your sincerity in preparing, and the right intention of both host and priest, bring the full merits of the prayer.</p>
      <p style="margin-top:1rem">Many families tell us they have hosted prayers before but could not feel their effects. We will not comment on the reasons. <strong class="co-name">Sri Rajarajeswari Divine Services</strong> was founded in 2009 for exactly this: to perform the poojas and homams that invoke God's grace properly, without cutting short any step. Engage us once and experience it for yourself.</p>
    </div>
    <div class="about-cards">
      <div class="about-card"><h3>Our vision</h3><p>A Sanatana Dharma community that helps everyone, regardless of caste, creed, race, religion or nationality.</p></div>
      <div class="about-card"><h3>Our mission</h3><p>To guide each family through their prayers, and along the way to teach them what truly matters, so that whoever they engage in future, they will know what a proper prayer requires. In this way, the original teachings are passed on, unchanged, to the younger generation, and every family continues to receive the full merits of their prayers.</p></div>
    </div>
  </div>
</div></section>
''' + CTA
page("extra_mile.htm", f"About Us | {NAME}", "Authentic, scripture-based poojas you can trust. Learn why families in Singapore choose Sri Rajarajeswari Divine Services.", "extra_mile.htm", why)

# ---------- PHOTOS ----------
import json
_g=[x for x in json.load(open('gallery.json')) if x[0] not in ('photo02.jpg','photo09.jpg','photo16.jpg','photo06.jpg','photo25.jpg','photo26.jpg','photo27.jpg','photo28.jpg','photo23.jpg','photo29.jpg','photo43.jpg','photo34.jpg')]  # hidden = archive; swap in quarterly
figs="\n".join(f'    <figure><img src="image/gallery/{n}" alt="{c}" loading="lazy" width="{w}" height="{h}"{' style="object-position:center 20%"' if n=='photo17.jpg' else ''}><figcaption>{c}</figcaption></figure>' for n,c,(w,h) in _g)
photos = f'''<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Gallery</p>
  <h1>Photos</h1>
  <p>Moments from poojas, homams and ceremonies we have conducted.</p>
</div></section>
<section><div class="wrap">
  <div class="gallery">
{figs}
  </div>
  <script>
(function(){{var g=document.querySelector('.gallery');if(!g)return;var o=document.createElement('div');o.className='mz-orn';o.setAttribute('aria-hidden','true');o.innerHTML='<img src="image/lotus_mandala.svg" alt="">';g.appendChild(o);
function place(){{o.style.display='none';var f=[].slice.call(g.querySelectorAll('figure'));if(!f.length)return;var gr=g.getBoundingClientRect(),cols={{}};
f.forEach(function(x){{var r=x.getBoundingClientRect();var k=Math.round(r.left-gr.left);if(!cols[k]||r.bottom>cols[k].b)cols[k]={{b:r.bottom,l:r.left-gr.left,w:r.width}};}});
var ks=Object.keys(cols);if(ks.length<2)return;var mx=0;ks.forEach(function(k){{mx=Math.max(mx,cols[k].b);}});var best=null;ks.forEach(function(k){{var gap=mx-cols[k].b;if(!best||gap>best.gap)best={{gap:gap,c:cols[k]}};}});
if(best.gap<140)return;var s=Math.min(best.gap-30,best.c.w*0.7,260);o.style.cssText='display:block;position:absolute;width:'+s+'px;height:'+s+'px;left:'+(best.c.l+(best.c.w-s)/2)+'px;top:'+(best.c.b-gr.top+(best.gap-s)/2)+'px';}}
window.addEventListener('load',place);window.addEventListener('resize',function(){{clearTimeout(window._mz);window._mz=setTimeout(place,150);}});[].forEach.call(g.querySelectorAll('img'),function(i){{i.addEventListener('load',place);}});place();}})();
  </script>
  <p class="copy-note">All photos © {NAME}. Please do not copy or reuse them without our written permission.</p>
</div></section>
''' + CTA
page("photo.htm", f"Pooja & Homam Photos, Singapore | {NAME}", "Photos from poojas, homams and ceremonies conducted by Sri Rajarajeswari Divine Services in Singapore.", "photo.htm", photos)

# ---------- CONTACT ----------
contact = f'''<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Contact</p>
  <h1>Get in touch</h1>
  <p>Contact us for more information on our services, or to arrange a pooja or ceremony.</p>
</div></section>
<section><div class="wrap">
  <div class="contact-grid">
    <div class="contact-card"><div class="ico">📞</div><h3>Call us</h3><a class="big" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><a class="btn btn-outline" href="tel:{PHONE_TEL}">Call now</a></div>
    <div class="contact-card"><div class="ico">💬</div><h3>WhatsApp</h3><a class="big" href="{WA}">{PHONE_DISPLAY}</a><a class="btn btn-outline" href="{WA}">Start a chat</a></div>
    <div class="contact-card"><div class="ico">✉</div><h3>Email</h3><a class="big" href="mailto:{EMAIL}">{EMAIL}</a><a class="btn btn-outline" href="mailto:{EMAIL}">Send an email</a></div>
  </div>
  <div class="note" style="margin:40px auto 0;max-width:760px;text-align:center"><strong>Enquiries:</strong> Monday to Friday, 11am – 5pm<br><strong>Ceremonies:</strong> by appointment, any day of the week</div>
  <p class="contact-close" style="font-style:normal">If we do not answer your call, we may be conducting a pooja at a family's home. Please leave us a WhatsApp message and we will get back to you as soon as we can.</p>
  <p class="contact-close">We look forward to hearing from you.</p>
</div></section>
'''
page("contact.htm", f"Contact a Hindu Priest in Singapore | {NAME}", "Contact Sri Rajarajeswari Divine Services in Singapore by phone, WhatsApp or email.", "contact.htm", contact)
print("built")

# =================== SEO ADDITIONS ===================
SERVICE_PAGES = [
 dict(slug="graha-pravesam.htm", short="Graha Pravesam", h1="Graha Pravesam (Housewarming) Pooja in Singapore",
  title="Graha Pravesam (Housewarming) Pooja in Singapore | Sri Rajarajeswari Divine Services",
  desc="Authentic Graha Pravesam housewarming pooja in Singapore, conducted by an experienced Hindu priest according to the Agamas and Shastras. WhatsApp +65 9850 5804.",
  img="photo03.jpg", alt="Milk-boiling ritual during a Graha Pravesam housewarming ceremony",
  intro="Graha Pravesam is the traditional Hindu ceremony for entering a new home. It purifies the house and invokes the blessings of the deities, so that the family begins life in their new home with peace, health and prosperity.",
  when="Families perform Graha Pravesam when moving into a newly bought or newly built home, including HDB flats, condominiums and landed houses. It is also often done after major renovation. The ceremony is held on an auspicious date and time (muhurtham).",
  includes=["Ganapati Pooja to remove obstacles","Punyaahavaachanam (purification of the home)","Dwara Pooja at the main entrance","The family's first entry into the new home","The traditional boiling of milk in the new kitchen","Offering the milk to the deities at the home altar"],
  addons=["Maha Ganapati Homam, or another homam of your choice","Navagraha Pooja"],
  note="", where="Conducted at your new home",
  quote=("He has been a guiding light in ensuring my first home is thoroughly blessed.","Vasellia S.","Graha Pravesam"),
  faq=[("When should we do Graha Pravesam?","On the day you move in, at an auspicious muhurtham. The family should stay overnight in the new home that same night, as the Graha Pravesam marks the day you begin living there."),
       ("Can it be done in an HDB flat?","Yes. We conduct Graha Pravesam in HDB flats, condominiums and landed homes.")]),
 dict(slug="ganapati-homam.htm", short="Ganapati Homam", h1="Maha Ganapati Homam in Singapore",
  title="Maha Ganapati Homam in Singapore | Sri Rajarajeswari Divine Services",
  desc="Maha Ganapati Homam in Singapore to remove obstacles before new beginnings, conducted strictly according to Vedic tradition. Book via WhatsApp +65 9850 5804.",
  img="photo45.jpg", alt="Sri Maha Ganapati invoked on the Kalasam for a Ganapati Homam",
  intro="Maha Ganapati Homam is a sacred fire ritual dedicated to Lord Ganesha. He is best known as the remover of obstacles, but like every deity He has the power to bless us in every way, with good health, wealth, wisdom and success. Offerings are made into the sacred fire with Vedic mantras, seeking His blessings for every aspect of life.",
  when="Ganapati Homam is commonly performed before any new beginning: moving into a new home, starting a business, starting a new job, before wedding preparations begin (so that everything goes smoothly), or on New Year's Day. Many families also perform it annually for general well-being.",
  includes=["Prayers at the home altar to seek the blessings of the family deities before we begin","Sankalpam stating the family's intention","Vighna Nivarana Ganapati Pooja","Punyaahavaachanam","Pradhaana Kalasam Pooja","Homam, with offerings into the sacred fire","Poornahuti and aarti","Prasadam and theertham are carried back to the home altar, where the ceremony is completed with final prayers"],
  quote=None,
  faq=[("Can Ganapati Homam be combined with other poojas?","Yes. It is often performed at the start of a Graha Pravesam, a business opening or other homams. Tell us your occasion and we will suggest the right combination.")]),
 dict(slug="navagraha-shanti-homam.htm", short="Navagraha Shanti Homam", h1="Navagraha Shanti Homam in Singapore",
  title="Navagraha Shanti Homam in Singapore | Sri Rajarajeswari Divine Services",
  desc="Navagraha Shanti Homam in Singapore to pacify the nine planets and bring peace and harmony. Authentic Vedic ritual. WhatsApp +65 9850 5804.",
  img="photo06.jpg", alt="Sacred fire homam",
  intro="Navagraha Shanti Homam is offered to the nine planetary deities (Navagrahas). It seeks to pacify unfavourable planetary influences and invite their blessings for peace, health and progress.",
  when="Families often perform this homam when a horoscope shows difficult planetary periods, before important life events, or on birthdays.",
  includes=["Invocation of each of the nine planetary deities","Offerings with the specific grains and samidh associated with each graha","Prayers for peace and harmony in the family"],
  quote=None,
  faq=[]),
 dict(slug="mrityunjaya-homam.htm", short="Mrityunjaya Homam", h1="Mrityunjaya Homam in Singapore",
  title="Mrityunjaya Homam in Singapore | Sri Rajarajeswari Divine Services",
  desc="Mrityunjaya Homam in Singapore, invoking Lord Shiva for health, recovery and long life. Conducted with devotion according to the Agamas. WhatsApp +65 9850 5804.",
  img="photo01.jpg", alt="Devi in alankaram",
  intro="Mrityunjaya Homam invokes Lord Shiva as Mrityunjaya, the conqueror of death, through the Maha Mrityunjaya mantra. It is performed for good health, recovery from illness and long life.",
  when="Families perform Mrityunjaya Homam when a loved one is unwell or recovering, on milestone birthdays, or simply for the health and protection of the family.",
  includes=["Sankalpam for the person or family","Chanting of the Maha Mrityunjaya mantra","Offerings into the sacred fire","Purnahuti and blessings"],
  quote=("He conducted the puja with great devotion, patience, and professionalism.","Vicki M.","Mrityunjaya Homam"),
  faq=[("Can it be done at home?","Yes. We conduct Mrityunjaya Homam at your own home.")]),
 dict(slug="business-inauguration-pooja.htm", short="Business Inauguration Pooja", h1="Business Inauguration Pooja in Singapore",
  title="Shop & Office Opening Pooja in Singapore | Sri Rajarajeswari Divine Services",
  desc="Business inauguration pooja for new shops, offices and restaurants in Singapore. Seek blessings for success and prosperity. WhatsApp +65 9850 5804.",
  img="photo07.jpg", alt="Sri Mahalakshmi in alankaram",
  intro="A business inauguration pooja seeks divine blessings when opening a new shop, office, clinic or restaurant, so that the venture begins on an auspicious note and prospers.",
  when="This pooja is performed on the opening day of a new business or premises, or when moving to a new office. It is held at an auspicious time.",
  includes=["Sri Maha Ganapati Pooja for a smooth start","Punyaahavaachanam (purification of the premises)","Sri Mahalakshmi Pooja for prosperity","Blessings for the owners and staff"],
  note="There are also specific poojas and homams that can help a business grow and stay strong in a competitive market. When you contact us, we will advise you personally on what suits your business.",
  where="Conducted at your own business premises",
  quote=None,
  faq=[("Can the pooja be done before opening hours?","Yes. The pooja can be held before opening hours, at the auspicious time you have chosen.")]),
]
import json as _json
def faq_schema(qas):
    return '<script type="application/ld+json">'+_json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":__import__("re").sub(r"<[^>]+>"," ",a)}} for q,a in qas]})+'</script>\n'


for sp in SERVICE_PAGES:
    inc = "".join(f"<li>{x}</li>" for x in sp["includes"])
    q = sp["quote"]
    quote_html = (f'<figure class="rv svc-quote"><span class="stars" aria-hidden="true">★★★★★</span><blockquote>“{q[0]}”</blockquote>'
                  f'<figcaption><strong>{q[1]}</strong> · {q[2]} · Google review</figcaption></figure>') if q else ""
    photo_html = f'<img class="svc-photo" src="image/gallery/{sp["img"]}" alt="{sp["alt"]}" loading="lazy">' if sp["img"] else ""
    _ad = sp.get("addons")
    addons_html = (f'<h3 style="margin-top:22px">Optional add-ons</h3><ul class="checklist">' + "".join(f"<li>{x}</li>" for x in _ad) + '</ul>') if _ad else ""
    _nt = sp.get("note", "")
    note_html = f'<p class="muted-note">{_nt}</p>' if _nt else ""
    faqs = ('<h2 style="margin-top:40px">Common questions</h2>' + "".join(f'<div class="faq-item"><h3>{a}</h3><p>{b}</p></div>' for a,b in sp["faq"])) if sp["faq"] else ""
    others = "".join(f'<li><a href="{o["slug"]}">{o["short"]}</a></li>' for o in SERVICE_PAGES if o is not sp)
    body = f'''<section class="page-hero"><div class="wrap">
  <p class="back-link"><a href="service.htm">← Back to Services</a></p>
  <p class="eyebrow"><a href="service.htm" style="color:inherit;text-decoration:none">Services</a> › {sp["short"]}</p>
  <h1>{sp["h1"]}</h1>
  <p>{sp["intro"]}</p>
</div></section>
<section><div class="wrap two-col svc-detail">
  <div>
    <h2>When is it performed?</h2>
    <p>{sp["when"]}</p>
    <h2 style="margin-top:28px">What the ceremony includes</h2>
    <ul class="checklist">{inc}</ul>
    {addons_html}{note_html}
  </div>
  <div>
    {photo_html}
    {quote_html}
  </div>
</div></section>
<section class="alt"><div class="wrap">
  <h3 style="margin-top:40px">Other services</h3>
  <ul class="related">{others}<li><a href="service.htm">All Services</a></li></ul>
  <p class="back-link" style="margin-top:28px"><a href="service.htm">← Back to Services</a></p>
</div></section>
''' + CTA
    page(sp["slug"], sp["title"], sp["desc"], "service.htm", body, img=("image/gallery/"+sp["img"]) if sp["img"] else "image/srds_logo.png")

# ---------- FAQ ----------
GEN_FAQ = [
 ("Where are the ceremonies conducted?","At your own home, or at your own business premises for a business opening."),
 ("In which language are the ceremonies conducted?","Mantras are chanted in Sanskrit, as laid down in the scriptures. We explain the meaning and steps in English and other Indian languages, so the whole family can follow and take part."),
 ("How do I book a pooja?","Message us on WhatsApp or call +65 9850 5804, or email sripoojaservices@gmail.com. Let us know the occasion, your preferred date and where the ceremony will take place. Enquiries are answered Monday to Friday, 11am to 5pm. Ceremonies can be held on any day by appointment, subject to our availability. If we already have a booking on that date and time, we will not be able to accept another."),
 ("How is a booking confirmed?","The details for confirming your booking are stated in the quotation we send you."),
 ("Can you help us choose an auspicious date and time?","Yes. Share the details with us and we will help you choose a suitable date and time for your ceremony."),
 ("Do you provide astrological services?","We do not offer astrological consultations as a separate service. However, we can check auspicious dates against your horoscope, and where there are hurdles or blockages in a particular matter, we can look into what may be causing them."),
 ("Can a ceremony be held during Brahma Muhurtham?","Brahma Muhurtham, the early hours before sunrise, is an auspicious time for worship. However, the day of the week must also be considered. Hindus avoid certain events on some days; for example, Graha Pravesam is avoided on Tuesdays and Saturdays.<br><br><strong>Please note:</strong> in the Hindu almanac, a day begins at sunrise, not at midnight. If sunrise in Singapore is at 7am on a Wednesday, the hours before 7am still belong to Tuesday. So a Graha Pravesam held at 5am on a Wednesday actually falls on Tuesday, and one held at 5am on a Sunday falls on Saturday. Many families are not aware of this. Please keep both the time and the day of the week in mind when choosing your date, and we will be happy to advise you."),
 ("Apart from the booking charge, is there anything else to pay?","Transport to and from the venue is to be arranged by the host.<br><br>Giving dakshina is entirely your choice. The scriptures highly recommend performing a charitable deed (daanam) after a ceremony in your home, and many families make their first such offering to the priest who performed the worship, as a token of gratitude, sometimes together with a veshti (dhoti). It is a gift, never a requirement.<br><br>In homes with a domestic helper, we also encourage families to give the helper a small token of appreciation, as such occasions bring extra work. If you wish, the priest can advise you on the right moment during the ceremony, so that the offering brings more merit."),
 ("Do you supply the pooja items?","No. We are registered as a service provider, not a supplier. Sourcing items for each family would add time and cost, and every home is different: most Hindu homes already have basic pooja utensils and trays, and fresh items such as fruits and flowers differ from shop to shop.<br><br>We also believe that choosing the items yourself is part of the worship. Just as you would personally choose a gift for someone you love, selecting the offerings with your own hands brings you closer to the Divine, and the blessings begin from there."),
 ("Will you guide us on what to buy and where to get it?","Yes. Once your booking is confirmed, we will guide you every step of the way, from the list of items and where to buy them to the arrangements needed, so that your ceremony goes smoothly."),
 ("What if we are not ready to start on time on the day?","Please understand that we may have another booking after your time slot, often with its own fixed muhurtham. If your ceremony starts late, it may not finish in time, which affects the next family. Since every ceremony follows auspicious timings, we kindly ask you to plan ahead and be ready at the agreed time, so that the ceremony can be completed within your slot."),
 ("Can we change or cancel a booking?","We believe that whether an event takes place is ultimately in God's hands. If unfortunate circumstances mean you need to reschedule or cancel, we understand it as God's will, and the same can happen on our side as well. Nobody cancels deliberately, so we ask for mutual understanding, accept it as being for the good, and move forward without hard feelings."),
 ("Can you perform a pooja that is not on your list?","Yes. Our services page lists the most common poojas and homams. If you would like another auspicious pooja or homam, please ask and we will let you know if we can arrange it."),
 ("Are there any ceremonies you do not conduct?","Yes. We do not conduct weddings, as wedding customs differ from one community to another, or ancestral rituals. We conduct poojas, homams and ceremonies offered in worship of the Divine, such as Graha Pravesam, Naamakaranam, Aksharabhyasam and the homams on our services page."),
 ("Do you serve families from all Hindu traditions?","Yes. We conduct authentic Vedic ceremonies for all Hindu families, following the Agamas and Shastras."),
 ("Can we use an aluminium tray or foil for the homam fire?","No. Please use a proper homa kundam made of metal or brick. Firstly, the sacred fire is where the deity is invited, so it deserves a proper, respectful place, just as you would give an honoured guest a proper seat. Secondly, it is a matter of health and safety. A homam fire is hot enough to break down aluminium foil, releasing fine metal particles into the smoke. Homams are usually held indoors, in an enclosed room, with everyone sitting close to the fire for an hour or more. Breathing in such fumes can irritate the lungs, and the elderly, young children and anyone with breathing difficulties are most at risk. As a registered business, we take the health and safety of every home seriously, and will advise you on a suitable kundam when you book."),
 ("Why do you insist on following the scriptures strictly?","We believe the blessings of a ceremony come from performing it correctly, exactly as the Rishis laid it down, with the right intention from both the host and the priest. That is why we do not alter the procedures."),
]
faq_body = '''<section class="page-hero"><div class="wrap">
  <p class="eyebrow">FAQ</p>
  <h1>Frequently asked questions</h1>
  <p>Answers to common questions about booking a pooja or homam with us in Singapore.</p>
</div></section>
<section><div class="wrap prose">
''' + "".join(f'<div class="faq-item{" faq-key" if "Brahma" in q else ""}"><h3>{q}</h3><p>{a}</p></div>' for q,a in GEN_FAQ) + '''
  <h2 style="margin-top:40px">Questions about a specific pooja?</h2>
  <ul class="related">''' + "".join(f'<li><a href="{o["slug"]}">{o["short"]}</a></li>' for o in SERVICE_PAGES) + '''<li><a href="service.htm">All Services</a></li></ul>
</div></section>
''' + CTA

# ======== REVIEWS PAGE ========
REV_THEMES = [
 ("Patient with every question", "Families are encouraged to ask, and every question is answered.", [
   ("I really appreciated how his list of pooja items was clear and included alternatives and supplementary notes. He was also very responsive when I reached out to him with questions.","Vasellia S.","Graha Pravesam"),
   ("Thank you Mr Muralee for conducting our grahapravesam and for promptly answering all of my queries very patiently.","Pirrita V.","Graha Pravesam"),
   ("Without any rush, our queries were answered very politely followed by your honest smile.","Mages A.","Housewarming")]),
 ("Calm, polite and respectful", "A peaceful ceremony starts with a calm and courteous priest.", [
   ("The priest was very polite, calm, and patient throughout the entire process.","Prem K.","Punyahavachanam"),
   ("He was very patient and did all the prayers in a calm manner and never rush at all.","Vasuki M.","Homam &amp; prayers"),
   ("We deeply appreciate his efforts and good cheer throughout the prayers.","Vijaya M.","Housewarming")]),
 ("Guided from the first call to the last mantra", "Clear lists, step-by-step explanations and help on the day itself.", [
   ("He created an elaborate process of House warming ceremony and gave us a list to procure and explained us step by step on what needs to be done. On the day itself he came an hour earlier and helped us in setting up the Pooja and homam.","Harsha C.","Graha Pravesam"),
   ("He guided us from the start, giving advice on the items to purchase as well as what is needed to be prepared for the actual day.","Priya M.","Housewarming"),
   ("He conducted the puja with great devotion, patience, and professionalism, while guiding us through the process in a clear and reassuring manner.","Vicki M.","Mrityunjaya Homam")]),
 ("There when you need us", "Last-minute requests, special arrangements and going the extra mile.", [
   ("We engaged Murali Iyer very last minute for our grahapravesam pooja, as our earlier booked one backed off last minute… we are happy that we found Murali Iyer.","Madhu B.","Graha Pravesam"),
   ("We hadn’t expected him to travel to JB - but he did, and we were truly grateful.","Vanishree P.","Graha Pravesam, Johor Bahru"),
   ("He was very professional, knowledgeable, and went above and beyond to meet our needs.","Buvanesh J.","Ganapathi Homam")]),
 ("Done properly, as laid down in the scriptures", "Authentic rituals, performed with care and devotion.", [
   ("He performed the puja and homam with great devotion, following the proper procedures and adapting them appropriately to the specific situation.","Sundaramoorthy S.","Pooja &amp; homam at home"),
   ("The prayer session from start to finish was very professionally and beautifully done.","Sujatha N.","Prayers at home"),
   ("It was divine and one of a kind.","Dhanasekhar D.","Navavarana Maha Meru Pooja")]),
 ("A home filled with positive energy", "What families feel after the ceremony.", [
   ("The ceremony was conducted with such devotion and care, and it filled our home with positive energy. Our family felt deeply blessed and uplifted.","Vanishree P.","Graha Pravesam"),
   ("The positive energy can be felt in my humble abode and altar after the session.","Pirrita V.","Graha Pravesam"),
   ("From the moment he arrived, his warm presence and deep knowledge of the rituals created an atmosphere of peace and positivity.","Roger H.","Home pooja")]),
 ("Families who come back", "Many families invite us again, some every year for their annual prayers.", [
   ("This was the second time we engaged Mr Murali’s service and he conducted the housewarming ceremony punctually and efficiently.","Jaynthi K.","Housewarming"),
   ("Everything was planned and executed well… Next year I will engage him again. A very satisfied customer.","Rajaletchimi S.","Aadi pooja"),
   ("We are very happy with the prayers looking forward to have you on our future prayers including our extended family also.","Somasundram P.","Prayers at home")]),
]
def rev_cards(items):
    return '<div class="rv-grid">' + ''.join(f'<figure class="rv"><span class="stars" aria-hidden="true">★★★★★</span><blockquote>“{t}”</blockquote><figcaption><strong>{n}</strong> · {c}</figcaption></figure>' for t,n,c in items) + '</div>'
_themes = "".join(f'  <div class="rv-theme"><header class="svc-sub"><h2>{h}</h2><p>{sub}</p></header>{rev_cards(items)}</div>\n' for h,sub,items in REV_THEMES)
reviews_body = f"""<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Reviews</p>
  <h1>What families say</h1>
  <p>Every quote below is taken word for word from our Google reviews, written by different families, for different ceremonies.</p>
</div></section>
<section><div class="wrap">
{_themes}  <p class="rv-note">Quotes are taken from our Google reviews.</p>
</div></section>
""" + CTA
page("reviews.htm", f"Reviews from Families in Singapore | {NAME}", "What families in Singapore say about our poojas, homams and ceremonies: patient, calm, authentic and well guided. Quotes taken word for word from our Google reviews.", "reviews.htm", reviews_body)

page("faq.htm", f"FAQ: Booking a Hindu Priest in Singapore | {NAME}",
     "Common questions about booking a pooja or homam in Singapore: languages, areas served, preparation and how to book.",
     "faq.htm", faq_body, extra_head=faq_schema(GEN_FAQ))

# ---------- SITEMAP / ROBOTS ----------
import datetime as _dt
_today = _dt.date.today().isoformat()
_urls = "".join(f"  <url><loc>{SITE}/{'' if p=='index.htm' else p}</loc><lastmod>{_today}</lastmod></url>\n" for p in ALL_PAGES)
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+_urls+'</urlset>\n')
open("robots.txt","w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
print("seo done", len(ALL_PAGES), "pages")

# keep the root page (index.html) identical to index.htm
import shutil as _sh
_sh.copyfile("index.htm", "index.html")
