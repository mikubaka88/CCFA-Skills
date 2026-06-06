# ICASSP Venue Guide

> Migrated from the legacy `ccf-conference-skills/icassp/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-venue-format-guide`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `icassp` |
| Venue family | Signal Processing |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/ICASSP/IEEEtran.cls` |
| Official URL | https://2026.ieeeicassp.org/ |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# ICASSP 2026 Conference Writing Skill

**CCF-B | Signal Processing | Publisher: IEEE**
**Conference:** https://2026.ieeeicassp.org/
**Template:** `ICASSP/IEEEtran.cls`

## Document Setup

### Preamble Structure

```latex
\documentclass[conference]{IEEEtran}

% Required packages
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{cite}
\usepackage{times}   % Strongly recommended: Times-Roman font
\usepackage{url}

\begin{document}

% Title
\title{Paper Title}

% Author blocks — names included (ICASSP is NOT double-blind)
\author{
  \IEEEauthorblockN{Author Name}
  \IEEEauthorblockA{Institution\\Department\\email@example.com}
}

\maketitle

\begin{IEEEabstract}
\IEEEabstractnarrowsection
Your abstract here (100--150 words, no references).
\end{IEEEabstract}

\section{Introduction}
...
```

### Required Packages

```latex
\usepackage{graphicx}   % Figures
\usepackage{amsmath}    % Math
\usepackage{cite}       % IEEE numbered citations
\usepackage{times}      % Times-Roman font (strongly encouraged)
\usepackage{url}         % URLs in references
```

## Page Limits

|| Section | Limit |
|---------|--------|
| Main content (text, figures, references) | **4 pages** |
| References only | **1 optional page** (5th page) |
| **Total** | **5 pages maximum** |

The 5th page may contain **only references**. All other pages must not exceed the 4-page limit.

## Anonymity Requirements

**ICASSP is NOT double-blind.** Author names and affiliations must appear in the submission. Do not attempt to anonymize the PDF. Authors' names should be included in the standard IEEE author block format.

## Title and Author Formatting

```latex
% Single author:
\author{
  \IEEEauthorblockN{Author Name}
  \IEEEauthorblockA{Institution\\Department\\email@example.com}
}

% Multiple authors (separate blocks):
\author{
  \IEEEauthorblockN{First Author}
  \IEEEauthorblockA{Institution 1\\email1@example.com}
  \and
  \IEEEauthorblockN{Second Author}
  \IEEEauthorblockA{Institution 2\\email2@example.com}
}
```

## Abstract Formatting

ICASSP uses the `IEEEabstract` environment:

```latex
\begin{IEEEabstract}
\IEEEabstractnarrowsection
Your abstract content here. Abstract should be 100--150 words.
Describe the problem, method, and key results in a concise paragraph.
\end{IEEEabstract}
```

## Section Organization

Standard ICASSP paper structure:
1. Abstract
2. Introduction — Problem, motivation, contributions
3. Background / Prior Work
4. Proposed Method / System
5. Experiments / Evaluation
6. Conclusion
7. References

## Figures and Tables

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figure}
  \caption{Figure caption here (lowercase, period at end).}
  \label{fig:label}
\end{figure}
```

- Use vector formats (.pdf) where possible
- Caption **below** figures, **above** tables
- Number figures and tables sequentially
- Ensure figures are legible in grayscale

## References (IEEEtran)

IEEE numbered citation style:

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}

% Inline citations:
\cite{key1, key2}      % [1], [2]
\citep{key}            % [1]
\citet{key}           % Author [1]
```

## Formatting Rules

- **Format:** IEEE conference two-column (default with `conference` option)
- **Font:** Times-Roman strongly encouraged, minimum 9pt throughout
- **Margins:** 1" top, 0.75" sides, bottom to accommodate footer
- **Paper size:** US Letter (8.5 × 11 inch)
- **Text:** Fully justified, single-spaced
- **Column width:** 3.39", 0.24" gap between columns
- **Print area:** 7" wide × 9" tall

## Camera-Ready Preparation

After acceptance:
1. Ensure all content fits within page limits
2. Verify fonts are embedded
3. Complete author information is correct
4. Check that two-column layout is maintained
5. Register at least one author at non-student rate before the deadline
6. Paper will be published in IEEE Xplore 30 days before the conference

## Submission Checklist

- [ ] 4 pages of content maximum (references may extend to page 5)
- [ ] Author names included in submission
- [ ] PDF uses Times-Roman or equivalent font
- [ ] All fonts embedded
- [ ] US Letter paper size
- [ ] Two-column layout
- [ ] Compiles with `pdflatex`
- [ ] References in IEEEtran format
