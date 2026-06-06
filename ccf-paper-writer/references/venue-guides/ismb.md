# ISMB Venue Guide

> Migrated from the legacy `ccf-conference-skills/ismb/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `ismb` |
| Venue family | Computational Biology |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/ISMB/llncs.cls` |
| Official URL | https://www.iscb.org/ismb2026 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# ISMB 2026 Conference Writing Skill

**CCF-B | Computational Biology | Publisher: Oxford University Press**
**Conference:** https://www.iscb.org/ismb2026
**Template:** `ISMB/llncs.cls` (Springer LNCS class)

> **Note:** ISMB proceedings are published in the OUP journal *Bioinformatics*. Check the CFP for whether the conference or journal formatting style applies, as submission and publication formats may differ.

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION / CAMERA-READY MODE ===
\documentclass[runningheads]{llncs}

\usepackage[T1]{fontenc}
\usepackage{graphicx}
\usepackage{url}
\usepackage{booktabs}
\usepackage{amsmath}
```

### Required Packages

```latex
\usepackage[T1]{fontenc}    % T1 font encoding (required)
\usepackage{graphicx}        % Figures (use EPS format)
\usepackage{url}             % URLs in references
\usepackage{booktabs}       % Professional tables
\usepackage{amsmath}         % Math
\usepackage{microtype}       % Improved typography
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper | **~10 pages** (check CFP) |
| References | No limit |
| Appendix | Check CFP |

Always check the official ISMB CFP for the exact page limit, as it may differ from the LNCS default.

## Anonymity Requirements

ISMB typically uses **double-blind review**. Check the current CFP for submission requirements:

1. No author names or affiliations in submission (if double-blind)
2. Use third-person self-citations
3. Anonymize all URLs
4. Clear PDF metadata
5. Remove acknowledgments from submission

## Title and Author Formatting

```latex
\title{Your Paper Title}
%\titlerunning{Abbreviated paper title}  % For running heads

\author{First Author\inst{1} \and
  Second Author\inst{2} \and
  Third Author\inst{1,2}}

\institute{
  Institution 1\\
  email@example.com
  \and
  Institution 2\\
  email2@example.com
}
```

## Camera-Ready Differences

After acceptance:

1. Restore all author names and affiliations
2. Add acknowledgments if desired
3. Verify page count
4. Submit final source files to the conference system

## Section Organization

ISMB papers typically follow a computational biology research structure:

1. **Introduction** — Biological problem, motivation, contributions
2. **Background / Related Work** — Prior work in the domain
3. **Methods** — Proposed algorithm, model, or computational approach
4. **Results** — Experiments on benchmark datasets
5. **Discussion** — Biological interpretation, limitations
6. **Conclusion**
7. References

## Figures and Tables

```latex
\begin{figure}
  \centering
  \includegraphics[width=0.8\linewidth]{figs/pipeline}
  \caption{Overview of the proposed computational pipeline.}
  \label{fig:pipeline}
\end{figure}

\begin{table}
  \caption{Performance comparison on benchmark datasets.}
  \label{tab:results}
  \centering
  \begin{tabular}{lccc}
    \hline
    Method & Precision & Recall & F1 \\
    \hline
    Baseline & 0.82 & 0.79 & 0.80 \\
    Ours & 0.89 & 0.86 & 0.87 \\
    \hline
  \end{tabular}
\end{table}
```

- Use EPS format for figures where possible
- Caption **below** figures
- Use horizontal rules (`\hline`) per LNCS convention (not `booktabs` rules)

## References (numbered)

LNCS uses **numbered citations** with `splncs04.bst`:

```latex
\bibliographystyle{splncs04}
\bibliography{references}

% Citations:
\cite{key}      % [1]
\cite{key1,key2}  % [1,2]
```

## ISMB-Specific Writing Conventions

- **Biological significance**: Clearly explain the biological relevance of findings
- **Datasets**: Report dataset sources (e.g., UniProt, PDB, GEO), sizes, and preprocessing
- **Evaluation metrics**: Use domain-appropriate metrics (AUC, MCC, etc.) with confidence intervals
- **Reproducibility**: Include enough detail to reproduce computational results
- **Supplementary material**: Check CFP for supplementary data policy
- **Code availability**: Consider sharing code and data for reproducibility

## Formatting Rules

- **Paper size:** A4 (LNCS default)
- **Font:** 10pt default (Helvetica or Times New Roman)
- **Margins:** LNCS default (12.2cm text width, 19.3cm text height)
- **Columns:** Two-column format

## Submission Checklist

- [ ] `\documentclass[runningheads]{llncs}`
- [ ] Author info removed (if double-blind)
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] Compiles with `pdflatex`
- [ ] References in splncs04 format (numbered)
- [ ] Datasets and evaluation metrics clearly described
