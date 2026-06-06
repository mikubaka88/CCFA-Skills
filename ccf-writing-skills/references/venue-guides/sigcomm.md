# SIGCOMM Venue Guide

> Migrated from the legacy `ccf-conference-skills/sigcomm/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `sigcomm` |
| Venue family | Networks |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/SIGCOMM/acmart.cls` |
| Official URL | https://sigcomm2026.sigcomm.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# SIGCOMM 2026 Conference Writing Skill

**CCF-A | Networks | Publisher: ACM**
**Conference:** https://sigcomm2026.sigcomm.org
**Template:** `SIGCOMM/acmart.cls` (ACM acmart, sigconf format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigconf,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigconf]{acmart}
\acmConference[SIGCOMM 2026]{SIGCOMM '26: ACM SIGCOMM 2026 Conference}
               {August 4--8, 2026}{São Paulo, Brazil}
\acmISBN{978-X-XXXX-XXXX-X/XX/XX}
\acmDOI{10.5555/XXXXXXX.XXXXXXX}
```

### Required Packages

```latex
\usepackage[round]{natbib}     % Author-year citations
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{listings}
\lstset{basicstyle=\small\ttfamily}
\usepackage{booktabs}
\usepackage{graphicx}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **14 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

SIGCOMM enforces a 14-page limit for the main body. References and appendix do not count.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. No author names anywhere in submission
2. Third-person self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs (GitHub, institutional pages)
4. Clear PDF metadata
5. Do not include acknowledgments

## Camera-Ready Differences

After acceptance:

1. Remove `review` and `anonymous` options
2. Fill in `\acmConference`, `\acmISBN`, `\acmDOI`
3. Restore author names and affiliations
4. Add appropriate `\setcopyright` mode
5. Enable page numbers with `\settopmatter{printfolios=true}`

## Section Organization

SIGCOMM papers follow the networking research structure:

1. **Introduction** — Problem, motivation, contributions (enumerate contributions)
2. **Background & Motivation** — Why the problem matters, existing approaches and limits
3. **Design/Approach** — Core contribution with formal treatment
4. **Implementation** — System/prototype details, complexity
5. **Evaluation** — Rigorous experimental methodology, measurement studies, sensitivity analysis
6. **Related Work** — Thorough positioning against prior art
7. **Conclusion** — Summary and future directions
8. References
9. Appendix (optional)

## Networking-Specific Conventions

SIGCOMM values rigorous networking research:

### Protocol Design

```latex
\section{Protocol Design}

\subsection{Overview}
Our protocol consists of three components:
\begin{itemize}
  \item \textbf{Control plane}: Distributed routing with
    $O(\log n)$ convergence time
  \item \textbf{Data plane}: Wire-speed forwarding with
    minimal state requirements
  \item \textbf{Management}: Telemetry and monitoring APIs
\end{itemize}

\subsection{Formal Properties}
We prove the following properties:
\begin{itemize}
  \item \textbf{Loop freedom}: Packets never traverse loops
  \item \textbf{Path optimality}: Selected paths are within
    factor 2 of optimal
  \item \textbf{Load balance}: Maximum link utilization is
    within $\frac{\log n}{n}$ of optimal
\end{itemize}
```

### Measurement Studies

SIGCOMM often includes real-world measurement:

```latex
\section{Measurement Study}

We analyze traffic from a tier-1 ISP backbone network:
\begin{itemize}
  \item \textbf{Dataset}: 48 hours of packet traces
    (anonymized), totaling 2.3 TB
  \item \textbf{Coverage}: 120 PoPs across 4 continents
  \item \textbf{Methodology}: Passive traffic analysis using
    custom packet inspection tools
\end{itemize}
```

## Evaluation

```latex
\section{Evaluation}

We evaluate our design through:
\begin{itemize}
  \item \textbf{Simulation}: ns-3 simulation of 1000-node
    network topology
  \item \textbf{Testbed}: 20-node testbed with commodity
    hardware
  \item \textbf{Real deployment}: 6-month deployment in
    production network
\end{itemize}
```

## Figures and Tables

- Use vector formats (.pdf) for all figures
- Ensure grayscale legibility
- Include network topology diagrams
- Tables should have clear column headers and units

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/topology}
  \caption{Network topology used in evaluation. Links are
    labeled with propagation delay. Our protocol achieves
    40\% lower convergence time than BGP while maintaining
    loop freedom guarantees.}
  \label{fig:topology}
\end{figure}
```

## References (natbib)

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\citet{doe2025}      % Doe et al. (2025)
\citep{doe2025}     % (Doe et al. 2025)
```

All references must list **every author by full name**.

## Formatting Rules

- **Format:** ACM sigconf (two-column, single-spaced)
- **Paper size:** US Letter
- **Body font:** 9pt minimum
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in

## Submission Checklist

- [ ] 14 pages or fewer (main body)
- [ ] `\documentclass[sigconf,review,anonymous]`
- [ ] All author identification removed
- [ ] No self-referential citations in first person
- [ ] Anonymized all URLs
- [ ] PDF metadata cleared
- [ ] References list all authors
- [ ] Figures legible in grayscale

## Camera-Ready Checklist

- [ ] Remove `review` and `anonymous` options
- [ ] Add conference metadata
- [ ] Restore author information
- [ ] Enable page numbers
