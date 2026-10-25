# Security policy

## Supported versions

This repository is a curated list plus a static GitHub Pages site. There are no
runtime services, databases, or user accounts. The latest commit on `main` is
the only supported version.

## Reporting a vulnerability

We take these seriously even for a list project. If you find any of the
following, report it privately rather than opening a public issue:

- A vulnerability in the **GitHub Pages site** (injected content, malicious
  links, broken-out scripts).
- A **malicious entry** listed in the README or the section guides — for
  example, a project that has changed ownership into malware, a link that now
  serves an exploit kit, or a package whose registry page was taken over.
- Anything in this repository that could harm a visitor who follows a link.

**How to report:** use [GitHub private vulnerability reporting][pvr] on this
repository (Security → Report a vulnerability), or contact
[@RanaKhan77](https://github.com/RanaKhan77) directly. Please include the entry
name, the URL you reached, and what you observed. Screenshots help.

We aim to respond within 72 hours. Confirmed malicious entries are removed
first and investigated after — safety outranks curation.

## What is not a security issue

- Dead links, moved repositories, or changed licences — those are ordinary
  [bug reports](https://github.com/RanaKhan77/Awesome-Bangladesh/issues).
- The content of third-party projects we link to. We list projects; we do not
  distribute or endorse their code. Report issues with a listed project to that
  project's own maintainers.

## Link-safety commitments

- Every listed URL is fetched live at verification time.
- Entry URLs point to canonical sources (the repository or the registry page),
  never to deep links that can silently repoint.
- CI runs a scheduled link check; broken or suspicious redirects become issues
  automatically.

[pvr]: https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability
