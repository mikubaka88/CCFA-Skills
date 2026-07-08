# Visual Contract

Start every non-trivial figure or table with a contract. The contract keeps scientific meaning ahead of decoration and prevents panels from becoming disconnected result dumps.

## Required Fields

```text
Artifact:
Target venue / format:
Core claim:
Reviewer question:
Evidence layer: main / mechanism / robustness / limitation / qualitative
Source data:
Statistics / uncertainty:
Figure prototype or table type:
Panel or table map:
Caption role:
Manuscript placement:
Output formats:
Traceability:
```

## Evidence Hierarchy

- Main result: answers the paper's central claim.
- Mechanism: explains why the result happens.
- Robustness: tests stability across settings, datasets, seeds, or perturbations.
- Limitation: bounds the claim honestly.
- Qualitative or case study: makes behavior inspectable, never a substitute for quantitative evidence.

## Panel Map Rules

- Each panel must answer one distinct scientific question.
- Every panel needs an explicit role: overview, comparison, mechanism, robustness, failure, example, or source-data summary.
- If removing a panel does not change the figure's conclusion, merge it, move it to appendix, or drop it.
- Prefer an asymmetric information structure when the science calls for it: one anchor panel plus smaller supporting panels often reads better than a uniform grid.
- Keep source-data traceability visible in the contract even when the final figure is visually compact.

## Table Map Rules

- A table should compare, audit, or summarize evidence; it should not be a spreadsheet pasted into a paper.
- Group rows/columns by reviewer question, dataset family, method family, or claim.
- Use consistent metric direction, units, uncertainty, and numeric precision.
- Move secondary columns to appendix when they weaken the main comparison.

## Stateful Iteration

When a project directory exists and the task is larger than one artifact, keep visual state in a local working folder:

```text
visual-composer/visual-contract.md
visual-composer/qa-ledger.md
visual-composer/iteration-log.md
```

Use the files as working state, not as conversation memory. If repeated tweaks do not fix a problem, pivot the structure: split a table, use a full-width float, change the chart family, reduce panel count, or move secondary material to appendix.
