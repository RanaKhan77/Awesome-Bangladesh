# 🔌 APIs & integrations

<img src="../../assets/sections/banner-apis.svg" width="896" alt="🔌 APIs & integrations banner">

> Part of **[Awesome Bangladesh](../../README.md)** · All section guides: **[index](index.md)**

Public and free-tier APIs serving Bangladesh data — geography, prayer times, exchange rates, news feeds, railway information and more. Where an API needs a key we say so; keyless endpoints are marked as the easiest starting points. Live endpoints are checked during verification, not just their documentation pages. Official commercial APIs (payments, logistics) live in the [Fintech](fintech.md) and [Services](services.md) sections instead, and the open-source SDKs that wrap them live there too.

**15 verified entries** · Last verified: 2026-10-25 · Rules: [curation policy](../curation-policy.md)

## The full table

| Project | What it does | Licence (as stated) | Bangladesh link |
|---|---|---|---|
| [bdapis](https://github.com/AbmSourav/bdapis) | REST API for divisions, districts, upazilas, thanas, post offices and postcodes in both Bangla and English, live at [bdapis.com](https://bdapis.com/). The fastest way to stand up anything geographic without shipping a copy of the data. | MIT | 🟢 BD-based |
| [bdapi4all](https://github.com/fakhrul62/bdapi4all) | One keyless API covering BD geography, prayer times, holidays, exchange rates and input validators — a batteries-included endpoint set for prototyping local apps. | ⚠️ Licence unspecified | see list |
| [bd-apis](https://github.com/SudipMHX/bd-apis) | Community collection of Bangladesh-focused APIs — a starting index when you are hunting for what exists before committing to a provider. | ⚠️ No licence file | 🟢 BD-based |
| [bangla-apis](https://github.com/rdnasim/bangla-apis) | Curated directory of BD-context APIs (payments, couriers, SMS, government, banking, laws) with auth and pricing columns; reviewed October 2026. Linked as a reference directory — its data is not copied here. | Linked as a reference directory (no licence — data is not copied) | see list |
| [Bangladesh Bank daily rates](https://allratestoday.com/api/open/central-bank/bb) | Keyless JSON endpoint serving Bangladesh Bank's official published exchange rates, maintained by AllRatesToday with visible attribution — the closest thing to an official BB API that actually exists. | — | 🔵 BD org / for-BD |
| [World Bank Bangladesh API](https://api.worldbank.org/v2/country/BGD/indicator/SP.POP.TOTAL?format=json) | Keyless REST API for every World Bank Bangladesh indicator, from population to GDP — a clean, documented, always-on source for national statistics. | CC-BY-4.0 (World Bank open data terms) | 🔵 BD org / for-BD |
| [Bangladesh Railway e-ticketing API](https://railspaapi.shohoz.com/v1.0/web/all-trains/info) | The keyless JSON API behind the official Shohoz rail e-ticketing site — train schedules and routes as the production site itself reads them. Unofficial and without published terms; use respectfully. | — | 🔵 BD org / for-BD |
| [Open-Meteo (Bangladesh)](https://api.open-meteo.com/v1/forecast?latitude=23.8103&longitude=90.4125&hourly=temperature_2m) | Free keyless weather forecasts and historical data for any Bangladeshi coordinate — the practical alternative to the Meteorological Department's purchase-only data (see the [services section](services.md)). | CC-BY-4.0 (free tier, attribution required) | see list |
| [bangladesh-bank-exchange-rate](https://www.npmjs.com/package/bangladesh-bank-exchange-rate) | npm client for Bangladesh Bank's daily published rates — import it and read taka rates without hand-parsing the bank's site. | MIT | 🔵 BD org / for-BD |
| [ExchangeRate-API open endpoint](https://open.er-api.com/v6/latest/BDT) | Free, keyless exchange rates for BDT refreshed daily — the community endpoint of ExchangeRate-API, and the pragmatic choice until Bangladesh Bank publishes a real API. | — | see list |
| [Prothom Alo RSS](https://www.prothomalo.com/feed) | Verified RSS 2.0 feed of the leading Bangla daily — headline data for news apps and Bangla NLP pipelines without scraping. | — | see list |
| [The Daily Star RSS](https://www.thedailystar.net/frontpage/rss.xml) | Front-page feed of the leading English daily — the English-language counterpart for the same use cases. | — | see list |
| [barta](https://github.com/iRaziul/barta) | Bangladeshi SMS gateways for Laravel — one clean interface over providers that each have their own quirks. | MIT | 🟢 BD-based |
| [laravelbdsms](https://github.com/arif98741/laravelbdsms) | Multi-gateway SMS package for Laravel covering Bangladeshi providers — swap providers without rewriting your notification code. | MIT | 🟢 BD-based |
| [sms-service-with-bd-providers](https://github.com/sarahman/sms-service-with-bd-providers) | Laravel SMS service across BD providers — a third take on the same real problem, useful when the first two do not cover your gateway. | ⚠️ Licence unspecified | 🟢 BD-based |

## Editor's picks

### [bdapis](https://github.com/AbmSourav/bdapis)

Keyless REST API for divisions, districts, upazilas, post offices and postcodes in both Bangla and English. Division-to-postcode hierarchy in one place, no API key, no registration — the fastest way to stand up anything geographic in a Bangladeshi app.

### **open.er-api.com BDT rates**

Free daily exchange rates for the taka without registration. It earned its place by replacing a popular endpoint that claimed to serve BDT but never actually did — every entry in this section is tested for what it really returns, not what it promises.

## How this section is verified

- Every link is fetched live at verification time — dead links are removed, not kept for history.
- Bangladesh connections are evidenced (profile location, org page, or the product's own docs) — see the [scope rules](../scope-and-eligibility.md).
- Dormant items (3+ years without activity) move to the [legacy file](../../legacy.md) with their last-activity date.
- Licence information is quoted as the publisher states it; gaps are flagged with ⚠️ rather than guessed.
