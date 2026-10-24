# 💒 Fintech & e-commerce

<img src="../../assets/blog/blog-payments.png" width="896" alt="💒 Fintech & e-commerce banner">

> Part of **[Awesome Bangladesh](../../README.md)** · All section guides: **[index](index.md)**

Payment gateways, SDKs and commerce integrations for Bangladesh's financial system — bKash, Nagad, SSLCommerz, PortWallet and friends. Official vendor SDKs and community wrappers are separated where it matters, and licence gaps are flagged with ⚠️. Several popular gateway wrappers have gone quiet; those moved to legacy.md so what remains here is genuinely buildable today.

**28 verified entries** · Last verified: 2026-10-25 · Rules: [curation policy](../curation-policy.md)

## The full table

| Project | What it does | Licence (as stated) | Bangladesh link |
|---|---|---|---|
| [shurjopay-plugins](https://github.com/shurjopay-plugins) | 12 official shurjoPay SDKs: Flutter, Java, Spring, JS, PHP, Python, Node.js, .NET, Rust and usage examples | MIT | 🔵 BD org / for-BD |
| [sslcommerz](https://github.com/sslcommerz) | Official SSLCommerz integrations (Laravel, PHP, Flutter, WooCommerce, ASP.NET) plus the [sslcommerz-lts](https://www.npmjs.com/package/sslcommerz-lts) npm package | ⚠️ Repo licences not specified | 🔵 BD org / for-BD |
| [UddoktaPay](https://github.com/UddoktaPay) | Official payment-automation SDKs including the Laravel SDK. | — | see list |
| [laravel-bkash-tokenize](https://packagist.org/packages/karim007/laravel-bkash-tokenize) | bKash Tokenized Checkout for Laravel. | — | 🟡 Diaspora |
| [sslcommerz-laravel](https://github.com/iRaziul/sslcommerz-laravel) | Clean SSLCommerz integration for Laravel | MIT | 🟢 BD-based |
| [nagadApi](https://github.com/arif98741/nagadApi) | Nagad payment API for PHP | ⚠️ No licence file | 🟢 BD-based |
| [nagad-api](https://packagist.org/packages/xenon/nagad-api) | Nagad API client for Laravel. | — | see list |
| [bkash-rs](https://github.com/dibakarsutradhar/bkash-rs) | bKash payment client for Rust | Custom licence | 🟢 BD-based |
| [SSLCommerz-Python](https://github.com/dreygur/SSLCommerz-Python) | SSLCommerz client for Python | MIT | 🟢 BD-based |
| [bkashgo](https://github.com/dreygur/bkashgo) | bKash API client for Go | MIT | 🟢 BD-based |
| [flutter-bkash](https://github.com/codeboxrcodehub/flutter-bkash) | bKash checkout for Flutter | BSD-3-Clause | 🔵 BD org / for-BD |
| [takaden](https://github.com/saagoor/takaden) | bKash, Nagad, Rocket and Upay payments for Laravel | MIT | see list |
| [laravel-bdpaygate](https://github.com/byteminus/laravel-bdpaygate) | Every Bangladeshi payment gateway behind one Laravel API, with [bdpaygate-js](https://github.com/byteminus/bdpaygate-js) for Node | MIT | see list |
| [bkash (Laravel, msilabs)](https://github.com/msilabs/bkash) | bKash API for Laravel | MIT | 🔵 BD org / for-BD |
| [paykit-bd](https://www.npmjs.com/package/paykit-bd) | Payment clients for Bangladeshi gateways | MIT | 🟢 BD-based |
| [bkash-js](https://www.npmjs.com/package/bkash-js) | bKash web client | MIT | 🟢 BD-based |
| [react-bangla-pay-icons](https://www.npmjs.com/package/react-bangla-pay-icons) | Bangladeshi payment brand icons as React components | MIT | 🟢 BD-based |
| [bd-bank-routing](https://www.npmjs.com/package/bd-bank-routing) | BEFTN bank routing numbers as structured data | MIT | 🟢 BD-based |
| [tutor-sslcommerz](https://github.com/hasinhayder/tutor-sslcommerz) | SSLCommerz payment gateway for Tutor LMS | ⚠️ No licence file | see list |
| [eps-gateway-nodejs](https://www.npmjs.com/package/eps-gateway-nodejs) | Node.js SDK for Dutch-Bangla Bank's EPS payment system | MIT | 🔵 BD org / for-BD |
| [@dreygur/steadfast-api](https://www.npmjs.com/package/@dreygur/steadfast-api) | SDK for the Steadfast Courier API (parcel create, track, cancel) | MIT | 🟢 BD-based |
| [steadfast-courier](https://pypi.org/project/steadfast-courier/) | Python client for the Steadfast Courier API | MIT | 🔵 BD org / for-BD |
| [bangladeshi-parcel-tracker](https://github.com/mdminhazulhaque/bangladeshi-parcel-tracker) | Track parcels across BD couriers (also on [PyPI](https://pypi.org/project/bangladeshi-parcel-tracker/)) | MIT | 🟢 BD-based |
| [RouteXpress](https://github.com/bytebrain3/RouteXpress) | Courier management with [routexpress-bd](https://www.npmjs.com/package/routexpress-bd) npm package for Steadfast, Pathao and RedX | MIT | 🟢 BD-based |
| [pathao-courier (Laravel)](https://github.com/codeboxrcodehub/pathao-courier) | Pathao courier integration for Laravel | MIT | see list |
| [pathao-courier (TypeScript)](https://github.com/shahria7k/pathao-courier) | Pathao courier SDK for TypeScript | MIT | 🟢 BD-based |
| [courier-woocommerce-plugin](https://github.com/pathao-eng/courier-woocommerce-plugin) | Official Pathao courier plugin for WooCommerce | GPL-3.0 | 🔵 BD org / for-BD |
| [Fraud-Checker-BD-Courier-Laravel](https://github.com/AbiruzzamanMolla/Fraud-Checker-BD-Courier-Laravel) | Courier fraud checking for Bangladeshi e-commerce | Custom licence | 🟢 BD-based |

## Editor's picks

### **sslcommerz (official)**

The official integration collection spanning Laravel, PHP, Flutter, WooCommerce and ASP.NET — the vendor-maintained path for the country's most-used gateway.

### **bkash-php / bKash community SDKs**

Community-maintained Tokenized Checkout implementations that show exactly how the bKash grant flow works in practice.

## How this section is verified

- Every link is fetched live at verification time — dead links are removed, not kept for history.
- Bangladesh connections are evidenced (profile location, org page, or the product's own docs) — see the [scope rules](../scope-and-eligibility.md).
- Dormant items (3+ years without activity) move to the [legacy file](../../legacy.md) with their last-activity date.
- Licence information is quoted as the publisher states it; gaps are flagged with ⚠️ rather than guessed.
