# CHI Venue Guide

> Migrated from the legacy `ccf-conference-skills/chi/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-venue-format-guide`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `chi` |
| Venue family | HCI |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/CHI/acmart.cls` |
| Official URL | https://chi2026.acm.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# CHI 2026 Conference Writing Skill

**CCF-A | HCI | Publisher: ACM**
**Conference:** https://chi2026.acm.org
**Template:** `CHI/acmart.cls` (ACM acmart, sigchi format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigchi, review, anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigchi]{acmart}
\acmConference[CHI 2026]{CHI '26: Extended Abstracts of the 2026...}
               {April 26--May 1, 2026}{Yokohama, Japan}
\acmISBN{978-X-XXXX-XXXX-X/XX/XX}
\acmDOI{10.5555/XXXXXXX.XXXXXXX}
```

CHI uses the `sigchi` format option. For the abstract, include both CCS Concepts and author keywords as required metadata blocks.

### Required Packages

```latex
\usepackage[round]{natbib}     % Author-year citations
\usepackage{amsmath}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{balance}
\usepackage{soul}              % For highlighting (strikethrough, etc.)
\usepackage{cleveref}          % Consistent cross-references
```

### Abstract Metadata Blocks

CHI abstracts require CCS Concepts and keywords:

```latex
\begin{abstract}
  % Brief summary of contributions, findings, and implications
  We present a new interaction technique that enables...
  Results from a user study ($N=24$) show significant improvements
  in task completion time and subjective satisfaction.
\end{abstract}

% CCS Concepts (generated at http://dl.acm.org/ccs.cfm)
\ccsdesc[500]{Human-centered computing~Interaction design}
\ccsdesc[300]{Human-centered computing~User studies}
\ccsdesc[100]{Human-centered computing~Empirical studies in HCI}

% Author keywords
\keywords{interaction techniques, user study, mobile devices,
  touch input, gesture recognition}

% (CCS Concepts and keywords are placed before \maketitle)
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **10 pages** |
| References | No limit |
| Appendix / Supplementary | Not permitted |

CHI enforces a strict 10-page limit for the main body. References do not count toward the limit. **No appendix or supplementary materials** are permitted.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. No author names or affiliations in submission
2. Third-person self-citations: "Prior work showed..." not "we showed..."
3. Anonymize all URLs (GitHub, participant recruitment pages, personal pages)
4. Clear PDF metadata
5. Remove acknowledgments
6. Anonymize media files (videos) — remove identifying information

## Camera-Ready Differences

After acceptance:

1. Remove `review` and `anonymous` options
2. Fill in `\acmConference`, `\acmISBN`, `\acmDOI`
3. Restore author names, affiliations, and contact information
4. Add appropriate `\setcopyright` mode
5. Enable page numbers with `\settopmatter{printfolios=true}`

## Section Organization

CHI papers follow a user-centered research structure:

1. **Introduction** — Problem space, motivation, research questions, contributions (enumerate 3-5 contributions)
2. **Background & Related Work** — Prior HCI research, theoretical grounding, positioning
3. **Design & Approach** — The system, technique, or intervention being studied
4. **User Study / Research Methods** — Participants, procedure, measures, analysis plan
5. **Results** — Quantitative and/or qualitative findings
6. **Discussion** — Interpretation, implications for HCI, design guidelines
7. **Conclusion & Future Work**
8. References

CHI values papers where the **contribution is clear** and **evidence supports the claims**.

## Contribution Statement

CHI papers should explicitly state contributions in the introduction:

```latex
\section{Introduction}
Despite the widespread adoption of touch interfaces, ...
We address this gap by investigating ...
This paper makes the following contributions:
\begin{itemize}
  \item A novel gesture-based technique that ...
  \item Empirical evidence from a controlled study ($N=32$) showing
    that our technique reduces error rates by 40\%
  \item Design implications for ...
\end{itemize}
```

## User Study Methodology

User studies are central to CHI papers. Report methodology thoroughly:

```latex
\section{Research Methods}

\subsection{Participants}
We recruited 24 participants (12 self-identified as female,
12 as male; $M_{age}=28.4$, $SD=5.1$) through university
mailing lists. Sample size was determined via power analysis
($\alpha=0.05$, power=$0.80$, $d=0.6$). All participants
had normal or corrected-to-normal vision and were daily
smartphone users.

\subsection{Apparatus}
The study was conducted on a Google Pixel 7 running Android 13.
We used a Tobii Pro Nano eye tracker for gaze data.

\subsection{Procedure}
Participants performed three tasks: ...
The study took approximately 60 minutes. Task order was
counterbalanced using a Latin square.

\subsection{Measures}
\begin{itemize}
  \item \textbf{Objective}: Task completion time, error rate
  \item \textbf{Subjective}: System Usability Scale (SUS),
    NASA-TLX for workload
\end{itemize}

\subsection{Analysis}
We used repeated-measures ANOVA with post-hoc Bonferroni
corrections for objective measures, and Wilcoxon signed-rank
tests for subjective ratings. Effect sizes are reported
as partial $\eta^2$.
```

## IRB and Ethics

CHI requires ethical research practices:

```latex
\section{Ethics}
This study was reviewed and approved by the Institutional
Review Board of [University Name] (protocol #XXXX-XXXX).
All participants provided informed consent and were
compensated \$20 for their time.
```

## CCS Concepts and Keywords

Generate CCS Concepts at http://dl.acm.org/ccs.cfm and include them as shown above. Keywords are also required and appear after the CCS Concepts block.

## Figures and Tables

CHI emphasizes visual communication:

- Use high-quality vector figures (.pdf, .eps)
- Ensure grayscale legibility
- Include rich visual representations (screenshots, interface mockups, study setups)
- Number figures/tables sequentially

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/study-setup}
  \caption{(a) Eye-tracking setup with participant and display,
    (b) close-up of the stimulus showing the three target regions
    indicated by dashed outlines.}
  \label{fig:setup}
\end{figure}
```

For study stimuli and screenshots, include visual callouts:

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=\linewidth]{figs/interface}
  \caption{The main interface showing (a) the primary input area,
    (b) the feedback panel, and (c) the settings menu accessed
    via the hamburger icon. Red arrows indicate the critical
    interaction point at step 3.}
  \label{fig:interface}
\end{figure}
```

## References (natbib)

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\citet{norman2013}      % Norman (2013)
\citep{norman2013}      % (Norman 2013)
```

All references must list **every author by full name**.

## Formatting Rules

- **Format:** ACM sigchi (single-column for submission in some years, two-column camera-ready)
- **Paper size:** US Letter
- **Body font:** 9pt minimum, Times New Roman
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in

## CHI Writing Conventions

- **Evidence-based**: Claims must be supported by study data or other evidence
- **Methodological transparency**: Enough detail to replicate the study
- **Contribution clarity**: Explicit contribution statement in the introduction
- **Visual quality**: CHI has high standards for figure and interface presentation
- **Theoretical grounding**: Connect findings to relevant HCI theory
- **No appendix**: all essential content must fit within 10 pages

## Submission Checklist

- [ ] 10 pages or fewer (no appendix)
- [ ] `\documentclass[sigchi, review, anonymous]`
- [ ] CCS Concepts and keywords included in abstract
- [ ] All author identification removed
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] IRB/ethics statement included
- [ ] Methodology fully described (participants, procedure, measures)
- [ ] References list all authors
- [ ] High-quality, grayscale-legible figures
