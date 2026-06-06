# MobiSys Venue Guide

> Migrated from the legacy `ccf-conference-skills/mobisys/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-venue-format-guide`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `mobisys` |
| Venue family | Networks |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/MobiSys/acmart.cls` |
| Official URL | https://www.sigmobile.org/mobisys/2026 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# MobiSys 2026 Conference Writing Skill

**CCF-B | Networks | Publisher: ACM**
**Conference:** https://www.sigmobile.org/mobisys/2026
**Template:** `MobiSys/acmart.cls` (ACM acmart, sigconf format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigconf,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigconf]{acmart}
\acmConference[MobiSys 2026]{MobiSys '26: The 24th Annual International...}
               {June 28--July 1, 2026}{Minneapolis, USA}
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

MobiSys enforces a 12-page limit for the main body. References and appendix do not count.

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

MobiSys papers follow the mobile systems structure:

1. **Introduction** — Problem, motivation, contributions (enumerate contributions)
2. **Background & Motivation** — Why the problem matters, existing approaches
3. **System Design / Approach** — Core technical contribution
4. **Implementation** — Prototype details, hardware platform, software stack
5. **Evaluation** — Real-world experiments, user studies, comparison
6. **Related Work** — Positioning against prior art
7. **Conclusion** — Summary and future directions
8. References
9. Appendix (optional)

## Mobile Systems Conventions

MobiSys values systems that work on real devices with real users:

### System Overview

```latex
\section{System Design}

Our mobile system, called \textbf{BatteryMind}, extends
smartphone battery life through intelligent background
task scheduling:
\begin{itemize}
  \item \textbf{Challenge}: Background apps drain battery
    even when idle
  \item \textbf{Approach}: ML-based prediction of app
    usage patterns to defer background work
  \item \textbf{Result}: 28\% improvement in battery life
    with no user-perceptible delays
\end{itemize}

\subsection{Key Techniques}
\begin{enumerate}
  \item \textbf{Usage prediction}: LSTM model predicts
    app launch probability for next hour
  \item \textbf{Deferral scheduling}: Batch background
    work to align with charging periods
  \item \textbf{Energy budgeting}: Enforce per-app energy
    caps based on usage patterns
\end{enumerate}
```

### Mobile Platform Implementation

```latex
\subsection{Implementation}
We implement BatteryMind as:
\begin{itemize}
  \item \textbf{Platform}: Android 13 with custom system
    services
  \item \textbf{ML model}: TensorFlow Lite, 50KB quantized
    LSTM model
  \item \textbf{Overhead}: 0.3\% CPU, 2MB RAM
  \item \textbf{User study}: 50 participants over 4 weeks
\end{itemize}
```

## Evaluation

MobiSys emphasizes real-world evaluation with real users:

```latex
\section{Evaluation}

We evaluate BatteryMind through:
\begin{itemize}
  \item \textbf{User study}: 50 participants using BatteryMind
    for 4 weeks in daily life
  \item \textbf{A/B comparison}: 2-week baseline vs. 2-week
    BatteryMind
  \item \textbf{Ground truth}: Participant surveys and
    semi-structured interviews
\end{itemize}

\subsection{Results}
\begin{itemize}
  \item \textbf{Battery improvement}: 28\% average (range:
    12\% to 45\%)
  \item \textbf{User satisfaction}: 4.3/5.0 average rating
  \item \textbf{Perceived performance}: 89\% of users reported
    no noticeable slowdowns
\end{itemize}
```

## Figures and Tables

- Use vector formats (.pdf) for all figures
- Ensure grayscale legibility
- Include system architecture and UI screenshots
- Tables should have clear column headers and units

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/system-arch}
  \caption{System architecture of BatteryMind: (a) usage predictor
    component running as a background service, (b) deferral scheduler
    coordinating with Android's WorkManager, (c) energy budgeting
    module enforcing per-app policies. Total system overhead is
    less than 0.5\% of battery capacity.}
  \label{fig:system-arch}
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
