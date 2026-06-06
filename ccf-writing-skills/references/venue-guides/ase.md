# ASE Venue Guide

> Migrated from the legacy `ccf-conference-skills/ase/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `ase` |
| Venue family | SE |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/ASE/acmart.cls` |
| Official URL | https://conf.researchr.org/track/ase-2026/ase-2026-papers |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# ASE Conference Writing Skill

**CCF-A | SE | Publisher: ACM/IEEE**
**Conference:** https://conf.researchr.org/track/ase-2026/ase-2026-papers
**Template:** `ASE/acmart.cls` (ACM acmart, SIGCONF format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigconf,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigconf]{acmart}
\setcopyright{acmlicensed}
\acmConference[ASE 2026]{Proceedings of the 41st IEEE/ACM International Conference
  on Automated Software Engineering}{September 1--5, 2026}{Vancouver, Canada}
\acmISBN{978-X-XXXX-XXXX-X/26/09}
\acmDOI{10.1145/XXXXXXX}
\acmPrice{}
```

### Required Packages

```latex
\usepackage[round]{natbib}     % Author-year citations
\usepackage{algorithm}
\usepackage[noend]{algorithmic}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{listings}
\lstset{basicstyle=\small\ttfamily}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **14 pages** |
| Tool paper | **8 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

ASE enforces a strict 14-page limit for regular papers and 8 pages for tool papers. References and appendix do not count toward this limit, but reviewers are not required to read the appendix.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. Do not include author names anywhere in the submission
2. Use third person for self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize URLs (e.g., GitHub repositories, institutional links)
4. Remove PDF metadata that reveals authorship
5. Do not include acknowledgments

## Camera-Ready Differences

When preparing camera-ready after acceptance:

1. Remove `review` and `anonymous` options from `\documentclass`
2. Add `\setcopyright{acmlicensed}` or appropriate rights mode
3. Fill in `\acmConference` with full conference title and dates
4. Add `\acmISBN`, `\acmDOI`, and `\acmPrice` fields
5. Restore all author names and affiliations
6. Add acknowledgments if desired

## Section Organization

Standard ASE paper structure:

1. **Introduction** — Problem, motivation, contributions (enumerate contributions explicitly)
2. **Background/Motivation** — Context, related work positioning
3. **Approach/Method** — Core technical contribution
4. **Implementation/Development** — System details, tool support
5. **Evaluation** — Experimental methodology, results, comparison
6. **Discussion** — Threats to validity, limitations
7. **Related Work** — Positioning against prior art
8. **Conclusion** — Summary and future work
9. References

## Theorem Environments

ASE papers may include formal reasoning:

```latex
\theoremstyle{plain}
\newtheorem{definition}{Definition}
\newtheorem{property}{Property}

\theoremstyle{plain}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}
```

## Code Listings

```latex
% Inline code:
The tool uses \lstinline!soot! for bytecode analysis.

% Code blocks:
\begin{lstlisting}[language=Java, caption={Bug pattern detector}, label={lst:detector}]
public class NPEDetector extends BodyTransformer {
    @Override
    protected void internalTransform(Body b, String phaseName,
                                     Map<String, Object> options) {
        UnitPatchingGraph g = new UnitPatchingGraph(b);
        for (Unit u : g.getUnits()) {
            if (isNullCheck(u)) {
                // Check if dereference happens without guard
            }
        }
    }
}
\end{lstlisting}
```

## Figures and Tables

- Use vector formats (.pdf) where possible
- Ensure figures are legible in grayscale
- Number figures and tables sequentially
- Captions should be descriptive and self-contained

## References (natbib)

ACM-Reference-Format bibstyle with author-year citations:

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

% Citations:
\citet{smith2023}      % Smith et al. (2023)
\citep{smith2023}      % (Smith et al. 2023)
```

Each reference must list **all authors** — do not use "et al." in the bibliography.

## Formatting Rules

- **Format:** ACM sigconf (two-column, single-spaced)
- **Paper size:** US Letter
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in
- **Body font:** 9pt minimum, Times New Roman
- **References:** 8pt, no page limit
- **Line spacing:** Single-spaced (template default)

## Submission Checklist

- [ ] 14 pages or fewer (regular paper) or 8 pages (tool paper)
- [ ] `\documentclass[sigconf,review,anonymous]`
- [ ] All author/anonymization info removed
- [ ] No self-identifying URLs or citations
- [ ] PDF metadata cleared
- [ ] References list all authors
- [ ] Figures legible in grayscale
- [ ] Compiles with `pdflatex`

## Camera-Ready Checklist

- [ ] Remove `review` and `anonymous` options
- [ ] Add `\setcopyright{acmlicensed}` (or appropriate)
- [ ] Fill `\acmConference`, `\acmISBN`, `\acmDOI`, `\acmPrice`
- [ ] Restore author names and affiliations
- [ ] Include page numbers (`\settopmatter{printfolios=true}`)
