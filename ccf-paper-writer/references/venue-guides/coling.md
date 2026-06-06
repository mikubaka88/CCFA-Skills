# COLING Venue Guide

> Migrated from the legacy `ccf-conference-skills/coling/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-venue-format-guide`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `coling` |
| Venue family | TBD |
| CCF tier | TBD |
| Template path | `ccf-latex-templates/COLING` |
| Official URL | TBD |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# COLING 2026 Conference Writing Skill

## Overview

This skill covers LaTeX formatting, submission rules, and writing conventions for **COLING (International Conference on Computational Linguistics)** — a **CCF-B** conference in the AI category, held at [https://coling2026.org](https://coling2026.org). The publisher is **ICCL**.

> **Prerequisite:** COLING shares the same `acl.sty` template as ACL, EMNLP, and NAACL. **Read the ACL skill first** for shared formatting rules. This skill covers COLING-specific rules only.

**Template path:** `ccf-latex-templates/COLING/`
- `acl_latex.tex` — main template (identical to ACL/EMNLP/NAACL)
- `acl.sty` — shared style file

---

## Document Class and Modes

COLING uses the same three-mode system as ACL:

```latex
% Submission (anonymized review)
\documentclass[11pt]{article}
\usepackage[review]{acl}

% Camera-ready (final)
\documentclass[11pt]{article}
\usepackage{acl}

% Non-anonymous preprint
\documentclass[11pt]{article}
\usepackage[preprint]{acl}
```

---

## Page Limit

**COLING 2026: 8 pages** for the main paper, **excluding** references and appendix.

---

## Submission Policies

### Double-Blind Review

- Submission must be anonymized: no author names, affiliations, or acknowledgments.
- In review mode, `acl.sty` automatically shows "Anonymous ACL submission".
- **Self-citations:** Remove or anonymize citations to prior work by the authors.
- Do not post anonymized drafts to public repositories.

### Reproducibility

COLING values reproducible research:
- Include hyperparameters in appendices
- Provide code links (anonymized if submitted)
- Report results with standard deviation

---

## Camera-Ready Preparation

After acceptance:

- [ ] Switch `\usepackage[review]{acl}` to `\usepackage{acl}`
- [ ] Restore author names and affiliations
- [ ] Restore self-citations
- [ ] Add/update Acknowledgments section
- [ ] Verify page count ≤ 8 pages (excluding refs/appendix)

---

## Checklist Summary

- [ ] `\usepackage[review]{acl}` for submission
- [ ] All authors anonymized (auto via review mode)
- [ ] Self-citations anonymized or removed
- [ ] ≤ 8 pages main text (excluding refs/appendix)
- [ ] Dataset descriptions complete
- [ ] Camera-ready: switch to `\usepackage{acl}`
