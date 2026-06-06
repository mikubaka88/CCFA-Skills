# ECOOP Venue Guide

> Migrated from the legacy `ccf-conference-skills/ecoop/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `ecoop` |
| Venue family | SE/PL |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/ECOOP/acmart.cls` |
| Official URL | https://www.ecoop.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# ECOOP Conference Writing Skill

**CCF-B | SE/PL | Publisher: ACM**
**Conference:** https://www.ecoop.org
**Template:** `ECOOP/acmart.cls` (ACM acmart, SIGPLAN format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigplan,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigplan]{acmart}
\setcopyright{acmlicensed}
\acmConference[ECOOP 2026]{Proceedings of the 40th European Conference on
  Object-Oriented Programming}{July 13--17, 2026}{Amsterdam, Netherlands}
\acmISBN{978-X-XXXX-XXXX-X/26/07}
\acmDOI{10.1145/XXXXXXX}
\acmPrice{}
```

### Required Packages

```latex
\usepackage[round]{natbib}     % Author-year citations
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{listings}
\lstset{basicstyle=\small\ttfamily}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **12 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

ECOOP enforces a strict 12-page limit for the main body. References and appendix do not count toward this limit, but reviewers are not required to read the appendix.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. Do not include author names anywhere in the submission
2. Use third person for self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize URLs (e.g., GitHub repositories)
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

Standard ECOOP paper structure:

1. **Introduction** — Problem, motivation, contributions (enumerate contributions explicitly)
2. **Background** — Technical context, OO programming foundations
3. **Language/Approach** — Core definitions, type system, semantics
4. **Technical Development** — Proofs, metatheory, design decisions
5. **Implementation** — Compiler/interpreter details
6. **Evaluation** — Experimental results
7. **Related Work** — Positioning against prior art
8. **Conclusion** — Summary and future work
9. References

## Theorem Environments

ECOOP papers commonly use formal reasoning environments:

```latex
\theoremstyle{plain}
\newtheorem{definition}{Definition}
\newtheorem{property}{Property}

\theoremstyle{plain}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}
\newtheorem*{proposition}{Proposition}
\newtheorem*{corollary}{Corollary}
```

Use `\qed` (from amsthm) to close proofs.

## Code Listings

ECOOP papers typically include object-oriented code (Java, Scala, Kotlin, etc.):

```latex
% Inline code:
The method \lstinline!getInstance()! implements the singleton pattern.

% Code blocks:
\begin{lstlisting}[language=Java, caption={Singleton implementation}, label={lst:singleton}]
public class Singleton {
    private static volatile Singleton instance;

    public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
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

- **Format:** ACM sigplan (two-column, single-spaced)
- **Paper size:** US Letter
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in
- **Body font:** 9pt minimum, Times New Roman
- **References:** 8pt, no page limit
- **Line spacing:** Single-spaced (template default)

## Submission Checklist

- [ ] 12 pages or fewer (main body)
- [ ] `\documentclass[sigplan,review,anonymous]`
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
