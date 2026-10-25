#!/usr/bin/env python3
"""Generate all pages: index.html, 13 section pages, sitemap, robots, llms.txt, 404."""
import os, json, re, shutil
from site_lib import (SECTIONS, SITE, GH, INDEXNOW_KEY, parse_guide, md_links_to_html, esc,
                      licence_chip, bd_chip, github_mark, OUT, REPO_SRC)
import gen_site as T

def html_href(u):
    return u or "#"

os.makedirs(OUT, exist_ok=True)
os.makedirs(OUT + "/assets", exist_ok=True)

TOTAL = 0
GUIDES = {}
for slug, emoji, title, desc, kw in SECTIONS:
    g = parse_guide(slug)
    GUIDES[slug] = g
    TOTAL += len(g["rows"])

# Dynamic stats from data/*.json (auto-sync: counts never go stale)
def _jlen(name):
    try:
        return len(json.load(open(os.path.join(REPO_SRC, "data", name), encoding="utf-8")))
    except Exception:
        return None
REPOS_COUNT = (_jlen("projects.json") or 0) + (_jlen("registries.json") or 0) or TOTAL
# prefer the guide's verified count so the index stat always agrees with the section page
DATASETS_COUNT = int(GUIDES["datasets"]["count"] or 0) or _jlen("datasets.json") or 0

# ---------------- index.html ----------------
idx_jsonld_website = {
    "@context": "https://schema.org", "@type": "WebSite",
    "name": "Awesome Bangladesh", "url": SITE + "/",
    "description": "Hand-verified directory of Bangladeshi open source, open data and free APIs.",
    "inLanguage": "en",
    "publisher": {"@type": "Person", "name": "Rana Khan", "url": "https://github.com/RanaKhan77"},
    "mainEntity": {"@type": "ItemList", "numberOfItems": len(SECTIONS),
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": f"{e} {t}",
                             "url": f"{SITE}/{s}.html"} for i, (s, e, t, _, _) in enumerate(SECTIONS)]},
}
idx_jsonld_faq = {
    "@context": "https://schema.org", "@type": "FAQPage",
    "mainEntity": [{"@type": "Question", "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in T.FAQS],
}
idx_jsonld_org = {
    "@context": "https://schema.org", "@type": "CollectionPage",
    "name": "Awesome Bangladesh", "url": SITE + "/",
    "isPartOf": {"@type": "WebSite", "url": SITE + "/"},
    "about": {"@type": "Thing", "name": "Open source in Bangladesh"},
    "speakable": {"@type": "SpeakableSpecification",
                  "cssSelector": [".answer", "h1"]},
}

cards = []
for slug, emoji, title, desc, kw in SECTIONS:
    g = GUIDES[slug]
    cards.append(f'''<article class="card fade">
<span class="n">{g['count']} entries</span>
<h3><a href="{slug}.html">{emoji} {esc(title)}</a></h3>
<p>{esc(desc.split('—')[1].strip() if '—' in desc else desc)}</p>
<div class="links"><a href="{slug}.html">Explore section →</a><a href="{GH}/blob/main/docs/sections/{slug}.md">GitHub guide ↗</a></div>
</article>''')

faq_html = "\n".join(
    f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in T.FAQS)

INDEX_TITLE = "Awesome Bangladesh — Open Source, Datasets & Free APIs"
INDEX_DESC = (f"Hand-verified directory of {TOTAL} Bangladeshi open-source projects, datasets and free APIs. "
              f"Licences stated, links checked — {len(SECTIONS)} sections from NLP to fintech.")
assert len(INDEX_TITLE) <= 60, f"index title too long: {len(INDEX_TITLE)}"
assert len(INDEX_DESC) <= 158, f"index desc too long: {len(INDEX_DESC)}"

index_html = f'''<!doctype html>
<html lang="en">
<head>
{T.head_block(INDEX_TITLE, INDEX_DESC, "awesome bangladesh, bangladesh open source, bangla nlp, bangladesh dataset, bangladesh api, made in bangladesh, bangladeshi developers, bddevs, bengali ai, bangladesh open data", SITE + "/")}
<script type="application/ld+json">{json.dumps(idx_jsonld_website, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(idx_jsonld_faq, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(idx_jsonld_org, ensure_ascii=False)}</script>
<style>{T.CSS}</style>
</head>
<body>
<h1 class="vh">Awesome Bangladesh — open source, open data and free APIs from Bangladesh</h1>
<header class="hero">
{T.HERO_SVG}
<p class="answer"><b>Awesome Bangladesh</b> is a hand-verified directory of <b>{TOTAL} open-source projects, datasets and free APIs</b> connected to Bangladesh — built by Bangladeshis at home and in the diaspora, or built for Bangladesh. Every entry is checked live, carries its licence, and its Bangladesh connection is evidenced. The list itself is <b>CC0</b> — copy it freely.</p>
<div class="hero-under">
<span class="pill">🗓 Verified {T.TODAY}</span>
<span class="pill">📦 {len(SECTIONS)} sections</span>
<span class="pill">⚖️ Licences stated on every entry</span>
<span class="pill">🇧🇩 Made in Bangladesh</span>
</div>
<div class="search"><input id="q" type="search" placeholder="Search across all sections — try “bkash”, “geojson”, “OCR”…" aria-label="Search entries"></div>
<p id="stats-line">showing all {TOTAL} entries</p>
</header>
{T.nav_block()}
<div class="wrap">
<div class="stats">
<div class="stat"><b>{TOTAL}</b><span>verified entries</span></div>
<div class="stat"><b>{len(SECTIONS)}</b><span>sections</span></div>
<div class="stat"><b>{REPOS_COUNT}</b><span>open-source repos &amp; packages</span></div>
<div class="stat"><b>{DATASETS_COUNT}</b><span>datasets &amp; corpora</span></div>
<div class="stat"><b>CC0</b><span>list licence</span></div>
</div>
<h2 style="text-align:center;color:var(--deep)">Explore the sections</h2>
<div class="grid" id="grid">
{"".join(cards)}
</div>
<section class="block faq">
<h2>Frequently asked questions</h2>
{faq_html}
</section>
<div class="ghcta">
<div class="mark">{github_mark(84)}</div>
<div>
<h2>The whole list lives on GitHub</h2>
<p>Star it, fork it, open an issue — every entry's evidence trail is public.</p>
<a class="btn" href="{GH}">★ RanaKhan77/Awesome-Bangladesh</a>
<a class="btn ghost" href="{GH}/blob/main/CONTRIBUTING.md">Contribute</a>
</div>
</div>
</div>
{T.footer_block()}
<script>
const q=document.getElementById('q'),stats=document.getElementById('stats-line');
const cards=[...document.querySelectorAll('#grid .card')];
function apply(){{const s=q.value.trim().toLowerCase();let n=0;
for(const c of cards){{let hit=!s||c.textContent.toLowerCase().includes(s);c.classList.toggle('hide',!hit);if(hit)n++;}}
stats.textContent=s?n+' section'+(n==1?'':'s')+' match':'showing all {TOTAL} entries in '+{len(SECTIONS)}+' sections';}}
q.addEventListener('input',apply);apply();
</script>
</body>
</html>'''
open(OUT + "/index.html", "w", encoding="utf-8").write(index_html)
print("index.html", len(index_html) // 1024, "KB")

# ---------------- section pages ----------------
for si, (slug, emoji, title, desc, kw) in enumerate(SECTIONS):
    g = GUIDES[slug]
    url = f"{SITE}/{slug}.html"
    prev = SECTIONS[si - 1] if si > 0 else None
    nxt = SECTIONS[si + 1] if si + 1 < len(SECTIONS) else None

    jsonld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": title, "item": url}]},
            {"@type": "CollectionPage", "name": f"{title} — Awesome Bangladesh", "url": url,
             "isPartOf": {"@type": "WebSite", "name": "Awesome Bangladesh", "url": SITE + "/"},
             "description": desc,
             "mainEntity": {"@type": "ItemList", "numberOfItems": len(g["rows"]),
                 "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": r["name"],
                                      "url": r["url"] or url} for i, r in enumerate(g["rows"]) if r["url"]][:40]}},
        ]
    }

    entries = []
    for r in g["rows"]:
        name_html = r["name_html"]
        desc_html = md_links_to_html(r["desc"])
        entries.append(f'''<li><span class="t">{name_html}</span>
<span class="d">{desc_html}</span>
<span class="chips">{licence_chip(r['licence'])} {bd_chip(r['bd'])}</span></li>''')

    picks = ""
    if g["picks"]:
        ph = []
        for p in g["picks"]:
            t = f'<a href="{html_href(p["url"])}">{esc(p["title"])}</a>' if p.get("url") else esc(p["title"])
            ph.append(f'<h3>{t}</h3><p>{md_links_to_html(p["body"])}</p>')
        picks = f'<div class="picks"><h2 style="margin-top:0">✨ Editor&rsquo;s picks</h2>{"".join(ph)}</div>'

    verified = "".join(f"<li>{md_links_to_html(v)}</li>" for v in g["verified"])

    page_title = f"{title} | Awesome Bangladesh"
    assert len(page_title) <= 60, f"title too long ({len(page_title)}): {page_title}"
    assert len(desc) <= 158, f"desc too long ({len(desc)}): {slug}"

    page = f'''<!doctype html>
<html lang="en">
<head>
{T.head_block(page_title, desc, kw + ", awesome bangladesh", url)}
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
<style>{T.CSS}</style>
</head>
<body>
{T.nav_block(slug)}
<div class="wrap">
<p class="crumbs"><a href="/Awesome-Bangladesh/">Awesome Bangladesh</a> › <strong>{esc(title)}</strong></p>
<div style="margin:14px 0 4px">{T.SECTION_BANNER(slug, title, T.BN_LETTER[slug])}</div>
<section class="block">
<h1 class="sech1">{emoji} {esc(title)} <span class="chip" style="vertical-align:middle">{g['count']} verified entries</span></h1>
<p style="color:var(--soft)">{md_links_to_html(g['intro'])}</p>
<p style="font-size:.86rem"><a href="{GH}/blob/main/docs/sections/{slug}.md">{github_mark(16)} Edit this section on GitHub</a> · Last verified {T.TODAY} · Rules: <a href="{GH}/blob/main/docs/curation-policy.md">curation policy</a></p>
</section>
<section class="block">
<h2>All entries</h2>
<ul class="entries">
{"".join(entries)}
</ul>
</section>
{picks}
<section class="block">
<h2>How this section is verified</h2>
<ul class="vlist">{verified}</ul>
</section>
<div class="pagenav">
{'<a href="' + prev[0] + '.html">← ' + prev[1] + ' ' + T.short(prev[2]) + '</a>' if prev else '<span></span>'}
<a href="/Awesome-Bangladesh/">🏠 All sections</a>
{'<a href="' + nxt[0] + '.html">' + nxt[1] + ' ' + T.short(nxt[2]) + ' →</a>' if nxt else '<span></span>'}
</div>
<div class="ghcta">
<div class="mark">{github_mark(56)}</div>
<div>
<h2 style="font-size:1.15rem">View this section on GitHub</h2>
<p>docs/sections/{slug}.md — part of RanaKhan77/Awesome-Bangladesh</p>
<a class="btn" href="{GH}/blob/main/docs/sections/{slug}.md">Open the guide ↗</a>
</div>
</div>
</div>
{T.footer_block()}
</body>
</html>'''
    open(OUT + f"/{slug}.html", "w", encoding="utf-8").write(page)
    print(f"{slug}.html", len(page) // 1024, "KB,", len(g["rows"]), "entries")

# ---------------- sitemap / robots / llms.txt / 404 / nojekyll ----------------
urls = [f"<url><loc>{SITE}/</loc><lastmod>{T.TODAY}</lastmod><changefreq>weekly</changefreq><priority>1.0</priority></url>"] + [
    f"<url><loc>{SITE}/{s[0]}.html</loc><lastmod>{T.TODAY}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>"
    for s in SECTIONS]
open(OUT + "/sitemap.xml", "w").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "\n".join(urls) + "\n</urlset>\n")

open(OUT + "/robots.txt", "w").write(
    "User-agent: *\nAllow: /\n\n"
    "# AI search citability crawlers — explicitly welcome (GEO/AEO)\n"
    "User-agent: OAI-SearchBot\nAllow: /\n"
    "User-agent: ChatGPT-User\nAllow: /\n"
    "User-agent: Claude-SearchBot\nAllow: /\n"
    "User-agent: Claude-User\nAllow: /\n"
    "User-agent: PerplexityBot\nAllow: /\n\n"
    "# AI training crawlers — allowed by owner preference\n"
    "User-agent: GPTBot\nAllow: /\n"
    "User-agent: ClaudeBot\nAllow: /\n"
    "User-agent: Google-Extended\nAllow: /\n\n"
    "Sitemap: " + SITE + "/sitemap.xml\n")

llms = f'''# Awesome Bangladesh

> A hand-verified directory of {TOTAL} open-source projects, datasets and free APIs connected to Bangladesh. Every entry is link-checked, licence-stated and Bangladesh-connection-evidenced. List content is CC0.

Maintained by Rana Khan (https://github.com/RanaKhan77). Repository: {GH}.

## Sections

'''
for slug, emoji, title, desc, kw in SECTIONS:
    g = GUIDES[slug]
    llms += f"- [{title}]({SITE}/{slug}.html): {desc} ({g['count']} entries)\n"
llms += f'''
## Key facts

- Verification date: {T.TODAY}; dead links removed rather than kept
- Licence model: stated per entry exactly as published; ⚠️ flags gaps and non-commercial terms
- Dormancy policy: items unmaintained 3+ years move to legacy.md with last-activity dates
- Data files: data/*.json (209 structured records) with a published JSON schema
- Licensing of the list itself: CC0-1.0

## Questions this site answers

- What open-source software is made in Bangladesh? -> See sections: developer tools, fintech, Bangla NLP
- Where can I get Bangladesh datasets? -> {SITE}/datasets.html
- Are there free Bangladesh APIs? -> {SITE}/apis.html
- What Bangla NLP models exist? -> {SITE}/bangla-nlp.html and {SITE}/aiml.html
- How do I accept bKash/SSLCommerz payments in code? -> {SITE}/fintech.html
'''
open(OUT + "/llms.txt", "w").write(llms)

open(OUT + "/404.html", "w").write('''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Page not found — Awesome Bangladesh</title><meta name="robots" content="noindex"><style>body{font-family:system-ui;background:#f7f4ec;display:grid;place-items:center;min-height:100vh;margin:0}div{text-align:center}a{color:#006a4e}</style></head><body><div><h1 style="color:#006a4e;font-size:4rem;margin:0">404</h1><p style="font-size:1.1rem">That page drifted off the map — like a lost rickshaw in Dhaka traffic.</p><p><a href="/Awesome-Bangladesh/"><b>← Back to Awesome Bangladesh</b></a></p></div></body></html>''')

open(OUT + "/.nojekyll", "w").write("")

# ---------------- static site assets (copied from repo assets/pages/) ----------------
PAGES_ASSETS = os.path.join(REPO_SRC, "assets", "pages")
copied = []
for fn in ["footer.svg", "logo.svg", "og-card.png"]:
    src = os.path.join(PAGES_ASSETS, fn)
    if os.path.exists(src):
        shutil.copyfile(src, os.path.join(OUT, "assets", fn)); copied.append("assets/" + fn)
for fn in ["favicon.svg", "favicon.ico", "apple-touch-icon.png"]:
    src = os.path.join(PAGES_ASSETS, fn)
    if os.path.exists(src):
        shutil.copyfile(src, os.path.join(OUT, fn)); copied.append(fn)

# IndexNow key file (search engines verify ownership via this file)
open(os.path.join(OUT, INDEXNOW_KEY + ".txt"), "w").write(INDEXNOW_KEY)

print("sitemap.xml, robots.txt, llms.txt, 404.html, .nojekyll written")
print("static assets copied:", ", ".join(copied) or "NONE (assets/pages/ missing!)")
print("indexnow key file written:", INDEXNOW_KEY + ".txt")
print("TOTAL ENTRIES:", TOTAL, "| repos:", REPOS_COUNT, "| datasets:", DATASETS_COUNT)
