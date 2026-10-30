# 💒 Fintech & e-commerce

<img src="../../assets/sections/banner-fintech.svg" width="896" alt="💒 Fintech & e-commerce banner">

> Part of **[Awesome Bangladesh](../../README.md)** · All section guides: **[index](index.md)**

Payment gateways, SDKs and commerce integrations for Bangladesh's financial system — bKash, Nagad, SSLCommerz, PortWallet and friends. Official vendor SDKs and community wrappers are separated in the table so you know whose code you are trusting, and licence gaps are flagged with ⚠️ because a payment integration with unclear licensing is a compliance problem, not just a technical one. Several popular gateway wrappers have gone quiet; those moved to legacy.md so what remains here is genuinely buildable today. The commercial services themselves (bKash, Nagad, SSLCommerz portals) live in the [services section](services.md).

**28 verified entries** · Last verified: 2026-10-25 · Rules: [curation policy](../curation-policy.md)

## The full table

| Project | What it does | Licence (as stated) | Bangladesh link |
|---|---|---|---|
| [shurjopay-plugins](https://github.com/shurjopay-plugins) | 12 official shurjoPay SDKs — Flutter, Java, Spring, JS, PHP, Python, Node.js, .NET, Rust and usage examples. The most complete official SDK family any Bangladeshi gateway has shipped. | MIT | 🔵 BD org / for-BD |
| [sslcommerz](https://github.com/sslcommerz) | Official SSLCommerz integrations (Laravel, PHP, Flutter, WooCommerce, ASP.NET) plus the [sslcommerz-lts](https://www.npmjs.com/package/sslcommerz-lts) npm package — the vendor-maintained path for the country's most-used gateway. | ⚠️ Repo licences not specified | 🔵 BD org / for-BD |
| [UddoktaPay](https://github.com/UddoktaPay) | Official payment-automation SDKs including the Laravel SDK — the automation-focused Bangladeshi gateway's developer stack. | — | see list |
| [laravel-bkash-tokenize](https://packagist.org/packages/karim007/laravel-bkash-tokenize) | bKash Tokenized Checkout for Laravel — the community-standard Laravel wrapper for the modern bKash API generation. | — | 🟡 Diaspora |
| [sslcommerz-laravel](https://github.com/iRaziul/sslcommerz-laravel) | Clean SSLCommerz integration for Laravel — a minimal, readable wrapper that got the integration right without vendor bloat. | MIT | 🟢 BD-based |
| [nagadApi](https://github.com/arif98741/nagadApi) | Nagad payment API for PHP — community-maintained code against a service that publishes no public developer portal. | ⚠️ No licence file | 🟢 BD-based |
| [nagad-api](https://packagist.org/packages/xenon/nagad-api) | Nagad API client for Laravel on Packagist — the other maintained Nagad wrapper, usable composer-side. | — | see list |
| [bkash-rs](https://github.com/dibakarsutradhar/bkash-rs) | bKash payment client for Rust — for the growing minority of BD backend work written in Rust. | Custom licence | 🟢 BD-based |
| [SSLCommerz-Python](https://github.com/dreygur/SSLCommerz-Python) | SSLCommerz client for Python — Django/Flask shops get a clean SDK instead of hand-rolled requests. | MIT | 🟢 BD-based |
| [bkashgo](https://github.com/dreygur/bkashgo) | bKash API client for Go — same story for Go services, from the same maintainer. | MIT | 🟢 BD-based |
| [flutter-bkash](https://github.com/codeboxrcodehub/flutter-bkash) | bKash checkout for Flutter — mobile apps get native payment flows instead of a webview compromise. | BSD-3-Clause | 🔵 BD org / for-BD |
| [takaden](https://github.com/saagoor/takaden) | bKash, Nagad, Rocket and Upay payments for Laravel — one package across the four MFS giants. | MIT | see list |
| [laravel-bdpaygate](https://packagist.org/packages/byteminus/laravel-bdpaygate) | Every Bangladeshi payment gateway behind one Laravel API — gateway-agnostic by design, so swapping providers is a config change. Survives on Packagist; the GitHub repo and bdpaygate-js Node companion have since been deleted. | MIT | see list |
| [bkash (Laravel, msilabs)](https://github.com/msilabs/bkash) | bKash API for Laravel from msilabs — the wrapper that documented the grant flow for a generation of BD Laravel developers. | MIT | 🔵 BD org / for-BD |
| [paykit-bd](https://www.npmjs.com/package/paykit-bd) | Payment clients for Bangladeshi gateways on npm — multi-gateway support for Node services. | MIT | 🟢 BD-based |
| [bkash-js](https://www.npmjs.com/package/bkash-js) | bKash web client for browser-side checkout flows. | MIT | 🟢 BD-based |
| [react-bangla-pay-icons](https://www.npmjs.com/package/react-bangla-pay-icons) | Bangladeshi payment brand icons as React components — bKash, Nagad, Rocket and friends as drop-in components instead of scraped logos. | MIT | 🟢 BD-based |
| [bd-bank-routing](https://www.npmjs.com/package/bd-bank-routing) | BEFTN bank routing numbers as structured data — the lookup table every Bangladeshi banking app needs, published once. | MIT | 🟢 BD-based |
| [tutor-sslcommerz](https://github.com/hasinhayder/tutor-sslcommerz) | SSLCommerz payment gateway for Tutor LMS — by one of Bangladesh's best-known PHP educators. | ⚠️ No licence file | see list |
| [eps-gateway-nodejs](https://www.npmjs.com/package/eps-gateway-nodejs) | Node.js SDK for Dutch-Bangla Bank's EPS payment system — card payments from the bank that issues most Bangladeshi debit cards. | MIT | 🔵 BD org / for-BD |
| [@dreygur/steadfast-api](https://www.npmjs.com/package/@dreygur/steadfast-api) | SDK for the Steadfast Courier API — parcel create, track, cancel from Node. | MIT | 🟢 BD-based |
| [steadfast-courier](https://pypi.org/project/steadfast-courier/) | Python client for the Steadfast Courier API — the PyPI counterpart for Python backends. | MIT | 🔵 BD org / for-BD |
| [bangladeshi-parcel-tracker](https://github.com/mdminhazulhaque/bangladeshi-parcel-tracker) | Track parcels across BD couriers (also on [PyPI](https://pypi.org/project/bangladeshi-parcel-tracker/)) — one interface over the courier tracking mess. | MIT | 🟢 BD-based |
| [RouteXpress](https://github.com/bytebrain3/RouteXpress) | Courier management with the [routexpress-bd](https://www.npmjs.com/package/routexpress-bd) npm package covering Steadfast, Pathao and RedX — a full courier-ops stack, not just a client. | MIT | 🟢 BD-based |
| [pathao-courier (Laravel)](https://github.com/codeboxrcodehub/pathao-courier) | Pathao courier integration for Laravel, from the same team as the Flutter bKash package. | MIT | see list |
| [pathao-courier (TypeScript)](https://github.com/shahria7k/pathao-courier) | Pathao courier SDK for TypeScript — typed client for the country's biggest courier API. | MIT | 🟢 BD-based |
| [courier-woocommerce-plugin](https://github.com/pathao-eng/courier-woocommerce-plugin) | Official Pathao courier plugin for WooCommerce — the production integration used by real Bangladeshi e-commerce shops. | GPL-3.0 | 🔵 BD org / for-BD |
| [Fraud-Checker-BD-Courier-Laravel](https://github.com/AbiruzzamanMolla/Fraud-Checker-BD-Courier-Laravel) | Courier fraud checking for Bangladeshi e-commerce — cod-order fraud is a local industry problem, and this is a local tool for it. | Custom licence | 🟢 BD-based |

## Editor's picks

### [sslcommerz (official)](https://github.com/sslcommerz)

The official integration collection spanning Laravel, PHP, Flutter, WooCommerce and ASP.NET — when money is involved, vendor-maintained code with a real org behind it beats a community wrapper of unknown provenance. The licence gap is flagged honestly; weigh it before shipping.

### **The bKash community SDK family**

laravel-bkash-tokenize (Laravel), bkashgo (Go), bkash-rs (Rust), bkash-js (web) and flutter-bkash (Flutter) together cover the bKash Tokenized Checkout across the whole modern stack — community-maintained implementations that document exactly how the grant and payment flows work in practice.

## How this section is verified

- Every link is fetched live at verification time — dead links are removed, not kept for history.
- Bangladesh connections are evidenced (profile location, org page, or the product's own docs) — see the [scope rules](../scope-and-eligibility.md).
- Dormant items (3+ years without activity) move to the [legacy file](../../legacy.md) with their last-activity date.
- Licence information is quoted as the publisher states it; gaps are flagged with ⚠️ rather than guessed.
