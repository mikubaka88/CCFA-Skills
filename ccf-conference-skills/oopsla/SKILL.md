---
name: oopsla
description: Writing and formatting guidance for OOPSLA (ACM SIGPLAN Conference on Object-Oriented Programming, Systems, Languages, and Applications). Use when drafting, formatting, or submitting to OOPSLA. Covers ACM acmart with sigplan format, anonymous double-blind review mode, OOPSLA page limits (12 pages), formal semantics, theorem environments, code listings, camera-ready preparation with DOI/ISBN, and ACM-Reference-Format citations.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# OOPSLA Conference Writing Skill

**CCF-A | SE/PL | Publisher: ACM**
**Conference:** https://2026.esec-fse.org/track/oopsla-2026
**Template:** `OOPSLA/acmart.cls` (ACM acmart, SIGPLAN format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigplan,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigplan]{acmart}
\setcopyright{acmlicensed}
\acmConference[OOPSLA 2026]{Proceedings of the 2026 ACM SIGPLAN Conference on
  Object-Oriented Programming, Systems, Languages, and Applications}{October 19--25, 2026}{Chicago, IL, USA}
\acmISBN{978-X-XXXX-XXXX-X/26/10}
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

OOPSLA enforces a strict 12-page limit for the main body. References and appendix do not count toward this limit, but reviewers are not required to read the appendix.

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

Standard OOPSLA paper structure:

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

OOPSLA papers commonly use formal reasoning:

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

## Code Listings

OOPSLA papers typically include object-oriented code:

```latex
% Inline code:
The method \lstinline!accept()! implements the visitor pattern.

% Code blocks:
\begin{lstlisting}[language=Java, caption={Visitor pattern implementation}, label={lst:visitor}]
interface Visitor<R> {
    R visitConcreteA(ConcreteA a);
    R visitConcreteB(ConcreteB b);
}

interface Element {
    <R> R accept(Visitor<R> v);
}

class ConcreteA implements Element {
    public <R> R accept(Visitor<R> v) {
        return v.visitConcreteA(this);
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
