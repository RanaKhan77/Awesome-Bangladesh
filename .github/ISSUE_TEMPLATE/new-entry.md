name: "Suggest a new entry"
description: "Propose a project, dataset, API or community for the list"
title: "[New entry]: <name>"
labels: ["entry"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for helping map Bangladesh's open ecosystem!
        Before you fill this in, please read [scope and eligibility](https://github.com/RanaKhan77/Awesome-Bangladesh/blob/main/docs/scope-and-eligibility.md) — it answers most rejections.
  - type: input
    id: name
    attributes:
      label: Name
      description: The project's name exactly as it appears on its canonical page.
    validations:
      required: true
  - type: input
    id: url
    attributes:
      label: Canonical URL
      description: The repository or registry page itself — not a blog post about it.
    validations:
      required: true
  - type: dropdown
    id: section
    attributes:
      label: Which section does it belong in?
      options:
        - Developer tools & libraries
        - Datasets & open data
        - APIs & integrations
        - Bangla language & NLP
        - AI/ML & research
        - Fintech & e-commerce
        - Cybersecurity & privacy
        - Civic tech & public services
        - Crisis response
        - Geography & open maps
        - Education & learning
        - Awesome lists & communities
        - Developer services (not open)
    validations:
      required: true
  - type: textarea
    id: evidence
    attributes:
      label: Bangladesh-connection evidence (required)
      description: A URL we can check — maintainer profile with location, organisation page, or a README/product page showing it is built for Bangladesh. "The author is Bangladeshi" without a link is not evidence.
      placeholder: https://github.com/<maintainer> (profile shows location) — or an org page, README quote, product page...
    validations:
      required: true
  - type: input
    id: license
    attributes:
      label: Licence
      description: As stated on the repository or registry page. Write "no licence file" if there is none — that is allowed, it just gets flagged.
    validations:
      required: true
  - type: textarea
    id: description
    attributes:
      label: One-sentence description
      description: What it does and why it matters. Keep it factual — we will edit for style.
    validations:
      required: true
