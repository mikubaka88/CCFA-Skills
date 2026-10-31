# SIGGRAPH Venue Guide

> Migrated from the legacy `ccf-conference-skills/siggraph/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `siggraph` |
| Venue family | Graphics |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/SIGGRAPH/acmart.cls` |
| Official URL | https://s2026.siggraph.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Domain guidance retained; obsolete policy blocks removed. Query the target official requirements before formatting. |

## Usage Boundary

- Use this file for domain writing guidance. Annual submission rules are resolved through `ccf-submission-checker`, not copied from historical templates.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Match the exact year/track/stage before applying any format change; reuse current verified official rules and preserve supplied verified templates.

## Migrated Venue Notes

# SIGGRAPH 2026 Conference Writing Skill

**CCF-A | Graphics | Publisher: ACM**
**Conference:** https://s2026.siggraph.org
**Historical template:** See the local path above for examples only; it is not a verified target submission bundle.

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

Use visual or quantitative comparisons according to the claimed graphics contribution. The example below illustrates their presentation; its dataset, metric values, and significance notation are not evidence for a new manuscript:

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

## Content Checklist

- [ ] High-quality, grayscale-legible figures
- [ ] Detailed captions on all figures
- [ ] Quantitative evaluation included
- [ ] References list all authors
