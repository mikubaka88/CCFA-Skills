---
name: cade
description: Writing and formatting guidance for CADE (International Conference on Automated Deduction) conference papers. Use when drafting, formatting, or submitting to CADE 2026. Covers Springer LNCS llncs class, theorem proving conventions (theorem environments, proofs, inference rules), page limits, and camera-ready submission requirements.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CADE 2026 Conference Writing Skill

**CCF-B | Theorem Proving | Publisher: Springer**
**Conference:** https://cade2026.compute.dela
**Template:** `CADE/llncs.cls` (Springer LNCS)

## Document Setup

### Preamble Structure

```latex
\documentclass[envcountsame]{llncs}

\usepackage{makeidx}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{graphicx}
\usepackage{url}
\usepackage{hyperref}
\hypersetup{colorlinks=true}
```

### Springer LNCS Options

| Option | Description |
|--------|-------------|
| `envcountsame` | Number theorem-like environments per section |
| `envcountreset` | Reset theorem counters per section |
| `runningheads` | Short titles in page headers |

## Page Limits

|| Section | Limit |
|---------|-------|
| Main paper | **15 pages** |
| References | No specific limit |

CADE typically allows 15 pages for the main content. Check the official CFP for the current year's exact limits.

## Title and Author Formatting

```latex
\title{Your Paper Title Here}

\author{First Author\inst{1} \and
        Second Author\inst{2}}

\institute{
  Institution 1\\
  \email{author1@example.com}
  \and
  Institution 2\\
  \email{author2@example.com}
}
```

## Abstract

```latex
\begin{document}
\maketitle

\begin{abstract}
Your abstract here. Summarize the problem, approach, and main results.
\keywords{keyword1, keyword2, keyword3}
\end{abstract}
```

## Section Organization

Standard CADE paper structure:

1. **Abstract** — Summary of problem, approach, and results
2. **Introduction** — Problem, motivation, contributions
3. **Preliminaries** — Formal definitions and notation
4. **Background** — Related systems and approaches
5. **Main Contribution** — Core technical contribution
6. **Implementation** (optional) — System details
7. **Evaluation** — Experimental results
8. **Related Work** — Comparison with prior work
9. **Conclusion** — Summary and future work
10. References

## Theorem Environments

CADE papers emphasize formal reasoning:

```latex
\theoremstyle{plain}
\newtheorem{conjecture}{Conjecture}
\newtheorem{problem}{Problem}
\newtheorem{property}{Property}

\theoremstyle{plain}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}
\newtheorem*{corollary}{Corollary}
\newtheorem*{proposition}{Proposition}
\newtheorem*{claim}{Claim}

\theoremstyle{Proof}
\newtheorem{Proof}{Proof}
```

## Inference Rules

CADE papers often use inference rules:

```latex
\begin{figure}
\infrule[RuleName]
  {Premise$_1$ \quad Premise$_2$}
  {Conclusion}

\infrule
  {\forall x. P(x)}
  {P(t)}
  {\rulename{Inst}}
\end{figure}
```

## Figures and Tables

```latex
\begin{figure}[t]
\centering
includegraphics[width=0.8\linewidth]{fig/system}
\caption{System architecture.}
\label{fig:system}
\end{figure}
```

- Use PDF, PNG, or EPS
- Ensure grayscale legibility
- Self-contained captions
- Use `booktabs` for tables (no vertical rules)

## References (natbib)

```latex
\bibliographystyle{spbasic}  % Springer basic style
\bibliography{references}

\citet{smith2023}      % Smith et al. (2023)
\citep{smith2023}      % (Smith et al. 2023)
```

## Formatting Rules

- **Format:** Two-column, single-spaced
- **Paper size:** A4
- **Body font:** 10pt
- **Margins:** 2.5cm all around

## Submission Checklist

- [ ] 15 pages or fewer (main body)
- [ ] Springer LNCS llncs document class
- [ ] Abstract and keywords included
- [ ] All figures in .pdf/.png/.eps format
- [ ] References in correct format
- [ ] Compiles with `pdflatex`
