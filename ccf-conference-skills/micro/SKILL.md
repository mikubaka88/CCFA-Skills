---
name: micro
description: Writing and formatting guidance for MICRO (IEEE/ACM International Symposium on Microarchitecture) papers. Use when drafting, formatting, or submitting to MICRO 2026. Covers ACM acmart sigplan format, microarchitecture-specific writing conventions (architecture description, methodology, evaluation with simulation/hardware, area/performance/power tradeoffs), double-blind anonymity, page limits, and camera-ready preparation.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# MICRO 2026 Conference Writing Skill

**CCF-A | Architecture | Publisher: IEEE/ACM**
**Conference:** https://www.microarch.org/micro59
**Template:** `MICRO/main.tex` (ACM acmart, sigconf format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigconf, review, anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigconf]{acmart}
\acmConference[MICRO 2026]{59th IEEE/ACM International Symposium...}
               {October 31--November 4, 2026}{Athens, Greece}
\acmISBN{978-X-XXXX-XXXX-X/XX/XX}
\acmDOI{10.5555/XXXXXXX.XXXXXXX}
```

MICRO 2026 uses the `sigconf` format (not `sigplan`), based on the ACM acmart class.

### Required Packages

```latex
\usepackage[round]{natbib}     % Author-year citations
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{listings}
\lstset{basicstyle=\small\ttfamily}
\usepackage{booktabs}          % Professional tables
\usepackage{graphicx}
\usepackage{balance}           % Balance columns on last page
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **11 pages** |
| References | No limit |
| Appendix | **Not permitted** |

MICRO enforces a strict 11-page limit for the main body. **No appendix is allowed.** References are unlimited and do not count toward the limit.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. No author names or affiliations anywhere in submission
2. Third-person self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs (GitHub, personal pages, institutional pages)
4. Clear PDF metadata
5. Remove acknowledgments

## Camera-Ready Differences

After acceptance:

1. Remove `review` and `anonymous` options from class
2. Fill in `\acmConference` with full conference details
3. Add `\acmISBN` and `\acmDOI`
4. Restore author names and affiliations
5. Enable page numbers with `\settopmatter{printfolios=true}`

## Section Organization

MICRO papers follow a well-established architecture paper structure:

1. **Introduction** — Problem, microarchitectural challenge, contributions (enumerate 3-5 key contributions)
2. **Background & Motivation** — Relevant microarchitectural context, why existing approaches fall short
3. **Overview / High-Level Design** — Big-picture description before diving into details
4. **Detailed Design** — Microarchitectural specifics, data structures, control logic
5. **Hardware Implementation** — Area, timing, synthesis results, complexity
6. **Evaluation** — Simulation methodology, comparison with baselines, sensitivity analysis
7. **Related Work** — Positioning against prior microarchitectural work
8. **Conclusion**
9. References

## Microarchitecture Description

MICRO papers must describe the architecture in sufficient detail:

```latex
% Use clear diagrams and pseudo-code for hardware structures
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/overview}
  \caption{Block diagram of the proposed memory hierarchy.
    The shaded region indicates the new L1.5 cache layer.}
  \label{fig:overview}
\end{figure}

% Document key structures
\begin{table}[t]
  \caption{Hardware parameters for the proposed design.}
  \label{tab:params}
  \centering
  \begin{tabular}{lr}
    \toprule
    Parameter & Value \\
    \midrule
    L1.5 cache size & 256 KB \\
    Associativity & 8-way \\
    Hit latency & 2 cycles \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Evaluation Methodology

MICRO evaluation is rigorous and simulation/hardware-focused:

- **Simulation framework**: Specify the simulator (e.g., gem5, Sniper, ChampSim) and configuration
- **Workloads**: Report benchmark suite, input sets, and why they were chosen
- **Baselines**: Compare against clearly stated prior designs (not strawmen)
- **Metrics**: Performance (IPC, throughput), area, power/energy, latency
- **Sensitivity analysis**: Vary key parameters to show robustness

```latex
\begin{table*}[t]
  \caption{Performance comparison (normalized IPC, higher is better).
    Baseline is a 4-wide out-of-order processor.}
  \label{tab:perf}
  \centering
  \begin{tabular}{lrrrr}
    \toprule
    \multirow{2}{3em}{Benchmark} &
      \multicolumn{2}{c}{Baseline} &
      \multicolumn{2}{c}{Our design} \\
    \cmidrule{2-3} \cmidrule{4-5}
    & IPC & Energy & IPC & Energy \\
    \midrule
    bwaves & 1.00 & 1.00 & \textbf{1.23} & 1.05 \\
    cactusADM & 1.00 & 1.00 & 1.15 & \textbf{0.92} \\
    \bottomrule
  \end{tabular}
\end{table*}
```

## Area, Power, and Timing

MICRO papers often include synthesis results:

```latex
% Synthesis results table
\begin{table}[t]
  \caption{Synthesis results in TSMC 28nm at 1 GHz.}
  \label{tab:synth}
  \begin{tabular}{lrr}
    \toprule
    Component & Area (mm$^2$) & Power (mW) \\
    \midrule
    L1.5 Cache & 0.12 & 45 \\
    Directory & 0.03 & 12 \\
    \bottomrule
  \end{tabular}
\end{table}
```

## References (natbib)

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\citet{smith2025}      % Smith et al. (2025)
\citep{smith2025}      % (Smith et al. 2025)
```

All references must list **every author by full name**.

## Formatting Rules

- **Format:** ACM sigconf (two-column, single-spaced)
- **Paper size:** US Letter
- **Body font:** 9pt minimum, Times New Roman
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in

## MICRO Writing Conventions

- **Architecture clarity**: Provide enough detail that another architect could implement the design
- **Tradeoff discussion**: Explicitly discuss area/performance/energy tradeoffs
- **Fair baselines**: Compare against the strongest existing designs, not strawmen
- **Methodology transparency**: Describe simulation setup in sufficient detail for reproducibility
- **No appendix**: all content must fit in 11 pages; no supplementary materials

## Submission Checklist

- [ ] 11 pages or fewer (no appendix)
- [ ] `\documentclass[sigconf, review, anonymous]`
- [ ] All author identification removed
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] Clear methodology description
- [ ] Comparison with meaningful baselines
- [ ] References list all authors
- [ ] Figures legible in grayscale
