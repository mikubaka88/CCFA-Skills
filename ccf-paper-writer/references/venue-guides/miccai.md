# MICCAI Venue Guide

> Migrated from the legacy `ccf-conference-skills/miccai/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-venue-format-guide`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `miccai` |
| Venue family | Medical Imaging / AI |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/MICCAI/MICCAI2026-main conference paper template.tex` |
| Official URL | https://miccai2026.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# MICCAI 2026 Conference Writing Skill

**CCF-B | Medical Imaging / AI | Publisher: Springer**
**Conference:** https://miccai2026.org
**Template:** `MICCAI/MICCAI2026-main conference paper template.tex` (modified llncs.cls)

> **Important:** The MICCAI template is pre-configured for **double-blind submission**. The author block is already anonymized. Do not remove or modify it to gain extra writing space — doing so will lead to desk rejection.

## Document Setup

### Preamble Structure

The MICCAI template is pre-configured for anonymized submission. Use it as-is:

```latex
\documentclass[runningheads]{llncs}

\usepackage[T1]{fontenc}
\usepackage{graphicx,verbatim}
```

### Author Block (Pre-anonymized)

The template provides a pre-anonymized author block. For submission, use:

```latex
\author{Anonymized Authors}
\authorrunning{Anonymized Author et al.}
\institute{Anonymized Affiliations \\
    \email{email@anonymized.com}}
```

For camera-ready, restore real author information:

```latex
\author{First Author\inst{1}\orcidID{0000-1111-2222-3333} \and
Second Author\inst{2}\orcidID{1111-2222-3333-4444}}

\authorrunning{F. Author et al.}

\institute{Institution 1\\
    email@example.com \and
    Institution 2\\
    email2@example.com}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main content | **8 pages** (text, figures, tables, abstract, keywords, acknowledgments) |
| References | **up to 2 pages** |
| Supplementary materials | **Multimedia only** (videos); no PDF supplementary |

**Important:**
- Acknowledgments and disclaimer **count toward the 8-page limit** if included in the submission
- The reference section does not need to start on a new page
- PDF supplementary materials are **not allowed** in 2026 unless citing an unpublished paper

## Anonymity Requirements

MICCAI uses **strict double-blind review**:

1. Do **not** modify or remove the provided anonymized author section
2. Cite your own prior work in **third person**
3. Anonymize **all** URLs (GitHub repositories, dataset links)
4. Mask data collection locations for private datasets
5. Ensure supplementary materials (videos) contain **no identifying information**
6. Clear PDF metadata
7. Do not upload anonymized drafts to public repositories

## Abstract and Keywords

```latex
\begin{abstract}
  The abstract should briefly summarize the contents of the paper
  in 150--250 words. If you include a repository link, ensure it is
  anonymized for the double-blind review phase.
\end{abstract}

\keywords{First keyword \and Second keyword \and Another keyword.}
% Authors must provide keywords and are not allowed to remove this section.
```

## Section Organization

MICCAI papers typically follow this structure:

1. **Introduction** — Medical/clinical problem, motivation, contributions
2. **Related Work** — Prior medical imaging research
3. **Methods** — Proposed model, architecture, training procedure
4. **Experiments / Results** — Datasets, evaluation metrics, comparisons with state-of-the-art
5. **Discussion** — Clinical significance, limitations
6. **Conclusion**
7. References
8. Acknowledgments (counts toward page limit)
9. Disclosure of Interests (counts toward page limit)

## Figures and Tables

```latex
\begin{figure}
  \centering
  \includegraphics[width=0.8\linewidth]{fig1}
  \caption{A figure caption placed below the illustration.}
  \label{fig:sample}
\end{figure}
```

Rules:
- **No inline figures** (wrapping text around figures is not allowed)
- **Minimum 8pt font size** for table text
- Tables must not be inserted as figures
- Ensure figures and tables do not extend into the margins
- Use EPS or vector formats where possible

## References (numbered)

LNCS uses **numbered citations** with `splncs04.bst`:

```latex
\bibliographystyle{splncs04}
\bibliography{references}

% Citations:
\cite{key}      % [1]
\cite{key1,key2}  % [1,2]
```

## Theorem Environments

```latex
\begin{theorem}
  This is a sample theorem.
\end{theorem}

\begin{proof}
  Proof text...
\end{proof}
```

MICCAI supports: `theorem`, `definition`, `lemma`, `proposition`, `corollary`, `remark`, `example`.

## Disallowed Formatting

The following are **strictly prohibited** and will result in desk rejection:

- `\vspace` or `\hspace` commands to reduce whitespace
- Changing default margins, font size, or font type
- Inline figures (wrapping text)
- Tables inserted as figures
- PDF supplementary materials (unless citing unpublished work)
- Modifying the anonymized author section

## Camera-Ready Checklist

After acceptance:

- [ ] Remove the anonymized author block and insert real author names, affiliations, and ORCID IDs
- [ ] Restore acknowledgments and disclosure of interest sections
- [ ] Verify total page count (main content ≤ 8 pages, references ≤ 2 pages)
- [ ] Ensure all author-provided keywords are included
- [ ] Check that figures/tables do not extend into margins
- [ ] Remove anonymity from any repository links

## MICCAI-Specific Writing Conventions

- **Clinical relevance**: Clearly explain the medical/clinical significance
- **Datasets**: Describe medical imaging datasets (source, modality, size, demographics)
- **Evaluation metrics**: Report standard medical imaging metrics (Dice score, IoU, sensitivity, specificity)
- **Statistical reporting**: Include mean ± standard deviation, p-values where appropriate
- **Reproducibility**: Include key hyperparameters, preprocessing pipeline, and model architecture details
- **Visual quality**: High-quality figures are essential; include representative slices/3D views
