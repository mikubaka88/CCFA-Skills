# ACM MM Venue Guide

> Migrated from the legacy `ccf-conference-skills/acmmm/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `acmmm` |
| Venue family | Multimedia |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/ACM-MM/acmart.cls` |
| Official URL | https://www.acmmm.org/2026 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# ACM MM 2026 Conference Writing Skill

**CCF-A | Multimedia | Publisher: ACM**
**Conference:** https://www.acmmm.org/2026
**Template:** `ACM-MM/acmart.cls` (ACM acmart, sigconf format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigconf, review, anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigconf]{acmart}
\acmConference[ACM MM 2026]{MM '26: 2026 ACM International Conference on Multimedia}
               {October 13--17, 2026}{Singapore}
\acmISBN{978-X-XXXX-XXXX-X/XX/XX}
\acmDOI{10.5555/XXXXXXX.XXXXXXX}
```

### Required Packages

```latex
\usepackage[round]{natbib}     % Author-year citations
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{balance}
\usepackage{cleveref}          % For consistent cross-references
\usepackage{algorithm}
\usepackage[noend]{algorithmic}
\usepackage{xcolor}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **8 pages** |
| References | No limit |
| Appendix / Supplementary | Permitted (not counted) |

ACM MM enforces a strict 8-page limit for the main body. References and supplementary materials do not count toward this limit, but reviewers are not required to read supplementary materials.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. No author names or affiliations in submission
2. Third-person self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs, project pages, GitHub links
4. Clear PDF metadata
5. Remove acknowledgments
6. Anonymize any embedded video/animation content

## Camera-Ready Differences

After acceptance:

1. Remove `review` and `anonymous` options
2. Fill in `\acmConference`, `\acmISBN`, `\acmDOI`
3. Restore all author names and affiliations
4. Add appropriate `\setcopyright` mode
5. Enable page numbers with `\settopmatter{printfolios=true}`

## Section Organization

ACM MM papers follow a multimedia research paper structure:

1. **Abstract** — Concise summary of contribution
2. **Introduction** — Problem, multimedia challenge, contributions (enumerate explicitly)
3. **Background & Related Work** — Multimedia foundations, prior methods
4. **Problem Definition** — Formal definition with notation
5. **Proposed Approach** — Core algorithm, model, or system
6. **Experiments** — Multimedia datasets, metrics, baselines, results
7. **Discussion** — Limitations, extensions, implications
8. **Conclusion**
9. References
10. Appendix / Supplementary (optional)

## Multimedia Evaluation

ACM MM evaluation requires multimedia-specific benchmarks:

```latex
\section{Experiments}
\subsection{Datasets}
We evaluate on three standard multimedia benchmarks:

\begin{itemize}
  \item \textbf{VideoQA~\citep{tang2018movieqa}}: 6,494 questions on 308 movies
  \item \textbf{MSR-VTT~\citep{xu2016msr}}: 10,000 video-caption pairs
  \item \textbf{AudioCaps~\citep{kim2019audiocaps}}: 10,000 audio clips with captions
\end{itemize}

\subsection{Metrics}
We report standard metrics for each task:
\begin{itemize}
  \item VideoQA: accuracy
  \item Video captioning: BLEU@4, METEOR, CIDEr, SPICE
  \item Audio captioning: BLEU@4, SPIDEr
\end{itemize}

\subsection{Baselines}
We compare against state-of-the-art multimodal methods:
LSTM encoders~\citep{hodosh2013framing}, attention-based models~\citep{xu2016msa},
and vision-language transformers~\citep{radford2021learning}.
```

## Multi-Modal Figures

ACM MM papers often contain rich multi-modal figures combining images, audio waveforms, text:

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=\linewidth]{figs/pipeline}
  \caption{Pipeline of our multimodal fusion approach.
    Video frames are encoded by a 3D CNN (green), audio spectrograms
    by a CNN (blue), and text by a BERT encoder (orange).
    Cross-modal attention (red) learns to align representations across
    modalities. Final predictions are generated by a multimodal decoder.}
  \label{fig:pipeline}
\end{figure}

% For combined audio-visual figures:
\begin{figure}[t]
  \centering
  \begin{minipage}{0.48\linewidth}
    \centering
    \includegraphics[width=\linewidth]{figs/frames}
    \subcaption{Key video frames}
  \end{minipage}
  \hfill
  \begin{minipage}{0.48\linewidth}
    \centering
    \includegraphics[width=\linewidth]{figs/spectrogram}
    \subcaption{Corresponding audio spectrogram}
  \end{minipage}
  \caption{Video and audio synchronization in our dataset.
    The spectrogram peaks (arrows) align with visual action onsets.}
  \label{fig:multimodal}
\end{figure}
```

## References (natbib)

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\citet{radford2021learning}  % Radford et al. (2021)
\citep{radford2021learning}  % (Radford et al. 2021)
```

## Formatting Rules

- **Format:** ACM sigconf (two-column, single-spaced)
- **Paper size:** US Letter
- **Body font:** 9pt minimum, Times New Roman
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in
- **Supplementary materials**: Uploaded separately, not counted toward page limit

## Submission Checklist

- [ ] 8 pages or fewer (main body)
- [ ] `\documentclass[sigconf, review, anonymous]`
- [ ] All author identification removed
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs and links
- [ ] Multi-modal datasets and metrics used
- [ ] High-quality, grayscale-legible figures
- [ ] References list all authors

## Camera-Ready Checklist

- [ ] Remove `review` and `anonymous` options
- [ ] Add conference metadata
- [ ] Restore author information
- [ ] Enable page numbers
- [ ] Add acknowledgments if desired
