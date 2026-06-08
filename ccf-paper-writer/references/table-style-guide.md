# Table Style Guide

Use this file whenever drafting, revising, or beautifying LaTeX tables for CCF venue papers. These rules apply to all result tables, configuration tables, ablation tables, and comparison tables.

## Golden Rules

1. Never use vertical rules (`|` in column specs or `\hline` for vertical lines).
2. Use `\toprule`, `\midrule`, `\bottomrule` from `booktabs` — never `\hline`.
3. Numbers in the same column must have the same number of decimal places.
4. Every table must have exactly one message; if a table has two messages, split it.
5. Caption goes above the table, states the setting and the main takeaway.

## Required Packages

```latex
\usepackage{booktabs}
\usepackage{array}
```

Optional but recommended for complex tables:

```latex
\usepackage{multirow} % for cells spanning multiple rows
\usepackage{makecell} % for multi-line header text
\usepackage{siunitx} % for number alignment on decimal point
```

## Minimal Example: Two-Column Table

```latex
\begin{table}[t]
 \centering
 \caption{Final translation quality on the test set.}
 \label{tab:example}
 \begin{tabular}{l r}
 \toprule
 Model & BLEU \\
 \midrule
 Transformer (base) &27.3 \\
 Transformer (big) &28.4 \\
 Previous best &26.0 \\
 \bottomrule
 \end{tabular}
\end{table}
```

## Three-Column Table With Mixed Content

```latex
\begin{table}[t]
 \centering
 \caption{Comparison of sequence modeling layers. $n$: sequence length; $d$: model dimension.}
 \label{tab:complexity}
 \begin{tabular}{l c c}
 \toprule
 Layer Type & Complexity & Max Path \\
 \midrule
 Self-attention & $O(n^2 \cdot d)$ & $O(1)$ \\
 Recurrent & $O(n \cdot d^2)$ & $O(n)$ \\
 Convolutional & $O(k \cdot n \cdot d^2)$ & $O(\log_k n)$ \\
 \bottomrule
 \end{tabular}
\end{table}
```

Key points:
- Second column (math) uses `c` for centering — consistent with the `l` column.
- Units or variable definitions go in the caption, not repeated in every cell.
- `\midrule` separates header from body; no extra rules between body rows.

## Table With Sub-Headers (Grouped Columns)

```latex
\begin{table}[t]
 \centering
 \caption{Transformer configurations used in experiments.}
 \label{tab:config}
 \begin{tabular}{l c c c c c}
 \toprule
 & $N$ & $d_{\text{model}}$ & $d_{\text{ff}}$ & $h$ & $P_{\text{drop}}$ \\
 \midrule
 Base &6 &512 &2048 &8 &0.1 \\
 Big &6 &1024 &4096 &16 &0.3 \\
 \bottomrule
 \end{tabular}
\end{table}
```

To add a grouped header row, insert a second header line before `\midrule`:

```latex
 \toprule
 & \multicolumn{3}{c}{Dimensions} & \\
 \cmidrule(lr){2-4}
 & $d_{\text{model}}$ & $d_{\text{ff}}$ & $d_k$ & $h$ \\
 \midrule
```

Use `\cmidrule(lr){2-4}` (with small left/right trim `(lr)`) instead of `\cline` for partial horizontal rules.

## Handling Narrow Columns

When a column contains long single words that cause underfull hboxes, use one of these fixes **in priority order**:

1. **Abbreviate**: shorten headers to an abbreviation and expand in the caption or table note.
2. **Reduce font size**: wrap the tabular in `\small` or `\footnotesize`.
3. **Allow ragged-right**: use `p{2.5cm}` with `\raggedright`:

```latex
\usepackage{array}
% In preamble:
\newcolumntype{P}[1]{>{\raggedright\arraybackslash}p{#1}}
% In table:
\begin{tabular}{l P{3.0cm} P{3.5cm}}
```

4. **Rotate wide headers**: use `\makecell` or `\rotatebox`.
5. **Hyphenate long monospace words**: in narrow columns, long identifiers like `ccf-experiment-designer` will overflow even with `\raggedright`. Abbreviate to a shorter form (e.g., `ccf-expt-designer`) and explain in the caption or a table note. Do not let the compiler produce overfull hboxes from unbreakable words.

## Number and Precision Rules

| Situation | Rule |
| --- | --- |
| Metrics (BLEU, accuracy, F1) | Same decimal places in every cell of that column |
| Standard deviations | `$\pm$` notation: `27.3 $\pm$0.2` |
| Percentages | Use `\%` and align: `87.3\%` |
| Large integers | Use commas or scientific notation consistently |
| Zero values | Write `0.0` not `0` when other values have decimals |
| Table-wide consistency | If most values need1 decimal, apply1 decimal everywhere |

## Bold Best Results

Use `\textbf{}` to highlight the best result in each column:

```latex
\textbf{28.4} % best BLEU
```

Alternatively, underline second-best with `\underline{}`. Do not bold AND underline — pick one convention and apply it consistently.

## Column-Width Awareness

In two-column conference formats (ICLR, NeurIPS, ICML, CVPR, ICCV, ACL, EMNLP, AAAI, etc.), a single column is approximately7.0--8.0 cm wide. Every table must fit within this width. Before writing any table:

1. Estimate the number of columns and their typical widths.
2. If the table would exceed7.5 cm, plan for one of the fixes below.
3. For tables with4+ columns, immediately plan for \\small\ or \\footnotesize\ and abbreviated headers.

A simple check: a column of numbers (e.g., \27.3\) needs about1.5 cm; a short word column (e.g., \Model\) needs about2.0 cm; a longer text column needs3.0+ cm. A three-column table \{l r r}\ fits easily. A five-column table \{l c c c c}\ often needs \\small\. A six-column table almost always needs \\small\ and abbreviated headers.

## Tables Too Wide for the Column

In two-column formats, wide tables need special handling. In priority order:

1. **Reduce font size**: `\small` or `\footnotesize` around the `tabular`.
2. **Abbreviate headers**: `Seq. Ops` instead of `Sequential Operations`.
3. **Use `table*` for full-width**: switches to single-column mode spanning both columns.

```latex
\begin{table*}[t]
 \centering
 \caption{Full comparison across all benchmarks.}
 \label{tab:wide}
 \small
 \begin{tabular}{l c c c c c}
 \toprule
 ...
 \end{tabular}
\end{table*}
```

4. **Reduce column separation**: `\setlength{\tabcolsep}{4pt}` before the tabular (default is6pt).

## Captions

Captions go **above** the table. A good caption has three parts:

```latex
\caption{What is shown. Condition or setting. Main takeaway or notable finding.}
```

Examples:

- **Weak**: `\caption{Results.}` — says nothing.
- **Good**: `\caption{Translation quality (BLEU) on WMT2014 English-German newstest2014. The Transformer big model outperforms the previous best single-model result by2.4 BLEU.}`
- **Concise**: `\caption{Translation quality (BLEU) on WMT2014 English-German.}` — states what and where.

## Table Notes

Use `\multicolumn` to add notes below the table body:

```latex
\bottomrule
\multicolumn{2}{p{0.9\columnwidth}}{\small \textit{Note:} All values are single-model results without ensembling. Bold indicates best in column.}
\end{tabular}
```

## Table Placement

- Use `[t]` (top) for most tables — places the table at the top of a page.
- Use `[h]` only for very small inline tables; LaTeX will convert it to `[ht]`.
- Never use `[H]` (from the `float` package) in submission drafts — it breaks the venue template's page breaking.
- If a table floats to the wrong section, let LaTeX handle it; the reviewer will find it.

## Quick Checklist Before Submitting

- [ ] All tables use `booktabs` rules: `\toprule`, `\midrule`, `\bottomrule`.
- [ ] No vertical rules anywhere.
- [ ] No `\hline` anywhere.
- [ ] All numbers in a column have the same decimal precision.
- [ ] Caption is above the table, states what + where + key finding.
- [ ] Every table answers exactly one reviewer question.
- [ ] Best results are highlighted (bold or underline, consistent convention).
- [ ] Column alignment is logical: `l` for text, `c` for equal-width symbols/math, `r` for numbers.
- [ ] No underfull or overfull hbox warnings from table rows.
- [ ] Wide tables use `table*`, `\small`, or abbreviated headers — not squeezed columns.