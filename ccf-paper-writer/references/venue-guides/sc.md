# SC Venue Guide

> Migrated from the legacy `ccf-conference-skills/sc/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-venue-format-guide`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `sc` |
| Venue family | HPC |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/SC/IEEEtran.cls` |
| Official URL | https://sc26.supercomputing.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# SC 2026 Conference Writing Skill

**CCF-A | HPC | Publisher: IEEE**
**Conference:** https://sc26.supercomputing.org
**Template:** `SC/IEEEtran.cls` (IEEEtran conference mode)

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
| Appendix | Not typically permitted |

SC enforces a strict 12-page limit for the main body. References do not count.

## Anonymity Requirements

SC uses double-blind review:

1. No author names or affiliations in submission
2. Use third person for self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs (GitHub repos, institutional pages)
4. Clear PDF metadata
5. Remove acknowledgments from submission

## Camera-Ready Differences

After acceptance:

1. Restore all author names and affiliations using IEEE author blocks
2. Fill in IEEE-specific metadata
3. Add acknowledgments
4. Verify PDF compliance with IEEE Xplore requirements

## Section Organization

SC papers follow the HPC systems structure:

1. **Introduction** — Problem, HPC challenges, contributions (enumerate contributions)
2. **Background & Motivation** — HPC context, existing approaches and limitations
3. **Design/Approach** — Core contribution with parallel algorithm or system design
4. **Implementation** — System details, optimizations, porting effort
5. **Evaluation** — Rigorous performance evaluation, baselines, scalability
6. **Related Work** — Comparison with prior HPC approaches
7. **Conclusion** — Summary and future work
8. References

## HPC-Specific Conventions

### Performance Evaluation

SC papers must have rigorous HPC performance evaluation:

```latex
\section{Evaluation}

\subsection{Experimental Setup}
We conduct experiments on:
\begin{itemize}
  \item \textbf{System}: Summit at Oak Ridge National Laboratory
  \item \textbf{Configuration}: 512 nodes, IBM Power9 CPUs, NVIDIA V100 GPUs
  \item \textbf{Software}: CUDA 11.8, OpenMPI 4.1
\end{itemize}

\subsection{Strong Scaling}
We report strong scaling results using:
\begin{itemize}
  \item \textbf{Baseline}: Single-node execution
  \item \textbf{Metrics}: Speedup, parallel efficiency ($S_p = T_1/T_p$)
  \item \textbf{Comparison}: State-of-the-art HPC frameworks
\end{itemize}

\subsection{Weak Scaling}
We evaluate weak scaling with problem size $N = 1024^3$ per node.
```

### Scalability Analysis

Include both strong and weak scaling analysis:
- **Strong scaling**: Fixed problem size, vary number of processors
- **Weak scaling**: Vary problem size proportionally with processors

```latex
\begin{table}[t]
  \caption{Strong scaling results on 1024$^3$ grid.
    Speedup is relative to single-node baseline.}
  \label{tab:scaling}
  \centering
  \begin{tabular}{lrrrr}
    \toprule
    Nodes & Time (s) & Speedup & Efficiency \\
    \midrule
    1     & 1024.2   & 1.0$\times$   & 100\% \\
    16    & 68.4     & 14.9$\times$  & 93\% \\
    64    & 17.8     & 57.5$\times$  & 90\% \\
    256   & 4.9      & 209.0$\times$ & 82\% \\
    \bottomrule
  \end{tabular}
\end{table}
```

## HPC Benchmarks

Common HPC benchmarks and workloads:
- LINPACK (HPL)
- HPCG
- NPB (NAS Parallel Benchmarks)
- HPC applications (climate, molecular dynamics, etc.)

## Figures and Tables

- Use vector formats (.pdf, .eps) for all figures
- Ensure grayscale legibility
- Include error bars for performance measurements
- Report confidence intervals where applicable

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/strong-scaling}
  \caption{Strong scaling comparison on Summit. Our approach
    achieves near-linear speedup up to 256 nodes, outperforming
    the state-of-the-art by 1.8$\times$ at full scale.}
  \label{fig:scaling}
\end{figure}
```

## References

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}

% Citations:
~\cite{doe2025}         % [1]
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
- [ ] Strong and weak scaling results included
- [ ] Figures legible in grayscale

## Camera-Ready Checklist

- [ ] Restore author names with IEEE author blocks
- [ ] Add acknowledgments
- [ ] Verify PDF compliance with IEEE Xplore
- [ ] Check figure resolution and quality
