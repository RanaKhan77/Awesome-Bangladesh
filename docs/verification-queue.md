# Verification queue

Items that look promising but do not yet meet the evidence bar for the main
list. Anyone may supply evidence (a profile link, an org page, a README
quote) via issue or PR — see [CONTRIBUTING](../CONTRIBUTING.md). Items with
negative findings are marked so we do not re-research them endlessly.

Last reviewed: 2026-10-24.

## Missing Bangladesh-connection evidence

| Item | What it is | What's missing | Where to look next |
|---|---|---|---|
| [olovajs/olova](https://github.com/olovajs/olova) | JS reactive framework, 183★, MIT | Any BD evidence at all — org page and README are silent | [org members page](https://github.com/orgs/olovajs/people), npm publisher, commit authors |
| [BanglaLLM](https://github.com/BanglaLLM) | Bangla LLM datasets org (bangla-alpaca-orca on HF) | Org location/description empty; only hint is a community reference | Org members, dataset card authors |
| [Kowsher](https://github.com/Kowsher) | BanglaFastText (PyPI), bangla-bert (HF), ekushey fonts module | Location shows "UCF", no country evidence | Personal site, university pages, co-authors |
| [EMTIAZZ](https://huggingface.co/EMTIAZZ) | bangladeshi-bangla-tts-vits model | Profile has only a first name, no affiliation | Model card, paper, social accounts |
| [Arunavaonly](https://huggingface.co/Arunavaonly) | Bangla sentiment model, 2M+ downloads | Likely Indian-Bengali; no BD evidence found — **negative lean** | Author page, associated papers |
| [iamshnoo](https://huggingface.co/iamshnoo) | alpaca-cleaned-bengali dataset | No BD evidence found — **negative lean** | Author page (CMU affiliation hints non-BD) |
| [evolve75](https://github.com/evolve75) | bangla-date PyPI package (186 dl/month) | No BD evidence | Commit history, email in old commits |
| [faruk-ahmad](https://github.com/faruk-ahmad) | bengali PyPI package | Tokyo-based; no BD evidence | Employer page, conference bios |
| [Foysal87](https://github.com/Foysal87) | bn_nlp toolkit | No location; Orbitax affiliation unconfirmed | Orbitax office pages, LinkedIn |
| [asiff00](https://github.com/asiff00) | bangla-pdf-ocr | No location evidence | Profile, org memberships |
| [mbs57](https://github.com/mbs57) | bangla-render PyPI package | No location evidence | PyPI author email, repo commits |
| [soikat](https://github.com/soikat) | prayer-time-bd npm package | No repo URL on registry; profile has no location | npm publisher email |
| [mahinmd](https://github.com/mojnomiya) | pathao PyPI wrapper | Location unknown | PyPI author field, profile |
| [transactbd](https://www.npmjs.com/package/transactbd) | Multi-gateway payment abstraction | GitHub account 404s; npm publisher only | npm publisher profile, download stats |
| [Y3454R](https://github.com/Y3454R) | bd-geojson npm package (747 dl/month) | No location evidence | npm profile, repo README |
| [TasfiqulGhani](https://github.com/TasfiqulGhani) | bd-offline-geocoder | Bangkok-based; BD origin unconfirmed | LinkedIn, previous employers |
| [wovosoft](https://github.com/wovosoft) | bd-geocode + bkb-offices Packagist packages | Org identity unclear | Packagist maintainer links, company registry |
| [eabgitbd](https://github.com/eabgitbd) | PrescribePro-Rx health platform | Org identity unknown; README says "worldwide" | Org members, domain WHOIS |
| [shahariar-ahmad/courier-fraud-checker-bd](https://packagist.org/packages/shahariar-ahmad/courier-fraud-checker-bd) | Courier fraud checker | Maintainer profile unverified | Packagist profile, GitHub link |
| [UGFoundation/swaralipi-js](https://www.npmjs.com/package/@ugfoundation/swaralipi-js) | Rabindra Sangeet notation library | Maintainer nationality unconfirmed; possibly Indian-Bengali | Org page, project history |
| [apakabarlabs/bengali-romanizer](https://pypi.org/project/bengali-romanizer/) | Bengali romanizer | "apakabar" phrasing suggests Indonesian origin — possible exclusion | Lab website, authors |
| [Tahsin-Mayeesha](https://huggingface.co/datasets/Tahsin-Mayeesha/Bengali-SQuAD) | Bengali SQuAD translation | BigScience member; BD tie not pinned down | Personal site, Bangla ASR paper credits |
| [BanglishRev](https://huggingface.co/datasets/BanglishRev/bangla-english-and-code-mixed-ecommerce-review-dataset) | Daraz e-commerce review dataset | Org/maintainer unverified | Dataset card, associated paper |
| [Jakir057](https://huggingface.co/datasets/Jakir057/bangladeshi_banknotes_70k) | Banknote image dataset | Maintainer unverified | HF profile |
| [Mahadih534](https://huggingface.co/datasets/Mahadih534/Institutional-Information-of-Bangladesh) | Institutional directory dataset | Maintainer unverified | HF profile |
| [ArnobBot](https://huggingface.co/datasets/ArnobBot/Medicine-Dataset-of-Bangladesh) | Medicine dataset | Maintainer unverified | HF profile |
| [Hasin2026](https://huggingface.co/datasets/Hasin2026/bangladesh-scob-judgment-summarization) | Supreme Court judgment dataset | Maintainer unverified | HF profile |
| [hisab-calculator](https://www.npmjs.com/package/hisab-calculator) | Bengali-numerals calculator PWA | Maintainer unverified | npm publisher |

## Needs-review (safety / policy)

| Item | Concern |
|---|---|
| [bKash-Sync](https://github.com/zenjahid/bKash-Sync) | Reads bKash transaction SMS on-device; plausibly a legitimate personal tool, but automatic financial-SMS harvesting is privacy-sensitive. Requires a maintainer statement of legitimate use before listing. |
| [prantiksoft/laravel-mfs-sms-gateway](https://packagist.org/packages/prantiksoft/laravel-mfs-sms-gateway) | Auto-approves orders by parsing received bKash/Nagad/Rocket SMS — may violate MFS provider terms; needs a ToS review. |
| [nagad_cLone](https://github.com/evanemran/nagad_cLone) | Flutter UI clone of the Nagad app; financial-app lookalikes are phishing-adjacent. Excluded unless the maintainer clarifies it is a design study with no payment function. |

## Canonical-source questions

| Item | Question |
|---|---|
| [OmicronLab](https://github.com/OmicronLab) | Historic Avro Keyboard home; all current repos are mirrors of the pre-GitHub project. Which mirror (if any) should be canonical for the Avro family, versus torifat/iAvro and OpenBangla? |

## Negative findings (do not re-research)

- **GDG Dhaka / DevCon Bangladesh** — no meaningful GitHub organisation exists
  (only stale one-off event repos). Confirmed absent, October 2026.
- **bd-laws.pages.dev** — DNS-dead; the companion API endpoint returns an
  anti-bot challenge to plain GETs. Re-check both before ever listing.
- **gnewsapi.net BD path** — DNS-dead.
- **doptor-portal.tappware.com holiday API** — SSL mismatch.
- **bdnews24 legacy RSS URL** — returns HTML, not a feed.
- **bulksmsbd.com API endpoint** — connection failure from our sandbox at
  audit time; the service itself may still be up for customers.
