# RTSS Venue Guide

> Migrated from the legacy `ccf-conference-skills/rtss/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-venue-format-guide`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `rtss` |
| Venue family | Real-Time |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/RTSS/IEEEtran.cls` |
| Official URL | https://2026.rtss.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# RTSS 2026 Conference Writing Skill

**CCF-A | Real-Time | Publisher: IEEE**
**Conference:** https://2026.rtss.org
**Template:** `RTSS/IEEEtran.cls` (IEEEtran, conference format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[conference]{IEEEtran}

% Author block for anonymous submission:
\author{
  \IEEEauthorblockN{Anonymous Author}
  \IEEEauthorblockA{
    \IEEEauthorrefmark{1}Anonymous Institution\\
    anonymous@institution.edu}
}

% === CAMERA-READY MODE ===
\documentclass[conference]{IEEEtran}
% Restore full author/affiliation information
% Add conference-specific copyright notice
```

### Required Packages

```latex
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{cite}
\usepackage{balance}
\usepackage{cleveref}
\usepackage{algorithm}
\usepackage{algorithmic}
\usepackage{url}
\usepackage{xcolor}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **10 pages** |
| References | No limit |
| Appendix | Permitted |

RTSS typically enforces a 10-page limit for the main body. References do not count toward the limit. Always verify the current CFP for exact limits.

## Anonymity Requirements

RTSS uses double-blind review:

1. Remove or replace author names/affiliations in the submission
2. Use "Anonymous" as author during submission
3. Third-person self-citations: "Smith et al. showed..." not "we showed..."
4. Anonymize all URLs, GitHub links, personal pages
5. Clear PDF metadata
6. Remove acknowledgments

## Camera-Ready Differences

After acceptance:

1. Restore all author names and affiliations
2. Add the conference-specific copyright notice provided by IEEE
3. Ensure Xplore-compatible PDF (CMYK colors, embedded fonts)
4. Submit via IEEE PDF eXpress

## Section Organization

RTSS papers follow a real-time systems paper structure:

1. **Abstract** — Problem, solution, timing guarantees summary
2. **Introduction** — Real-time problem, system model, contributions (enumerate explicitly)
3. **System Model & Assumptions** — Task model, platform, timing parameters
4. **Problem Statement** — Formal problem definition with notation
5. **Proposed Approach** — Scheduling algorithm, resource allocation, etc.
6. **Theoretical Analysis** — Schedulability analysis, WCET bounds, proofs
7. **Implementation** — System details, prototype
8. **Evaluation** — Simulation, implementation, experimental results
9. **Related Work**
10. **Conclusion**
11. References
12. Appendix (optional)

## Real-Time Formalism

RTSS papers require rigorous timing and schedulability analysis:

```latex
\section{System Model}
We consider a real-time task set $\tau$ executed on a uniprocessor
under preemptive fixed-priority scheduling.

\subsection{Task Model}
Each task $\tau_i$ is characterized by:
\begin{itemize}
  \item Period $T_i$: the minimum time between successive job releases
  \item Execution time $C_i$: the worst-case execution time (WCET)
  \item Relative deadline $D_i$: typically $D_i \leq T_i$
  \item Priority $p_i$: higher values indicate higher priorities
\end{itemize}

A task set $\tau$ is said to be \emph{feasible} if there exists a
schedule such that all tasks meet their deadlines under all possible
job releases and execution times bounded by their WCETs.
```

## Schedulability Analysis

Core to RTSS papers is the schedulability analysis:

```latex
\section{Schedulability Analysis}

\begin{main*}[Sufficient Schedulability Test]
  \label[main*]{thm:schedulability}
  A task set $\tau$ is schedulable under FPPS if for all tasks $\tau_i$:
  \begin{equation}
    \label{eq:response-time}
    R_i = C_i + \sum_{\forall \tau_j \in hp(i)} \left\lceil
      \frac{R_i}{T_j} \right\rceil C_j \leq D_i
  \end{equation}
  where $hp(i)$ denotes the set of tasks with higher priority than $\tau_i$,
  and $R_i$ is the worst-case response time of $\tau_i$.
\end{main*}

\begin{Proof}
  The proof proceeds by computing the worst-case response time
  iteratively using the recurrence relation of \autoref{eq:response-time}.
  Since $R_i$ is monotonically non-decreasing and bounded by $D_i$,
  the algorithm terminates with either $R_i \leq D_i$ for all tasks
  (proving schedulability) or $R_i > D_i$ for some task (proving infeasibility).
\end{Proof}
```

## Worst-Case Execution Time (WCET)

```latex
\section{WCET Analysis}

We compute WCET bounds using abstract interpretation~\citep{absint}.
Our analysis operates on the control flow graph (CFG) of the program:

\begin{itemize}
  \item \textbf{Flow facts}: Loop bounds derived from induction variable
    analysis; infeasible paths eliminated using constraint solving
  \item \textbf{Cache analysis}: Abstract interpretation of the cache
    state using the must/may analysis framework
  \item \textbf{Pipeline analysis}: Implicit path enumeration with
    pipeline hazard modeling
\end{itemize}

The final WCET estimate is the maximum over all paths:
\begin{equation}
  \label{eq:wcet}
  C_i = \max_{p \in \text{paths}(cfg)} \left(
    \sum_{b \in p} C_b^{cache} + C_b^{pipeline} \right)
\end{equation}
```

## Algorithm Formatting

```latex
\begin{algorithm}[t]
\caption{Rate-Monotonic Scheduling with Server}
\label[algorithm]{alg:rms-server}
\begin{algorithmic}[1]
\REQUIRE Task set $\tau = \{\tau_1, \dots, \tau_n\}$, server budget $Q_s$, period $T_s$
\ENSURE Feasibility check and schedule
\STATE Sort tasks by period (shorter periods = higher priority)
\STATE $t \gets 0$, $Q \gets Q_s$, $T \gets 0$
\WHILE{$\text{all tasks pending}$}
  \STATE $R \gets$ current ready queue (sorted by priority)
  \IF{$R \neq \emptyset$ and $Q > 0$}
    \STATE Execute highest-priority task $\tau_i$ for $\delta = \min(Q, C_i - C_i^{exec})$
    \STATE $C_i^{exec} \gets C_i^{exec} + \delta$, $Q \gets Q - \delta$
  \ELSIF{$Q = 0$}
    \STATE Execute background tasks
  \ENDIF
  \IF{$T = T_s$}
    \STATE $Q \gets Q_s$, $T \gets 0$
  \ENDIF
\ENDWHILE
\end{algorithmic}
\end{algorithm}
```

## Experimental Evaluation

RTSS evaluation combines analysis with empirical results:

```latex
\section{Evaluation}
We evaluate our approach using both analysis-based bounds and
implementation on a real-time testbed.

\subsection{Simulation Setup}
We simulate 10,000 randomly generated task sets with:
\begin{itemize}
  \item Number of tasks: 5--20
  \item Total utilization: 50\%--95\% (uniform distribution)
  \item Periods: drawn from log-uniform distribution in [10ms, 1000ms]
  \item Deadline type: constrained ($D_i = T_i$)
\end{itemize}

\subsection{Results}
\autoref{tab:acceptance} shows the acceptance ratio (fraction of
feasible task sets correctly identified as feasible) for different
utilization levels. Our test achieves 94.3\% acceptance ratio at
80\% utilization, compared to 87.2\% for the baseline test.
```

## Figures and Tables

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/schedulability}
  \caption{Acceptance ratio vs. total utilization for different
    schedulability tests. Our approach (solid red) consistently
    outperforms the baseline (dashed blue) across all utilization levels.}
  \label{fig:schedulability}
\end{figure}

\begin{table}[t]
  \caption{Schedulability test comparison on synthetic task sets.
    AR = acceptance ratio, CT = computation time (ms).}
  \label{tab:acceptance}
  \begin{tabular}{lcccc}
    \toprule
    \multirow{2}{*}{Utilization} & \multicolumn{2}{c}{Baseline} & \multicolumn{2}{c}{Ours} \\
    \cmidrule(lr){2-3}\cmidrule(lr){4-5}
    & AR & CT & AR & CT \\
    \midrule
    50\% & 0.98 & 0.3 & 0.99 & 0.4 \\
    70\% & 0.93 & 0.5 & 0.97 & 0.7 \\
    80\% & 0.87 & 0.8 & 0.94 & 1.1 \\
    90\% & 0.72 & 1.2 & 0.85 & 1.8 \\
    \bottomrule
  \end{tabular}
\end{table}
```

## References

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}

% Numeric citations
\cite{liu2000real}
```

## Formatting Rules

- **Format:** IEEE conference (single-column)
- **Paper size:** US Letter
- **Body font:** 10pt minimum
- **Margins:** 1" all sides
- **Xplore-compatible PDF**: CMYK colors, embedded fonts

## Submission Checklist

- [ ] 10 pages or fewer (main body)
- [ ] Author information removed/anonymized
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] PDF metadata cleared
- [ ] Formal schedulability analysis included
- [ ] WCET analysis performed
- [ ] Both theoretical and empirical evaluation
- [ ] Grayscale-legible figures

## Camera-Ready Checklist

- [ ] Restore author information
- [ ] Add IEEE copyright notice
- [ ] Generate Xplore-compatible PDF
- [ ] Use CMYK colors for figures
- [ ] Embed all fonts
- [ ] Submit via IEEE PDF eXpress
