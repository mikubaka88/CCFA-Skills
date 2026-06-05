---
name: sigmod
description: Writing and formatting guidance for SIGMOD (ACM SIGMOD International Conference on Management of Data) papers. Use when drafting, formatting, or submitting to SIGMOD 2026. Covers ACM acmart sigconf format with double-blind review mode, SIGMOD page limits (10 pages), PVLDB reference format for journal track, theorem environments for theoretical results, and ACM camera-ready requirements.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# SIGMOD 2026 Conference Writing Skill

**CCF-A | DB | Publisher: ACM**
**Conference:** https://sigmod.org/sigmod-2026
**Template:** `SIGMOD/acmart.cls` (ACM acmart, sigconf format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigconf, review, anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigconf]{acmart}
\acmConference[SIGMOD 2026]{SIGMOD '26: 2026 ACM SIGMOD International...}
               {June 22--27, 2026}{Chicago, IL, USA}
\acmISBN{978-X-XXXX-XXXX-X/XX/XX}
\acmDOI{10.5555/XXXXXXX.XXXXXXX}
```

### Required Packages

```latex
\usepackage[round]{natbib}     % Author-year citations
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{listings}
\lstset{basicstyle=\small\ttfamily}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{balance}
\usepackage{cleveref}          % For consistent cross-references
\usepackage{algorithm}
\usepackage[noend]{algorithmic}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **10 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

SIGMOD enforces a strict 10-page limit for the main body. References and appendix do not count toward this limit, but reviewers are not required to read the appendix.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. No author names or affiliations in submission
2. Third-person self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs, GitHub links, personal pages
4. Clear PDF metadata
5. Remove acknowledgments

## Camera-Ready Differences

After acceptance:

1. Remove `review` and `anonymous` options
2. Fill in `\acmConference`, `\acmISBN`, `\acmDOI`
3. Restore all author names and affiliations
4. Add appropriate `\setcopyright` mode
5. Enable page numbers with `\settopmatter{printfolios=true}`

## Section Organization

SIGMOD papers typically follow a database-systems paper structure:

1. **Introduction** — Problem, motivation, contributions (enumerate explicitly)
2. **Background & Preliminaries** — System model, definitions, assumptions
3. **Problem Statement** — Formal problem definition where applicable
4. **Proposed Approach / Design** — Core technical contribution
5. **Implementation** — System details, complexity, optimization choices
6. **Evaluation** — Experimental methodology, benchmarks, comparisons
7. **Related Work** — Positioning against prior database systems work
8. **Conclusion**
9. References
10. Appendix (optional)

## Theorem Environments

SIGMOD papers commonly include formal reasoning:

```latex
\theoremstyle{plain}
\newtheorem{definition}{Definition}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}
\newtheorem*{corollary}{Corollary}

\theoremstyle{plain}
\newtheorem{property}{Property}
```

## Algorithm Formatting

Use `algorithm` and `algorithmic` environments with `noend` option:

```latex
\begin{algorithm}[t]
\caption{Query Optimization Algorithm}
\label{alg:query-opt}
\begin{algorithmic}[1]
\STATE $Q \gets \text{parse}(query)$
\STATE $P \gets \text{init\_plan}(Q)$
\FOR{$i \in \{1, \dots, k\}$}
    \STATE $P \gets \text Refine$(P)
\ENDFOR
\RETURN $P$
\end{algorithmic}
\end{algorithm}
```

## Figures and Tables

- Vector formats (.pdf) for diagrams and system architectures
- Ensure grayscale legibility (reviewers often print in B&W)
- Number sequentially
- Use `booktabs` for tables (no vertical rules)
- Caption below figures, above tables
- Self-contained captions that explain the figure independently

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/system-arch}
  \caption{System architecture showing the query processor,
    storage engine, and transaction manager components.}
  \label{fig:system-arch}
\end{figure}
```

## References (natbib)

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\citet{garcia-molina}  % Garcia-Molina et al. (2008)
\citep{garcia-molina}  % (Garcia-Molina et al. 2008)
```

All references must list **every author by full name**.

## Formatting Rules

- **Format:** ACM sigconf (two-column, single-spaced)
- **Paper size:** US Letter
- **Body font:** 9pt minimum, Times New Roman
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in
- **Line spacing:** Single-spaced (template default)

## Submission Checklist

- [ ] 10 pages or fewer (main body)
- [ ] `\documentclass[sigconf, review, anonymous]`
- [ ] All author identification removed
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs and code links
- [ ] Formal problem definition included where applicable
- [ ] References list all authors
- [ ] Grayscale-legible figures

## Camera-Ready Checklist

- [ ] Remove `review` and `anonymous` options
- [ ] Add conference metadata (`\acmConference`, `\acmISBN`, `\acmDOI`)
- [ ] Restore author information
- [ ] Enable page numbers (`\settopmatter{printfolios=true}`)
- [ ] Add acknowledgments if desired
