# MobiCom Venue Guide

> Migrated from the legacy `ccf-conference-skills/mobicom/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `mobicom` |
| Venue family | Networks |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/MobiCom/acmart.cls` |
| Official URL | https://www.sigmobile.org/mobicom/2026 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# MobiCom 2026 Conference Writing Skill

**CCF-A | Networks | Publisher: ACM**
**Conference:** https://www.sigmobile.org/mobicom/2026
**Template:** `MobiCom/acmart.cls` (ACM acmart, sigconf format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigconf,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigconf]{acmart}
\acmConference[MobiCom 2026]{MobiCom '26: The 32nd Annual International...}
               {October 13--17, 2026}{New York City, USA}
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

MobiCom enforces a 12-page limit for the main body. References and appendix do not count.

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

MobiCom papers follow the mobile systems structure:

1. **Introduction** — Problem, motivation, contributions (enumerate contributions)
2. **Background & Motivation** — Why the problem matters, existing approaches
3. **System Design / Approach** — Core technical contribution
4. **Implementation** — Prototype details, hardware/software platform
5. **Evaluation** — Real-world experiments, measurement studies, comparison
6. **Related Work** — Positioning against prior art
7. **Conclusion** — Summary and future directions
8. References
9. Appendix (optional)

## Mobile/Wireless Conventions

MobiCom values systems that work in the real world:

### System Overview

```latex
\section{System Design}

Our system, called \textbf{WiFiSense}, enables fine-grained
indoor localization using commodity WiFi hardware:
\begin{itemize}
  \item \textbf{Challenge}: GPS does not work indoors
  \item \textbf{Approach}: Channel state information (CSI)
    analysis for fingerprinting
  \item \textbf{Result}: Sub-meter accuracy with zero
    infrastructure changes
\end{itemize}

\subsection{Design Overview}
The system consists of three components:
\begin{enumerate}
  \item \textbf{CSI Extractor}: Modifies firmware to
    extract per-subcarrier CSI at 1 kHz
  \item \textbf{Fingerprint Engine}: ML-based localization
    using CSI patterns
  \item \textbf{Position Estimator}: Kalman filter for
    smooth tracking
\end{enumerate}
```

### Hardware Platform

```latex
\subsection{Implementation Platform}
We implement WiFiSense on:
\begin{itemize}
  \item \textbf{Hardware}: Intel 5300 WiFi NIC with modified
    firmware
  \item \textbf{Software}: Linux 5.15, custom CSI collection daemon
  \item \textbf{Evaluation sites}: 3 office buildings, 2 homes
  \item \textbf{Participants}: 15 volunteers with informed consent
\end{itemize}
```

## Evaluation

MobiCom emphasizes real-world evaluation:

```latex
\section{Evaluation}

We evaluate WiFiSense through:
\begin{itemize}
  \item \textbf{Localization accuracy}: 95th percentile error
    of 0.8m in office environments
  \item \textbf{Power consumption}: 12mW additional draw on
    commodity hardware
  \item \textbf{User study}: 15 participants over 2 weeks
    of daily use
\end{itemize}
```

## Figures and Tables

- Use vector formats (.pdf) for all figures
- Ensure grayscale legibility
- Include system diagrams and hardware photos
- Tables should have clear column headers and units

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/system-arch}
  \caption{System architecture: (a) CSI extraction from WiFi NIC,
    (b) fingerprint database building phase, (c) online localization
    phase using live CSI. The entire system runs on commodity
    hardware without any infrastructure modifications.}
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
