---
name: dac
description: Writing and formatting guidance for DAC (Design Automation Conference) papers. Use when drafting, formatting, or submitting to DAC 2026. Covers ACM acmart sigconf format with anonymous review mode, EDA/architecture paper conventions (design automation, circuit optimization, CAD tool methodology), 12-page limit, and camera-ready preparation.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# DAC 2026 Conference Writing Skill

**CCF-A | Architecture | Publisher: ACM**
**Conference:** https://www.dac.com
**Template:** `DAC/acmart.cls` (ACM acmart, sigconf format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigconf,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigconf]{acmart}
\acmConference[DAC 2026]{DAC '26: 63rd ACM/IEEE Design Automation...}
               {July 13--17, 2026}{San Francisco, CA, USA}
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
| Main paper (submission) | **12 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

DAC enforces a 12-page limit for the main body. References and appendix do not count.

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

DAC papers follow the EDA/architecture structure:

1. **Introduction** — Problem, motivation, contributions (enumerate contributions)
2. **Background & Motivation** — EDA context, existing tools and limitations
3. **Proposed Approach** — Core contribution with formal treatment
4. **Implementation / Algorithm** — CAD tool details, optimization techniques
5. **Experimental Results** — Evaluation on benchmark circuits, comparison
6. **Related Work** — Positioning against prior art
7. **Conclusion** — Summary and future directions
8. References
9. Appendix (optional)

## EDA Conventions

DAC focuses on design automation and CAD tools:

### Problem Formulation

```latex
\section{Problem Formulation}

Given a circuit netlist $C$ with $n$ gates and target delay
constraint $T$, we aim to find an optimal gate sizing solution
that minimizes power consumption while satisfying the delay
constraint.

Formally, we solve:
\begin{minimize}
  \sum_{i=1}^{n} P_i(w_i)
\end{minimize}
\begin{subequations}
\begin{assign}
  w_i \in [w_{min}, w_{max}] & \forall i \in \{1, \dots, n\} \\
  d(C, w) \leq T & \text{(timing constraint)}
\end{assign}
\end{subequations}
where $P_i(w_i)$ is the power of gate $i$ with size $w_i$
and $d(C, w)$ is the critical path delay.
```

### Algorithm Design

```latex
\section{Proposed Algorithm}

Our algorithm, called \textbf{GateSense}, uses a gradient-based
optimization approach:

\begin{enumerate}
  \item \textbf{Initialization}: Start with minimum-sized gates
  \item \textbf{Sensitivity computation}: Calculate power-delay
    sensitivity for each gate
  \item \textbf{Greedy upsizing}: Iteratively upsize the gate
    with highest sensitivity until timing constraint is met
  \item \textbf{Local refinement}: Apply simulated annealing
    for fine-grained optimization
\end{enumerate}
```

## Evaluation

```latex
\section{Experimental Results}

We evaluate GateSense on ISCAS-85 and ITC-99 benchmark circuits:
\begin{itemize}
  \item \textbf{Implementation}: Python + C++ mixed implementation
  \item \textbf{Baselines}: Commercial EDA tool (baseline), prior
    work (GateSizer)
  \item \textbf{Metrics}: Power reduction, runtime, timing slack
\end{itemize}

Results on 10 largest ITC-99 circuits:
\begin{itemize}
  \item \textbf{Power}: 18.3\% average reduction vs. baseline
  \item \textbf{Runtime}: 2.1$\times$ faster than GateSizer
  \item \textbf{Quality}: Within 2\% of commercial tool
\end{itemize}
```

## Figures and Tables

- Use vector formats (.pdf) for all figures
- Ensure grayscale legibility
- Include circuit diagrams and optimization landscapes
- Tables should have clear column headers and units

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/algorithm}
  \caption{Algorithm flow: (a) sensitivity analysis phase,
    (b) greedy upsizing phase, (c) simulated annealing
    refinement. Our approach combines the speed of greedy
    methods with the quality of stochastic optimization.}
  \label{fig:algorithm}
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

- [ ] 12 pages or fewer (main body)
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
