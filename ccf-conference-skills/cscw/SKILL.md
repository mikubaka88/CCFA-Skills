---
name: cscw
description: Writing and formatting guidance for CSCW (ACM Conference on Computer-Supported Cooperative Work and Social Computing) papers. Use when drafting, formatting, or submitting to CSCW 2026. Covers ACM acmart sigchi format with anonymous review mode, CSCW-specific requirements (CCS Concepts, author keywords), empirical/research methodology standards, ethics and IRB requirements, figure quality, double-blind anonymity, page limits, and camera-ready preparation.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CSCW 2026 Conference Writing Skill

**CCF-A | HCI | Publisher: ACM**
**Conference:** https://cscw.acm.org/2026
**Template:** `CSCW/acmart.cls` (ACM acmart, sigchi format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigchi, review, anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigchi]{acmart}
\acmConference[CSCW 2026]{CSCW '26: Proceedings of the 2026 ACM Conference...}
               {April 25--29, 2026}{Shanghai, China}
\acmISBN{978-X-XXXX-XXXX-X/XX/XX}
\acmDOI{10.5555/XXXXXXX.XXXXXXX}
```

CSCW uses the `sigchi` format option. For the abstract, include both CCS Concepts and author keywords as required metadata blocks.

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

CSCW abstracts require CCS Concepts and keywords:

```latex
\begin{abstract}
  We present a novel approach to...
  Findings from a field study ($N=32$) demonstrate...
\end{abstract}

% CCS Concepts (generated at http://dl.acm.org/ccs.cfm)
\ccsdesc[500]{Human-centered computing~Collaborative interaction}
\ccsdesc[300]{Human-centered computing~Computer supported cooperative work}
\ccsdesc[100]{Human-centered computing~Social computing}

% Author keywords
\keywords{collaboration, CSCW, social computing, coordination, awareness}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **10 pages** |
| References | No limit |
| Appendix / Supplementary | Not permitted |

CSCW enforces a strict 10-page limit for the main body. References do not count toward the limit. **No appendix or supplementary materials** are permitted.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. No author names or affiliations in submission
2. Third-person self-citations: "Prior work showed..." not "we showed..."
3. Anonymize all URLs (GitHub, participant recruitment pages, personal pages)
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

CSCW papers follow a research-centered structure:

1. **Introduction** — Problem space, motivation, research questions, contributions (enumerate 3-5 contributions)
2. **Background & Related Work** — Prior CSCW and HCI research, theoretical grounding
3. **Research Context & Methods** — Study design, participants, data collection (field study, interview, experiment, etc.)
4. **Findings** — Empirical or qualitative findings
5. **Discussion** — Interpretation, implications for CSCW, design recommendations
6. **Conclusion & Future Work**
7. References

CSCW values papers where the **contribution is clear** and **evidence supports the claims**. CSCW accepts empirical studies, design research, and theory-building work.

## Contribution Statement

```latex
\section{Introduction}
Despite the widespread use of collaborative tools...
We address this gap by investigating...
This paper makes the following contributions:
\begin{itemize}
  \item An empirical study of coordination practices in...
  \item A novel framework for understanding...
  \item Design implications for collaborative tools in...
\end{itemize}
```

## Research Methods

CSCW accepts diverse methodologies:

```latex
\section{Research Methods}

\subsection{Study Context}
We conducted a qualitative field study in...

\subsection{Participants}
We recruited 20 participants through...

\subsection{Data Collection}
Data was collected over 3 months through...

\subsection{Analysis}
We used thematic analysis with an iterative coding process...
```

## IRB and Ethics

CSCW requires ethical research practices:

```latex
\section{Ethics Statement}
This study was reviewed and approved by the Institutional
Review Board of [University Name] (protocol #XXXX-XXXX).
All participants provided informed consent.
```

## CCS Concepts and Keywords

Generate CCS Concepts at http://dl.acm.org/ccs.cfm and include them as shown above. Keywords are also required and appear after the CCS Concepts block.

## Figures and Tables

CSCW emphasizes visual communication and empirical data presentation:

- Use high-quality vector figures (.pdf, .eps)
- Ensure grayscale legibility
- Include screenshots, study setups, and design artifacts
- Number figures/tables sequentially
- Tables should use `booktabs` (no vertical rules)

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/study-context}
  \caption{The collaborative workspace showing (a) shared calendar,
    (b) chat interface, and (c) notification panel.}
  \label{fig:context}
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

- **Format:** ACM sigchi (single-column for submission, two-column camera-ready)
- **Paper size:** US Letter
- **Body font:** 9pt minimum, Times New Roman
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in

## CSCW Writing Conventions

- **Evidence-based**: Claims must be supported by study data or other evidence
- **Methodological transparency**: Enough detail to understand and (where possible) replicate the study
- **Contribution clarity**: Explicit contribution statement in the introduction
- **Theoretical grounding**: Connect findings to relevant CSCW and HCI theory
- **Design implications**: CSCW values practical takeaways for designers
- **No appendix**: All essential content must fit within 10 pages

## Submission Checklist

- [ ] 10 pages or fewer (no appendix)
- [ ] `\documentclass[sigchi, review, anonymous]`
- [ ] CCS Concepts and keywords included in abstract
- [ ] All author identification removed
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] IRB/ethics statement included
- [ ] Methodology fully described
- [ ] References list all authors
- [ ] High-quality, grayscale-legible figures
