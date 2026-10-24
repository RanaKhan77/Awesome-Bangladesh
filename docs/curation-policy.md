# Curation policy

How entries are chosen, ordered, and kept fresh.

## Selection criteria

Within scope (see [scope-and-eligibility](scope-and-eligibility.md)), an
entry is included when it is:

1. **Useful to someone** — a developer, researcher, student or open-data user
   can realistically benefit from it.
2. **Accessible** — working canonical link, no login wall for the code/data
   itself.
3. **Honest about licensing** — licence stated, or explicitly flagged as
   unspecified. Non-commercial licences are always badged.
4. **Not duplicated** — if two projects do the same thing, both may be listed,
   described factually (community SDKs of the same gateway coexist happily).

Popularity helps ordering but is not a requirement: a two-star MIT utility
that solves a real Bangladeshi problem beats a thousand-star archive that
stopped working in 2019.

## Ordering

- Within a section, closely-related entries are grouped (e.g. official SDK
  families before community SDKs; portals before individual datasets).
- Otherwise, loose ordering by usefulness — most useful first.
- Alphabetical order is not enforced; logical grouping wins.

## Freshness

- Link checks run continuously in CI; broken links become issues
  automatically.
- Licence and activity claims carry a capture date in `data/*.json` where
  machine-readable records exist.
- **Dormancy rule (3 years).** An item with no release, commit or publish
  activity for three or more years moves to [legacy.md](../legacy.md) with its
  last-activity date and the reason it moved. It is never silently deleted —
  legacy.md keeps the history and the honest labels.
- **Stale-rules / stale-data override.** Data or rules that are supposed to
  track a changing reality (tax slabs, medicine listings, laws, postcodes) move
  to legacy.md at any age once they no longer reflect that reality — a
  three-year-old tax calculator is already wrong.
- **Frozen-by-design carve-out.** Research corpora, benchmarks, trained models
  and paper-companion code do not need activity to stay listed: a frozen
  dataset is complete, not unmaintained. They stay in the main list as long as
  they remain genuinely usable (downloadable, loadable, cited).
- **Community carve-out.** Community organisations are listed for their
  community role, not for their GitHub push activity — their real activity
  happens offline (events, deployments, mentorship).
- Moving an item to legacy.md is a normal maintenance action, not a judgement
  against its author. Anyone may argue an item back into the main list by
  showing renewed releases.

## Section rules

- No empty sections. A category with fewer than three solid entries is folded
  into the nearest fitting section.
- Section emoji are part of the anchors — do not change them casually; TOC
  links depend on them.
- New sections require an issue discussion first.

## Data files

`data/*.json` mirrors a subset of the README for programmatic use:

- Only entries with complete metadata (URL, licence, BD-connection evidence,
  last-verified date) appear in data files.
- The README is the human-curated source of truth; data files are generated
  companions, never the reverse.
- Each record carries a `license` field exactly as published at the source,
  and a `bd_evidence` URL.

## Verification queue

Items that look promising but lack Bangladesh-connection evidence live in
[verification-queue.md](verification-queue.md). The queue records:

- What the item is,
- What evidence is missing,
- Where to look next.

Anyone may supply evidence in an issue or PR; maintainers re-check it before
the item graduates into the list.

## Behaviour standards

- We do not list malicious tools — not even with warnings. Names of excluded
  malicious repos are kept internally, never published or linked.
- We do not star, fork, or interact with excluded repositories as part of
  curation work.
- Corrections are applied fast, with thanks, regardless of who files them.
