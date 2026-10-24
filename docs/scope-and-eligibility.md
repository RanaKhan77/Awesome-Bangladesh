# Scope and eligibility

This document defines what belongs in Awesome Bangladesh. It exists so that
every accept/reject decision can be traced to a rule instead of a mood.

## The two qualifying paths

An entry qualifies in exactly one of two ways:

### Path A — A Bangladeshi person or organisation made it

| Tier | Definition | Typical evidence |
|---|---|---|
| **A — BD-based** | Maintainer's profile shows they are based in Bangladesh | GitHub `location`, org page, company page |
| **B — Diaspora** | Maintainer is of Bangladeshi origin, living abroad | Profile bio with 🇧🇩, Bangladeshi employer/education history, public self-identification |
| **C — BD organisation** | A Bangladeshi company, university group, or community maintains it | Org page with BD location or affiliation (BUET NLP, Bengali.AI, Pathao, BDOSN…) |

### Path B — The product is explicitly for Bangladesh

The maintainer's nationality is unknown, but the project itself is
unambiguously built for Bangladesh (a bKash gateway, a Dhaka flood alert
system, a BD postcode API). Evidence = the product's own README or docs.

Path B entries are described by what they do, without claiming anything about
who made them.

## Hard exclusions

- **Indian-Bengali projects with no BD connection.** Bengali is a shared
  language; nationality is not inferred from names or script. A Kolkata
  project with no BD link is out of scope even if excellent.
- **Malicious or abusive tools** — SMS bombers, phishing pages, malware
  collections, piracy IPTV lists, fake payment pages. Rejected regardless of
  popularity.
- **Privacy-sensitive borderline tools** (e.g. automatic harvesting of
  financial SMS) go to the needs-review queue, not the list, until their
  legitimate-use case is clear.
- **Projects with no working canonical link.** Dead is dead.

## What "verified" means here

Every entry carries, at the time it was added:

1. **Canonical URL** that resolves.
2. **Bangladesh-connection evidence URL** (Path A) or the product's own
   Bangladesh-specific description (Path B).
3. **Licence** as stated by the repository/registry — or an explicit
   `⚠️ No licence file` note. We never guess licences.
4. **Activity snapshot** (stars/last push or registry downloads) captured at
   verification time — used for ordering and later freshness checks.

Anything that cannot satisfy all four goes to the
[verification queue](verification-queue.md), where it waits for evidence.
The queue is public: picking an item and supplying evidence is a valid and
valued contribution.

## Non-free services

Commercial services (payment gateways, SMS providers, paid government APIs)
are listed separately under **Developer services (not open)** with their
access model and a practical "what you can do" note. They are never mixed
into the open-source sections, and listing them is not an endorsement.

## Relationship to neighbouring lists

We link to specialist Bangladesh lists; we do not copy their entries.
Each list curates with different rules — duplicating their work would create
divergent copies and waste their maintainers' effort.
