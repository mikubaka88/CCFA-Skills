# Table Style Guide

Use this file for LaTeX result, configuration, ablation, and comparison tables. Venue requirements and the user's established layout take precedence over these defaults.

## Golden Rules

1. Prefer a clear layout without vertical rules unless the required or established style uses them.
2. Prefer `\toprule`, `\midrule`, `\bottomrule` from `booktabs` for horizontal rules when compatible with that style.
3. Align comparable quantities at a precision supported by their source values. Preserve meaningful small values, thresholds, intervals, and significant digits; appearance must not change the reported result.
4. Give each table a clear purpose; related comparisons can share grouped columns. Do not split a table solely to enforce a message count.
5. Follow the required caption placement and state the setting and any supported takeaway.

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

For visible overflow or poor spacing, choose an appropriate fix below. Inspect compiler warnings in the rendered table; an underfull hbox alone is not a defect.

1. **Abbreviate**: shorten headers to an abbreviation and expand in the caption or table note.
2. **Adjust widths**: give long labels enough space while retaining readable numeric columns.
3. **Allow ragged-right**: use `p{2.5cm}` with `\raggedright`:

```latex
\usepackage{array}
% In preamble:
\newcolumntype{P}[1]{>{\raggedright\arraybackslash}p{#1}}
% In table:
\begin{tabular}{l P{3.0cm} P{3.5cm}}
```

4. **Rotate wide headers**: use `\makecell` or `\rotatebox`.
5. **Handle long identifiers**: allow appropriate breaks or use an explained abbreviation. Reduce font size only when the template permits it and readability remains adequate.

## Number and Precision Rules

| Situation | Rule |
| --- | --- |
| Metrics (BLEU, accuracy, F1) | Use a consistent precision for comparable measurements when supported by their sources |
| Standard deviations | `$\pm$` notation: `27.3 $\pm$0.2` |
| Percentages | Use `\%` and align: `87.3\%` |
| Large integers | Use commas or scientific notation consistently |
| Zero and small values | Distinguish an exact zero from a rounded value or reporting threshold; use scientific notation when needed |
| Mixed quantities | Format each quantity according to its units and supported precision; never round the entire table by majority convention |

## Bold Best Results

Use `\textbf{}` to highlight the best result in each column:

```latex
\textbf{28.4} % best BLEU
```

Alternatively, underline second-best with `\underline{}`. Do not bold AND underline — pick one convention and apply it consistently.

## Column-Width Awareness

Read the actual template and enclosing environment. Use the available `\linewidth`, `\columnwidth`, or `\textwidth` as appropriate, not a fixed width inferred from the conference name. Inspect the rendered table before changing font size or layout.

## Tables Too Wide for the Column

Choose among these options according to the actual layout:

1. **Shorten or wrap headers** while keeping terminology understandable.
2. **Adjust column widths and spacing** without crowding the values.
3. **Use `table*` in a two-column layout** when a full-width float is appropriate.

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

4. **Reduce font size** only if permitted and still readable.

## Captions

Follow the venue and established user style for caption placement. State the content and necessary setting; include a takeaway only when results support it. The following is a functional example, not a required three-sentence pattern:

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
- Use forced placement only when compatible with the template and inspected layout.
- Inspect float order and its relationship to the discussion; correct distant or misleading placement without overriding venue constraints.

## Quick Checklist Before Submitting

- [ ] Table rules match the required or established style; use `booktabs` defaults where appropriate.
- [ ] Comparable numbers align without hiding meaningful differences or implying unsupported precision.
- [ ] Caption placement is correct; its scope and any conclusion match the available evidence.
- [ ] Each table has a clear scientific purpose.
- [ ] Any best-result emphasis uses actual comparable measurements and a consistent convention; unknown cells are not ranked or highlighted.
- [ ] Column alignment is logical: `l` for text, `c` for equal-width symbols/math, `r` for numbers.
- [ ] No visible overflow, overlap, or distracting spacing remains; warnings have been inspected in context.
- [ ] Table width and font size are readable in the actual layout.
