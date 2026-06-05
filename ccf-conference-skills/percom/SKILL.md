---
name: percom
description: Writing and formatting guidance for PerCom (IEEE International Conference on Pervasive Computing and Communications) papers. Use when drafting, formatting, or submitting to PerCom 2026. Covers IEEEtran.cls conference format, double-blind anonymity with peerreview mode, CCS Concepts for ACM-published proceedings, page limits, reference formatting with IEEEtran BibTeX style, and camera-ready preparation. PerCom is a CCF-B conference on pervasive computing published by IEEE.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# PerCom 2026 Conference Writing Skill

**CCF-B | Pervasive / HCI | Publisher: IEEE**
**Conference:** https://www.computer.org/percom
**Template:** `PERCOM/IEEEtran.cls`

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind peer review) ===
\documentclass[10pt,conference,peerreviewca]{IEEEtran}

% === CAMERA-READY MODE ===
\documentclass[10pt,conference]{IEEEtran}

% Required packages
\usepackage{cite}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{url}
```

### Required Packages

```latex
\usepackage{cite}              % IEEE citation style
\usepackage{amsmath}           % Math
\usepackage{graphicx}         % Figures
\usepackage{booktabs}         % Professional tables
\usepackage{url}               % URLs in references
\usepackage{microtype}         % Improved typography
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **6 pages** (typical, check CFP) |
| References | No limit |
| Appendix | Not typically permitted |

Always check the official CFP for the exact page limit. IEEE conferences may have varying limits.

## Anonymity Requirements

PerCom uses a **double-blind peer review** process. Use the `peerreviewca` class option:

1. No author names or affiliations in the submission
2. Use third-person self-citations
3. Anonymize all URLs
4. Clear PDF metadata
5. Remove acknowledgments from the submission

## Title and Author Formatting

```latex
% Camera-ready (all authors visible):
\title{Your Paper Title}

\author{
  \IEEEauthorblockN{First Author}
  \IEEEauthorblockA{Department\\
    University\\
    email@example.com}
  \and
  \IEEEauthorblockN{Second Author}
  \IEEEauthorblockA{Department\\
    University\\
    email2@example.com}
}
```

## Camera-Ready Differences

After acceptance:

1. Remove the `peerreviewca` option
2. Add author names and affiliations
3. Add `\IEEEmembership{}` if needed
4. Include the standard IEEE copyright notice (typically added by the conference)

## Section Organization

1. **Introduction** — Problem, motivation, contributions
2. **Background & Related Work** — Prior pervasive computing research
3. **System Design / Approach** — The pervasive computing system or technique
4. **Implementation** — Technical details
5. **Evaluation** — Experiments, deployment study, or user study
6. **Discussion** — Implications, limitations
7. **Conclusion**
8. References

## Figures and Tables

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/system-overview}
  \caption{System architecture overview.}
  \label{fig:system}
\end{figure}

\begin{table}[t]
  \caption{Performance comparison.}
  \label{tab:results}
  \centering
  \begin{tabular}{lcc}
    \toprule
    Method & Accuracy & Latency \\
    \midrule
    Baseline & 85.2 & 12ms \\
    Ours & 91.7 & 8ms \\
    \bottomrule
  \end{tabular}
\end{table}
```

- Use vector formats (.pdf, .eps) where possible
- Ensure grayscale legibility
- Caption **below** figures, **above** tables

## References

IEEEtran uses numbered citations:

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}

% Citations:
\citep{key}    % [1]
\citep{key1,key2}  % [1,2]
```

## Formatting Rules

- **Paper size:** US Letter
- **Font:** 10pt default, Times New Roman recommended
- **Margins:** Top 0.75in, bottom 1in, left/right 0.75in or 1in (check CFP)
- **Columns:** Two-column format

## Submission Checklist

- [ ] `\documentclass[10pt,conference,peerreviewca]{IEEEtran}`
- [ ] No author identification in submission
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] Compiles with `pdflatex`
- [ ] References in IEEEtran format
