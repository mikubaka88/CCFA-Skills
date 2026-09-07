# ICASSP Venue Guide

> Migrated from the legacy `ccf-conference-skills/icassp/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `icassp` |
| Venue family | Signal Processing |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/ICASSP/spconf.sty`, `ccf-latex-templates/ICASSP/Template.tex`, `ccf-latex-templates/ICASSP/IEEEbib.bst`, `ccf-latex-templates/ICASSP/strings.bib`, `ccf-latex-templates/ICASSP/refs.bib` |
| Official URL | https://2027.ieeeicassp.org/ |
| Paper Kit URL | https://cmsworkshops.com/ICASSP2027/papers/paper_kit.php |
| Last verified | Verified against official ICASSP 2027 Paper Kit on 2026-09-07. |
| Source status | Official ICASSP 2027 Paper Kit (`cmsworkshops.com/ICASSP2027/papers/paper_kit.php`). |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# ICASSP 2027 Conference Writing Skill

**CCF-B | Signal Processing | Publisher: IEEE (IEEE Signal Processing Society)**
**Conference:** https://2027.ieeeicassp.org/
**Paper Kit:** https://cmsworkshops.com/ICASSP2027/papers/paper_kit.php
**Templates:** `ccf-latex-templates/ICASSP/spconf.sty`, `Template.tex`, `IEEEbib.bst`, `strings.bib`, `refs.bib`

---

## Document Setup

### Preamble Structure

Official ICASSP 2027 uses `\documentclass{article}` with `spconf.sty` and `IEEEbib.bst`:

```latex
\documentclass{article}
\usepackage{spconf,amsmath,graphicx,hyperref}

% Title: ALL CAPITALS, boldface, 14pt
\title{PAPER TITLE IN ALL CAPITAL LETTERS}

% Single Address (1-2 authors at same institution):
\name{Author Name(s)\thanks{Thanks to XYZ agency for funding.}}
\address{Department, Institution, City, Country\\
         \texttt{\{author1, author2\}@institution.edu}}

\begin{document}
%\ninept % Uncomment if needed to typeset in 9pt

\maketitle

\begin{abstract}
Your abstract here (100--150 words, no references).
\end{abstract}

\begin{keywords}
One, two, three, four, five
\end{keywords}

\section{Introduction}
\label{sec:intro}
...
```

### Required Packages

```latex
\usepackage{spconf}     % ICASSP/ICIP official style file
\usepackage{amsmath}    % Math formatting
\usepackage{graphicx}   % Figures
\usepackage{hyperref}   % Hyperlinks (supported in official template)
```

---

## Page Limits

| Section | Limit | Note |
| --- | --- | --- |
| Technical content (text, figures, tables) | **Up to 4 pages** | References may also appear on pages 1–4 |
| References & compliance | **1 optional page (5th page)** | **ONLY** references, funding acknowledgements, and ethical statement |
| **Total Maximum** | **5 pages maximum** | Any document exceeding 5 pages or with technical content on page 5 is rejected |

- The 5th page may contain **only references, funding acknowledgements, and a *Compliance with Ethical Standards* statement**.
- All technical text, algorithms, figures, and tables must fit within the 4-page limit.

---

## Anonymity Requirements

**ICASSP is NOT double-blind (single-blind review).**
- Author names and affiliations **must appear** on the submitted PDF manuscript. Do not anonymize.
- Submissions with blank author lists will fail document inspection.
- The author list and ordering on the uploaded PDF must match the online submission form **exactly**.
- **ORCiD Requirement (New in 2027):** Every author named on the paper must have a valid ORCiD ID (`https://orcid.org/0000-xxxx-xxxx-xxxx`) entered in the submission form.

---

## Title and Author Formatting

### Title Formatting
- The title must appear in **ALL CAPITALS**, boldface, 14pt, centered.
- **Do not use LaTeX math notation** (e.g. `$x_y$`) or uncommon acronyms in the title; the title must be representable in plain Unicode.

### Author Blocks

```latex
% Single address (or authors sharing one affiliation):
\name{Author One and Author Two\thanks{Supported by funding agency.}}
\address{Department, University, City, Country\\
         \texttt{\{author1, author2\}@univ.edu}}

% Two addresses (separate columns):
\twoauthors
  {Author One\sthanks{Supported by ABC.}}
  {Department A\\ University A\\ \texttt{author1@univ-a.edu}}
  {Author Two\sthanks{Supported by XYZ.}}
  {Department B\\ University B\\ \texttt{author2@univ-b.edu}}

% Multiple authors (3+ affiliations):
\name{First Author$^{\star \dagger}$ \qquad Second Author$^{\star}$ \qquad Third Author$^{\dagger}$}
\address{$^{\star}$ First Institution, Department, Country \\
         $^{\dagger}$ Second Institution, Department, Country}
```

---

## Abstract and Keywords Formatting

```latex
\begin{abstract}
Your abstract content here (100--150 words).
Positioned at top of left column, ~12 mm below title, <= 80 mm in length.
Must match the abstract entered in the online submission form.
\end{abstract}

\begin{keywords}
Five, keywords, separated, by, commas
\end{keywords}
```

---

## Section Organization

Standard ICASSP paper structure:
1. **Abstract & Keywords**: 100–150 words, up to 5 keywords.
2. **1. Introduction**: Problem definition, motivation, contributions.
3. **2. Relation to Prior Work**:
   - ICASSP explicitly expects discussion showing how contributions differ from prior studies and foundational literature.
   - Can be a separate section or integrated, but must clearly differentiate what is novel.
4. **3. Proposed Method / Algorithm**: Formulation, architecture, mathematical details.
5. **4. Experiments and Results**: Datasets, baselines, metrics, discussion.
6. **5. Conclusion**: Summary of findings and future work.
7. **References**: IEEE style (max page 5).

---

## Formatting and Typography Rules

- **Paper Size:** US Letter (8.5 × 11 in / 216 × 279 mm) preferred; A4 acceptable (leave bottom 12 mm empty).
- **Print Area:** 178 mm × 229 mm (7 in × 9 in). Everything must stay strictly within this area.
- **Margins:**
  - Left margin: 19 mm (0.75 in).
  - Top margin: 25 mm (1.0 in), except title page which begins at 35 mm (1.375 in).
  - Title block area: top 50 mm (2 in) reserved across both columns.
- **Columns:** Two columns, each 86 mm (3.39 in) wide, with 6 mm (0.24 in) space between columns.
- **Text:** Fully justified, single-spaced.
- **Font Face:** Times-Roman or Computer Modern strongly encouraged. TrueType or Type 1 vector fonts only (no Type 3 bitmap fonts).
- **Font Size:** Minimum 9pt throughout the paper, including captions and footnotes (`\ninept` can be used). Line density <= 3.2 lines/cm (8 lines/inch).
- **Headings:**
  - Major headings: ALL CAPITALS, boldface, centered, with period after number (e.g. `1. INTRODUCTION`).
  - Subheadings: Lowercase (initial capitalized), boldface, flush left on separate line.
  - Sub-subheadings: Discouraged; if used, lowercase italics flush left.
- **Page Numbers:** **Do not include page numbers.** The document must be unpaginated (`\pagestyle{empty}`).

---

## Figures and Tables

```latex
\begin{figure}[htb]
  \centering
  \includegraphics[width=0.85\linewidth]{figure_name}
  \caption{Figure caption here (lowercase, period at end).}
  \label{fig:example}
\end{figure}
```

- Position figures at the **top of columns** whenever possible. May span two columns if necessary.
- Captions **below** figures, **above** tables.
- Number figures and tables sequentially.
- Ensure all figures are legible in black and white (printed proceedings are monochrome).
- Use vector formats (`.pdf`, `.eps`) for line plots and diagrams.
- **Column Balancing:** On the last page, use `\vfill\pagebreak` to balance the two column lengths evenly.

---

## References (`IEEEbib.bst`)

Numbered citation style in square brackets:

```latex
\bibliographystyle{IEEEbib}
\bibliography{strings,refs}

% Inline citation:
\cite{key1, key2}   % [1], [2]
```

- References must follow standard IEEE Citation Guidelines.
- Produced using BibTeX with `IEEEbib.bst`, loading `strings.bib` (string definitions) and `refs.bib` (entries).
- References may appear on pages 1–4 and extend to page 5.
- Page 5 must not contain any body text, figures, tables, or appendix material.

---

## Camera-Ready Preparation

After acceptance:
1. Ensure strict adherence to the 4-page technical + 1-page references limit.
2. Sign the IEEE Electronic Copyright Form (eCF) through the submission portal.
3. Verify all fonts are embedded and subset (PDF v3.2 specification).
4. PDF file size must be <= 5 MB and named `<first_author_lastname>.pdf`.
5. Preprints on arXiv / TechRxiv are permitted; must include standard IEEE copyright notice upon transfer.

---

## Submission Checklist (Paper Writing)

- [ ] Technical content (intro, method, results) is strictly <= 4 pages
- [ ] Page 5 (if used) contains ONLY references, funding acknowledgements, and ethical standards statement
- [ ] Total page count <= 5 pages
- [ ] Author names and affiliations are visible on the first page of the PDF (not anonymous)
- [ ] All authors have valid ORCiD IDs ready for submission form
- [ ] Paper title is in ALL CAPITALS, boldface, without math notation ($x$)
- [ ] Abstract is 100–150 words with up to 5 keywords
- [ ] Includes clear discussion on "Relation to Prior Work"
- [ ] No page numbers in PDF (`\pagestyle{empty}`)
- [ ] All fonts embedded and subset (vector Type 1 / TrueType, no Type 3)
- [ ] Margins and print area conform to 178 mm × 229 mm (7 × 9 in)
- [ ] Font size is >= 9pt throughout (including captions)
- [ ] Figures are legible in grayscale
- [ ] References formatted with `IEEEbib.bst` (`\bibliography{strings,refs}`) according to IEEE Citation Guidelines
