# UIST Venue Guide

> Migrated from the legacy `ccf-conference-skills/uist/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `uist` |
| Venue family | HCI |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/UIST/acmart.cls` |
| Official URL | https://uist.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# UIST 2026 Conference Writing Skill

**CCF-A | HCI | Publisher: ACM**
**Conference:** https://uist.org
**Template:** `UIST/acmart.cls` (ACM acmart, sigchi format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigchi, review, anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigchi]{acmart}
\acmConference[UIST 2026]{UIST '26: Proceedings of the 2026 ACM Symposium...}
               {October 20--23, 2026}{Los Angeles, CA, USA}
\acmISBN{978-X-XXXX-XXXX-X/XX/XX}
\acmDOI{10.5555/XXXXXXX.XXXXXXX}
```

UIST uses the `sigchi` format option. For the abstract, include both CCS Concepts and author keywords.

### Required Packages

```latex
\usepackage[round]{natbib}     % Author-year citations
\usepackage{amsmath}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{balance}
\usepackage{cleveref}          % Consistent cross-references
```

### Abstract Metadata Blocks

UIST abstracts require CCS Concepts and keywords:

```latex
\begin{abstract}
  We present a novel interaction technique that enables...
  Results from a user study ($N=24$) show significant improvements
  in task completion time and subjective satisfaction.
\endabstract}

% CCS Concepts (generated at http://dl.acm.org/ccs.cfm)
\ccsdesc[500]{Human-centered computing~Interaction techniques}
\ccsdesc[300]{Human-centered computing~User interface design}
\ccsdesc[100]{Human-centered computing~User studies}

% Author keywords
\keywords{interaction techniques, user study, touch input, gesture recognition}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **10 pages** |
| References | No limit |
| Appendix / Supplementary | Not permitted |

UIST enforces a strict 10-page limit for the main body. References do not count toward the limit.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. No author names or affiliations in submission
2. Third-person self-citations: "Prior work showed..." not "we showed..."
3. Anonymize all URLs (GitHub, dataset links, personal pages)
4. Clear PDF metadata
5. Remove acknowledgments
6. Anonymize any videos or media files

## Camera-Ready Differences

After acceptance:

1. Remove `review` and `anonymous` options
2. Fill in `\acmConference`, `\acmISBN`, `\acmDOI`
3. Restore author names, affiliations, and contact information
4. Add appropriate `\setcopyright` mode
5. Enable page numbers with `\settopmatter{printfolios=true}`

## Section Organization

UIST papers follow a user interface research structure:

1. **Introduction** — Problem space, motivation, research questions, contributions (enumerate 3-5 contributions)
2. **Background & Related Work** — Prior HCI and UIST research, theoretical grounding
3. **Design & Approach** — The system, technique, or interaction modality being presented
4. **Implementation** — Technical details of the interface or system
5. **User Study / Evaluation** — Participants, procedure, measures, results
6. **Discussion** — Interpretation, implications for UI software and technology
7. **Conclusion & Future Work**
8. References

UIST values papers where the **contribution is clear**, the **design is innovative**, and **evidence supports the claims**.

## Contribution Statement

```latex
\section{Introduction}
Despite the widespread adoption of...
We address this gap by designing...
This paper makes the following contributions:
\begin{itemize}
  \item A novel gesture-based interaction technique that...
  \item Empirical evidence from a user study ($N=24$) showing
    40\% improvement in task completion time
  \item Design implications for future interaction systems
\end{itemize}
```

## User Study Methodology

UIST emphasizes empirical evaluation:

```latex
\section{User Study}

\subsection{Participants}
We recruited 24 participants (12 self-identified female,
12 male; $M_{age}=26.4$, $SD=4.8$) through university
mailing lists. Sample size was determined via power analysis.

\subsection{Apparatus}
The study was conducted on a Samsung Galaxy S23 running Android 14.
We used a Tobii Pro Nano eye tracker for gaze data.

\subsection{Procedure}
Participants performed three tasks in counterbalanced order.
Task completion time and error rate were recorded.

\subsection{Measures}
\begin{itemize}
  \item \textbf{Objective}: Task completion time, error rate
  \item \textbf{Subjective}: System Usability Scale (SUS), NASA-TLX
\end{itemize}
```

## IRB and Ethics

UIST requires ethical research practices:

```latex
\section{Ethics Statement}
This study was reviewed and approved by the Institutional
Review Board of [University Name] (protocol #XXXX-XXXX).
All participants provided informed consent and were
compensated \$20 for their time.
```

## CCS Concepts and Keywords

Generate CCS Concepts at http://dl.acm.org/ccs.cfm and include them as shown above. Keywords are also required.

## Figures and Tables

UIST has high standards for figure and interface presentation:

- Use high-quality vector figures (.pdf, .eps)
- Ensure grayscale legibility
- Include rich visual representations (screenshots, interface mockups, study setups)
- Number figures/tables sequentially
- Use `booktabs` for tables (no vertical rules)

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/interface}
  \caption{The main interface showing (a) the primary input area,
    (b) the feedback panel, and (c) the settings menu. Red arrows
    indicate the critical interaction point at step 3.}
  \label{fig:interface}
\end{figure}
```

## References (natbib)

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\citet{key}    % Author (Year)
\citep{key}    % (Author, Year)
```

All references must list **every author by full name**.

## Formatting Rules

- **Format:** ACM sigchi
- **Paper size:** US Letter
- **Body font:** 9pt minimum, Times New Roman
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in

## UIST Writing Conventions

- **Design innovation**: The interaction technique or system must be novel
- **Evidence-based**: Claims must be supported by user study data
- **Methodological transparency**: Enough detail to replicate the study
- **Contribution clarity**: Explicit contribution statement in the introduction
- **Visual quality**: UIST has very high standards for figure presentation
- **No appendix**: All essential content must fit within 10 pages

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
