# 💒 Fintech & e-commerce

<img src="../../assets/sections/banner-fintech.svg" width="896" alt="💒 Fintech & e-commerce banner">

> Part of **[Awesome Bangladesh](../../README.md)** · All section guides: **[index](index.md)**

Payment gateways, SDKs and commerce integrations for Bangladesh's financial system — bKash, Nagad, SSLCommerz, PortWallet and friends. Official vendor SDKs and community wrappers are separated in the table so you know whose code you are trusting, and licence gaps are flagged with ⚠️ because a payment integration with unclear licensing is a compliance problem, not just a technical one. Several popular gateway wrappers have gone quiet; those moved to legacy.md so what remains here is genuinely buildable today. The commercial services themselves (bKash, Nagad, SSLCommerz portals) live in the [services section](services.md).

**46 verified entries** · Last verified: 2026-11-06 · Rules: [curation policy](../curation-policy.md)

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
| [Bangladesh Tax Calculator](https://github.com/nadimtuhin/tax-calculator) | Browser app that computes Bangladeshi income tax for salaried people, comparing FY 2025-26 vs 2026-27 rules — does the math for salaried people in Bangladesh and shows FY 2025-26 next to FY 2026-27; live at tax.nadimtuhin.com. | MIT | 🟢 BD-based |
| [Bhromon](https://github.com/rbr48/Bhromon) | Offline-first Flutter app for families, offices, messes and samities: chat, shared expenses, ledgers, SOS — one app for every group ... messes, housing societies, savings groups; engines incl. Ledger Paisa Engine and Samity Ledger; live on Google Play. | Apache-2.0 | 🟢 BD-based |
| [Cashout Counter](https://github.com/Shishir-ip/Bkash-Cashout-Counter) | Free offline Android calculator for bKash and Nagad cash-out charges in Bangladesh; Kotlin/Compose — lightweight Android calculator for mobile financial services (MFS) in Bangladesh ... bKash, Nagad; free, offline, APK releases. | MIT | 🔵 BD org / for-BD |
| [Cloud Accounting & ERP](https://github.com/imranbru99/cloud-accounting-erp) | Laravel 12 multi-tenant accounting ERP with exact-precision double-entry ledger, maker-checker approvals, invoicing and inventory; BN/EN UI. | MIT | 🟢 BD-based |
| [AI Sales Assistant (Laravel)](https://github.com/imranbru99/laravel-ai-sales-assistant) | Laravel platform that scores leads, drafts follow-ups and runs sales ops, with bKash/Nagad/SSLCommerz gateways and Bangla/English output — README: 'Inbound leads are scored in 35ms... Local Bangladesh gateways: bKash, Nagad, Rocket, SSLCommerz' — 728KB PHP, 50 passing tests, 7 first-party Packagist packages. | MIT | 🟢 BD-based |
| [DeshiPay](https://github.com/hello2himel/deshiPay) | Gives a shop or creator one payment link: a Bangla QR with the amount baked in, plus bKash, Nagad and bank details to copy. Not a processor. | AGPL-3.0 | 🟢 BD-based |
| [Echo & Aura Ticketing](https://github.com/Ashfak-Hossain/EchoAndAura) | Ticketing platform for a Dhaka live-events organiser: public shop, admin console and door scanner around manual bKash verification. | AGPL-3.0 | 🟢 BD-based |
| [DokanOS](https://github.com/razikuljoni/DokanOS) | Multi-tenant POS, inventory and baki credit-ledger SaaS for Bangladeshi corner shops, with offline queuing and Taka ageing buckets. Demo. | MIT | 🟢 BD-based |
| [ERPNext Bangladesh VAT Compliance](https://github.com/invento-software-limited/ERPNext-Bangladesh-VAT-Compliance) | Frappe app adding Bangladesh VAT compliance to ERPNext: Mushak 6.1/6.2/6.3 reports, VAT challans, VDS handling and compliant invoicing — README: 'A Frappe app for managing VAT compliance in Bangladesh... Mushak 6.3: VAT Challan' — 264KB Python, bench-installable, pre-commit ruff/eslint, user guide. | MIT | 🟢 BD-based |
| [Taka Plan](https://github.com/sm-supports/taka-plan) | Free no-signup personal-finance planner PWA in Bangla, English and 10 more languages; goal-based monthly savings plans — "A free personal-finance planner for everyone... Made in Bangla and English, now in 12 languages. No sign-up. No ads." Deployed at taka-plan.pages.dev.. | MIT | 🟢 BD-based |
| [DailyTally](https://github.com/CodeWithRoni/DailyTally) | Mobile-friendly bilingual (Bangla/English) expense and lending ledger with budgets, reminders, CSV/PDF reports and cloud backups — "DailyTally is a mobile-friendly accounting app... Bengali and English interfaces" and "Bangla ledger with mandatory Bangladesh mobile-number/password accounts." Live app on Render.. | ⚠️ No licence file | 🟢 BD-based |
| [GearUp](https://github.com/abdullahmamun1/gearUp-frontend) | Sports and outdoor gear rental marketplace for Bangladesh: live availability, Stripe payments with deposits, owner chat and AI trip planner — "Tents, kayaks, bikes and cameras from local providers across Bangladesh: live availability for your dates, Stripe payments with deposits" — live site + separate backend repo.. | ⚠️ No licence file | 🟢 BD-based |
| [Nikhut Hisab](https://github.com/almamun252/Nikhut-Hisab-App) | Android personal-finance app in English and Bangla: income/expenses, debts, budgets, shopping lists, PDF reports and Drive backup — "Android personal finance app for everyday income, expenses, receivables, payables, budgets, and shopping lists. It supports English and Bangla" — Kotlin/Room with WorkManager.. | ⚠️ No licence file | 🔵 BD org / for-BD |
| [Giftbook (উপহারের খাতা)](https://github.com/montasim/giftbook) | Bangla wedding-gift ledger PWA that records গায়ে হলুদ/বিয়ে gifts in the family's own Google Sheet; works offline with Bangla digits — "বিয়ে, গায়ে হলুদ, বউভাত... কে কী দিল, কাকে কী দিলাম... পুরো UI বাংলায়, সংখ্যা বাংলা অঙ্কে" — live at giftbook.netlify.app.. | ⚠️ No licence file | 🟢 BD-based |
| [Hajj Tracking Software](https://github.com/Ehasan07/hajj-tracking-software) | Production Hajj-agency management system: bilingual money receipts with QR verification, zamzam delivery tracking and monthly statements — "A5 money receipt in Bangla and English, with a QR code anyone can verify... Zamzam water deliveries by shop" — Next.js 16/tRPC/PostgreSQL-RLS, Docker, live site.. | ⚠️ No licence file | 🟢 BD-based |
| [Hishab (My Daily Hishab)](https://github.com/shahriarjahin/my-daily-hishab) | Personal money app with wallets, budgets and bookkeeping in English, Bangla and Banglish; ships signed Android APK releases — "Wallets, budgets and smarter bookkeeping — in English, বাংলা and Banglish" with GitHub release APK downloads; React + Capacitor + FastAPI.. | ⚠️ No licence file | 🟢 BD-based |
| [Taka Tracker](https://github.com/Ehasan07/takatracker) | Offline-first personal accounting PWA for Bangladesh: income, expenses, loans, DPS savings, insurance and AI analytics in Bengali. | ⚠️ No licence file | 🟢 BD-based |
| [BakiBondhu (বাকিবন্ধু)](https://github.com/mrofiqul/bakibondhu) | Bangla-first offline credit-ledger app for Bangladeshi micro-merchants: customer baki, payments, sales and SMS/WhatsApp reminders. | MIT | 🟢 BD-based |



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
