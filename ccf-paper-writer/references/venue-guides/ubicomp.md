# UbiComp Venue Guide

> Migrated from the legacy `ccf-conference-skills/ubicomp/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-venue-format-guide`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `ubicomp` |
| Venue family | Pervasive / HCI |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/UbiComp/acmart.cls` |
| Official URL | https://ubicomp.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# UbiComp 2026 Conference Writing Skill

**CCF-A | Pervasive / HCI | Publisher: ACM**
**Conference:** https://ubicomp.org
**Template:** `UbiComp/acmart.cls` (ACM acmart, sigchi format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigchi, review, anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigchi]{acmart}
\acmConference[UbiComp 2026]{UbiComp '26: Proceedings of the 2026 ACM International...}
               {September 13--17, 2026}{Seattle, WA, USA}
\acmISBN{978-X-XXXX-XXXX-X/XX/XX}
\acmDOI{10.5555/XXXXXXX.XXXXXXX}
```

UbiComp uses the `sigchi` format option. For the abstract, include both CCS Concepts and author keywords.

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

UbiComp abstracts require CCS Concepts and keywords:

```latex
\begin{abstract}
  We present a pervasive computing system that...
  Results from a deployment study ($N=48$) show...
\end{abstract}

% CCS Concepts (generated at http://dl.acm.org/ccs.cfm)
\ccsdesc[500]{Human-centered computing~Ubiquitous computing}
\ccsdesc[300]{Human-centered computing~Mobile computing}
\ccsdesc[100]{Computer systems organization~Sensor networks}

% Author keywords
\keywords{ubicomp, pervasive computing, mobile, sensors, context-awareness}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **10 pages** |
| References | No limit |
| Appendix / Supplementary | Not permitted |

UbiComp enforces a strict 10-page limit for the main body. References do not count toward the limit.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. No author names or affiliations in submission
2. Third-person self-citations: "Prior work showed..." not "we showed..."
3. Anonymize all URLs (GitHub, dataset links, personal pages)
4. Clear PDF metadata
5. Remove acknowledgments
6. Anonymize any deployment location or user-identifying information

## Camera-Ready Differences

After acceptance:

1. Remove `review` and `anonymous` options
2. Fill in `\acmConference`, `\acmISBN`, `\acmDOI`
3. Restore author names, affiliations, and contact information
4. Add appropriate `\setcopyright` mode
5. Enable page numbers with `\settopmatter{printfolios=true}`

## Section Organization

UbiComp papers follow a pervasive computing research structure:

1. **Introduction** — Problem space, motivation, research questions, contributions (enumerate 3-5 contributions)
2. **Background & Related Work** — Prior pervasive/ubicomp research, theoretical grounding
3. **System Design / Approach** — The pervasive computing system, sensor network, or interaction modality
4. **Implementation** — Technical details, platform, algorithms
5. **Evaluation** — Deployment study, user study, or technical evaluation
6. **Discussion** — Implications for pervasive computing, limitations, future work
7. **Conclusion**
8. References

UbiComp values papers where the **contribution is clear**, the **system is substantively implemented**, and **evidence supports the claims**.

## Contribution Statement

```latex
\section{Introduction}
Despite the growing interest in...
We address this gap by designing...
This paper makes the following contributions:
\begin{itemize}
  \item A novel pervasive sensing system that...
  \item A deployment study with 48 participants over 3 months...
  \item Design implications for context-aware applications in...
\end{itemize}
```

## UbiComp-Specific Methodology

UbiComp covers systems research, deployment studies, and user studies:

```latex
\section{System Design}

\subsection{Architecture Overview}
Our system consists of three components:...

\subsection{Sensors and Data Collection}
We use smartphone sensors (accelerometer, GPS, Wi-Fi)...

\section{Evaluation}

\subsection{Deployment Study}
We deployed our system with 48 participants...
```

## IRB and Ethics

UbiComp requires ethical research practices for studies involving human subjects:

```latex
\section{Ethics Statement}
This study was reviewed and approved by the Institutional
Review Board of [University Name] (protocol #XXXX-XXXX).
All participants provided informed consent and were
compensated \$15 per session.
```

## CCS Concepts and Keywords

Generate CCS Concepts at http://dl.acm.org/ccs.cfm and include them as shown above. Keywords are also required.

## Figures and Tables

UbiComp emphasizes visual communication of system architecture and sensor data:

- Use high-quality vector figures (.pdf, .eps)
- Ensure grayscale legibility
- Include system diagrams, deployment maps, sensor placement visuals
- Number figures/tables sequentially
- Use `booktabs` for tables (no vertical rules)

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/system-arch}
  \caption{System architecture showing (a) edge device,
    (b) cloud backend, and (c) mobile client components.}
  \label{fig:system}
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

## UbiComp Writing Conventions

- **System substantiation**: The system must be real, implemented, and evaluated
- **Evidence-based**: Claims must be supported by data or evaluation
- **Methodological transparency**: Enough detail to understand the system
- **Contribution clarity**: Explicit contribution statement in the introduction
- **Privacy considerations**: Address data collection and privacy implications
- **No appendix**: All essential content must fit within 10 pages

## Submission Checklist

- [ ] 10 pages or fewer (no appendix)
- [ ] `\documentclass[sigchi, review, anonymous]`
- [ ] CCS Concepts and keywords included in abstract
- [ ] All author identification removed
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] IRB/ethics statement included
- [ ] System fully described and implemented
- [ ] Evaluation results presented
- [ ] References list all authors
- [ ] High-quality, grayscale-legible figures
