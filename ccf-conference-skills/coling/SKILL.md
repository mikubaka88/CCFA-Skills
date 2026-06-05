---
name: coling
description: Writing and formatting guidance for COLING (International Conference on Computational Linguistics) papers. Use when drafting, formatting, and submitting to COLING 2026. COLING shares the acl.sty template with ACL and EMNLP. Covers review/final mode switching, double-blind anonymity, COLING-specific page limits, and NLP writing conventions. See the ACL skill for shared formatting rules.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

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
