# WWW Venue Guide

> Migrated from the legacy `ccf-conference-skills/www/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-venue-format-guide`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `www` |
| Venue family | Web |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/WWW/acmart.cls` |
| Official URL | https://www2026.thewebconf.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# WWW 2026 Conference Writing Skill

**CCF-A | Web | Publisher: ACM**
**Conference:** https://www2026.thewebconf.org
**Template:** `ccf-latex-templates/WWW/acmart.cls` (ACM acmart, sigconf format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigconf, review, anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigconf]{acmart}
\acmConference[WWW 2026]{The Web Conference 2026}
               {April 19--23, 2026}{Sydney, Australia}
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
\usepackage{cleveref}
\usepackage{algorithm}
\usepackage[noend]{algorithmic}
\usepackage{xcolor}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **14 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

WWW enforces a 14-page limit for the main body. References and appendix do not count toward this limit.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. No author names or affiliations in submission
2. Third-person self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs, GitHub links, personal pages, dataset links
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

WWW papers follow a Web systems/research paper structure:

1. **Abstract** — Concise summary of contribution
2. **Introduction** — Web problem, motivation, contributions (enumerate explicitly)
3. **Background & Related Work** — Web foundations, prior systems
4. **Problem Definition** — Formal definition with notation
5. **Proposed Approach** — Core algorithm, model, or system
6. **Theoretical Analysis** — Optional: correctness, complexity
7. **Experimental Evaluation** — Web datasets, metrics, baselines, results
8. **Discussion** — Limitations, implications, ethical considerations
9. **Conclusion**
10. References
11. Appendix (optional)

## WWW-Specific Writing Conventions

### Introduction Structure for WWW Papers

```latex
\section{Introduction}
% Paragraph 1-2: Problem and motivation
The Web has become a primary platform for [application type].
With [N] billion users and [M] billion pages, [Web-scale challenge]
is more important than ever.

% Paragraph 3: Gap in prior work
Prior work has addressed [aspect] through [approaches].
However, these approaches fail to account for [Web-specific factor].

% Paragraph 4: Our approach
In this paper, we propose a novel approach that [key contribution].
Our approach leverages [Web-specific insight] to achieve [benefit].

% Paragraph 5: Contributions (numbered)
Our main contributions are:
\begin{itemize}
    \item We formalize the problem of [X] in the context of [Web phenomenon].
    \item We propose [Name], a [system/model] that achieves [benefit].
    \item We evaluate on [large-scale Web datasets] showing [results].
    \item We make our [code/datasets] publicly available.
\end{itemize}
```

### Web-Specific Content

#### Scale and Network Effects

```latex
\section{Evaluation}
\subsection{Datasets}
We evaluate on large-scale Web datasets:

\begin{itemize}
    \item \textbf{Link Graph}: A snapshot of the Web graph from Common Crawl
    (3.5 billion pages, 128 billion links)
    \item \textbf{Social Network}: A real-world social graph with
    1 billion users and 500 billion edges
    \item \textbf{Search Query Log}: 30 days of search queries from
    a commercial search engine (anonymized)
\end{itemize}

\subsection{Metrics}
We report standard metrics:
\begin{itemize}
    \item \textbf{Ranking quality}: NDCG@K, MAP, MRR
    \item \textbf{Scalability}: throughput (queries/second), latency percentiles
    \item \textbf{Resource efficiency}: memory usage, CPU utilization
\end{itemize}
```

#### User Studies

```latex
\subsection{User Study}
We conducted a user study with 120 participants recruited via
Amazon Mechanical Turk. Participants were randomly assigned to
two conditions and evaluated the quality of search results.

\textbf{Procedure:} After informed consent, participants completed
a demographic questionnaire, followed by a training session, then
the main task (10 search queries). Each query required participants
to rate the relevance of top-5 results on a 5-point scale and
select their preferred result.

\textbf{Results:} Our method significantly outperformed the baseline
on subjective preference (Wilcoxon signed-rank test, $p < 0.001$)
and achieved comparable objective relevance ratings.
```

## Figures and Tables

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/system-arch}
  \caption{Architecture of the proposed Web-scale recommendation system.
    The system consists of three layers: (1) candidate generation
    using approximate nearest neighbor search, (2) reranking with
    a learned scoring function, and (3) diversity-aware final ranking.}
  \label{fig:system}
\end{figure}

\begin{table}[t]
  \caption{Comparison with baselines on the Web ranking task.
    Best results in bold. $\dagger$ indicates $p < 0.01$ vs. baselines.}
  \label{tab:results}
  \begin{tabular}{lcccc}
    \toprule
    Method & NDCG@10 & MRR & MAP \\
    \midrule
    BM25 & 0.312 & 0.289 & 0.198 \\
    QLM & 0.341 & 0.315 & 0.223 \\
    BERT-base & 0.398 & 0.367 & 0.278 \\
    \textbf{Ours} & \textbf{0.441} & \textbf{0.412} & \textbf{0.315} \\
    \bottomrule
  \end{tabular}
\end{table}
```

## References (natbib)

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\citet{page1999pagerank}    % Page et al. (1999)
\citep{page1999pagerank}     % (Page et al. 1999)
```

## Formatting Rules

- **Format:** ACM sigconf (two-column, single-spaced)
- **Paper size:** US Letter
- **Body font:** 9pt minimum, Times New Roman
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in

## Submission Checklist

- [ ] 14 pages or fewer (main body)
- [ ] `\documentclass[sigconf, review, anonymous]`
- [ ] All author identification removed
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs and links
- [ ] Large-scale Web datasets used for evaluation
- [ ] Statistical significance testing performed
- [ ] References list all authors
- [ ] Grayscale-legible figures

## Camera-Ready Checklist

- [ ] Remove `review` and `anonymous` options
- [ ] Add conference metadata
- [ ] Restore author information
- [ ] Enable page numbers
- [ ] Add acknowledgments if desired
