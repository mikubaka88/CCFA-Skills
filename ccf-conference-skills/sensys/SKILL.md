---
name: sensys
description: Writing and formatting guidance for SenSys (ACM Conference on Embedded Networked Sensor Systems) papers. Use when drafting, formatting, or submitting to SenSys 2026. Covers ACM acmart sigconf format with anonymous review mode, sensor systems paper conventions (real deployments, energy efficiency, distributed sensing), 12-page limit, and camera-ready preparation.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# SenSys 2026 Conference Writing Skill

**CCF-B | Networks | Publisher: ACM**
**Conference:** https://www.sigmobile.org/sensys/2026
**Template:** `SenSys/acmart.cls` (ACM acmart, sigconf format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigconf,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigconf]{acmart}
\acmConference[SenSys 2026]{SenSys '26: Conference on Embedded...}
               {November 4--6, 2026}{Tokyo, Japan}
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

SenSys enforces a 12-page limit for the main body. References and appendix do not count.

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

SenSys papers follow the sensor systems structure:

1. **Introduction** — Problem, motivation, contributions (enumerate contributions)
2. **Background & Motivation** — Why the problem matters, existing approaches
3. **System Design / Approach** — Core technical contribution
4. **Implementation** — Prototype details, hardware platform, software stack
5. **Evaluation** — Real deployment results, comparison, sensitivity analysis
6. **Related Work** — Positioning against prior art
7. **Conclusion** — Summary and future directions
8. References
9. Appendix (optional)

## Sensor Systems Conventions

SenSys values real-world sensor deployments:

### System Overview

```latex
\section{System Design}

Our sensor system, called \textbf{ForestWatch}, enables
large-scale environmental monitoring:
\begin{itemize}
  \item \textbf{Challenge}: Battery-powered sensors must last
    years in remote forests
  \item \textbf{Approach}: Duty cycling with event-triggered
    wake-up radios
  \item \textbf{Result}: 3-year battery life with 10-minute
    sampling rate
\end{itemize}

\subsection{Hardware Platform}
We build ForestWatch on:
\begin{itemize}
  \item \textbf{MCU}: ARM Cortex-M4 at 48MHz
  \item \textbf{Radio}: Sub-GHz LoRa for long-range communication
  \item \textbf{Sensors}: Temperature, humidity, light, soil moisture
  \item \textbf{Power}: 2x AA batteries (10,000 mAh total)
\end{itemize}
```

### Energy Analysis

Energy efficiency is critical for SenSys:

```latex
\subsection{Energy Consumption}
Our power profiling shows:
\begin{itemize}
  \item \textbf{Sleep}: 3 $\mu$A (MCU in deep sleep)
  \item \textbf{Sense}: 12 mA for 50ms per sample
  \item \textbf{Transmit}: 45 mA for 200ms per transmission
\end{itemize}
Average power consumption: 8.3 $\mu$W, yielding
3.8 years of operation on 2x AA batteries.
```

## Evaluation

SenSys emphasizes real-world deployment:

```latex
\section{Evaluation}

We evaluate ForestWatch through:
\begin{itemize}
  \item \textbf{Long-term deployment}: 15 nodes over 6 months
    in a 10km$^2$ forest area
  \item \textbf{Controlled experiments}: 30 nodes in laboratory
    with ground truth sensors
  \item \textbf{Comparison}: Against existing sensor platforms
    (TelosB, MicaZ)
\end{itemize}

\subsection{Results}
\begin{itemize}
  \item \textbf{Data collection}: 98.2\% delivery rate
    across all nodes
  \item \textbf{Accuracy}: Temperature within 0.3$^\circ$C of
    reference weather station
  \item \textbf{Lifetime}: All nodes operational at 6-month
    mark (projected 3.8 years)
\end{itemize}
```

## Figures and Tables

- Use vector formats (.pdf) for all figures
- Ensure grayscale legibility
- Include hardware diagrams and deployment photos
- Tables should have clear column headers and units

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/node-arch}
  \caption{ForestWatch node architecture: (a) PCB layout showing
    MCU, radio, and sensor interfaces, (b) deployed sensor node
    in forest environment. The node measures 5cm x 3cm and
    weighs 45g including batteries.}
  \label{fig:node-arch}
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
