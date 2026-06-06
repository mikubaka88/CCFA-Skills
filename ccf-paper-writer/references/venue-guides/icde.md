# ICDE Venue Guide

> Migrated from the legacy `ccf-conference-skills/icde/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `icde` |
| Venue family | DB |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/ICDE/IEEEtran.cls` |
| Official URL | https://icde2026.github.io |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# ICDE 2026 Conference Writing Skill

**CCF-A | DB | Publisher: IEEE**
**Conference:** https://icde2026.github.io
**Template:** `ICDE/IEEEtran.cls` (IEEEtran, conference format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[conference]{IEEEtran}

% For anonymous submission, remove author block or use placeholder
% IEEEtran does not have built-in anonymous mode

% === CAMERA-READY MODE ===
\documentclass[conference]{IEEEtran}
% Add conference-specific commands provided by IEEE
```

### Required Packages

```latex
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{cite}
\usepackage{balance}
\usepackage{cleveref}
\usepackage{algorithm}
\usepackage{algorithmic}
\usepackage{url}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **12 pages** |
| References | No limit |
| Appendix | Check CFP |

ICDE typically enforces a 12-page limit for the main body. References do not count toward the limit. Always verify the current CFP for exact limits.

## Anonymity Requirements

ICDE uses double-blind review. Since IEEEtran does not have a built-in anonymous mode:

1. Remove or replace author names/affiliations in the submission
2. Use "Anonymous" as author during submission
3. Third-person self-citations: "Smith et al. showed..." not "we showed..."
4. Anonymize all URLs, GitHub links, personal pages
5. Clear PDF metadata
6. Remove acknowledgments

```latex
% Author block for anonymous submission:
\author{
  \IEEEauthorblockN{Anonymous Author}
  \IEEEauthorblockA{
    \IEEEauthorrefmark{1}Anonymous Institution\\
    anonymous@institution.edu}
}
```

## Camera-Ready Differences

After acceptance:

1. Restore all author names and affiliations with correct formatting
2. Add the conference-specific copyright notice provided by IEEE
3. Ensure Xplore-compatible PDF (CMYK colors, embedded fonts)
4. Submit via IEEE PDF eXpress if required

## Section Organization

ICDE papers typically follow a data engineering paper structure:

1. **Abstract** — Concise summary
2. **Introduction** — Problem, motivation, contributions (enumerate explicitly)
3. **Background & Preliminaries** — System model, definitions
4. **Problem Definition** — Formal problem statement
5. **Proposed Approach** — Core technical contribution
6. **Implementation** — System details, complexity
7. **Experimental Evaluation** — Benchmarks, comparisons, analysis
8. **Related Work**
9. **Conclusion**
10. References
11. Appendix (optional)

## Theorem Environments

ICDE papers often include formal reasoning:

```latex
\theoremstyle{plain}
\newtheorem{definition}{Definition}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}
\newtheorem*{corollary}{Corollary}
\newtheorem{property}{Property}
```

## Figures and Tables

- IEEE uses a single-column format for conference papers
- Vector formats (.pdf) for diagrams
- Grayscale legibility required
- Number sequentially
- Use `booktabs` for tables (no vertical rules)
- IEEE convention: figures at top, tables at bottom

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/system}
  \caption{System architecture of the proposed data integration
    framework showing the query processor, optimizer, and
    data sources components.}
  \label{fig:system}
\end{figure}

\begin{table}[t]
  \caption{Experimental results on TPC-H benchmark.}
  \label{tab:results}
  \begin{tabular}{cccc}
    \toprule
    Query & Baseline (s) & Ours (s) & Speedup \\
    \midrule
    Q1 & 12.3 & 4.1 & 3.0x \\
    Q2 & 8.7 & 2.9 & 3.0x \\
    Q3 & 15.2 & 5.8 & 2.6x \\
    \bottomrule
  \end{tabular}
\end{table}
```

## References

IEEE uses the `cite` package and numeric citations:

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}

% Citations are numeric:
\cite{garcia2008db}
% Or: \citep{} from natbib if loaded
```

## Formatting Rules

- **Format:** IEEE conference (single-column)
- **Paper size:** US Letter (8.5" x 11")
- **Body font:** 10pt minimum
- **Margins:** 1" all sides
- **References:** 8pt, no page limit
- **Xplore-compatible PDF**: CMYK colors, embedded fonts

## Submission Checklist

- [ ] 12 pages or fewer (main body)
- [ ] Author information removed/anonymized
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] PDF metadata cleared
- [ ] Grayscale-legible figures
- [ ] Compiles with `pdflatex`

## Camera-Ready Checklist

- [ ] Restore author information
- [ ] Add IEEE copyright notice
- [ ] Generate Xplore-compatible PDF
- [ ] Use CMYK colors for figures
- [ ] Embed all fonts
- [ ] Submit via IEEE PDF eXpress
