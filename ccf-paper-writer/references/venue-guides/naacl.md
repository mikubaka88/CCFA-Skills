# NAACL Venue Guide

> Migrated from the legacy `ccf-conference-skills/naacl/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-venue-format-guide`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `naacl` |
| Venue family | TBD |
| CCF tier | TBD |
| Template path | `ccf-latex-templates/NAACL` |
| Official URL | TBD |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# NAACL 2026 Conference Writing Skill

## Overview

This skill covers LaTeX formatting, submission rules, and writing conventions for **NAACL (North American Chapter of the Association for Computational Linguistics)** — a **CCF-B** conference in the AI category, held annually at [https://2026.naacl.org](https://2026.naacl.org). The publisher is **ACL**.

> **Prerequisite:** NAACL shares the same `acl.sty` template as ACL, EMNLP, COLING, and CoNLL. **Read the ACL skill first** for shared formatting rules. This skill covers NAACL-specific rules only.

**Template path:** `ccf-latex-templates/NAACL/`
- `acl_latex.tex` — main template (identical to ACL/EMNLP)
- `acl.sty` — shared style file

---

## Document Class and Modes

NAACL uses the same three-mode system as ACL:

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

**NAACL 2026: 8 pages** for the main paper, **excluding** references and appendix.

---

## Submission Policies

### Double-Blind Review

- Submission must be anonymized: no author names, affiliations, or acknowledgments.
- In review mode, `acl.sty` automatically shows "Anonymous ACL submission".
- **Self-citations:** Remove or anonymize citations to prior work by the authors.
- Do not post anonymized drafts to public repositories.

### Originality and Reproducibility

- Submissions must be original, unpublished work.
- NAACL emphasizes **reproducibility**:
  - Hyperparameters and training details in appendices
  - Links to code repositories (anonymized if submitted)
  - Results averaged over multiple random seeds

---

## Camera-Ready Preparation

After acceptance:

- [ ] Switch `\usepackage[review]{acl}` to `\usepackage{acl}`
- [ ] Restore author names and affiliations
- [ ] Restore self-citations
- [ ] Add/update Acknowledgments section
- [ ] Verify page count ≤ 8 pages (excluding refs/appendix)
- [ ] Include ACL Anthology bibliography

---

## NLP Writing Conventions for NAACL

NAACL papers typically follow this structure:

1. **Abstract** — 150–200 words
2. **Introduction** — motivation, task, challenge, contributions
3. **Related Work** — prior work categorized by approach
4. **Background / Preliminaries** — formal notation, task definition
5. **Method / Model** — core contribution
6. **Experimental Setup** — datasets, metrics, baselines
7. **Results and Analysis** — quantitative, ablation, error analysis
8. **Conclusion** — summary, limitations
9. **Acknowledgments**
10. **References**

### Key NAACL Expectations

- **Datasets:** Describe source, size, language, preprocessing, licensing
- **Baselines:** Compare against strong, established baselines
- **Metrics:** Report standard NLP metrics with confidence intervals
- **Ablation:** Study contribution of each component
- **Error Analysis:** Qualitative examples of successes/failures
- **Limitations:** Discuss limitations honestly

---

## Checklist Summary

- [ ] `\usepackage[review]{acl}` for submission
- [ ] All authors anonymized (auto via review mode)
- [ ] Self-citations anonymized or removed
- [ ] ≤ 8 pages main text (excluding refs/appendix)
- [ ] natbib citations: `\citet{}`, `\citep{}`
- [ ] ACL Anthology bibliography included
- [ ] Dataset descriptions complete
- [ ] Baseline methods properly cited
- [ ] Statistical significance tested
- [ ] Camera-ready: switch to `\usepackage{acl}`
