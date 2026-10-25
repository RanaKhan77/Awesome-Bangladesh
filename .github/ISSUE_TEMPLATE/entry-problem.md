name: "Report a problem with a listed entry"
description: "Dead link, wrong licence, misplaced section, stale claim"
title: "[Fix]: <entry name>"
labels: ["fix"]
body:
  - type: input
    id: entry
    attributes:
      label: Entry name
      description: Exactly as it appears in the README or section guide.
    validations:
      required: true
  - type: dropdown
    id: problem
    attributes:
      label: What is wrong?
      options:
        - Dead link (404 / repo deleted / domain gone)
        - Link redirects somewhere unexpected
        - Licence note is wrong
        - It is in the wrong section
        - Description is out of date
        - Project changed ownership or went malicious
        - Other
    validations:
      required: true
  - type: textarea
    id: details
    attributes:
      label: Details
      description: What you expected vs what you found. For licence fixes, link to the licence file. For ownership changes, link to the new owner.
    validations:
      required: true
  - type: checkboxes
    id: safety
    attributes:
      label: Safety check
      options:
        - label: This is not a security/safety problem requiring private reporting (if it is, use the security policy instead of this issue)
          required: true
