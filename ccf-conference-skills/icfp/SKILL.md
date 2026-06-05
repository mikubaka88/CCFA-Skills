---
name: icfp
description: Writing and formatting guidance for ICFP (International Conference on Functional Programming). Use when drafting, formatting, or submitting to ICFP. Covers ACM acmart with sigplan format, anonymous double-blind review mode, ICFP page limits (12 pages), formal semantics, theorem environments, code listings in functional style, camera-ready preparation with DOI/ISBN, and ACM-Reference-Format citations.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# ICFP Conference Writing Skill

**CCF-B | SE/PL | Publisher: ACM**
**Conference:** https://icfp24.icfp-conf.org
**Template:** `ICFP/acmart.cls` (ACM acmart, SIGPLAN format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigplan,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigplan]{acmart}
\setcopyright{acmlicensed}
\acmConference[ICFP 2026]{Proceedings of the 31st ACM SIGPLAN International
  Conference on Functional Programming}{September 7--13, 2026}{Seattle, WA, USA}
\acmISBN{978-X-XXXX-XXXX-X/26/09}
\acmDOI{10.1145/XXXXXXX}
\acmPrice{}
```

### Required Packages

```latex
\usepackage[round]{natbib}     % Author-year citations
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{mathpartir}       % For inference rules
\usepackage{listings}
\lstset{basicstyle=\small\ttfamily}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **12 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

ICFP enforces a strict 12-page limit for the main body. References and appendix do not count toward this limit, but reviewers are not required to read the appendix.

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

Standard ICFP paper structure:

1. **Introduction** — Problem, motivation, contributions (enumerate contributions explicitly)
2. **Background** — Technical context, functional programming foundations
3. **Language/Approach** — Core definitions, type system, semantics
4. **Technical Development** — Proofs, metatheory
5. **Implementation** — Compiler/interpreter details, optimization
6. **Evaluation** — Experimental results (if applicable)
7. **Related Work** — Positioning against prior art
8. **Conclusion** — Summary and future work
9. References

## Theorem Environments

ICFP papers commonly use formal reasoning environments:

```latex
\theoremstyle{plain}
\newtheorem{definition}{Definition}
\newtheorem{property}{Property}

\theoremstyle{plain}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}
\newtheorem*{proposition}{Proposition}
\newtheorem*{corollary}{Corollary}

\theoremstyle{plain}
\newtheorem*{invariant}{Invariant}
```

Use `\qed` (from amsthm) to close proofs.

## Code Listings

ICFP papers typically include Haskell, OCaml, or other functional code:

```latex
% Inline code:
The function \lstinline!map! applies a transformation to each element.

% Code blocks:
\begin{lstlisting}[language=Haskell, caption={Higher-order list processing}, label={lst:haskell}]
map :: (a -> b) -> [a] -> [b]
map _ []     = []
map f (x:xs) = f x : map f xs
\end{lstlisting}

% OCaml example:
\begin{lstlisting}[language=caml, caption={Polymorphic variant usage}, label={lst:ocaml}]
type color = [`Red | `Green | `Blue]
let hex_of_color : color -> string = function
  | `Red -> "#ff0000"
  | `Green -> "#00ff00"
  | `Blue -> "#0000ff"
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
