# Legacy

Items that still exist and mostly still work, but have not been maintained for
years. They were moved out of the main list so that the list stays a directory
of things you can build on today; they stay here so the history is not lost
and nobody re-researches them from scratch.

Reasons are labelled per item:

- **unmaintained-software** — the code still runs, but nothing has shipped for years.
- **stale-data** — the data was accurate once but the world it describes has moved on.
- **stale-rules** — the encoded rules/laws changed and the project never caught up.

## Unmaintained software

- [go-avro-phonetic](https://github.com/sadlil/go-avro-phonetic) — Avro Phonetic parser in Go. MIT. Last push 2020-09 (6.2y); 38 stars. Still works; Avro parsing is a stable algorithm.
- [rupantor](https://crates.io/crates/rupantor) — Avro Phonetic parser crate (13.5k downloads; 6.1y since the last crate update). MPL-2.0. Same 2020-frozen codebase as [OpenBangla/rupantor-rs](https://github.com/OpenBangla/rupantor-rs) on GitHub; the parser survives inside the actively-developed OpenBangla Keyboard.
- [easy-bangla-date](https://packagist.org/packages/ronisaha/easy-bangla-date) — Bangla date conversion for PHP. 8.9k downloads. Last release 2017-08 (9.2y).
- [bangla-calendar](https://www.npmjs.com/package/bangla-calendar) — Bangla calendar for JavaScript. MIT. Last publish ~2023 (3.4y); calendar math is stable.
- [to_bn](https://rubygems.org/gems/to_bn) — English-to-Bangla numeral conversion for Ruby. Last version 2013 (12.5y); 20.5k downloads.
- [BanglaToEnglish](https://rubygems.org/gems/BanglaToEnglish) — Bangla-to-English text conversion for Ruby. Last version 2019 (6.2y); 6.1k downloads.
- [bd_location](https://rubygems.org/gems/bd_location) — Bangladesh address and location data for Ruby. MIT. Version 0.0.1 on RubyGems, released January 2016 (10.7y); never updated since. The gem still installs, but the data inside is frozen.
- [bd-newspaper-crawlers](https://github.com/KSMubasshir/bd-newspaper-crawlers) — Crawlers for Bangladeshi newspaper archives. MIT. Last push 2023 (3.7y); crawlers drift as newspaper sites change layouts.
- [bengalianalyzer](https://github.com/BengaliAI/bengalianalyzer) — Bengali text analysis library. BSD-3-Clause. Last push 2022 (4.0y).
- [sslcommerz-sdk](https://pypi.org/project/sslcommerz-sdk/) — SSLCommerz client for Python. MIT. Last release 2021-06 (5.4y).
- [satellite_image_tinhouse_detector](https://github.com/yasserius/satellite_image_tinhouse_detector) — Detecting tin-roof houses from Bangladesh satellite imagery. No licence file; last push 2021 (5.9y). The notebooks are real; the project is frozen.
- [@portwallet/nodejs-sdk](https://www.npmjs.com/package/@portwallet/nodejs-sdk) — Official PortWallet payment SDK. MIT. Last publish ~2021 (5.8y).
- [bkash (PHP)](https://github.com/Shipu/bkash) — bKash payment client for PHP. MIT. 187 stars; last push 2023 (3.5y).
- [bkash-payment-gateway](https://github.com/shahriar-shojib/bkash-payment-gateway) — bKash Tokenized Checkout for Node.js. MIT. Last push 2023 (3.2y).
- [nagad-payment-gateway](https://github.com/shahriar-shojib/nagad-payment-gateway) — Nagad payment integration for Node.js. MIT. Last push 2023 (3.9y).
- [laravel-sslcommerz](https://packagist.org/packages/dgvai/laravel-sslcommerz) — SSLCommerz for Laravel. 53.9k downloads. Last release 2022-03 (4.7y).
- [BanglaTranslator](https://github.com/menon92/BanglaTranslator) — Bangla machine translation experiments. Apache-2.0. Last push 2021 (4.6y); a transformers-era experiment repo.

- [WikiTextCorpusDownloader](https://github.com/Rajan-sust/WikiTextCorpusDownloader) — Language-independent Wikipedia text-corpus downloader by a Sylhet-based researcher. No licence file; last push 2019-11 (6.9y). The tool still runs; Wikipedia's API changes may need small patches.
- [bangla-ocr](https://github.com/kmhasan-class/bangla-ocr) — Bangla OCR research code from a Dhaka CS faculty account. MIT. Last push 2016 (10y); kept as research history.
- [Katha Bangla TTS](https://sourceforge.net/projects/blp/files/Katha_Bangla_TTS/) — First-generation Bangla text-to-speech from the BLPI group (incl. Mumit Khan, BRAC University). Beta releases 2009–2010 on SourceForge; a founding artefact of BD speech research.
- [pakhi-bhasha](https://github.com/Shafin098/pakhi-bhasha) — Dynamically typed Bangla programming language written in Rust, by a Dhaka developer. MIT. Last push 2021-07 (5.3y); language and playground still work.
## Stale data

- [medicinedb](https://github.com/WSAyan/medicinedb) — Bangladeshi medicine information dataset. MIT. Last push 2021 (5.1y). The project's own README notes the data is years old — the drug market moves faster than the dataset.
- [Postcodes-of-Bangladesh](https://github.com/aiFdn/Postcodes-of-Bangladesh) — Postal code dataset. MIT. Last push 2017 (9.6y). Postal codes change rarely, so most of the data is still valid, but it is frozen.

## Stale rules

- [bd-income-tax-calculator](https://github.com/ssi-anik/bd-income-tax-calculator) — Bangladeshi income tax calculator. MPL-2.0. 87 stars. Last commit 2020-11; the live site computes FY2020-21 slabs (the 300k/350k/450k/475k thresholds). Tax rules change every June — verify current slabs before relying on any number it gives you.
