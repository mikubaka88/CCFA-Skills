---
name: dasfaa
description: Writing and formatting guidance for DASFAA (Database Systems for Advanced Applications) conference papers. Use when drafting, formatting, or submitting to DASFAA 2026. Covers Springer LNCS llncs class with two-column format, page limits, natbib citation commands, figure/table formatting, and camera-ready submission requirements.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# DASFAA 2026 Conference Writing Skill

**CCF-B | DB | Publisher: Springer**
**Conference:** https://www DASFAA2026.org
**Template:** `DASFAA/llncs.cls` (Springer LNCS)

## Document Setup

### Preamble Structure

```latex
\documentclass[envcountsame, r運行]{llncs}

\usepackage{llncsdoc}
\usepackage{makeidx}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{graphicx}
\usepackage{url}
\usepackage{natbib}
\usepackage{hyperref}
\hypersetup{colorlinks=true}
```

### Springer LNCS Options

| Option | Description |
|--------|-------------|
| `envcountsame` | Number theorem-like environments per section |
| `envcountreset` | Reset theorem counters per section |
| `runningheads` | Short titles in page headers |
| `citeauthoryear` | Author-year citation style |

## Page Limits

|| Section | Limit |
|---------|-------|
| Main paper | **15 pages** |
| References | No specific limit |

DASFAA typically allows 15 pages for the main content. Check the official CFP for the current year's exact limits.

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
Keywords: keyword1, keyword2, keyword3
\end{abstract}
```

## Section Organization

Standard DASFAA paper structure:

1. **Abstract** — Summary of problem, approach, and results
2. **Introduction** — Problem, motivation, contributions
3. **Preliminaries** — Background and definitions
4. **Proposed Method** — Core contribution
5. **Theoretical Analysis** (optional) — Complexity, correctness
6. **Experimental Evaluation** — Datasets, baselines, results
7. **Related Work** — Comparison with prior work
8. **Conclusion** — Summary and future work
9. References

## Figures and Tables

```latex
\begin{figure}[t]
\centering
includegraphics[width=0.8\linewidth]{fig/example}
\caption{System architecture.}
\label{fig:architecture}
\end{figure}
```

- Use PDF, PNG, or EPS
- Ensure grayscale legibility
- Captions below figures, above tables
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
