# WINE Venue Guide

> Migrated from the legacy `ccf-conference-skills/wine/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `wine` |
| Venue family | Game Theory / Economics / AI |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/WINE/llncs.cls` |
| Official URL | https://wine2026.cs.umass.edu |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# WINE 2026 Conference Writing Skill

**CCF-B | Game Theory / Economics / AI | Publisher: Springer**
**Conference:** https://wine2026.cs.umass.edu
**Template:** `WINE/llncs.cls` (Springer LNCS class)

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
\usepackage{amssymb}
```

### Required Packages

```latex
\usepackage[T1]{fontenc}    % T1 font encoding (required)
\usepackage{graphicx}        % Figures (use EPS format)
\usepackage{url}             % URLs in references
\usepackage{booktabs}       % Professional tables
\usepackage{amsmath}         % Math
\usepackage{amssymb}         % Additional math symbols
\usepackage{microtype}       % Improved typography
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper | **~15 pages** (check CFP) |
| References | No limit |
| Appendix | Check CFP |

Always check the official WINE CFP for the exact page limit.

## Anonymity Requirements

WINE typically uses **double-blind review**. Check the current CFP:

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
4. Submit final source files

## Section Organization

WINE papers typically follow an algorithmic game theory structure:

1. **Introduction** — Economic/Internet problem, motivation, contributions
2. **Model / Definitions** — Formal game-theoretic or mechanism design model
3. **Results** — Theorems, lemmas, and proofs
4. **Applications / Case Studies** — Practical applications
5. **Related Work** — Positioning vs. prior work
6. **Conclusion / Discussion**
7. References

WINE values **theoretical contributions** (new equilibrium concepts, mechanism designs, complexity results) supported by **proofs**.

## Theorem Environments

WINE papers heavily use formal mathematics:

```latex
\begin{definition}
  A Nash equilibrium is a strategy profile...
\end{definition}

\begin{lemmas}
  Lemma text...
\end{lemmas}

\begin{theorems}
  Theorem text...
\end{theorems}

\begin{proposition}
  Proposition text...
\end{proposition}

\begin{corrlary}
  Corollary text...
\end{corrlary}

\begin{example}
  Example text...
\end{example}

\begin{Proof}
  Proof text...
\end{Proof}
```

## Figures and Tables

```latex
\begin{figure}
  \centering
  \includegraphics[width=0.8\linewidth]{figs/example}
  \caption{Example illustrating the mechanism.}
  \label{fig:example}
\end{figure}

\begin{table}
  \caption{Experimental results.}
  \label{tab:results}
  \centering
  \begin{tabular}{lcc}
    \hline
    Algorithm & Revenue & Welfare \\
    \hline
    Baseline & 100 & 80 \\
    Ours & 120 & 95 \\
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

## WINE-Specific Writing Conventions

- **Formal modeling**: Clearly define the game-theoretic model
- **Proof quality**: Include complete proofs; appendices are acceptable for long proofs
- **Algorithm descriptions**: Describe algorithms in sufficient detail
- **Experimental validation**: Complement theoretical results with simulations or empirical studies
- **Economic interpretation**: Explain the economic implications of theoretical findings
- **Motivation**: Clearly motivate the problem from a real-world Internet economics perspective

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
- [ ] All theorems, lemmas, and proofs clearly labeled
