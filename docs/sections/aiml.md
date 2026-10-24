# 🤖 AI/ML & research

<img src="../../assets/sections/banner-aiml.svg" width="896" alt="🤖 AI/ML & research banner">

> Part of **[Awesome Bangladesh](../../README.md)** · All section guides: **[index](index.md)**

Models, benchmarks and research code from Bangladeshi labs and companies — from BUET's encoder models to Dhaka-built LLM families, plus two MCP servers that bring Bangladesh data into LLM workflows. Each entry notes its licence honestly: community-licence LLMs and non-commercial research checkpoints are labelled, so commercial users know what they can ship before they build on it. Government AI assets are here too, through the banglagov Hugging Face org — the state's first openly published model family.

**26 verified entries** · Last verified: 2026-10-25 · Rules: [curation policy](../curation-policy.md)

## The full table

| Project | What it does | Licence (as stated) | Bangladesh link |
|---|---|---|---|
| [banglagov (Hugging Face)](https://huggingface.co/banglagov) | Official Hugging Face org of the Bangla.gov.bd government initiative: banGPT2-Base, banBERT-Base, banELECTRA-Base and banT5-Base pretrained models plus the Ban-Sign-Sent-9K sign-language dataset. The first time a Bangladeshi state body has published model weights openly. | Licence terms per model card | 🔵 BD org / for-BD |
| [BanglaBERT](https://github.com/csebuetnlp/banglabert) | Pretrained Bangla language models from the BUET NLP group — ELECTRA-based encoders that became the default starting checkpoint for Bangla downstream tasks (classification, NER, retrieval) in research and production alike. | ⚠️ CC BY-NC-SA 4.0 — non-commercial | 🔵 BD org / for-BD |
| [BanglaNLG](https://github.com/csebuetnlp/BanglaNLG) | BanglaT5 generation and summarisation models from BUET — the natural continuation from their encoder work into text generation for Bangla. | ⚠️ No licence file | 🔵 BD org / for-BD |
| [mT5_multilingual_XLSum](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum) | Multilingual summarisation checkpoint covering Bangla — one of the most widely used ready-made summarizers for Bangla news text on Hugging Face. | ⚠️ CC BY-NC-SA 4.0 — non-commercial | see list |
| [normalizer](https://github.com/csebuetnlp/normalizer) | Bangla text normalisation utilities used across the csebuetnlp stack — punctuation, Unicode and encoding cleanup that every Bangla pipeline needs before the first model call. | ⚠️ No licence file | 🔵 BD org / for-BD |
| [xl-sum](https://github.com/csebuetnlp/xl-sum) | Research code for the XL-Sum summarisation dataset — the 45-language BBC-sourced benchmark that became a standard evaluation for low-resource summarisation, including Bangla. | ⚠️ No licence file | 🔵 BD org / for-BD |
| [CrossSum](https://github.com/csebuetnlp/CrossSum) | Cross-lingual summarisation across 45 languages — generate a summary in one language from a document in another, built on the same BBC corpus lineage as XL-Sum. | ⚠️ No licence file | 🔵 BD org / for-BD |
| [IllusionVQA](https://github.com/csebuetnlp/IllusionVQA) | Optical-illusion visual question answering benchmark — a genuinely adversarial test of whether vision-language models actually perceive or just pattern-match, from the BUET group. | ⚠️ No licence file | 🔵 BD org / for-BD |
| [bangla-bert-base](https://huggingface.co/sagorsarker/bangla-bert-base) | Community Bangla BERT — one of the most-used Bangla encoders on Hugging Face, and a permissively licensed alternative to the research-licensed BUET models. | MIT | see list |
| [bangla-bert](https://github.com/sagorbrur/bangla-bert) | Training and fine-tuning code for Bangla BERT models — the how-it-was-done repository behind the community encoder above. | MIT | see list |
| [bbocr](https://github.com/BengaliAI/bbocr) | Bangla handwriting OCR research from the Bengali.AI Kaggle competition lineage — the code behind the grapheme recognition effort that pulled hundreds of Bangladeshi students into ML. | BSD-3-Clause | 🔵 BD org / for-BD |
| [graphemePrepare](https://github.com/BengaliAI/graphemePrepare) | Grapheme recognition data preparation — tooling for the famous handwritten-grapheme dataset that remains the reference point for Bangla OCR work. | MIT | 🔵 BD org / for-BD |
| [BanglaConformer](https://huggingface.co/bengaliAI/BanglaConformer) | Conformer-based Bangla speech recognition model — a modern ASR architecture trained for Bangla and published with permissive terms. | MIT | see list |
| [BangalASR](https://github.com/menon92/BangalASR) | Automatic Bangla speech recognition experiments from a SUST researcher — the DeepSpeech-era lineage of Bangladeshi open-source ASR. | MIT | 🟢 BD-based |
| [Bangla-Word2Vec](https://github.com/menon92/Bangla-Word2Vec) | Pretrained Bangla word embeddings — the classic static-embedding layer for Bangla NLP before transformers took over, still useful for lightweight systems. | MIT | 🟢 BD-based |
| [banglanlptoolkit](https://pypi.org/project/banglanlptoolkit/) | All-in-one Bangla NLP toolkit from the ACI MIS AI and Intelsense AI teams — stemming, POS tagging, NER and more behind one PyPI install. | ⚠️ Licence unspecified | 🟡 Diaspora |
| [BanglaBBQ](https://github.com/SummitAnthony/BanglaBBQ-benchmark) | Bias benchmark for question answering in the Bangladeshi context — measuring whether models reproduce social biases when asked about Bangladesh. | MIT | see list |
| [bangla-speech-to-text-benchmark](https://github.com/riverbornai/bangla-speech-to-text-benchmark) | Open benchmark of eight Bengali speech-to-text APIs (Sarvam, Deepgram, Gemini, OpenAI, Groq Whisper and others) evaluated on 1,001 Bangla audio clips — the honest scorecard before you pick an ASR vendor. | MIT | 🟢 BD-based |
| [TituLM](https://huggingface.co/hishab/titulm-llama-3.2-3b-v2.0) | Open-weight Bangla LLM family from Hishab (Dhaka), trained on their own 24.3M-document titulm-bangla-corpus; paper arXiv 2502.11187. The most complete locally-published LLM stack: corpus, base models and paper together. | Llama 3.2 community licence | 🟢 BD-based |
| [BanglaLLama](https://huggingface.co/BanglaLLM/bangla-llama-7b-instruct-v0.1) | Instruction-tuned Bangla LLM from the Bangladesh-led BanglaLLM org — an earlier open-weight 7B entry in the local LLM lineage. | Llama 2 community licence | 🟢 BD-based |
| [bangladeshi-bangla-tts-vits](https://huggingface.co/EMTIAZZ/bangladeshi-bangla-tts-vits) | Bangladeshi-dialect Bangla text-to-speech built on VITS, with running demo spaces, by a Dhaka-based ML engineer — TTS tuned to how Bangla is actually spoken in Bangladesh rather than Kolkata-standard prose. | Apache-2.0 | 🟢 BD-based |
| [BanglaTag](https://huggingface.co/arafatfahim/BanglaTag) | Bangla part-of-speech tagging model by a Dhaka developer — a drop-in POS tagger for pipelines that need morphological context. | Apache-2.0 | 🟢 BD-based |
| [bengali-whisper-medium](https://huggingface.co/SayedShaun/bengali-whisper-medium) | Whisper fine-tune for Bangla speech recognition from a Dhaka-based maintainer — the practical route to good Bangla transcription on consumer hardware. | Apache-2.0 | 🟢 BD-based |
| [BengaliRegionalASR (Barishal & Sylhet)](https://huggingface.co/sha1779/BengaliRegionalASR_barishal_sylhet) | Dialect-aware ASR trained on BengaliAI's regional-dialect data for two Bangladeshi divisions — addressing the reality that Barishai and Sylheti Bangla break standard ASR models. | Apache-2.0 | 🔵 BD org / for-BD |
| [@entrogic-net/mcp-server-bangladesh](https://www.npmjs.com/package/@entrogic-net/mcp-server-bangladesh) | MCP server exposing Bangladesh reference data (geography, utilities and more) to LLM clients, from the BanglaClaw team — so AI assistants can answer BD questions with real data instead of guessing. | Apache-2.0 | 🟢 BD-based |
| [bangla-news-mcp](https://pypi.org/project/bangla-news-mcp/) | MCP server that retrieves live Bangla news into LLM contexts, by Abid Mohammad Jawad (open source, GitHub hurutta/bangla-news-mcp) — current-events grounding for Bangla-speaking AI workflows. | — | 🟢 BD-based |

## Editor's picks

### [banglagov (Hugging Face)](https://huggingface.co/banglagov)

banGPT2, banBERT, banELECTRA and banT5 from the Bangla.gov.bd government initiative — the state publishing base model weights openly is new for Bangladesh, and the org also carries the Ban-Sign-Sent-9K sign-language dataset. Worth watching: this is the institutional AI capacity of the country being built in public.

### [TituLM (Hishab)](https://huggingface.co/hishab/titulm-llama-3.2-3b-v2.0)

Open-weight Bangla LLM family from a Dhaka AI company with a public 24M-document training corpus and an accompanying paper — the most complete local LLM stack currently published. When the corpus, the weights and the write-up all exist openly, others can verify rather than trust.

## How this section is verified

- Every link is fetched live at verification time — dead links are removed, not kept for history.
- Bangladesh connections are evidenced (profile location, org page, or the product's own docs) — see the [scope rules](../scope-and-eligibility.md).
- Dormant items (3+ years without activity) move to the [legacy file](../../legacy.md) with their last-activity date.
- Licence information is quoted as the publisher states it; gaps are flagged with ⚠️ rather than guessed.
