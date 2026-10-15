# Result Templates

Use these templates to produce fill-in result tables from the supplied experiment design. For manuscript LaTeX, reuse `\emptycell` or define `\newcommand{\emptycell}{\textemdash}` once. For Markdown use `—`. Missing values are not zero, failure, or inapplicability; use separately explained `N/A` for the latter. Do not write `TBD` in manuscript prose, compute unknown aggregates, highlight an unknown winner, or supply predicted result analysis.

These are schema examples, not a compulsory experiment package. Include only applicable tests within the requested scope. Pending results can coexist with a complete content-first draft; an explicit request to leave the entire experiment section blank takes precedence. Internal planning fields such as expected observations and claim status do not automatically become paper text.

## Claim-Evidence Matrix

```md
| Claim | Reviewer question | Evidence needed | Dataset/benchmark | Baselines | Metrics | Result placeholder | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | — | planned / running / done |
```

## Main Comparison Table

```md
| Method | Source | Setting | Metric 1 ↑/↓ | Metric 2 ↑/↓ | Metric 3 ↑/↓ | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| User method | current work |  | — | — | — |  |
| Baseline A | verified source |  | — | — | — |  |
| Baseline B | verified source |  | — | — | — |  |
```

## Ablation Table

```md
| Variant | Component changed | Mechanism tested | Metric 1 ↑/↓ | Metric 2 ↑/↓ | Interpretation after user fills result |
| --- | --- | --- | --- | --- | --- |
| Full method | none | full mechanism | — | — |  |
| w/o component A | remove A | necessity of A | — | — |  |
| generic replacement | replace A | specificity of design | — | — |  |
```

## Robustness / Stress Test Table

```md
| Stress condition | Why it matters | Dataset/workload | Metric | User result | Failure threshold | Reviewer concern answered |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | — |  |  |
```

## Qualitative / Case Study Table

```md
| Case | Selection rule | Expected observation | User-provided result | What it demonstrates | Failure or limitation |
| --- | --- | --- | --- | --- | --- |
|  | representative / hard / failure |  | — |  |  |
```

## Execution Priority Table

```md
| Priority | Experiment | Claim defended | Cost | Dependency | Appendix/main | Stop condition |
| --- | --- | --- | --- | --- | --- | --- |
| P0 |  |  | low/medium/high |  | main |  |
```

## No-Fabrication Reminder

Use a brief note outside manuscript prose when needed; pending table captions state the quantities and protocol without claiming an outcome:

```text
Empty cells await actual results from the stated method and protocol. Update all dependent aggregates and textual claims when those values are supplied.
```
