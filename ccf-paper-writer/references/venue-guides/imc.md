# IMC Venue Guide

> Migrated from the legacy `ccf-conference-skills/imc/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-venue-format-guide`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `imc` |
| Venue family | Networks |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/IMC/usenix-2020-09.sty` |
| Official URL | https://www.imc2026.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# IMC 2026 Conference Writing Skill

**CCF-B | Networks | Publisher: ACM/USENIX**
**Conference:** https://www.imc2026.org
**Template:** `IMC/usenix-2020-09.sty` (or `usenix2019_v3.sty`)

## Document Setup

### Preamble Structure

```latex
\documentclass[letterpaper,twocolumn,10pt]{article}
\usepackage{usenix-2020-09}
% OR: \usepackage{usenix2019_v3}

% Optional packages
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{cite}
\usepackage{hyperref}
```

### Required Packages

```latex
\usepackage{usenix-2020-09}  % or usenix2019_v3
\usepackage{cite}             % order multiple entries in \cite{...}
\usepackage{url}             % allow \url in bibtex for clickable links
\usepackage{xcolor}           % color definitions
\usepackage[]{hyperref}      % clickable refs within pdf
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **14 pages** |
| References | No limit |
| Appendix | Permitted |

IMC enforces a 14-page limit for the main body. References and appendix do not count.

## Anonymity Requirements

IMC uses double-blind review:

1. No author names anywhere in the submission
2. Use third person for self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs (GitHub repos, institutional pages)
4. Clear PDF metadata
5. Do not include acknowledgments in submission

## Camera-Ready Differences

After acceptance:

1. Restore all author names and affiliations
2. Add acknowledgments if desired
3. Verify figure quality and resolution
4. USENIX provides page numbers for camera-ready

## Section Organization

IMC papers follow the measurement study structure:

1. **Introduction** — Measurement question, motivation, contributions (enumerate findings)
2. **Background & Methodology** — Measurement context, data collection approach
3. **Data Collection** — Measurement infrastructure, dataset description
4. **Analysis / Findings** — Key measurement results
5. **Discussion** — Implications, limitations, open questions
6. **Related Work** — Prior measurement studies
7. **Conclusion** — Summary and future directions
8. References
9. Appendix (optional)

## Measurement Study Conventions

IMC is a premier venue for Internet measurement research:

### Measurement Methodology

```latex
\section{Measurement Methodology}

We measure DNS resolver behavior using a distributed
measurement infrastructure:
\begin{itemize}
  \item \textbf{Platform}: 500 vantage points across
    80 countries
  \item \textbf{Duration}: 3 months of continuous measurement
  \item \textbf{Method}: Active probing of top 10,000 domains
  \item \textbf{Ethics}: Approved by our IRB, no user data collected
\end{itemize}

\subsection{Measurement Traces}
We collect:
\begin{itemize}
  \item DNS query-response pairs (anonymized)
  \item RTT measurements from each vantage point
  \item Resolver IP addresses (city-level geolocation only)
\end{itemize}
```

### Data Analysis

```latex
\section{Measurement Results}

\subsection{Key Finding 1: CDN Concentration}
We find that 65\% of DNS resolution goes through just
5 resolver operators:
\begin{itemize}
  \item Google (32.1\%)
  \item Cloudflare (18.4\%)
  \item Quad9 (7.8\%)
  \item OpenDNS (4.3\%)
  \item CleanBrowsing (2.8\%)
\end{itemize}
This concentration has implications for DNS security
and privacy.
```

## Figures and Tables

- Use vector formats (.pdf) for all figures
- Ensure grayscale legibility
- Include measurement topology and data distribution plots
- Tables should have clear column headers and units

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/vantage-points}
  \caption{Geographic distribution of our 500 measurement
    vantage points. Points are sized by measurement volume.
    We achieve coverage in 80 countries with at least
    3 vantage points per country for robustness.}
  \label{fig:vantage}
\end{figure}
```

## References

```latex
\bibliographystyle{plain}
\bibliography{references}

% Citations:
~\cite{smith2023}        % [1]
```

Use `plain` bibstyle with numerical citations.

## Formatting Rules

- **Format:** USENIX two-column, 10pt body
- **Paper size:** US Letter
- **Margins:** 0.75" sides, 1" top/bottom
- **Text width:** 7"
- **Column gap:** 0.33"
- **Font:** Times New Roman (mathptmx)

## Submission Checklist

- [ ] 14 pages or fewer (main body)
- [ ] All author identification removed
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] PDF metadata cleared
- [ ] References properly formatted
- [ ] Figures legible in grayscale

## Camera-Ready Checklist

- [ ] Restore author names and affiliations
- [ ] Verify figure quality (high resolution)
- [ ] Add acknowledgments
- [ ] Ensure no forbidden packages
