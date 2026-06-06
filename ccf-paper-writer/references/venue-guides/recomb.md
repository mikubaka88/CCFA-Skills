# RECOMB Venue Guide

> Migrated from the legacy `ccf-conference-skills/recomb/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `recomb` |
| Venue family | Computational Biology |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/RECOMB/llncs.cls` |
| Official URL | https://recomb2026.w |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# RECOMB 2026 Conference Writing Skill

**CCF-B | Computational Biology | Publisher: Springer**
**Conference:** https://recomb2026.w Demons!
**Template:** `RECOMB/llncs.cls` (Springer LNCS class)

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
| Main paper | **~12 pages** (check CFP) |
| References | No limit |
| Appendix | Check CFP |

Always check the official RECOMB CFP for the exact page limit.

## Anonymity Requirements

RECOMB uses **double-blind review**:

1. No author names or affiliations in submission
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
4. Submit final source files

## Section Organization

RECOMB papers typically follow a computational biology research structure:

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
  \includegraphics[width=0.8\linewidth]{figs/algorithm}
  \caption{Schematic overview of the proposed algorithm.}
  \label{fig:algorithm}
\end{figure}

\begin{table}
  \caption{Comparison with existing methods.}
  \label{tab:comparison}
  \centering
  \begin{tabular}{lccc}
    \hline
    Method & Accuracy & Runtime & Memory \\
    \hline
    Baseline & 0.82 & 120s & 2GB \\
    Ours & 0.89 & 45s & 1GB \\
    \hline
  \end{tabular}
\end{table}
```

- Use EPS format for figures where possible
- Caption **below** figures
- Use horizontal rules (`\hline`) per LNCS convention

## References (numbered)

LNCS uses **numbered citations** with `splncs04.bst`:

```latex
\bibliographystyle{splncs04}
\bibliography{references}

% Citations:
\cite{key}      % [1]
\cite{key1,key2}  % [1,2]
```

## RECOMB-Specific Writing Conventions

- **Biological significance**: Explain the biological relevance of findings
- **Datasets**: Report dataset sources (e.g., UniProt, PDB, GenBank), sizes, preprocessing
- **Evaluation metrics**: Use appropriate metrics (AUC, MCC, sensitivity, specificity)
- **Reproducibility**: Include enough detail to reproduce computational results
- **Theoretical contribution**: RECOMB values novel algorithms and theoretical insights
- **Supplementary material**: Check CFP for supplementary data policy

## Formatting Rules

- **Paper size:** A4 (LNCS default)
- **Font:** 10pt default (Helvetica or Times New Roman)
- **Margins:** LNCS default (12.2cm text width, 19.3cm text height)
- **Columns:** Two-column format

## Submission Checklist

- [ ] `\documentclass[runningheads]{llncs}`
- [ ] Author info removed (double-blind)
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] Compiles with `pdflatex`
- [ ] References in splncs04 format (numbered)
- [ ] Datasets and evaluation metrics clearly described
