# ICLR Venue Guide

> Migrated from the legacy `ccf-conference-skills/iclr/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `iclr` |
| Venue family | AI |
| CCF tier | CCF-A |
| Template | ICLR 2027 official style bundle; obtain it from the Author Guidelines before building. The bundled local style is for 2026 only. |
| Official URL | https://iclr.cc/Conferences/2027/AuthorGuidelines |
| Last verified | 2026-09-16 against the 2027 author/reviewer policies and official style bundle. |
| Source status | Year-specific guidance verified; recheck official policy before real submission. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.
- Select the requested year explicitly. The examples below target 2027; do not rename the bundled 2026 style or silently use it for 2027. Download the complete official bundle, including its bibliography style, into the task's established source directory and preserve project build paths.

## ICLR 2027 Adaptation

Verified source records: `iclr-2027-author-guidelines`, `iclr-2027-reviewer-guidelines`, `iclr-2027-ai-authors`, `iclr-2027-ai-reviewers`, and `iclr-2027-style-files` in the shared source registry. Read only the policy relevant to the task.

- Abstract deadline: September 18, 2026; full paper: September 25, 2026, both 23:59 AoE. Use the current Author Guidelines for dates; the reviewer FAQ still contains a conflicting September 16 example.
- Keep required prerequisites and all material review findings. Prioritize issues that can change the recommendation; avoid unrelated experiments and citation lists. Preserve the existing CCFA review structure and contribution-aware rubric.
- See the AI-use requirements below when drafting or checking a full submission. An author's internal pre-review remains distinct from an official assigned review.

### Existing ICLR 2026 Projects

Keep `ccf-latex-templates/ICLR/iclr2026_conference.sty` for projects explicitly targeting 2026, with the default review mode and `\iclrfinalcopy` for camera-ready. Use the complete matching official bundle when dependencies are missing or rendered headers differ. Consult the existing `iclr-2026-author-guide` source record for historical policy. Do not impose the 2027 AI-disclosure rules on a 2026 project.

## Double-Blind Review

ICLR 2027 reviews are double-blind; OpenReview hosting does not make the submission non-anonymous.

This means:
1. Use the default `iclr2027_conference` style for under-review submissions; add `\iclrfinalcopy` only for camera-ready.
2. Do not include author names, affiliations, acknowledgments, funding details, or identifying project links in the submitted PDF.
3. Cite prior work, including the authors' own public work, in the third person when needed.
4. Keep private code, supplementary, and artifact links anonymized until the venue permits de-anonymization.
5. Verify current official policy before final submission because OpenReview visibility and de-anonymization rules can change by year.

## Document Setup

### Preamble Structure

```latex
\documentclass{article}
\usepackage{iclr2027_conference,times}         % Submission/review
% \iclrfinalcopy                              % Enable only for camera-ready

% Additional packages:
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}                            % If theorem environments are used
\newtheorem{assumption}{Assumption}
\newtheorem{theorem}{Theorem}
\usepackage{hyperref}
\usepackage{url}
```

### Mode Options

| Mode | Option | Effect |
|------|--------|--------|
| Submission | default style | Under-review header and anonymous author block |
| Camera-Ready | `\iclrfinalcopy` | Published header and visible author block |

### Conditional Content

Use `\ificlrfinal` for content that differs between versions:

```latex
\ificlrfinal
  % Camera-ready specific content
  \section*{Acknowledgments}
\else
  % Submission specific content
\fi
```

## Page Limits

- ICLR 2027 submission: 9 pages for the main text, excluding references and appendix.
- Discussion and camera-ready versions: 10 pages for the main text, excluding references and appendix.
- Appendices and supplementary material are allowed but must follow current official instructions.
- Always re-check the official Author Guide before real submission.

## AI Use Statement (2027)

Include the mandatory AI-use section and consistent submission-form answers, including when no disclosable use occurred. The section is outside the main-text budget; the official template limits it to one page. Record actual assistance and human checks, not blanket assurances. Required disclosure covers, among other tasks, hypotheses, methods/experiments, method implementation, proofs, data processing, result interpretation, and translation; figure creation and readability editing are recommended disclosures. Check the full official task list for borderline cases. Do not assume translation is exempt polishing.

Use the existing manuscript and task history; create no separate ledger by default. Ask only for missing usage facts needed to finalize the statement; leave those facts explicitly unresolved meanwhile. Humanization and compression must retain the disclosure and its substance. Never invent non-use or completed human verification.

## Title and Author Formatting

```latex
\title{Your Paper Title Here}

% Multi-author with \And and \AND:
\author{
  Anonymous Authors
}
```

### Affiliation Formatting

```latex
% Camera-ready author block; submission uses the anonymous block above.
\author{
  Author Name \\
  Institution Name \\
  \texttt{author@example.org}
  \And
  Coauthor Name \\
  Institution Name
}
```

## Abstract and Keywords

```latex
\begin{abstract}
Your abstract here. Follow the current submission form's length constraint.
Explain the problem, approach, and main contributions.
ICLR reviewers read abstracts carefully — make it compelling.
\end{abstract}

```

Supply keywords in the submission form when requested. The official style does not define a `\keywords` command.

## Layout

Use the official single-column layout and `\maketitle`. Keep the style's margins, font sizes, and line spacing. Align figures to the available text width without shrinking labels below readability.

## Recommended ICLR Paper Structure

ICLR values clear, well-motivated papers with strong empirical and/or theoretical contributions. Adapt the outline to the actual contribution; empirical sections and SOTA claims are not universal requirements. Replace illustrative claims only with supplied evidence.

```latex
\section{Introduction}
% Paragraph 1-2: Problem and motivation
% Why is this problem important? What are the limitations of current approaches?

% Paragraph 3: Our approach
% What is the key insight? How does our approach work?
% What are the key contributions?

% Paragraph 4: Contributions (numbered)
The main contributions of this paper are:
\begin{itemize}
    \item We propose a novel approach to X that addresses Y...
    \item We provide theoretical analysis showing Z...
    \item We demonstrate through extensive experiments that...
\end{itemize}

% Paragraph 5 (optional): Roadmap
The remainder of this paper is organized as follows...

\section{Background and Motivation}
% Necessary context and notation
% Review of prior work and its limitations
% Clearly articulate the gap our work fills

\section{Method}
% Core technical contribution
% Include figures showing architecture/pipeline
% Mathematical formulation with clear equations
% Ablation-ready component design

\section{Theoretical Analysis (if applicable)}
% Formal guarantees, convergence proofs, complexity analysis
% Clear assumptions stated upfront

\section{Experiments}
\subsection{Setup}
% Datasets, metrics, baselines, implementation details
% All details necessary for reproducibility

\subsection{Main Results}
% Present main findings
% Compare against strong baselines
% Include statistical significance

\subsection{Ablation and Analysis}
% Study each component's contribution
% Error analysis, qualitative examples
% Sensitivity analysis

\section{Related Work}
% Position against existing literature
% Categorize by approach, not just list

\section{Conclusion}
% Summary, limitations, future directions
```

## References (natbib with authoryear)

The official style uses `natbib` with author-year citations:

```latex
% In document:
\bibliographystyle{iclr2027_conference}
\bibliography{references}

% Citations:
\citet{Author20}    % Author (2020)
\citep{Author20}    % (Author, 2020)
```

## Figures and Tables

```latex
% Figure within the official single-column text width
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.8\linewidth]{figure}
  \caption{Figure caption here.}
  \label{fig:example}
\end{figure}

% Table with booktabs:
\begin{table}[htbp]
  \caption{Table caption above.}
  \label{tab:example}
  \centering
  \begin{tabular}{ccc}
    \toprule
    Col1 & Col2 & Col3 \\
    \midrule
    data & data & data \\
    \bottomrule
  \end{tabular}
\end{table}
```

## ICLR-Specific Writing Conventions

### What ICLR Reviewers Value

1. **Clear motivation**: Why should we care about this problem?
2. **Novelty**: What is the new insight or approach?
3. **Theoretical depth**: Formal analysis and guarantees
4. **Empirical rigor**: Thorough experiments with strong baselines
5. **Reproducibility**: Sufficient detail to reproduce results
6. **Clarity**: Well-written, well-organized paper

### Theoretical Writing for ICLR

```latex
\section{Theoretical Analysis}

\begin{assumption}
\label{assum:1}
[State your assumptions clearly]
\end{assumption}

\begin{theorem}
\label{them:main}
Under Assumption \ref{assum:1}, the algorithm converges at rate...
\end{theorem}

\begin{proof}
State the proof here.
\end{proof}
```

### Experimental Rigor

```latex
\section{Experiments}

\subsection{Setup}
\textbf{Datasets:} [Actual datasets, splits, preprocessing, and metrics.]

\textbf{Baselines:} We compare against:
\begin{itemize}
    \item Standard methods from literature
    \item State-of-the-art approaches on each benchmark
    \item Ablation variants of our method
\end{itemize}

\textbf{Implementation:} [Actual software, hardware, and tuning protocol.]

\textbf{Statistics:} [Actual runs and appropriate uncertainty estimates.]

\subsection{Main Results}
[Describe only the supplied results and the comparisons they support.]

\subsection{Ablation Study}
\autoref{tab:ablation} shows the contribution of each component.
```

## OpenReview-Specific Requirements

Keep the review PDF, metadata, and supplementary material anonymous. Author identities belong in the private submission-form fields, not in the review PDF. Restore the author block only for camera-ready.

### Dual Submission Policy

ICLR has strict dual submission rules:
- Cannot submit the same paper to ICLR and another venue simultaneously
- Withdrawing only after acceptance does not cure a prohibited parallel submission
- Posting a preprint on arXiv is permitted
- Check current CFP for exact rules

### Preprint/ArXiv Policy

An arXiv preprint can coexist with anonymous review. Cite relevant prior work in third person and keep identifying cross-links out of the submitted version.

## Rebuttal Period

ICLR has an author discussion period. Use `ccf-rebuttal-writer` for responses grounded in the actual review and revision. The sketch below is conditional: include an action or result only after verifying it occurred.

### Rebuttal Structure

```latex
\section*{Response to Reviewers}

We thank the reviewers for their thoughtful comments and detailed feedback.

\textbf{Regarding Reviewer X's concern about Y:}
We appreciate this observation. To address this concern, we:

\begin{itemize}
    \item [Answer the concern using available evidence and its location.]
    \item [Identify any completed manuscript change and its location.]
    \item [State a remaining limitation when it affects the claim.]
\end{itemize}

\textbf{Regarding the comparison with method A:}
[Report an actual comparison, or explain what remains untested.]

\textbf{Regarding the theoretical assumptions:}
[Explain the supported assumptions and any verified proof correction.]
```

### Rebuttal Best Practices

**DO:**
- Thank reviewers for their time
- Address every concern specifically
- Provide new evidence when asked
- Be humble and constructive
- Clarify misunderstandings politely

**DON'T:**
- Be defensive or dismissive
- Argue about scores
- Make excuses
- Promise changes you can't deliver
- Be rude or aggressive

## Camera-Ready Compilation

```latex
\usepackage{iclr2027_conference,times}
\iclrfinalcopy
```

For camera-ready:
1. Remove line numbers
2. Add acknowledgments
3. Update author information if needed
4. Ensure all author affiliations are correct
5. Add supplementary materials if needed

### Camera-Ready Checklist

- [ ] Enabled `\iclrfinalcopy` with the correct year's style
- [ ] All author information complete and correct
- [ ] Acknowledgments section added
- [ ] Funding disclosures included
- [ ] No confidential information remaining
- [ ] PDF compiles without errors

## Formatting Rules

- **Paper size:** US Letter
- **Font:** Times family via the official preamble's `times` package
- **Text:** 10pt
- **Margins:** Standard conference margins
- **Columns:** Single-column format
- **Line spacing:** Check style file defaults

## Submission Process

1. Use the exact year's OpenReview portal from its Author Guidelines.
2. Check current author-registration, quota, and reciprocal-review requirements before final readiness.
3. Check the anonymous PDF and supplementary package, including required disclosures.
4. Author response and camera-ready follow the venue's stage-specific instructions.

## Checklist Before Submission

- [ ] Author identities hidden in the review PDF, metadata, and supplementary material
- [ ] PDF compiles without errors
- [ ] Abstract is clear and compelling
- [ ] Required AI-use section and submission-form answers complete and consistent
- [ ] References in correct format
- [ ] Figures/tables properly formatted
- [ ] No confidential information that shouldn't be public
- [ ] No prohibited concurrent archival submission
- [ ] All notation defined before use
- [ ] Baselines properly documented
- [ ] Uncertainty and ablations support the claims where applicable
- [ ] Reproducibility details provided
