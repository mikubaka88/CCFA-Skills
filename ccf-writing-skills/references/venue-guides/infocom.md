# INFOCOM Venue Guide

> Migrated from the legacy `ccf-conference-skills/infocom/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `infocom` |
| Venue family | Networks |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/INFOCOM/IEEEtran.cls` |
| Official URL | https://infocom2026.ieee-infocom.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# INFOCOM 2026 Conference Writing Skill

**CCF-A | Networks | Publisher: IEEE**
**Conference:** https://infocom2026.ieee-infocom.org
**Template:** `INFOCOM/IEEEtran.cls` (IEEEtran conference mode)

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
| Appendix | Permitted (supplementary) |

INFOCOM enforces a 12-page limit for the main body. References do not count.

## Anonymity Requirements

INFOCOM uses double-blind review:

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

INFOCOM papers follow the networking research structure:

1. **Introduction** — Problem, networking challenge, contributions (enumerate contributions)
2. **Background & Related Work** — Networking context, existing protocols and limitations
3. **System Model / Problem Formulation** — Formal problem statement
4. **Proposed Protocol / Design** — Core networking contribution
5. **Performance Analysis** — Theoretical bounds, complexity analysis
6. **Evaluation** — Simulation results, testbed evaluation, comparison
7. **Discussion** — Practical considerations, limitations
8. **Conclusion** — Summary and future work
9. References
10. Appendix (supplementary)

## Networking-Specific Conventions

### Network Simulations

INFOCOM papers typically include simulation evaluation:

```latex
\section{Evaluation}

\subsection{Simulation Setup}
We evaluate using ns-3:
\begin{itemize}
  \item \textbf{Topology}: 100-node random network (barabasi-albert)
  \item \textbf{Link capacity}: 100 Mbps with 10ms propagation delay
  \item \textbf{Traffic}: CBR and Pareto-distributed flows
  \item \textbf{Protocol parameters}: Window size, timers per RFC 9002
\end{itemize}

\subsection{Baselines}
We compare our protocol against:
\begin{itemize}
  \item \textbf{TCP CUBIC}: Linux default congestion control
  \item \textbf{BBR}: Model-based congestion control
  \item \textbf{DCTCP}: Data center TCP
\end{itemize}
```

### Performance Metrics

Common INFOCOM networking metrics:
- Throughput (Mbps, packets/sec)
- End-to-end latency (ms)
- Packet loss rate
- Jitter
- Fairness (Jain's index)
- Energy efficiency

## Protocol Design

INFOCOM values rigorous protocol design:

```latex
\section{Protocol Design}

\subsection{Overview}
Our protocol operates in three phases:
\begin{enumerate}
  \item \textbf{Handshake}: Connection establishment with key exchange
  \item \textbf{Data transfer}: Adaptive rate control based on ECN
  \item \textbf{Termination}: Graceful connection teardown
\end{enumerate}

\subsection{Formal Analysis}
We prove that our protocol achieves:
\begin{itemize}
  \item \textbf{Stability}: The system is stable under arbitrary traffic patterns
  \item \textbf{Fairness}: Max-min fair bandwidth allocation
  \item \textbf{Convergence}: Protocol converges within $O(\log n)$ rounds
\end{itemize}
```

## Figures and Tables

- Use vector formats (.pdf, .eps) for all figures
- Ensure grayscale legibility
- Include network topology diagrams
- Report error bars where applicable

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/throughput}
  \caption{Throughput comparison under varying link loss rates.
    Our protocol maintains 95\% throughput at 5\% loss rate,
    significantly outperforming TCP CUBIC (62\%) and BBR (78\%).}
  \label{fig:throughput}
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
- [ ] Simulation methodology fully described
- [ ] Figures legible in grayscale

## Camera-Ready Checklist

- [ ] Restore author names with IEEE author blocks
- [ ] Add acknowledgments
- [ ] Verify PDF compliance with IEEE Xplore
- [ ] Check figure resolution and quality
