#!/usr/bin/env python3
"""Site library: parse section .md guides -> structured data; SEO components."""
import re, html, os, json

# Portable paths: env overrides win; default assumes this file lives in <repo>/scripts/
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_SRC = os.environ.get("AWB_REPO_SRC") or os.path.dirname(_SCRIPT_DIR)
OUT = os.environ.get("AWB_OUT") or os.path.join(os.path.dirname(_SCRIPT_DIR), "_site")
SITE = "https://ranakhan77.github.io/Awesome-Bangladesh"
GH = "https://github.com/RanaKhan77/Awesome-Bangladesh"

# IndexNow key (public by design; file {key}.txt is written to the site root)
INDEXNOW_KEY = "a3f8c2e91d4b7f6a5c0e2b8d9f1a4c7e"

SECTIONS = [
    ("developer-tools", "🧰", "Developer tools & libraries",
     "Open-source developer tools from Bangladesh — React design systems, scraping toolkits, Bangla terminal editors and Docker images.",
     "developer tools, bangladesh libraries, react design system bangladesh, npm packages bangladesh, docker bangladesh"),
    ("datasets", "📦", "Datasets & open data",
     "58 verified Bangladesh datasets — government portals plus Hugging Face and Kaggle corpora for Bangla NLP, speech, weather, health and finance.",
     "bangladesh dataset, bangla dataset, bangladesh open data, data.gov.bd, kaggle bangladesh, huggingface bangla"),
    ("apis", "🔌", "APIs & integrations",
     "Free Bangladesh APIs — keyless endpoints for geography, prayer times, exchange rates, railway schedules and Bangla news, plus SDK wrappers.",
     "bangladesh api, free bangla api, bd apis, bangladesh exchange rate api, bangladesh railway api, keyless api"),
    ("bangla-nlp", "🇧🇩", "Bangla language & NLP",
     "Bangla NLP open source — Avro and OpenBangla keyboards, Unicode-Bijoy converters, tokenizers, spell checkers, speech-to-text and PDF libraries.",
     "bangla nlp, bengali nlp, avro keyboard, openbangla, bangla unicode, bangla tokenizer, bangla speech to text"),
    ("aiml", "🤖", "AI/ML & research",
     "Bangladeshi AI models — banglagov, BUET BanglaBERT, Hishab TituLM LLMs, dialect speech recognition and MCP servers, with licences stated.",
     "bangla bert, bangla llama, bangladesh ai models, banglagov, titulm, bengali ai, bangla asr"),
    ("fintech", "💒", "Fintech & e-commerce",
     "Bangladesh fintech SDKs — bKash, SSLCommerz, Nagad and shurjoPay for Laravel, Flutter, Node and Python, plus Pathao, RedX and Steadfast courier APIs.",
     "bkash api, sslcommerz, nagad api, bangladesh payment gateway sdk, pathao api, bangladesh fintech"),
    ("security", "🔒", "Cybersecurity & privacy",
     "Bangladesh cybersecurity open source — web vulnerability scanners, OSINT exposure checkers and BDIX network tools from local researchers.",
     "bangladesh cybersecurity, bdix tools, website vulnerability scanner, osint bangladesh, bd security tools"),
    ("civic-tech", "🏢", "Civic tech & public services",
     "Bangladesh civic tech — the Bangla.gov.bd AI portal (Kagaj, Jijnsha, Borno OCR), legal platforms, DESCO meter APIs and bill calculators.",
     "bangla.gov.bd, bangladesh civic tech, borno ocr, kagaj ai, desco api, bangladesh government ai"),
    ("crisis-response", "🚨", "Crisis response",
     "Bangladesh crisis response open source — offline-first flood SOS apps, community mesh networks and ML flood prediction for the haor region.",
     "bangladesh flood app, offline sos bangladesh, mesh network bangladesh, disaster response bd, haor flood"),
    ("geography", "🧭", "Geography & open maps",
     "Bangladesh geodata — division to union boundaries (4,540 unions with p-codes), GeoJSON libraries, OSM extracts and SVG district maps.",
     "bangladesh geojson, bangladesh map data, divisions districts upazila union, bd geodata, bangladesh boundaries"),
    ("education", "🎓", "Education & learning",
     "Learn programming in Bangla — system design, interview questions from Bangladeshi tech companies, algorithm visualizers and HSC study platforms.",
     "bangla programming, system design bangla, bangladesh interview questions, bangla tutorial, learn coding bangla"),
    ("awesome-lists", "📚", "Awesome lists & communities",
     "Awesome Bangladesh lists and communities — developer directories, FOSS indexes, Bengali.AI, Python Bangladesh, BDOSN and made-in-bangladesh.",
     "awesome bangladesh, bangladeshi developers, bddevs, bangladesh foss, python bangladesh, bengali.ai"),
    ("services", "🏪", "Developer services (not open)",
     "Bangladeshi developer services — bKash, SSLCommerz, Pathao, RedX and Barikoi portals and SMS gateways, with access models stated honestly.",
     "bkash developer, bangladesh sms gateway, barikoi api, porichoy api, bangladesh developer portal"),
]

MD_LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")

def resolve_href(url):
    """Map guide-relative md links to site pages or GitHub blobs."""
    if url.startswith("http"):
        return url
    base = url.split("#")[0]
    anchor = ("#" + url.split("#")[1]) if "#" in url else ""
    # bare section file -> section page
    m = re.match(r"^([a-z0-9-]+)\.md$", base)
    if m and os.path.exists(os.path.join(REPO_SRC, "docs", "sections", base)):
        return f"/Awesome-Bangladesh/{m.group(1)}.html{anchor}"
    # repo links (check ../../ before ../)
    if base.startswith("../../"):
        return GH + "/blob/main/" + base[4:] + anchor
    if base.startswith("../"):
        return GH + "/blob/main/docs/" + base[3:] + anchor
    return GH + "/blob/main/" + base + anchor

def esc(s):
    return html.escape(s, quote=False)

def md_links_to_html(text):
    """Convert [name](url) inside descriptions to <a>; escape the rest.
    Handles http URLs and guide-relative links (fintech.md, ../policy.md, ../../legacy.md)."""
    parts, pos = [], 0
    for m in MD_LINK.finditer(text):
        parts.append(esc(text[pos:m.start()]))
        href = resolve_href(m.group(2))
        ext = href.startswith("http") and "github.com" not in href
        parts.append(f'<a href="{html.escape(href)}"{" target=\"_blank\" rel=\"noopener\"" if ext else ""}>{esc(m.group(1))}</a>')
        pos = m.end()
    parts.append(esc(text[pos:]))
    return "".join(parts)

def parse_guide(slug):
    """Parse a section guide .md -> dict with intro, stats_line, rows, picks, verified bullets."""
    path = os.path.join(REPO_SRC, "docs", "sections", slug + ".md")
    src = open(path, encoding="utf-8").read()
    lines = src.split("\n")

    d = {"slug": slug, "rows": [], "picks": [], "verified": []}
    # intro = paragraph after the nav quote line
    for i, l in enumerate(lines):
        if l.startswith("> Part of"):
            # intro is next non-empty paragraph
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            para = []
            while j < len(lines) and lines[j].strip():
                para.append(lines[j].strip()); j += 1
            d["intro"] = " ".join(para)
            break
    m = re.search(r"\*\*(\d+) verified entries\*\*", src)
    d["count"] = m.group(1) if m else "?"

    # table rows: any row with >=4 cells that is not the header or separator
    for l in lines:
        ls = l.strip()
        if not ls.startswith("|") or ls.startswith("|--") or ls.startswith("| Project"):
            continue
        cells = [c.strip() for c in ls.strip("|").split("|")]
        if len(cells) < 4:
            continue
        first = cells[0]
        if not first or first.startswith("---"):
            continue
        links = MD_LINK.findall(first)
        if links:
            name, url = links[0]
        else:
            name, url = first, None
        d["rows"].append({
            "name_html": md_links_to_html(first),
            "name": name,
            "url": url,
            "desc": cells[1],
            "licence": cells[2],
            "bd": cells[3],
        })

    # picks: "### [x](url)" or "### **x**" until "## How this section is verified"
    in_picks = False
    for l in lines:
        if l.startswith("## Editor's picks"):
            in_picks = True; continue
        if l.startswith("## How this section is verified"):
            in_picks = False; continue
        if in_picks:
            if l.startswith("### "):
                title = l[4:].strip()
                tlinks = MD_LINK.findall(title)
                if tlinks:
                    t, u = tlinks[0]
                else:
                    t, u = title.strip("*"), None
                d["picks"].append({"title": t, "url": u, "body": []})
            elif l.strip() and d["picks"]:
                d["picks"][-1]["body"].append(l.strip())
    for p in d["picks"]:
        p["body"] = " ".join(p["body"])

    # verification bullets
    in_v = False
    for l in lines:
        if l.startswith("## How this section is verified"):
            in_v = True; continue
        if in_v and l.startswith("- "):
            d["verified"].append(l[2:].strip())
    return d

def licence_chip(lic):
    """Render licence cell as chip HTML."""
    t = lic.strip()
    if t in ("—", "", "see notes"):
        return '<span class="chip note">see notes</span>'
    if t.startswith("⚠️"):
        return f'<span class="chip warn" title="{esc(t)}">⚠ {esc(t.replace("⚠️","").strip(" —"))}</span>'
    return f'<span class="chip">{esc(t)}</span>'

def bd_chip(bd):
    t = bd.strip()
    color = {"🟢": "#0a7", "🟡": "#c90", "🔵": "#06a"}.get(t[:1], "#555")
    label = t[1:].strip()
    return f'<span class="chip" style="border-color:{color};color:{color}">{esc(label)}</span>'

def github_mark(size=28):
    """Official GitHub octocat mark (inline SVG path) — links to GitHub per brand policy."""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>'''
