# ICME Venue Guide

> Migrated from the legacy `ccf-conference-skills/icme/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `icme` |
| Venue family | Multimedia |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/ICME/IEEEtran.cls` |
| Official URL | https://2026.ieeeicme.org/ |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# ICME 2026 Conference Writing Skill

**CCF-B | Multimedia | Publisher: IEEE**
**Conference:** https://2026.ieeeicme.org/
**Template:** `ICME/IEEEtran.cls`

## Document Setup

### Preamble Structure

```latex
\documentclass[conference]{IEEEtran}

% Required packages
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{cite}
\usepackage{times}   % Strongly recommended: Times New Roman font
\usepackage{url}
\usepackage{stfloats}  % For bottom floats

\begin{document}

% Title
\title{Paper Title}

% Author blocks (include for camera-ready; follow double-blind rules for submission)
\author{
  \IEEEauthorblockN{Author Name}
  \IEEEauthorblockA{Institution\\Department\\email@example.com}
}

\maketitle

\begin{IEEEabstract}
\IEEEabstractnarrowsection
Your abstract here (100--150 words).
\end{IEEEabstract}

\section{Introduction}
...
```

### Required Packages

```latex
\usepackage{graphicx}   % Figures
\usepackage{amsmath}    % Math
\usepackage{cite}       % IEEE numbered citations
\usepackage{times}      % Times New Roman (strongly encouraged)
\usepackage{url}        % URLs in references
\usepackage{stfloats}  % Bottom floats (optional)
```

## Page Limits

|| Section | Limit |
|---------|--------|
| Main paper (text, figures, references) | **6 pages** |

ICME enforces a strict 6-page limit for all content including references.

## Anonymity Requirements

ICME 2026 uses **double-blind review**. Authors must anonymize their submissions:

1. Remove author names and affiliations from the PDF
2. Use third person for self-citations ("Smith et al. showed..." not "we showed...")
3. Anonymize URLs (e.g., GitHub, project pages)
4. Do not include acknowledgments in the submission
5. Supplemental material must also be anonymized
6. Papers that do not follow double-blind rules will be **automatically rejected**

## Title and Author Formatting

```latex
% Camera-ready (accepted paper):
\author{
  \IEEEauthorblockN{Author Name}
  \IEEEauthorblockA{Institution\\Department\\email@example.com}
}

% Multiple authors:
\author{
  \IEEEauthorblockN{First Author}
  \IEEEauthorblockA{Institution 1\\email1@example.com}
  \and
  \IEEEauthorblockN{Second Author}
  \IEEEauthorblockA{Institution 2\\email2@example.com}
}
```

## Abstract Formatting

```latex
\begin{IEEEabstract}
\IEEEabstractnarrowsection
Your abstract content here. Abstract should be approximately 100--150 words.
Describe the problem, method, and key results concisely.
\end{IEEEabstract}
```

## Section Organization

Standard ICME paper structure:
1. Abstract
2. Introduction — Problem, motivation, contributions
3. Related Work / Background
4. Proposed Method
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

\begin{table}[t]
  \caption{Table caption here (above table, period at end).}
  \label{tab:label}
  \centering
  \begin{tabular}{lll}
    \toprule
    Col 1 & Col 2 & Col 3 \\
    \midrule
    Data & Data & Data \\
    \bottomrule
  \end{tabular}
\end{table}
```

- Use vector formats (.pdf) where possible
- Caption **below** figures, **above** tables
- Use `booktabs` for professional tables (no vertical rules)
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
\citet{key}            % Author [1]
```

## Formatting Rules

- **Format:** IEEE conference two-column (use `conference` class option)
- **Font:** Times New Roman strongly encouraged, minimum 9pt throughout
- **Margins:** 1" top/bottom, 0.75" sides
- **Paper size:** US Letter (8.5 × 11 inch)
- **Text:** Fully justified
- **All fonts must be embedded in the PDF**
- **Review type:** Double-blind — anonymize all submissions

## Supplemental Material

Optional supplemental material may be uploaded:
- Must be anonymized
- Max 50 MB
- May include: video demonstrations, extended proofs, presentation slides
- Referenced appropriately in the main paper
- Reviewers are not obliged to review supplemental material

## Camera-Ready Preparation

After acceptance:
1. Restore all author names and affiliations
2. Add acknowledgments (if desired)
3. Verify all content fits within 6-page limit
4. Ensure fonts are embedded
5. Confirm US Letter paper size
6. At least one author must register at non-student rate before deadline
7. Failure to present in person may result in paper not appearing in IEEE Xplore

## Submission Checklist

- [ ] 6 pages or fewer (strictly enforced)
- [ ] Double-blind: no author names/affiliations in submission PDF
- [ ] Third-person self-citations
- [ ] All URLs anonymized
- [ ] No acknowledgments in submission
- [ ] Supplemental material anonymized (if any)
- [ ] Times New Roman font (strongly encouraged)
- [ ] All fonts embedded
- [ ] US Letter paper size
- [ ] Two-column layout
- [ ] Compiles with `pdflatex`
- [ ] References in IEEEtran format
