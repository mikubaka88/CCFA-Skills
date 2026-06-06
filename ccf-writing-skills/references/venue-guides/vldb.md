# VLDB Venue Guide

> Migrated from the legacy `ccf-conference-skills/vldb/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `vldb` |
| Venue family | DB |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/VLDB/main.tex` |
| Official URL | https://vldb.org/2026 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# VLDB 2026 Conference Writing Skill

**CCF-A | DB | Publisher: ACM (VLDB Endowment)**
**Conference:** https://vldb.org/2026
**Template:** `VLDB/main.tex` (ACM acmart, sigconf format, VLDB-specific author block)

## Document Setup

### Preamble Structure

```latex
% VLDB template version 2020-08-03 enhances ACM template v1.7.0
\documentclass[sigconf, nonacm]{acmart}

% === VLDB-specific metadata (must be filled in) ===
\newcommand{\vldbdoi}{XX.XX/XXX.XX}
\newcommand{\vldbpages}{XXX-XXX}
\newcommand{\vldbvolume}{14}
\newcommand{\vldbissue}{1}
\newcommand{\vldbyear}{2026}
% leave empty if no availability URL
\newcommand{\vldbavailabilityurl}{URL_TO_YOUR_ARTIFACTS}
% use 'plain' for review, 'empty' for camera-ready
\newcommand{\vldbpagestyle}{plain}

\begin{document}
```

### Required Packages

```latex
\usepackage[round]{natbib}     % Author-year citations
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{balance}
\usepackage{cleveref}          % For consistent cross-references
\usepackage{algorithm}
\usepackage[noend]{algorithmic}
\usepackage{hyperref}         % VLDB requires hyperlinks
```

## VLDB-Specific Author Block

VLDB has a mandatory author block after `\maketile`:

```latex
% === After \maketitle, include this mandatory block ===
\pagestyle{\vldbpagestyle}
\begingroup\small\noindent\raggedright\textbf{PVLDB Reference Format:}\\
\vldbauthors. \vldbtitle. PVLDB, \vldbvolume(\vldbissue): \vldbpages, \vldbyear.\\
\href{https://doi.org/\vldbdoi}{doi:\vldbdoi}
\endgroup
\begingroup
\renewcommand\thefootnote{}\footnote{\noindent
This work is licensed under the Creative Commons BY-NC-ND 4.0 International License.
Visit \url{https://creativecommons.org/licenses/by-nc-nd/4.0/} to view a copy of this license.
For any use beyond those covered by this license, obtain permission by emailing
\hrefmailto:info@vldb.org}{info@vldb.org}. Copyright is held by the owner/author(s).
Publication rights licensed to the VLDB Endowment.\\
Proceedings of the VLDB Endowment, Vol. \vldbvolume, No. \vldbissue \\
ISSN 2150-8097. \\
\href{https://doi.org/\vldbdoi}{doi:\vldbdoi}\\
}
\addtocounter{footnote}{-1}\endgroup

% Optional artifact availability block
\ifdefempty{\vldbavailabilityurl}{}{
\vspace{.3cm}
\begingroup\small\noindent\raggedright\textbf{PVLDB Artifact Availability:}\\
The source code, data, and/or other artifacts have been made available at
\url{\vldbavailabilityurl}.
\endgroup
}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **12 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

VLDB enforces a 12-page limit for the main body. References and appendix do not count toward this limit, but reviewers are not required to read the appendix.

## Anonymity Requirements

Double-blind review:

1. No author names or affiliations in submission
2. Third-person self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs, GitHub links, personal pages
4. Clear PDF metadata
5. Remove acknowledgments
6. For review, set `\vldbpagestyle{plain}` to show page numbers

## Camera-Ready Differences

After acceptance:

1. Set `\vldbpagestyle{empty}` to remove page numbers
2. Fill in `\vldbdoi`, `\vldbpages`, `\vldbyear`, `\vldbvolume`, `\vldbissue`
3. Restore all author names and affiliations
4. Add `\vldbavailabilityurl` if providing artifacts
5. Replace `nonacm` option with appropriate copyright mode

## Section Organization

VLDB papers typically follow a database-systems paper structure:

1. **Introduction** — Problem, motivation, contributions (enumerate explicitly)
2. **Background & Preliminaries** — System model, definitions, assumptions
3. **Problem Statement** — Formal problem definition where applicable
4. **Proposed Approach / System Design** — Core technical contribution
5. **Implementation** — System details, optimization choices
6. **Evaluation** — Experimental methodology, benchmarks, comparisons
7. **Related Work** — Positioning against prior systems work
8. **Conclusion**
9. References
10. Appendix (optional)

## PVLDB Reference Format

VLDB uses the PVLDB reference format with DOI:

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

% All references must include full author lists
\citet{garcia-molina}  % Garcia-Molina et al.
\citep{garcia-molina}   % (Garcia-Molina et al.)
```

## Artifact Availability

VLDB strongly encourages artifact availability. Use the optional block:

```latex
% Add after the copyright block
\vspace{.3cm}
\begingroup\small\noindent\raggedright\textbf{PVLDB Artifact Availability:}\\
The source code, data, and/or other artifacts have been made available at
\url{https://github.com/your-repo}.
\endgroup
```

## Figures and Tables

- Vector formats (.pdf) for diagrams and system architectures
- Ensure grayscale legibility
- Number sequentially
- Use `booktabs` for tables (no vertical rules)
- Caption below figures, above tables
- Self-contained captions

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figures/architecture}
  \caption{System architecture showing the query optimizer,
    execution engine, and storage manager components.}
  \label{fig:architecture}
\end{figure}
```

## Formatting Rules

- **Format:** ACM sigconf (two-column, single-spaced)
- **Paper size:** US Letter
- **Body font:** 9pt minimum, Times New Roman
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in
- **PVLDB DOI:** Required in the author block (provided by VLDB)
- **Creative Commons License:** CC BY-NC-ND 4.0 (required)

## Submission Checklist

- [ ] 12 pages or fewer (main body)
- [ ] VLDB author block included after `\maketile`
- [ ] `\vldbpagestyle{plain}` for review
- [ ] All author identification removed
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] References list all authors
- [ ] Grayscale-legible figures

## Camera-Ready Checklist

- [ ] Fill in all `\vldb*` macros with real values
- [ ] Set `\vldbpagestyle{empty}` for camera-ready
- [ ] Add artifact availability URL if applicable
- [ ] Restore author information
- [ ] Use correct `\setcopyright` mode
- [ ] Add DOI provided by VLDB
