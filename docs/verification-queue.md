# Verification queue

Items that look promising but do not yet meet the evidence bar for the main
list. Anyone may supply evidence (a profile link, an org page, a README
quote) via issue or PR — see [CONTRIBUTING](../CONTRIBUTING.md). Items with
negative findings are marked so we do not re-research them endlessly.

Last reviewed: 2026-10-25.

## Missing Bangladesh-connection evidence

| Item | What it is | What's missing | Where to look next |
|---|---|---|---|
| [olovajs/olova](https://github.com/olovajs/olova) | JS reactive framework, 183★, MIT | Any BD evidence at all — org page and README are silent | [org page](https://github.com/olovajs) (members list is hidden), npm publisher, commit authors |
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
- **yasserius/bangladesh_geojson_shapefile** — removed October 2026: the repo
  contains only a README and a screenshot; the claimed GeoJSON/shapefile
  exports do not exist in the repo (data sits on external drives). Promotional
  shell — do not re-list.
- **Frankfurter (frankfurter.app)** — removed October 2026: it does not serve
  BDT (ECB's reference-rate list has no BDT), so its "BDT rates" value was a
  false claim. Replaced by the keyless open endpoint
  [open.er-api.com/v6/latest/BDT](https://open.er-api.com/v6/latest/BDT)
  (verified live, daily updates).
- **ogdnew.portal.gov.bd** — domain retired (NXDOMAIN, October 2026); the OGD
  portal now lives at ogdnew.sdg.gov.bd (verified live), which is what the
  list points to.
- **BanglishRev (HF org)** — graduated from this queue October 2026: the
  companion paper (arXiv 2412.13161) lists UIU Dhaka faculty (Swakkhar
  Shatabda, Salekul Islam) as authors; BD connection now verified — eligible
  for the datasets section on the next content pass.

## From the October 2026 community-suggestion review

Forty-two suggested repositories were reviewed (plus twenty discovered during research).
Ten met the full bar and were added to the list; four BDIX IPTV collections were rejected
on scope (they distribute pirated streams); the rest are queued below, strongest first.

| Item | What it is | What's missing | Where to look next |
|---|---|---|---|
| [afnan-samin/lipilab](https://github.com/afnan-samin/lipilab) | Online Bangla dictionary lab, hosted at lipilab.pro.bd | LICENSE file is all-rights-reserved | Instant entry if the maintainer relicences; watch for a licence change |
| [OpenBangla/mul](https://github.com/OpenBangla/mul) | Bengali stemmer Rust crate (1.8k crate downloads) from the OpenBangla community | Low adoption vs our activity bar | Recheck adoption once downloads pass ~5k |
| [shhossain/BanglaTTS](https://github.com/shhossain/BanglaTTS) | Offline Bangla text-to-speech by the BanglaSpeech2Text maintainer | No licence file | Licence addition; maintainer is already verified |
| [banglatoolbox/banglatoolbox.github.io](https://github.com/banglatoolbox/banglatoolbox.github.io) | Bijoy to Unicode converter web app, Apache-2.0, BD maintainer, active | Low adoption; single-tool site | Recheck stars/usage after some growth |
| [fahimscirex/bangla-fonts](https://github.com/fahimscirex/bangla-fonts) | Curated 200+ Bangla fonts collection (28 stars, Dhaka maintainer) | Licence of the fonts themselves vs the collection | Font licences; whether redistribution is clean |
| [hmjoy17/lipik-dict](https://github.com/hmjoy17/lipik-dict) | 83,010-word dictionary for the privacy-focused Lipik Bangla keyboard | Source of the word list unclear | Provenance of the dictionary data |
| [asiff00/bangla-pdf-ocr](https://github.com/asiff00/bangla-pdf-ocr) | Extract Bangla text from PDFs (MIT, 22 stars) | Last push Oct 2024 - going stale | Any sign of renewed activity |
| [ardevcraft/bangla_pdf_fixer](https://github.com/ardevcraft/bangla_pdf_fixer) | Flutter package fixing broken Bangla fonts in PDFs (Apache-2.0, 7 stars) | New project, adoption unproven | pub.dev download stats |
| [open-admin-data/bangladesh-administrative-divisions](https://github.com/open-admin-data/bangladesh-administrative-divisions) | CC BY 4.0 full admin hierarchy dataset (8 divisions / 64 districts) | Maintainer identity unknown | Org page, data lineage |
| [sunrisesineast/bangladesh-grid](https://github.com/sunrisesineast/bangladesh-grid) | Dashboard on PGCB public grid data | Unofficial; unclear maintenance path | Maintainer profile, PGCB data terms |
| [COS-IT-FLOWS/RT_Flood_Monitoring_System](https://github.com/COS-IT-FLOWS/RT_Flood_Monitoring_System) | Real-time flood monitoring (EQUINOCT / UNILOD, MIT) | Deployment for Bangladesh unclear | Project reports, BD pilot evidence |
| [khalilurrrahmanridoykhan/bangladesh-dengue-2018-2025](https://github.com/khalilurrrahmanridoykhan/bangladesh-dengue-2018-2025) | Reproducible national dengue analysis (MIT, active) | New, zero adoption | Dataset provenance (DGHS citations) |
| [Druvo/Bangladesh](https://github.com/Druvo/Bangladesh) | PyPI package of Bangladesh districts and data (Dhaka maintainer, MIT) | New, low adoption | PyPI download stats |
| [Iamsdt/awesome-bengali-ai](https://github.com/Iamsdt/awesome-bengali-ai) | Companion awesome list for Bengali AI (MIT, Khulna maintainer) | List quality/maintenance depth | Sustained updates |
| [kishormorol/BanglaNLP-Hub](https://github.com/kishormorol/BanglaNLP-Hub) | Community catalog of Bangla NLP resources (MIT, 11 stars) | Overlap with existing NLP sections | Differentiation from bnlp/bnltk listings |
| [AbiruzzamanMolla/bangla-ocr-by-abir](https://github.com/AbiruzzamanMolla/bangla-ocr-by-abir) | Bangla OCR toolkit by an already-listed maintainer (MIT) | Early stage | Adoption and accuracy results |
| [muhib-karim/Rambler-Bangla](https://github.com/muhib-karim/Rambler-Bangla) | Gboard smali patcher for Bengali-first voice typing (GPL-3.0) | Bangladesh connection of the maintainer | Maintainer profile |
| [Al-Mahamud/kagoj](https://github.com/Al-Mahamud/kagoj) | Flutter e-paper reader (KUET maintainer, MIT, active) | Zero adoption so far | Any release or store listing |

Rejected with reasons (do not re-research): four BDIX IPTV M3U collections
(Rokon-IPTV, BDXI_KB, bdiptv, Mrgify-BDIX-IPTV) distribute pirated television
streams - excluded on scope regardless of popularity.
