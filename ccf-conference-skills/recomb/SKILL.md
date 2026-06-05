---
name: recomb
description: Writing and formatting guidance for RECOMB (International Conference on Research in Computational Molecular Biology) papers. Use when drafting, formatting, or submitting to RECOMB 2026. Covers Springer LNCS llncs.cls format, page limits, reference formatting with splncs04 BibTeX style, numbered citations, computational biology research conventions, and camera-ready preparation. RECOMB is a CCF-B computational biology conference published by Springer.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

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
