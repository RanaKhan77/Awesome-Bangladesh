# 🇧🇩 Bangla language & NLP

<img src="../../assets/sections/banner-bangla-nlp.svg" width="896" alt="🇧🇩 Bangla language & NLP banner">

> Part of **[Awesome Bangladesh](../../README.md)** · All section guides: **[index](index.md)**

Everything that makes Bangla work on computers: keyboards and input methods, Unicode-Bijoy conversion, normalizers, tokenizers, spell checkers, PDF generation and full NLP stacks. This is the deepest section of Bangladeshi open source — the Avro phonetic lineage alone spans two decades of maintained forks, from the original OmicronLab keyboard through today's Rust engines. Licences matter here and are stated per entry; the BUET research models with non-commercial terms live in the [AI/ML section](aiml.md) with their ⚠️ flags.

**73 verified entries** · Last verified: 2026-11-06 · Rules: [curation policy](../curation-policy.md)

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
| [Voxcribe](https://github.com/Ratul345/Voxcribe) | Local speech-to-text desktop app and CLI built on faster-whisper, tailored for Bengali transcription — specially tailored for Bengali transcription while offering complete multilingual speech recognition, automatic language detection, real-time streaming. | MIT | 🔵 BD org / for-BD |
| [Bangla Voice Clock](https://github.com/saifulmd0/bangla-voice-clock) | Desktop talking clock that speaks the time aloud in Bangla as said in Bangladesh; Flutter, offline — A free talking clock that tells the time aloud in Bangla, the way it is said in Bangladesh.. | GPL-3.0 | 🟢 BD-based |
| [Kothon](https://github.com/tanvir-talha058/Kothon) | Offline Windows voice typer (Vosk) for Bangla, English and Banglish that types into any focused app — kothon converts your speech to text locally with Vosk, applies Banglish-to-Bangla normalization, and types the result into whatever application is focused. | MIT | 🟢 BD-based |
| [LipiLab (লিপিল্যাব)](https://github.com/afnan-samin/lipilab) | Free Bangla Unicode-to-Bijoy converter with DOCX round-trip that preserves formatting; fully client-side — upload a .docx and download it back with the same layout - bold stays bold, tables stay tables; your text never leaves your device. | proprietary (all rights reserved) | 🔵 BD org / for-BD |
| [Bengali Coreference under Low-Resource Constraints](https://github.com/zenith19/bengali-coref-low-resource) | Research code and data for Bengali coreference: 41 gold docs beat 141 mixed docs; 66.73 CoNLL F1 best result — 41 gold-standard documents outperform 141 mixed gold + silver ones, for every model tested ... 66.73 CoNLL F1 (MuRIL-Large). | MIT | 🔵 BD org / for-BD |
| [Rickshaw Rong (রিকশা রং)](https://github.com/Teamz-Lab-LTD/rickshaw-rong-bangla-font) | Free OpenType-SVG color Bangla font painted in Dhaka rickshaw-art style; ships the .otf builds, specimen site and a Python build pipeline — README: 'A free Bangla color font, painted in Dhaka rickshaw-art style' — dist/RickshawRong-Regular.otf downloadable, shaping from Baloo Da 2, online generator at tool.teamzlab.com. | OFL-1.1 | 🟢 BD-based |
| [Odri for Windows](https://github.com/odri-bn/odri-windows) | Native Windows TSF input method turning phonetic Latin typing into Bangla script in real time; ships an installer and prebuilt x64 releases. | GPL-3.0 | 🔵 BD org / for-BD |
| [Orus-OCR-0.1](https://github.com/MahirHamiAbrar/Orus-OCR-V0) | Small CPU-fast OCR for Bangla, English and mixed handwriting-first pages; returns language, handwriting flag and structured text — README: '1.06M-parameter CTC line recognizer... Bangla handwriting 6.9% CER' vs 'Indra OCR 1.1: 84.6% (BN-HTRd)' — frozen release with weights, train.sh recipe, 8.4MB pipeline, run.py CLI. | MIT-NC (custom; det.onnx upstream OpenRAIL-M) | 🔵 BD org / for-BD |
| [Bornotoron (বর্ণতরণ)](https://github.com/TajkirHossen-14/Bornotoron) | Framework-free Banglish-to-Bangla writing tool: dictionary-first spelling from 4,000+ entries, homophone choices and learned corrections — README: 'Ami banglay likhchi → আমি বাংলায় লিখছি... 4000+ spelling entries. Zero frameworks. Your words stay yours.' — Avro-inspired engine, tests, offline PWA. | MIT | 🔵 BD org / for-BD |
| [Shobdo Keyboard](https://github.com/34rns/shobdo-keyboard) | Offline Android keyboard for Bangla (Probhat), Banglish phonetic and English, 13 themes, no INTERNET permission, no ads and no trackers. | MIT | 🟢 BD-based |
| [Project Lip Sync](https://github.com/BlahBlah23406/project-lip-sync) | Web tool that dubs English YouTube lectures into Bangla: Claude translation, Edge TTS voices, FFmpeg muxing and a dual-audio web player. | MIT | 🔵 BD org / for-BD |
| [Borno-LM](https://github.com/MdRimon29/borno-lm) | From-scratch decoder-only Bangla language model (152M params) in PyTorch: SentencePiece tokenizer, corpus training, checkpoints, generation — "builds a SentencePiece tokenizer, streams a small Bangla text corpus, pretrains the model, saves checkpoints, and generates text" — 152,510,976 parameters verified in-notebook.. | MIT | 🔵 BD org / for-BD |
| [Bangla Calendar (বাংলা ক্যালেন্ডার)](https://github.com/abusayed0206/bangla-calendar) | Windows desktop widget showing the Bangla date, full Bangla calendar, seasons and system-tray support; published on Microsoft Store — "A beautiful Bangla date widget for Windows... Display current Bangla date, full Bangla calendar view, current Bangla season" with Microsoft Store listing 9pcmxnfhvb6f.. | Apache-2.0 | 🟢 BD-based |
| [Uchcharonai (Uccharon AI)](https://github.com/HumbleHamim/Uccharon-AI-by-Kirrahdia-team) | Bangla pronunciation coach web app: record your voice, get a transcription, and see mismatched words highlighted against a target sentence. | ⚠️ No licence file | 🟢 BD-based |
| [Bangla Voice Typing](https://github.com/graphicarray/Bangla-Voice-Typing-Chrome-Extension) | Chrome extension (Manifest V3) that types punctuated Bangla text into any text box from speech, with spoken punctuation commands — "Speak Bangla. Get clean, punctuated Bangla text typed straight into any text box... Adds punctuation (including the Bangla দাঁড়ি ।), removes fillers (আ, উম, হুম)" — v2.1.0, hold Alt+C.. | MIT | 🔵 BD org / for-BD |
| [bangla-calendar](https://www.npmjs.com/package/bangla-calendar) | Convert JavaScript dates to the Bangla (Bengali) calendar. | ⚠️ Licence unspecified | 🔵 BD org / for-BD |
| [bangla-date-converter](https://www.npmjs.com/package/bangla-date-converter) | Comprehensive Bangla date converter with extensive formatting options. | ⚠️ Licence unspecified | 🔵 BD org / for-BD |
| [bn-translit](https://www.npmjs.com/package/bn-translit) | Bidirectional Bangla-Banglish transliteration with slugify support. | ⚠️ Licence unspecified | 🔵 BD org / for-BD |
| [avro-bangla-engine](https://www.npmjs.com/package/avro-bangla-engine) | The Avro Phonetic engine packaged for modern JS use. | ⚠️ Licence unspecified | 🔵 BD org / for-BD |
| [avro-bangla-suggestions](https://www.npmjs.com/package/avro-bangla-suggestions) | React hook for Avro Phonetic Bangla suggestions and autocomplete. | ⚠️ Licence unspecified | 🔵 BD org / for-BD |
| [bn-ansi-to-unicode](https://www.npmjs.com/package/bn-ansi-to-unicode) | ANSI (Bijoy) Bangla font text to Unicode converter in TypeScript. | ⚠️ Licence unspecified | 🔵 BD org / for-BD |
| [bd_number](https://www.npmjs.com/package/bd_number) | Bangla/English number conversion utilities. | ⚠️ Licence unspecified | 🔵 BD org / for-BD |
| [bangla-support](https://www.npmjs.com/package/bangla-support) | Bangla digits and Bangla calendar date utilities. | ⚠️ Licence unspecified | 🔵 BD org / for-BD |
| [bangla-stdlib](https://www.npmjs.com/package/bangla-stdlib) | A standard library of Bangla language functions. | ⚠️ Licence unspecified | 🔵 BD org / for-BD |
| [jquery.bangla](https://www.npmjs.com/package/jquery.bangla) | Versatile Bangla input tool for the web (jQuery). | ⚠️ Licence unspecified | 🔵 BD org / for-BD |



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
