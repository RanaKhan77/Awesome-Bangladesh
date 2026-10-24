# Contributing to Awesome Bangladesh

Thank you for helping map Bangladesh's open ecosystem! This list lives or dies
by the quality of its entries, so contributions go through a simple but firm
verification process.

## Before you start

Read these two documents first — they answer 90% of rejections:

- [Scope and eligibility](docs/scope-and-eligibility.md) — what counts as "Bangladeshi" and what is out of scope.
- [Curation policy](docs/curation-policy.md) — how entries are verified, ordered and maintained.

## What we accept

- **New entries** that meet the scope rules and include all required fields (below).
- **Corrections** — dead links, changed licences, stale descriptions, wrong sections.
- **Verifications** — items in the [verification queue](docs/verification-queue.md) move into the list only when someone provides solid Bangladesh-connection evidence. Picking one and verifying it is a great first contribution.
- **Translations of descriptions** are not accepted yet — English descriptions keep the list lint-clean and internationally readable.

## What we do not accept

- Malicious, abusive or infringing tools (SMS bombers, phishing kits, piracy IPTV lists, fake payment pages) — even if they are open source and popular in Bangladesh.
- Indian-Bengali projects with no verifiable Bangladesh connection. Language alone is not nationality.
- Unverifiable claims. "The author is Bangladeshi" needs a link — a profile page, an organisation page, a README, an article. Search-snippet claims are not evidence.
- Copied entries from other Bangladesh lists. Link to those lists in *Awesome lists & communities* instead — we never cannibalise neighbours.
- Empty or single-item sections without prior discussion in an issue.

## Entry format

One line per entry, in the section's existing style:

```
- [Name](canonical-url) — One-sentence description of what it does and why it matters. Licence.
```

Rules:

- Use the **canonical URL** (the repo itself, or the package page for registry-only projects).
- End the description with a period.
- Always state the licence. If the repository has no licence file, write `⚠️ No licence file` — do not guess.
- Non-commercial datasets must carry `⚠️ non-commercial` so they never sit in an MIT-looking context unnoticed.
- Alphabetical or logical order within a section — follow what is already there.

## Required information in your PR

For a new entry, include in the PR description (not necessarily in the README line):

1. **Bangladesh connection evidence** — a URL we can check: maintainer profile with location, organisation page, or a README/product page showing the project is built for Bangladesh.
2. **Licence** — from the repository or registry page.
3. **Why it belongs in the proposed section.**

Pull requests without the evidence link are closed with a pointer to this file — nothing personal, it keeps the list trustworthy.

## Process

1. Fork, branch (`add-<project-name>` or `fix-<topic>`), edit `README.md` (and `data/*.json` when applicable).
2. Open a pull request with the evidence described above.
3. A maintainer re-checks the link, licence and section fit, then merges.

Small and precise beats large and sloppy. A PR that adds one well-verified
entry is more welcome than one that adds twenty unverified ones.

## Reporting problems

- **Dead link** — open an issue with the entry name; we fix or remove it.
- **Wrong licence note** — open an issue with the correct licence and a link to it.
- **Project changed ownership or went malicious** — tell us; entries are removed fast for safety reasons.

## Code of conduct

Be kind. Maintainers and contributors are volunteers; the community is small
and everyone remembers how they were treated.
