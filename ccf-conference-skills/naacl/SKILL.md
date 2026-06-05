---
name: naacl
description: Writing and formatting guidance for NAACL (North American Chapter of the Association for Computational Linguistics) conference papers. Use when drafting, formatting, and submitting to NAACL 2026. NAACL shares the acl.sty template with ACL and EMNLP. Covers review/final mode switching, double-blind anonymity, NAACL-specific page limits (8 pages), and NLP writing conventions. See the ACL skill for shared formatting rules.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

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
