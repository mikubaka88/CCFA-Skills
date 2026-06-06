# ICPR Venue Guide

> Migrated from the legacy `ccf-conference-skills/icpr/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `icpr` |
| Venue family | Pattern Recognition / AI |
| CCF tier | CCF-C |
| Template path | `ccf-latex-templates/ICPR/IEEEtran.cls` |
| Official URL | https://icpr2026.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# ICPR 2026 Conference Writing Skill

**CCF-C | Pattern Recognition / AI | Publisher: IEEE**
**Conference:** https://icpr2026.org
**Template:** `ICPR/IEEEtran.cls`

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION / CAMERA-READY MODE ===
\documentclass[10pt,conference]{IEEEtran}

% Required packages
\usepackage{cite}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{url}
\usepackage{amssymb}     % For special symbols
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
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper | **6 pages** (typical, check CFP) |
| References | No limit |
| Appendix | Not typically permitted |

Always check the official ICPR CFP for the exact page limit.

## Anonymity Requirements

ICPR typically uses a **single-blind review process** (authors visible). Check the current CFP:

1. Author names and affiliations are typically shown
2. Use third-person self-citations if anonymity is expected
3. Clear PDF metadata
4. Remove acknowledgments from submission if required

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

1. Add author names and affiliations
2. Add `\IEEEmembership{}` if needed
3. Include the standard IEEE copyright notice

## Section Organization

ICPR papers typically follow a pattern recognition research structure:

1. **Introduction** — Pattern recognition problem, motivation, contributions
2. **Related Work** — Prior work in pattern recognition or computer vision
3. **Proposed Method** — Feature extraction, classification, or recognition approach
4. **Experiments** — Datasets, evaluation metrics, results
5. **Discussion** — Analysis, limitations
6. **Conclusion**
7. References

## Figures and Tables

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/method}
  \caption{Overview of the proposed pattern recognition method.}
  \label{fig:method}
\end{figure}

\begin{table}[t]
  \caption{Comparison with state-of-the-art methods.}
  \label{tab:results}
  \centering
  \begin{tabular}{lccc}
    \toprule
    Method & Accuracy & Precision & Recall \\
    \midrule
    Baseline & 85.2 & 84.1 & 86.3 \\
    Ours & 91.7 & 90.5 & 93.0 \\
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

## ICPR-Specific Writing Conventions

- **Method clarity**: Describe the pattern recognition or classification approach in detail
- **Datasets**: Report benchmark dataset details (source, size, splits)
- **Evaluation metrics**: Report standard PR metrics (accuracy, precision, recall, F1, AUC)
- **Statistical reporting**: Include mean ± standard deviation, statistical significance tests
- **Visual results**: Include confusion matrices, ROC curves, qualitative examples
- **Reproducibility**: Include key hyperparameters and training details

## Formatting Rules

- **Paper size:** US Letter
- **Font:** 10pt default, Times New Roman recommended
- **Margins:** Top 0.75in, bottom 1in, left/right 0.75in or 1in
- **Columns:** Two-column format

## Submission Checklist

- [ ] `\documentclass[10pt,conference]{IEEEtran}`
- [ ] Compiles with `pdflatex`
- [ ] References in IEEEtran format
- [ ] Datasets and evaluation metrics clearly described
- [ ] High-quality, grayscale-legible figures
