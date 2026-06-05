---
name: fse
description: Writing and formatting guidance for ESEC/FSE (European Software Engineering Conference / ACM SIGSOFT Symposium on the Foundations of Software Engineering). Use when drafting, formatting, or submitting to FSE. Covers ACM acmart with sigconf format, anonymous double-blind review mode, FSE page limits, software engineering conventions, camera-ready preparation with DOI/ISBN, and ACM-Reference-Format citations.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# ESEC/FSE Conference Writing Skill

**CCF-A | SE | Publisher: ACM**
**Conference:** https://conf.researchr.org/track/fse-2026/fse-2026-papers
**Template:** `FSE/acmart.cls` (ACM acmart, SIGCONF format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigconf,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigconf]{acmart}
\setcopyright{acmlicensed}
\acmConference[FSE 2026]{Proceedings of the 30th European Software Engineering
  Conference and the 30th ACM SIGSOFT Symposium on the Foundations of
  Software Engineering}{September 5--11, 2026}{Singapore}
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
| References | No limit |
| Appendix | Permitted (not counted) |

FSE enforces a strict 14-page limit for the main body. References and appendix do not count toward this limit, but reviewers are not required to read the appendix.

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

Standard FSE paper structure:

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

FSE papers may include formal reasoning:

```latex
\theoremstyle{plain}
\newtheorem{definition}{Definition}
\newtheorem{property}{Property}

\theoremstyle{plain}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}
\newtheorem*{corollary}{Corollary}

\theoremstyle{plain}
\newtheorem*{invariant}{Invariant}
```

## Code Listings

```latex
% Inline code:
The linter uses \lstinline!AST.Visitor! to traverse the parse tree.

% Code blocks:
\begin{lstlisting}[language=Python, caption={Bug detection pattern}, label={lst:pattern}]
class BugDetector(ast.NodeVisitor):
    def __init__(self):
        self.bugs = []

    def visit_Call(self, node):
        if self._is_unsafe(node):
            self.bugs.append(node)
        self.generic_visit(node)
\end{lstlisting}
```

## Figures and Tables

- Use vector formats (.pdf) where possible
- Ensure figures are legible in grayscale
- Number figures and tables sequentially
- Captions should be descriptive and self-contained

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/architecture}
  \caption{System architecture showing the main components and data flow.}
  \label{fig:architecture}
\end{figure}
```

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

- [ ] 14 pages or fewer (main body)
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
