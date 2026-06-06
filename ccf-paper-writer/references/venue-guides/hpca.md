# HPCA Venue Guide

> Migrated from the legacy `ccf-conference-skills/hpca/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-venue-format-guide`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `hpca` |
| Venue family | Architecture |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/HPCA/IEEEtran.cls` |
| Official URL | https://hpca2026.ece.ufl.edu |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# HPCA 2026 Conference Writing Skill

**CCF-A | Architecture | Publisher: IEEE**
**Conference:** https://hpca2026.ece.ufl.edu
**Template:** `HPCA/IEEEtran.cls` (IEEEtran conference mode)

## Document Setup

### Preamble Structure

```latex
\documentclass[conference]{IEEEtran}

% Optional packages
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{cite}
\usepackage{hyperref}
\usepackage{booktabs}
\usepackage[dvipsnames]{xcolor}
```

### Required Packages

```latex
\documentclass[conference]{IEEEtran}
\usepackage{graphicx}       % Figures
\usepackage{amsmath}        % Math
\usepackage{amssymb}        % Symbols
\usepackage{cite}           % Citations
\usepackage{booktabs}       % Professional tables
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **12 pages** |
| References | No limit |
| Appendix | Permitted (supplementary) |

HPCA enforces a 12-page limit for the main body. References do not count.

## Anonymity Requirements

HPCA uses double-blind review:

1. No author names or affiliations in submission
2. Use third person for self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs (GitHub repos, institutional pages)
4. Clear PDF metadata
5. Remove acknowledgments from submission

## Camera-Ready Differences

After acceptance:

1. Restore all author names and affiliations using IEEE author blocks
2. Fill in IEEE conference metadata
3. Add acknowledgments
4. Verify PDF compliance with IEEE Xplore requirements

## Section Organization

HPCA papers follow the architecture research structure:

1. **Introduction** — Problem, architecture challenge, contributions (enumerate contributions)
2. **Background & Motivation** — Architecture context, why current solutions are insufficient
3. **Design/Approach** — Core microarchitectural contribution with rationale
4. **Implementation/Methodology** — Simulation/hardware details, configuration
5. **Evaluation** — Performance results, comparison, sensitivity analysis
6. **Related Work** — Positioning within architecture literature
7. **Conclusion** — Summary and future directions
8. References
9. Appendix (supplementary)

## Architecture-Specific Conventions

### Simulation Methodology

HPCA papers must have rigorous simulation methodology:

```latex
\section{Methodology}

\subsection{Simulation Framework}
We use gem5 with Ruby memory system:
\begin{itemize}
  \item \textbf{ISA}: x86-64
  \item \textbf{CPU model}: Out-of-order, 4-wide issue
  \item \textbf{Cache hierarchy}: L1 (32KB I/D), L2 (256KB), L3 (8MB)
  \item \textbf{Clock}: 3.0 GHz
\end{itemize}

\subsection{Workloads}
We evaluate on:
\begin{itemize}
  \item \textbf{Benchmarks}: SPEC CPU 2017 (int and fp)
  \item \textbf{Input sizes}: ref dataset
  \item \textbf{Simulation points}: 1B instructions with 100M warm-up
\end{itemize}

\subsection{Baselines}
We compare against:
\begin{itemize}
  \item Conventional cache hierarchy
  \item State-of-the-art prediction techniques
\end{itemize}
```

### Hardware Evaluation

If implemented in hardware:

```latex
\subsection{Hardware Implementation}
We synthesize our design using:
\begin{itemize}
  \item \textbf{Target}: TSMC 7nm standard cell library
  \item \textbf{Tools}: Synopsys Design Compiler, IC Compiler II
  \item \textbf{Area}: 2.4 mm$^2$ (including tag array)
  \item \textbf{Latency}: 3 cycle tag lookup
\end{itemize}
```

### Performance Metrics

Common HPCA metrics:
- IPC (Instructions Per Cycle)
- CPI (Cycles Per Instruction)
- Performance speedup
- Cache miss rates (L1/L2/L3)
- Branch misprediction rates
- Energy efficiency (pJ/op)

## Sensitivity Analysis

HPCA values comprehensive sensitivity analysis:

```latex
\section{Sensitivity Analysis}
We vary key design parameters:

\subsection{Cache Size}
We sweep L2 cache size from 128KB to 1MB and observe consistent
performance improvements of 15-20\% across all configurations.

\subsection{Issue Width}
Our approach maintains benefits across issue widths from 2 to 8.
```

## Figures and Tables

- Use vector formats (.pdf, .eps) for all figures
- Ensure grayscale legibility
- Include microarchitecture diagrams
- Report error bars where applicable

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/microarch}
  \caption{Microarchitecture overview: (a) overall pipeline organization,
    (b) details of the proposed predictor unit. The predictor adds only
    2.4KB of storage overhead while reducing mispredictions by 34\%.}
  \label{fig:microarch}
\end{figure}
```

## References

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}

% Citations:
~\cite{smith2023}         % [1]
```

IEEEtran numbered citation style.

## Formatting Rules

- **Format:** IEEE conference (two-column)
- **Paper size:** US Letter
- **Margins:** Per IEEE conference guidelines
- **Body font:** 10pt typical
- **References:** 8pt, no page limit

## Submission Checklist

- [ ] 12 pages or fewer (main body)
- [ ] All author identification removed
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] PDF metadata cleared
- [ ] References in IEEE format
- [ ] Simulation methodology fully described
- [ ] Sensitivity analysis included
- [ ] Figures legible in grayscale

## Camera-Ready Checklist

- [ ] Restore author names with IEEE author blocks
- [ ] Add acknowledgments
- [ ] Verify PDF compliance with IEEE Xplore
- [ ] Check figure resolution and quality
