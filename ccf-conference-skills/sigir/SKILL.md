---
name: sigir
description: Writing and formatting guidance for SIGIR (ACM SIGIR Conference on Research and Development in Information Retrieval) papers. Use when drafting, formatting, and submitting to SIGIR 2026. Covers ACM acmart sigconf format with double-blind review mode, SIGIR page limits (10 pages), IR-specific writing conventions (research questions, retrieval models, evaluation with test collections), and ACM camera-ready preparation.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# SIGIR 2026 Conference Writing Skill

**CCF-A | IR | Publisher: ACM**
**Conference:** https://sigir.org/sigir2026
**Template:** `ccf-latex-templates/SIGIR/acmart.cls` (ACM acmart, sigconf format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigconf, review, anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigconf]{acmart}
\acmConference[SIGIR 2026]{SIGIR '26: 2026 ACM SIGIR Conference...}
               {December 1--5, 2026}{Madrid, Spain}
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
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **10 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

SIGIR enforces a strict 10-page limit for the main body. References and appendix do not count toward this limit, but reviewers are not required to read the appendix.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. No author names or affiliations in submission
2. Third-person self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs, GitHub links, data repository links
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

SIGIR papers typically follow an information retrieval paper structure:

1. **Introduction** — Research problem, gap in literature, contributions (enumerate explicitly with RQs)
2. **Background & Related Work** — IR foundations, positioning of the work
3. **Problem Definition / Research Questions** — Formal RQs or problem statement
4. **Proposed Approach** — Core retrieval model, algorithm, or system
5. **Theoretical Analysis** — Optional: mathematical properties, complexity
6. **Experimental Setup** — Test collection, metrics, baselines
7. **Results & Analysis** — Experimental findings, statistical significance
8. **Discussion** — Implications, limitations, future work
9. **Conclusion**
10. References
11. Appendix (optional)

## Research Questions

SIGIR values explicit research questions:

```latex
\section{Research Questions}
We investigate the following research questions:

\begin{itemize}
    \item \textbf{RQ1:} Does incorporating query reformulation history
    improve retrieval effectiveness for complex information needs?
    \item \textbf{RQ2:} How does the proposed model compare with
    neural rankers on datasets with sparse relevance labels?
    \item \textbf{RQ3:} What is the trade-off between retrieval
    effectiveness and computational efficiency?
\end{itemize}

\textbf{Answer to RQ1:} Our experiments in \autoref{tab:results} show that...
```

### Introduction with Research Questions

```latex
\section{Introduction}
% Paragraph 1: Problem and motivation
Information retrieval is fundamental to how users interact with large
document collections. When users issue queries, they often need to
reformulate their search terms to find relevant information.

% Paragraph 2: Gap in prior work
Prior work on query reformulation has focused on [approaches A and B].
However, these approaches fail to leverage [insight], leading to
suboptimal retrieval performance for [scenario].

% Paragraph 3: Our approach
In this paper, we propose a novel approach that [key insight].
Our approach models [phenomenon] by [technical contribution].

% Paragraph 4: Research Questions
We investigate three research questions:
RQ1: [Does X affect Y?]
RQ2: [How does our method compare to baselines?]
RQ3: [What are the trade-offs?]

% Paragraph 5: Contributions
Our main contributions are:
\begin{itemize}
    \item We formalize the problem of X as RQ1 and identify key factors.
    \item We propose [method], which achieves [benefit].
    \item We conduct extensive experiments on [datasets] showing [result].
    \item We release our code and datasets for reproducibility.
\end{itemize}
```

## Retrieval Model Formalization

SIGIR papers commonly formalize retrieval models mathematically:

```latex
\section{Proposed Approach}
We propose a retrieval model that combines term frequency with
document authority signals. The scoring function is:

\begin{equation}
  \label{eq:score}
  \text{Score}(d, q) = \sum_{t \in q} \text{tf}(t, d) \cdot
  \text{idf}(t) \cdot \text{PageRank}(d)
\end{equation}

where $\text{tf}(t, d)$ is the term frequency of term $t$ in
document $d$, $\text{idf}(t) = \log\frac{N}{n_t}$ is the inverse
document frequency, and $\text{PageRank}(d)$ is the PageRank score
of document $d$.
```

## IR-Specific Writing Conventions

### Dataset Description

```latex
\section{Experimental Setup}
\subsection{Test Collections}
We evaluate on three standard IR test collections:

\begin{table}[h]
  \caption{Test collection statistics.}
  \label{tab:collections}
  \centering
  \begin{tabular}{lrrrr}
    \toprule
    Collection & Docs & Topics & Relevance & Source \\
    \midrule
    TREC-8 & 528,155 & 50 & Qrels & TREC \\
    Gov2 & 25,205,179 & 150 & Qrels & TREC \\
    ClueWeb09 & 503,903,810 & 200 & Pooled & TREC \\
    \bottomrule
  \end{tabular}
\end{table}
```

### Standard IR Metrics

```latex
\subsection{Evaluation Metrics}
We report standard IR effectiveness metrics:

\textbf{Ranking metrics:}
\begin{itemize}
    \item \textbf{MAP}: Mean Average Precision
    \item \textbf{NDCG@K}: Normalized Discounted Cumulative Gain at K
    \item \textbf{P@K}: Precision at K
    \item \textbf{MRR}: Mean Reciprocal Rank
\end{itemize}

\textbf{Efficiency metrics:}
\begin{itemize}
    \item \textbf{QPS}: Queries per second
    \item \textbf{Latency}: Response time percentiles (P50, P95, P99)
    \item \textbf{Memory}: Index size in GB
\end{itemize}
```

### Baseline Methods

```latex
We compare against three categories of baselines:

\textbf{Classical retrieval models:}
\begin{itemize}
    \item \textbf{BM25}: The probabilistic model of \citet{robertson2009bm25}.
    \item \textbf{QLM}: Query likelihood model with Dirichlet smoothing.
\end{itemize}

\textbf{Neural retrieval models:}
\begin{itemize}
    \item \textbf{DRMM}: Deep relevance matching model \citep{guo2016}.
    \item \textbf{KNRM}: Kernel-based neural ranking model \citep{xiong2017}.
    \item \textbf{ANCE}: Approximate nearest neighbor contrastive encoding \citep{xiong2020}.
\end{itemize}
```

## Experimental Evaluation

SIGIR evaluation standards require:

- **Standard test collections**: TREC, CLEF, INEX, or equivalent
- **Standard metrics**: MAP, NDCG@K, Precision@K, MRR, ERR
- **Statistical significance**: paired t-tests, Wilcoxon signed-rank tests
- **Baseline comparisons**: strong IR baselines from literature
- **Error analysis**: qualitative analysis of failure cases

```latex
\section{Experimental Results}
\subsection{Main Results}
Results are summarized in \autoref{tab:main-results}.
Our model achieves statistically significant improvements over
all baselines on NDCG@20 (paired t-test, $p < 0.01$).

\begin{table}[h]
  \caption{Retrieval effectiveness on TREC Collections. Best
    results in bold. $\dagger$ indicates $p < 0.01$ vs. BM25.}
  \label{tab:main-results}
  \begin{tabular}{lcccc}
    \toprule
    \multirow{2}{*}{Model} & \multicolumn{2}{c}{TB06} & \multicolumn{2}{c}{MB06} \\
    \cmidrule(lr){2-3}\cmidrule(lr){4-5}
          & MAP & NDCG@20 & MAP & NDCG@20 \\
    \midrule
    BM25 & 0.182 & 0.341 & 0.195 & 0.362 \\
    QLM & 0.198 & 0.358 & 0.211 & 0.385 \\
    \textbf{Ours} & \textbf{0.231} & \textbf{0.412} & \textbf{0.248} & \textbf{0.437} \\
    \bottomrule
  \end{tabular}
\end{table}

\subsection{Ablation Study}
Removing the query expansion component degrades NDCG@20 by 4.2\%,
confirming its importance to the overall system.
```

### Statistical Significance Testing

```latex
We assess statistical significance using two-sided Wilcoxon signed-rank
tests \citep{wilcoxon1992} with $\alpha = 0.05$.
We apply Bonferroni correction for multiple comparisons.
Results marked with $\dagger$ indicate $p < 0.05$ after correction.
```

## Figures and Tables

- Vector formats (.pdf) for diagrams
- Grayscale legibility required
- Number sequentially
- Use `booktabs` for tables (no vertical rules)
- Self-contained captions

## References (natbib)

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\citet{robertson2009bm25}  % Robertson et al. (2009)
\citep{robertson2009bm25}  % (Robertson et al. 2009)
```

## Formatting Rules

- **Format:** ACM sigconf (two-column, single-spaced)
- **Paper size:** US Letter
- **Body font:** 9pt minimum, Times New Roman
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in

## Reproducibility Checklist

SIGIR increasingly values reproducibility:

```latex
\section*{Reproducibility}
\subsection{Code and Data}
Our code and evaluation scripts are available at [URL].
The processed datasets are available at [URL].

\subsection{Hyperparameters}
All hyperparameters were tuned on validation topics not used in
the main evaluation. The optimal settings are reported in the appendix.

\subsection{Random Seeds}
All neural models were trained with seeds 0-4 for reproducibility.
```

## Submission Checklist

- [ ] 10 pages or fewer (main body)
- [ ] `\documentclass[sigconf, review, anonymous]`
- [ ] All author identification removed
- [ ] Research questions clearly stated
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] Standard IR metrics and test collections used
- [ ] Statistical significance testing performed
- [ ] References list all authors
- [ ] Grayscale-legible figures

## Camera-Ready Checklist

- [ ] Remove `review` and `anonymous` options
- [ ] Add conference metadata
- [ ] Restore author information
- [ ] Enable page numbers
- [ ] Add acknowledgments if desired
