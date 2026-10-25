#!/usr/bin/env python3
"""Generate the multi-page super-SEO GitHub Pages site for Awesome Bangladesh."""
import os, json, datetime, re
from site_lib import (SECTIONS, SITE, GH, parse_guide, md_links_to_html, esc,
                      licence_chip, bd_chip, github_mark, OUT)

TODAY = datetime.date.today().isoformat()

CSS = """
:root{--green:#006A4E;--deep:#02382a;--red:#F42A41;--gold:#c9962e;--gold2:#f4c95d;--cream:#f7f4ec;--ink:#12261f;--soft:#5a6f66}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif;background:var(--cream);color:var(--ink);line-height:1.6}
a{color:var(--green)}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
header.hero{background:linear-gradient(180deg,#02382a,#006A4E 55%,#02382a);color:#fff;padding:0 0 26px}
header.hero svg{display:block;width:100%;height:auto}
.hero-under{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;align-items:center;margin-top:-6px}
.hero-under .pill{background:rgba(255,255,255,.08);border:1px solid rgba(244,201,93,.5);color:#f4c95d;border-radius:999px;padding:4px 14px;font-size:.86rem}
.answer{max-width:860px;margin:26px auto 6px;padding:0 20px;color:#eaf6f0;font-size:1.04rem;text-align:center}
.answer b{color:#f4c95d}
nav.top{position:sticky;top:0;z-index:50;background:rgba(2,56,42,.94);backdrop-filter:blur(6px);border-bottom:2px dashed var(--gold2)}
nav.top .wrap{display:flex;flex-wrap:nowrap;overflow-x:auto;gap:2px 10px;align-items:center;padding:8px 20px;scrollbar-width:none;-ms-overflow-style:none;justify-content:flex-start}
nav.top .wrap::-webkit-scrollbar{display:none}
nav.top::after{content:'';position:absolute;top:0;right:0;bottom:0;width:40px;background:linear-gradient(90deg,rgba(2,56,42,0),rgba(2,56,42,.94));pointer-events:none}
nav.top a{color:#eaf6f0;text-decoration:none;font-size:.84rem;padding:4px 7px;border-radius:8px;white-space:nowrap;flex:0 0 auto}
nav.top a:hover{background:rgba(244,201,93,.18);color:#fff}
nav.top a.home{font-weight:700;color:var(--gold2)}
nav.top a[aria-current="page"]{background:rgba(244,201,93,.22);color:var(--gold2);font-weight:700;box-shadow:inset 0 -2px 0 var(--gold2)}
.vh{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}
.stats{display:flex;flex-wrap:wrap;gap:14px;justify-content:center;margin:26px 0 8px}
.stat{background:#fff;border:1.5px solid #d8e5de;border-top:4px solid var(--green);border-radius:14px;padding:12px 22px;text-align:center;min-width:130px;box-shadow:0 2px 10px rgba(2,56,42,.06)}
.stat b{display:block;font-size:1.7rem;color:var(--green)}
.stat span{font-size:.82rem;color:var(--soft)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:18px;margin:26px 0}
.card{background:#fff;border:1.5px solid #d8e5de;border-radius:16px;padding:18px 20px;box-shadow:0 2px 10px rgba(2,56,42,.05);transition:transform .18s,box-shadow .18s;position:relative;overflow:hidden}
.card:hover{transform:translateY(-3px);box-shadow:0 8px 22px rgba(2,56,42,.12)}
.card::before{content:'';position:absolute;inset:0 auto 0 0;width:5px;background:linear-gradient(180deg,var(--red),var(--green))}
.card h3{margin:0 0 6px;font-size:1.05rem}
.card h3 a{color:var(--ink);text-decoration:none}
.card p{margin:0 0 10px;font-size:.9rem;color:var(--soft)}
.card .links{display:flex;gap:12px;font-size:.85rem;flex-wrap:wrap}
.card .n{position:absolute;top:14px;right:16px;background:var(--cream);border:1px solid #d8e5de;color:var(--green);border-radius:999px;font-size:.78rem;padding:2px 10px;font-weight:700}
section.block{background:#fff;border:1.5px solid #d8e5de;border-radius:16px;margin:22px 0;padding:22px 26px;box-shadow:0 2px 10px rgba(2,56,42,.05)}
section.block h2{margin-top:0;color:var(--green)}
section.block h1.sech1{margin-top:0;color:var(--green);font-size:1.5rem;line-height:1.3}
.entries{list-style:none;margin:0;padding:0}
.entries li{padding:12px 4px;border-bottom:1px dashed #d8e5de}
.entries li:last-child{border-bottom:none}
.entries .t{display:flex;flex-wrap:wrap;gap:8px;align-items:baseline}
.entries .t a{font-weight:700;font-size:1.02rem;text-decoration:none}
.entries .t a:hover{text-decoration:underline}
.entries .d{display:block;color:var(--soft);font-size:.92rem;margin-top:3px}
.entries .chips{display:flex;gap:6px;flex-wrap:wrap;margin-top:6px}
.chip{display:inline-block;border:1px solid #c9d8d0;border-radius:999px;padding:1px 10px;font-size:.74rem;background:#f2f7f4;color:#3c5a4e}
.chip.warn{border-color:#e6b98a;background:#fdf3e7;color:#9a5b13}
.chip.note{border-style:dashed}
.crumbs{font-size:.84rem;color:var(--soft);padding:14px 0 0}
.crumbs a{color:var(--green)}
.picks{background:linear-gradient(180deg,#f4faf7,#fff);border:1.5px solid #cfe5db;border-left:5px solid var(--gold);border-radius:14px;padding:16px 22px;margin:20px 0}
.picks h3{margin:14px 0 4px;color:var(--deep)}
.picks h3 a{color:var(--deep)}
.picks p{margin:0 0 8px;color:var(--soft);font-size:.94rem}
.vlist{margin:8px 0 0;padding-left:20px;color:var(--soft);font-size:.9rem}
.vlist li{margin-bottom:5px}
.vlist a{color:var(--green)}
.pagenav{display:flex;justify-content:space-between;gap:12px;margin:26px 0 6px;flex-wrap:wrap}
.pagenav a{background:#fff;border:1.5px solid #d8e5de;border-radius:12px;padding:10px 16px;text-decoration:none;font-size:.9rem}
.pagenav a:hover{border-color:var(--green)}
.ghcta{display:flex;flex-wrap:wrap;align-items:center;gap:22px;justify-content:center;background:linear-gradient(135deg,#02382a,#006A4E);border-radius:18px;color:#fff;padding:30px 28px;margin:30px 0;text-align:center}
.ghcta .mark{color:#fff}
.ghcta .mark svg{filter:drop-shadow(0 4px 10px rgba(0,0,0,.35))}
.ghcta h2{margin:0;color:#fff;font-size:1.5rem}
.ghcta p{margin:6px 0 14px;color:#cfe9dd}
.btn{display:inline-block;background:#fff;color:var(--deep);font-weight:700;border-radius:999px;padding:10px 24px;text-decoration:none;border:2px solid var(--gold2)}
.btn:hover{background:var(--gold2)}
.btn.ghost{background:transparent;color:#fff;border-color:rgba(255,255,255,.6)}
.faq details{background:#fff;border:1.5px solid #d8e5de;border-radius:12px;padding:12px 18px;margin:10px 0}
.faq summary{font-weight:700;color:var(--deep);cursor:pointer}
.faq p{color:var(--soft);font-size:.94rem}
footer{margin-top:40px;background:var(--deep);color:#cfe9dd;text-align:center;padding:8px 0 26px}
footer img{display:block;margin:0 auto;max-width:720px;width:92%;height:auto}
footer p{font-size:.86rem;padding:0 16px}
footer a{color:var(--gold2)}
.kantha{stroke-dasharray:14 10;animation:stitch 1.8s linear infinite}
@keyframes stitch{to{stroke-dashoffset:-24}}
.fade{animation:fadeup .7s ease both}
@keyframes fadeup{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.search{max-width:520px;margin:18px auto 0;display:flex;gap:8px}
.search input{flex:1;border:2px solid var(--gold);border-radius:999px;padding:10px 18px;font-size:1rem;background:#fff;color:var(--ink)}
.search input:focus{outline:3px solid rgba(244,201,93,.35);border-color:var(--green)}
#stats-line{text-align:center;color:var(--soft);font-size:.84rem;margin-top:6px}
.hide{display:none}
@media(max-width:640px){.ghcta{flex-direction:column}}
"""

HERO_SVG = '''<svg viewBox="0 0 1200 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Awesome Bangladesh — open source, open data and free APIs from Bangladesh" preserveAspectRatio="xMidYMid slice">
<defs>
<linearGradient id="field" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#03271e"/><stop offset=".55" stop-color="#00432f"/><stop offset="1" stop-color="#006a4e"/></linearGradient>
<radialGradient id="sunG" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ff6b62"/><stop offset=".6" stop-color="#f42a41"/><stop offset="1" stop-color="#c8102e"/></radialGradient>
<linearGradient id="gold" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8a6d1f"/><stop offset=".5" stop-color="#e9c46a"/><stop offset="1" stop-color="#8a6d1f"/></linearGradient>
</defs>
<rect width="1200" height="300" fill="url(#field)"/>
<path d="M0 18 H1200" stroke="url(#gold)" stroke-width="3" class="kantha"/>
<path d="M0 282 H1200" stroke="url(#gold)" stroke-width="3" class="kantha"/>
<g transform="translate(600,120)">
<circle r="44" fill="url(#sunG)"><animate attributeName="r" values="44;48;44" dur="4s" repeatCount="indefinite"/><animate attributeName="opacity" values="1;.88;1" dur="4s" repeatCount="indefinite"/></circle>
<circle r="56" fill="none" stroke="#f42a41" stroke-opacity=".55"><animate attributeName="r" values="54;92" dur="3.6s" repeatCount="indefinite"/><animate attributeName="stroke-opacity" values=".55;0" dur="3.6s" repeatCount="indefinite"/></circle>
<circle r="56" fill="none" stroke="#f42a41" stroke-opacity=".4"><animate attributeName="r" values="54;118" dur="3.6s" begin="1.2s" repeatCount="indefinite"/><animate attributeName="stroke-opacity" values=".4;0" dur="3.6s" begin="1.2s" repeatCount="indefinite"/></circle>
<circle r="56" fill="none" stroke="#f42a41" stroke-opacity=".3"><animate attributeName="r" values="54;140" dur="3.6s" begin="2.4s" repeatCount="indefinite"/><animate attributeName="stroke-opacity" values=".3;0" dur="3.6s" begin="2.4s" repeatCount="indefinite"/></circle>
<g fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" opacity=".95">
<path d="M-104 -16 l-14 14 14 14"/><path d="M104 -16 l14 14 -14 14"/>
</g>
</g>
<text x="600" y="218" text-anchor="middle" font-family="'Segoe UI',system-ui,Arial,sans-serif" font-size="34" font-weight="800" fill="#ffffff" letter-spacing="1">AWESOME BANGLADESH</text>
<text x="600" y="252" text-anchor="middle" font-family="'Segoe UI',system-ui,Arial,sans-serif" font-size="17" fill="#e9c46a">Open Source · Open Data · Free APIs — মেড ইন বাংলাদেশ</text>
</svg>'''

SECTION_BANNER = lambda slug, title, bn: f'''<svg viewBox="0 0 896 180" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{esc(title)} — Awesome Bangladesh section" preserveAspectRatio="xMidYMid slice">
<defs>
<linearGradient id="f" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#02382a"/><stop offset=".5" stop-color="#006A4E"/><stop offset="1" stop-color="#02382a"/></linearGradient>
<radialGradient id="s" cx=".4" cy=".35" r=".9"><stop offset="0" stop-color="#ff8d7a"/><stop offset=".5" stop-color="#F42A41"/><stop offset="1" stop-color="#b01129"/></radialGradient>
<linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#c9962e"/><stop offset=".5" stop-color="#f4c95d"/><stop offset="1" stop-color="#c9962e"/></linearGradient>
</defs>
<rect width="896" height="180" rx="14" fill="url(#f)"/>
<path d="M16 12 H880" stroke="url(#g)" stroke-width="2.5" class="kantha"/>
<path d="M16 168 H880" stroke="url(#g)" stroke-width="2.5" class="kantha"/>
<circle cx="120" cy="90" r="52" fill="url(#s)"><animate attributeName="r" values="52;56;52" dur="4.5s" repeatCount="indefinite"/></circle>
<circle cx="120" cy="90" r="64" fill="none" stroke="url(#g)" stroke-width="2" stroke-dasharray="4 12" stroke-linecap="round" opacity=".9"><animateTransform attributeName="transform" type="rotate" from="0 120 90" to="360 120 90" dur="50s" repeatCount="indefinite"/></circle>
<text x="120" y="106" text-anchor="middle" font-family="'Noto Sans Bengali','Nirmala UI','Bangla MN',sans-serif" font-size="52" font-weight="700" fill="#fff">{bn}</text>
<text x="215" y="86" font-family="'Segoe UI',system-ui,Arial,sans-serif" font-size="30" font-weight="800" fill="#ffffff">{esc(title)}</text>
<text x="215" y="118" font-family="'Segoe UI',system-ui,Arial,sans-serif" font-size="14.5" fill="#cfe9dd">Awesome Bangladesh — verified section guide</text>
</svg>'''

# Bangla letter per section (matches banner system)
BN_LETTER = {"developer-tools":"ড","datasets":"ত","apis":"এ","bangla-nlp":"ব","aiml":"য","fintech":"৳",
             "security":"ন","civic-tech":"স","crisis-response":"দ","geography":"ম","education":"শ",
             "awesome-lists":"অ","services":"প"}

FAQS = [
 ("What is Awesome Bangladesh?",
  "Awesome Bangladesh is a hand-verified directory of open-source software, datasets, APIs and research connected to Bangladesh — 200+ entries across 13 sections covering Bangla NLP, government open data, fintech SDKs, maps, security tools and learning resources. Every entry states its licence and Bangladesh connection, and the whole list is CC0-licensed."),
 ("Who maintains Awesome Bangladesh?",
  "The list is maintained by Rana Khan (RanaKhan77 on GitHub), with contributions welcome through the repository's CONTRIBUTING.md guide. Issues reporting stale links or wrong licence notes are treated as valuable contributions."),
 ("What counts as connected to Bangladesh?",
  "Four tiers qualify: a maintainer based in Bangladesh, a verified member of the Bangladeshi diaspora, a Bangladeshi organisation, or a product explicitly built for Bangladesh. The evidence for each entry's connection is recorded during verification."),
 ("Are the datasets and models free to use?",
  "Licences are stated per entry exactly as the publisher declares them. Government portals often leave licences unspecified and are flagged with a warning; several BUET research models carry non-commercial CC BY-NC-SA terms; the largest cleanly licensed corpus (TituLM, 24.3M documents) and Mozilla's 1,277-hour Bengali Common Voice release are CC-BY-4.0 and CC0 respectively."),
 ("How are entries verified?",
  "Links are fetched live at verification time, dead links are removed rather than kept for history, Bangladesh connections must have pointable evidence, and items unmaintained for three or more years move to a clearly-labelled legacy file instead of being silently deleted."),
 ("Can I contribute or suggest an entry?",
  "Yes — read the scope and eligibility rules first, then open an issue or pull request on GitHub. New entries need a verifiable Bangladesh connection, a working canonical link and licence information."),
]

def head_block(title, desc, keywords, url, og_image=None):
    og = og_image or SITE + "/assets/og-card.png"
    return f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="google-site-verification" content="udVeOT52mzcxhqNNak5tWgXAQpiCmsjgeW-fYJl9nPE">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="keywords" content="{esc(keywords)}">
<meta name="author" content="Rana Khan">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
<meta name="theme-color" content="#006A4E">
<link rel="canonical" href="{url}">
<link rel="icon" href="/Awesome-Bangladesh/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/Awesome-Bangladesh/favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="/Awesome-Bangladesh/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Awesome Bangladesh">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:image:secure_url" content="{og}">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1280">
<meta property="og:image:height" content="640">
<meta property="og:image:alt" content="Awesome Bangladesh — open source, open data and free APIs from Bangladesh">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{og}">
<meta name="twitter:image:alt" content="Awesome Bangladesh — open source, open data and free APIs from Bangladesh">'''

# Compact nav labels (single-line scrollable top menu; emoji comes from SECTIONS)
NAV_LABELS = {
    "developer-tools": "Dev tools", "datasets": "Data", "apis": "APIs",
    "bangla-nlp": "Bangla NLP", "aiml": "AI/ML", "fintech": "Fintech",
    "security": "Security", "civic-tech": "Civic", "crisis-response": "Crisis",
    "geography": "Maps", "education": "Learn", "awesome-lists": "Lists",
    "services": "Services",
}

def nav_block(active=None):
    out = ['<nav class="top" aria-label="Section navigation"><div class="wrap">']
    home_cls = ' class="home"' + (' aria-current="page"' if active is None else '')
    out.append(f'<a href="/Awesome-Bangladesh/"{home_cls}>🏠 Home</a>')
    for s in SECTIONS:
        slug = s[0]
        label = f"{s[1]} {NAV_LABELS[slug]}"
        cur = ' aria-current="page"' if slug == active else ""
        out.append(f'<a href="/Awesome-Bangladesh/{slug}.html"{cur}>{label}</a>')
    out.append("</div></nav>")
    return "".join(out)

def short(t):
    return (t.replace(" & ", " & ").replace(" (not open)", "")
             .replace("Developer tools", "Dev tools")
             .replace(" libraries", " libs")
             .replace("Awesome lists", "Lists")
             .replace(" communities", "communities")
             .replace("Cybersecurity & privacy", "Security")
             .replace("Bangla language", "Bangla")
             .replace("Civic tech & public services", "Civic")
             .replace("Geography & open maps", "Maps")
             .replace("Education & learning", "Learn")
             .replace("Crisis response", "Crisis")
             .replace("APIs & integrations", "APIs")
             .replace("AI/ML & research", "AI/ML")
             .replace("Fintech & e-commerce", "Fintech")
             .replace("Datasets & open data", "Data"))

def footer_block():
    return f'''<footer>
<img src="assets/footer.svg" width="720" height="103" alt="Awesome Bangladesh animated footer — red sun rising over a kantha-stitch border">
<p>Maintained by <a href="https://github.com/RanaKhan77">Rana Khan</a> · List content <a href="{GH}/blob/main/LICENSE">CC0-1.0</a> · <a href="{GH}">View on GitHub</a> · <a href="{GH}/blob/main/CONTRIBUTING.md">Contribute</a> · <a href="{GH}/blob/main/legacy.md">Legacy entries</a></p>
<p>Made in Bangladesh · মেড ইন বাংলাদেশ 🇧🇩 · Another live project: <a href="https://bangladeshexport.com/">bangladeshexport.com</a></p>
</footer>'''
