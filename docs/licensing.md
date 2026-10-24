# Licensing notes

## The list itself

The list content (README, docs, data files) is released under
[CC0-1.0](../LICENSE) — public domain dedication. Anyone may reuse, remix and
redistribute it without asking permission.

CC0 (rather than MIT) is deliberate: MIT is a code licence, and applying it
to a curated list implies a "source code" model that does not fit. CC0 matches
the practice of the wider awesome-list community.

## How licences are reported for entries

- The licence shown for each entry is exactly what the source repository or
  registry declares. When there is no licence file, we say
  `⚠️ No licence file` — absence of a licence means *all rights reserved* by
  default; readers must not assume permission to reuse.
- `⚠️ non-commercial` flags CC BY-NC (and similar) licences so they never sit
  unnoticed in an open-source-looking context.
- Licence claims are captured at verification time; a project relicensing
  later may make our note stale. File an issue if you spot this.

## Code vs data — the layered reality

Some projects mix several licences in one repository. The reference example
in this ecosystem is [bangladesh-geojson](https://github.com/ifahimreza/bangladesh-geojson):

| Layer | Licence |
|---|---|
| Code | MIT |
| OpenStreetMap-derived layers | ODbL 1.0 (share-alike, attribution required) |
| Boundary files (geoBoundaries) | CC-BY-4.0 |

We follow that model: when a project's layers carry different obligations, the
entry or the data record says so, and downstream users must respect each
layer's terms.

## Government data caveats

- **data.gov.bd / OGD portal / BBS** — many datasets say "License Not
  Specified". Browse and download freely, but verify the dataset page before
  redistributing.
- **Survey of Bangladesh** — terms verbatim prohibit reproduction, export and
  resale. We do not mirror their data; open alternatives are named in the
  [Developer services](../README.md#-developer-services-not-open) section.
- **Non-commercial research datasets (csebuetnlp and similar)** — free to use
  for research; commercial use requires separate permission from the authors.

## Machine-readable records

Every record in `data/*.json` carries:

- `license` — as published at the source,
- `source_url` — where the licence claim can be checked,
- `last_verified` — ISO date of our last check.

## Not legal advice

These notes describe what the sources say, not what a court would decide.
For anything commercially sensitive, read the licence texts yourself or ask a
lawyer.
