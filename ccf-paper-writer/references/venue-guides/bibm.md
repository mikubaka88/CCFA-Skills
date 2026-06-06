# BIBM Venue Guide

> Migrated from the legacy `ccf-conference-skills/bibm/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `bibm` |
| Venue family | Bioinformatics / AI |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/BIBM/IEEEtran.cls` |
| Official URL | https://ieeebibm.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# BIBM 2026 Conference Writing Skill

**CCF-B | Bioinformatics / AI | Publisher: IEEE**
**Conference:** https://ieeebibm.org
**Template:** `BIBM/IEEEtran.cls`

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind peer review) ===
\documentclass[10pt,conference,peerreviewca]{IEEEtran}

% === CAMERA-READY MODE ===
\documentclass[10pt,conference]{IEEEtran}

% Required packages
\usepackage{cite}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{url}
\usepackage{amssymb}  % For bioinformatics symbols
\usepackage{algorithm}  % For algorithmic descriptions
\usepackage[noend]{algorithmic}
```

### Required Packages

```latex
\usepackage{cite}              % IEEE citation style
\usepackage{amsmath}           % Math
\usepackage{graphicx}         % Figures
\usepackage{booktabs}         % Professional tables
\usepackage{url}               % URLs in references
\usepackage{microtype}         % Improved typography
\usepackage{amssymb}           % Special symbols
\usepackage{algorithm}         % Algorithm listings
\usepackage[noend]{algorithmic} % Pseudocode
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **8 pages** (typical, check CFP) |
| References | No limit |
| Appendix | Not typically permitted |

Always check the official BIBM CFP for the exact page limit.

## Anonymity Requirements

BIBM uses **double-blind peer review**. Use the `peerreviewca` class option:

1. No author names or affiliations in the submission
2. Use third-person self-citations
3. Anonymize all URLs (including database links)
4. Clear PDF metadata
5. Remove acknowledgments from the submission

## Title and Author Formatting

```latex
% Camera-ready (all authors visible):
\title{Your Paper Title}

\author{
  \IEEEauthorblockN{First Author}
  \IEEEauthorblockA{Department\\
    University\\
    email@example.com}
  \and
  \IEEEauthorblockN{Second Author}
  \IEEEauthorblockA{Department\\
    University\\
    email2@example.com}
}
```

## Camera-Ready Differences

After acceptance:

1. Remove the `peerreviewca` option
2. Add author names and affiliations
3. Add standard IEEE copyright notice

## Section Organization

BIBM papers typically follow this structure:

1. **Introduction** — Problem in bioinformatics/biomedicine, motivation, contributions
2. **Background & Related Work** — Prior work in the domain
3. **Methods** — Proposed algorithm, model, or pipeline
4. **Experiments** — Datasets, evaluation metrics, results
5. **Discussion** — Interpretation, limitations, biological significance
6. **Conclusion**
7. References

## Figures and Tables

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/pipeline}
  \caption{Overview of the proposed bioinformatics pipeline.}
  \label{fig:pipeline}
\end{figure}

\begin{table}[t]
  \caption{Performance comparison on benchmark datasets.}
  \label{tab:results}
  \centering
  \begin{tabular}{lccc}
    \toprule
    Method & Precision & Recall & F1 \\
    \midrule
    Baseline & 0.82 & 0.79 & 0.80 \\
    Ours & 0.89 & 0.86 & 0.87 \\
    \bottomrule
  \end{tabular}
\end{table}
```

- Use vector formats (.pdf, .eps) where possible
- Ensure grayscale legibility
- Caption **below** figures, **above** tables

## References

IEEEtran uses numbered citations:

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}

% Citations:
\citep{key}    % [1]
\citep{key1,key2}  % [1,2]
```

## BIBM-Specific Writing Conventions

- **Domain specificity**: Clearly describe the biological/biomedical problem
- **Datasets**: Report dataset sources, sizes, and preprocessing steps
- **Evaluation metrics**: Use domain-appropriate metrics (AUC, F1, etc.)
- **Statistical significance**: Report p-values, confidence intervals
- **Biological interpretation**: Discuss findings in biological context
- **Code and data availability**: Check CFP for reproducibility requirements

## Formatting Rules

- **Paper size:** US Letter
- **Font:** 10pt default, Times New Roman recommended
- **Margins:** Top 0.75in, bottom 1in, left/right 0.75in or 1in
- **Columns:** Two-column format

## Submission Checklist

- [ ] `\documentclass[10pt,conference,peerreviewca]{IEEEtran}`
- [ ] No author identification in submission
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] Compiles with `pdflatex`
- [ ] References in IEEEtran format
- [ ] Datasets and evaluation metrics clearly described
