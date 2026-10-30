# 🇧🇩 Bangla language & NLP

<img src="../../assets/sections/banner-bangla-nlp.svg" width="896" alt="🇧🇩 Bangla language & NLP banner">

> Part of **[Awesome Bangladesh](../../README.md)** · All section guides: **[index](index.md)**

Everything that makes Bangla work on computers: keyboards and input methods, Unicode-Bijoy conversion, normalizers, tokenizers, spell checkers, PDF generation and full NLP stacks. This is the deepest section of Bangladeshi open source — the Avro phonetic lineage alone spans two decades of maintained forks, from the original OmicronLab keyboard through today's Rust engines. Licences matter here and are stated per entry; the BUET research models with non-commercial terms live in the [AI/ML section](aiml.md) with their ⚠️ flags.

**48 verified entries** · Last verified: 2026-10-30 · Rules: [curation policy](../curation-policy.md)

## The full table

| Project | What it does | Licence (as stated) | Bangladesh link |
|---|---|---|---|
| [OpenBangla-Keyboard](https://github.com/OpenBangla/OpenBangla-Keyboard) | The leading open-source Bangla keyboard for Linux — the flagship consumer input method, cross-platform in spirit and the direct descendant of the original Avro that defined phonetic typing in Bangladesh. | GPL-3.0 | 🔵 BD org / for-BD |
| [riti](https://github.com/OpenBangla/riti) | Next-generation Bangla input method engine in Rust — the phonetic-conversion core that modern keyboards embed, built as a library first. | MPL-2.0 | 🔵 BD org / for-BD |
| [jsAvroPhonetic](https://github.com/torifat/jsAvroPhonetic) | Avro Phonetic conversion in JavaScript — the web-side implementation that powers phonetic typing in browsers. | ⚠️ No licence file | 🟡 Diaspora |
| [iAvro](https://github.com/torifat/iAvro) | Avro Phonetic for macOS — the port that kept Apple users typing phonetically when the original stopped. | ⚠️ No licence file | 🟡 Diaspora |
| [Lekho](https://github.com/ARahim3/Lekho) | Avro Phonetic input for Apple Silicon Macs — the modern continuation for the ARM Mac era (লেখা = to write). | Custom licence | see list |
| [Bangla-Keyboard](https://github.com/wpexpertinbd/Bangla-Keyboard) | Fixed-layout Bangla keyboard for macOS, Windows and Linux from one shared reordering engine — one codebase, three platforms. | MIT | 🟢 BD-based |
| [BornoTSF](https://github.com/JayedAhsan/BornoTSF) | Lightweight Windows Text Services Framework IME for Bangla typing by Codepotro — system-level input without heavyweight keyboard suites. | GPL-3.0 | 🟢 BD-based |
| [khipro-m17n](https://github.com/rank-coder/khipro-m17n) | Compositional Bangla input method — neither phonetic nor an app — for Linux, Windows and Android, built on the m17n framework. | MIT | 🟢 BD-based |
| [Bongo](https://github.com/mehedishakeel/Bongo) | Cross-platform Avro-style phonetic keyboard for macOS, Windows, Linux and Android, built on the riti engine — one project covering every desktop. | MPL-2.0 | 🟢 BD-based |
| [@subhesadek/avro-phonetic](https://www.npmjs.com/package/@subhesadek/avro-phonetic) | Avro Phonetic parser for the web on npm — drop-in phonetic conversion for web apps. | MPL-2.0 | see list |
| [avro.py](https://github.com/hitblast/avro.py) | Avro Phonetic parser in Python — the pip-installable way to convert phonetic strings server-side. | Apache-2.0 | 🟢 BD-based |
| [Bijoy2Unicode](https://github.com/JehadurRE/Bijoy2Unicode) | Bijoy to Unicode converter — bridging the legacy ASCII encoding that still powers Bangla DTP shops into modern Unicode. | MIT | see list |
| [okkhor](https://crates.io/crates/okkhor) | Unicode to Bijoy and back, in Rust (অক্ষর = letter) — the conversion layer for Rust services handling legacy-encoded Bangla text. | MIT | 🟢 BD-based |
| [poriborton](https://crates.io/crates/poriborton) | Unicode-Bijoy converter library (পরিবর্তন = change) — same problem, independent Rust implementation. | MIT | 🔵 BD org / for-BD |
| [upodesh](https://crates.io/crates/upodesh) | Autosuggest engine for Bangla input (উপদেশ = suggestion) — the predictive layer that makes phonetic keyboards feel fluent. | MIT | 🔵 BD org / for-BD |
| [emojicon](https://crates.io/crates/emojicon) | Emoji handling with Bangla text — emoji-aware processing for Bangla strings, where naive code breaks grapheme clusters. | MIT | 🔵 BD org / for-BD |
| [ponjika](https://crates.io/crates/ponjika) | Bengali (Bangladeshi) calendar library (পঞ্জিকা = almanac) — Bangla dates, months and holidays for scheduling code. | GPL-3.0 | 🟡 Diaspora |
| [bangla](https://crates.io/crates/bangla) | Number formatting and calendar utilities for Bangla — Bengali numerals and date rendering as a library. | MIT | 🟡 Diaspora |
| [obadh_engine](https://github.com/unmukto-org/obadh_engine) | Deterministic rule-based Roman-to-Bangla transliteration engine in Rust, powering the Obadh keyboards for Apple platforms (উবাধ = speech). | MIT | 🟡 Diaspora |
| [bnlp](https://github.com/sagorbrur/bnlp) | Bangla natural language processing toolkit — tokenisation, stemming, POS tagging and NER in one Python package. | MIT | 🟢 BD-based |
| [bnltk](https://github.com/asraf-patoary/bnltk) | Bangla NLP toolkit in Python — the NLTK-inspired take on the same stack. | MIT | 🟡 Diaspora |
| [BanglaSpeech2Text](https://github.com/shhossain/BanglaSpeech2Text) | Offline Bangla speech recognition — pip-installable, runs without cloud APIs, which matters for privacy and for poor connectivity alike. | Apache-2.0 | 🟢 BD-based |
| [bangla-tts](https://github.com/zabir-nabil/bangla-tts) | Bangla text-to-speech research code — an older research entry kept for lineage (see also the VITS and Katha systems in [legacy](../../legacy.md)). | ⚠️ No licence file | 🟡 Diaspora |
| [Nirmol](https://github.com/Sigmakib2/Nirmol) | Bangla slang detection dataset and API (নির্মল = clean) — content moderation tooling for Bangla platforms. | ⚠️ No licence file | see list |
| [BengaliDictionary](https://github.com/MinhasKamal/BengaliDictionary) | English-to-Bengali dictionary dataset and tools — a foundational lexicon from the DownGit author. | GPL-3.0 | 🟡 Diaspora |
| [avro-bangla-autocorrect-dictionary-enriched](https://github.com/afnan-hossain/avro-bangla-autocorrect-dictionary-enriched) | Enriched Avro autocorrect dictionary — better suggestions for the phonetic typing experience. | ⚠️ No licence file | see list |
| [laya-bangla](https://github.com/shamspias/laya-bangla) | Bangla-first LLM routing layer — routing prompts to models based on Bangla-language understanding (লয়া = flow). | Apache-2.0 | see list |
| [bangla-embed-e5-small-banglish](https://huggingface.co/kazalbrur/bangla-embed-e5-small-banglish) | Bangla/Banglish sentence embeddings — retrieval and semantic search that handles both scripts and the Romanized mix people actually type. | MIT | see list |
| [bangla-asr-conformer-120m-dialects](https://huggingface.co/kazalbrur/bangla-asr-conformer-120m-dialects) | Dialect-aware Bangla speech recognition — a Conformer model trained to survive regional accents. | Apache-2.0 | see list |
| [indicf5-bangla-tts](https://huggingface.co/ehzawad/indicf5-bangla-tts) | IndicF5-based Bangla text-to-speech from a Bangladesh-based researcher — Bangla TTS is scarce and this is a working checkpoint | ⚠️ Gated download, non-commercial research licence | 🟢 BD-based |
| [whisper-large-v3-turbo-bn-BD](https://huggingface.co/ehzawad/whisper-large-v3-turbo-bn-BD) | Whisper large-v3-turbo fine-tune for Bangla (Bangladesh) | ⚠️ Gated download, non-commercial research licence | 🟢 BD-based |
| [Qwen3-ASR-1.7B-bn-BD](https://huggingface.co/ehzawad/Qwen3-ASR-1.7B-bn-BD) | Compact Qwen3 ASR fine-tune for Bangla — a lighter-weight recognition option | ⚠️ Gated download, non-commercial research licence | 🟢 BD-based |
| [BanglaLLM (Hugging Face org)](https://huggingface.co/BanglaLLM) | Bangladesh-led org behind the BanglaLLama family, BanglaSafe, bangla-alpaca-orca and 30+ open Bangla models and datasets — the org page is the canonical entry point | Licence per model | 🟢 BD-based |
| [number-to-bangla](https://github.com/rakibdevs/number-to-bangla) | Convert numbers to Bangla words and digits for Laravel/PHP — invoices, cheques and amounts-in-words without hand-rolled rules. | MIT | 🟢 BD-based |
| [bangla-to-banglish](https://www.npmjs.com/package/bangla-to-banglish) | Bangla script to Banglish transliteration on npm — for platforms that still store Romanized Bangla. | MIT | 🟢 BD-based |
| [bangla-likhi](https://www.npmjs.com/package/bangla-likhi) | Bangla typing made easy (বাংলা লিখি = let's write Bangla) — a friendlier programmatic typing interface. | MIT | 🟢 BD-based |
| [bangla-pdf](https://www.npmjs.com/package/bangla-pdf) | Generate PDFs with Bangla text in Node — complex-script shaping handled for you. | BSD-3-Clause | 🟢 BD-based |
| [banglapdf](https://pypi.org/project/banglapdf/) | Bangla PDF generation for Python — the PyPI counterpart for server-side document pipelines. | MIT | 🟢 BD-based |
| [bangla-web-fonts](https://github.com/maateen/bangla-web-fonts) | Bangla web fonts packaged for the web — embeddable font stacks that render Bangla correctly on any browser. | ⚠️ No licence file | see list |
| [thikkit](https://www.npmjs.com/package/thikkit) | Bilingual Bangla-English address parsing (ঠিকানা = address) — turning the freeform addresses Bangladesh actually uses into structured data. | MIT | 🟢 BD-based |
| [bangla-to-english-name-translator](https://www.npmjs.com/package/bangla-to-english-name-translator) | Converts Bangla person names to English (শাহানাহিদ → Shahanaheed) — the unglamorous utility every BD database migration needs. | MIT | 🟢 BD-based |
| [transliteration-bangla](https://www.npmjs.com/package/transliteration-bangla) | Banglish-to-Bangla transliteration running ONNX models in the browser — machine-learned conversion client-side, no API calls. | MIT | 🔵 BD org / for-BD |
| [@pantho075/matra](https://www.npmjs.com/package/@pantho075/matra) | Bangla character stroke-order data and heuristics (মাত্রা = matra line) — the data layer for handwriting education apps. | MIT | 🟢 BD-based |
| [bangla-ipa](https://pypi.org/project/bangla-ipa/) | Bangla text to IPA transliteration, by Bangladeshi NLP researchers (open source, GitHub bipsec/bangla-ipa) — phonetic research and speech tooling. | — | 🟢 BD-based |
| [bn-i18n-notes](https://codeberg.org/adnan360/bn-i18n-notes) | Guidelines for translating software projects from English to Bangla, written in Bangla (Codeberg) — hard-won i18n conventions for the language. | GPL-3.0 | 🟢 BD-based |
| [LaTeXbangla](https://github.com/Neehan/LaTeXbangla) | Write Bangla (and Assamese) with ordinary LaTeX — typesetting without XeLaTeX gymnastics. | LPPL-1.3c | 🟡 Diaspora |
| [BOOKbangla](https://github.com/Neehan/BOOKbangla) | Book class and templates for writing Bangla and Assamese books with LaTeX memoir — the publishing-ready companion to LaTeXbangla. | LPPL-1.3c | 🟡 Diaspora |
| [sbnltk](https://github.com/Foysal87/sbnltk) | SUST-Bangla NLP toolkit: NER, POS tagging, stemming, word embeddings (MIT) | MIT | 🔵 BD org/for-BD |

## Editor's picks

### [OpenBangla Keyboard](https://github.com/OpenBangla/OpenBangla-Keyboard)

The flagship consumer Bangla input method — cross-platform, actively maintained, and the direct descendant of the original Avro that defined phonetic typing in Bangladesh. Two decades of lineage sit behind its suggestion engine, and its riti core is a library other keyboards now build on.

### [thikkit](https://www.npmjs.com/package/thikkit)

Bilingual Bangla-English address parsing is the kind of problem every Bangladeshi engineering team hits and few solve properly — freeform mixed-script addresses with no standard format. A focused npm package that does one hard local job well.

### [sbnltk](https://github.com/Foysal87/sbnltk)

A Bangla NLP toolkit self-described as the SUST-Bangla effort: named-entity recognition, POS tagging, stemming and Bangla word embeddings in one MIT-licensed Python package. Together with bnlp and bnltk, it gives Bangla NLP a third home-grown toolkit option.

## How this section is verified

- Every link is fetched live at verification time — dead links are removed, not kept for history.
- Bangladesh connections are evidenced (profile location, org page, or the product's own docs) — see the [scope rules](../scope-and-eligibility.md).
- Dormant items (3+ years without activity) move to the [legacy file](../../legacy.md) with their last-activity date.
- Licence information is quoted as the publisher states it; gaps are flagged with ⚠️ rather than guessed.
