# SIGGRAPH Venue Guide

> Migrated from the legacy `ccf-conference-skills/siggraph/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `siggraph` |
| Venue family | Graphics |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/SIGGRAPH/acmart.cls` |
| Official URL | https://s2026.siggraph.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# SIGGRAPH 2026 Conference Writing Skill

**CCF-A | Graphics | Publisher: ACM**
**Conference:** https://s2026.siggraph.org
**Template:** `SIGGRAPH/acmart.cls` (ACM acmart, siggraph format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[siggraph, review, anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[siggraph]{acmart}
\acmConference[SIGGRAPH 2026]{SIGGRAPH '26: ACM SIGGRAPH 2026 Conference}
               {July 27--31, 2026}{Vancouver, BC, Canada}
\acmISBN{978-X-XXXX-XXXX-X/XX/XX}
\acmDOI{10.5555/XXXXXXX.XXXXXXX}
```

SIGGRAPH uses the `siggraph` format option (single-column, larger page size for figures).

### Required Packages

```latex
\usepackage[round]{natbib}     % Author-year citations
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{balance}
\usepackage{cleveref}          % For consistent cross-references
\usepackage{xcolor}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **8 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

SIGGRAPH enforces a strict 8-page limit for the main body. References and appendix do not count toward this limit. This is one of the tightest page limits among top graphics venues.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. No author names or affiliations in submission
2. Third-person self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs, project pages, video links
4. Clear PDF metadata
5. Remove acknowledgments
6. Anonymize figures — remove author/affiliation watermarks

## Camera-Ready Differences

After acceptance:

1. Remove `review` and `anonymous` options
2. Fill in `\acmConference`, `\acmISBN`, `\acmDOI`
3. Restore all author names and affiliations
4. Add appropriate `\setcopyright` mode
5. Enable page numbers with `\settopmatter{printfolios=true}`

## Section Organization

SIGGRAPH papers typically follow a computer graphics paper structure:

1. **Abstract** — Concise summary of contribution (1 paragraph)
2. **Introduction** — Problem, prior work's limitations, contributions (enumerate explicitly)
3. **Previous Work / Background** — Technical foundations, related techniques
4. **Technical Approach** — Core algorithm, model, or system (the main contribution)
5. **Results & Validation** — Visual quality, quantitative evaluation, comparisons
6. **Limitations & Future Work**
7. **Conclusion**
8. References
9. Appendix (optional, e.g., additional technical details, proofs)

## Technical Approach

SIGGRAPH papers require deep technical depth. Structure the core contribution clearly:

```latex
\section{Technical Approach}
\subsection{Overview}
Our method builds on the observation that...

\subsection{Mathematical Formulation}
Given an input mesh $\mathcal{M}$, we compute the displacement field
$\mathbf{d}(\mathbf{v})$ for each vertex $\mathbf{v} \in \mathcal{M}$
using the energy functional:

\begin{equation}
  \label{eq:energy}
  E(\mathbf{d}) = \alpha E_{\text{smooth}}(\mathbf{d})
                 + \beta E_{\text{detail}}(\mathbf{d})
                 + \gamma E_{\text{constraint}}(\mathbf{d})
\end{equation}

where $E_{\text{smooth}}$ enforces $C^1$ continuity,
$E_{\text{detail}}$ preserves high-frequency details, and
$E_{\text{constraint}}$ enforces boundary conditions.

\subsection{Implementation}
The optimization in \autoref{eq:energy} is solved using a
conjugate gradient method with a pre-conditioned stiffness matrix.
The overall algorithm runs in $O(n \log n)$ time where $n$ is
the number of vertices.
```

## Visual Quality Standards

SIGGRAPH is known for high visual quality expectations:

- **Figures**: High-resolution, preferably vector-based (.pdf)
- **Images**: Minimum 300 DPI for raster images
- **Color**: Use perceptually uniform colormaps for quantitative plots
- **Grayscale**: Ensure all figures are legible in grayscale
- **Captions**: Detailed, self-contained captions that explain the figure

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=\linewidth]{figs/results-comparison}
  \caption{Comparison of our method against prior work on
    complex geometry. From left to right: input mesh, method
    of~\citet{smith2019}, method of~\citet{jones2020}, and our result.
    Notice the improved preservation of fine-scale geometric details
    while maintaining global structure smoothness.}
  \label{fig:results}
\end{figure}
```

## Quantitative Evaluation

SIGGRAPH papers should include both visual and quantitative comparisons:

```latex
\section{Results}
We evaluate our method on a benchmark of 100 meshes spanning
different geometry categories. We measure geometric accuracy using
Chamfer distance and Hausdorff distance, and we measure visual
quality using perceptual metrics.

\begin{table}[t]
  \caption{Quantitative comparison on benchmark meshes.
    Best results in bold. $\dagger$ indicates significance at $p < 0.01$.}
  \label{tab:quantitative}
  \begin{tabular}{lcccc}
    \toprule
    Method & Chamfer $\downarrow$ & Hausdorff $\downarrow$ & PSNR $\uparrow$ \\
    \midrule
    Baseline & 0.0234 & 0.0891 & 28.3 \\
    \citet{smith2019} & 0.0198 & 0.0712 & 31.2 \\
    \citet{jones2020} & 0.0156 & 0.0623 & 33.7 \\
    \textbf{Ours} & \textbf{0.0089} & \textbf{0.0412} & \textbf{38.1} \\
    \bottomrule
  \end{tabular}
\end{table}
```

## References (natbib)

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\citet{pharr}             % Pharr et al.
\citep{pharr}             % (Pharr et al.)
```

## Formatting Rules

- **Format:** ACM siggraph (single-column, two-column layout also accepted)
- **Paper size:** US Letter
- **Body font:** 9pt minimum, Times New Roman
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in
- **Single-column**: siggraph format uses single-column layout by default
- **High-resolution figures**: minimum 300 DPI for raster graphics

## Submission Checklist

- [ ] 8 pages or fewer (main body)
- [ ] `\documentclass[siggraph, review, anonymous]`
- [ ] All author identification removed
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs and video links
- [ ] High-quality, grayscale-legible figures
- [ ] Detailed captions on all figures
- [ ] Quantitative evaluation included
- [ ] References list all authors

## Camera-Ready Checklist

- [ ] Remove `review` and `anonymous` options
- [ ] Add conference metadata
- [ ] Restore author information
- [ ] Enable page numbers
- [ ] Add acknowledgments if desired
