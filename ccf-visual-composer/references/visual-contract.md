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
Source method / architecture content:
Statistics / uncertainty:
Figure prototype or table type:
Panel or table map:
Architecture topology / typed connections:
Exact label inventory:
Icon inventory: native primitive / public SVG / custom asset
Reference-layout sources and extracted composition principles:
Caption role:
Manuscript placement:
Output formats:
PPTX editability target: native / SVG-convertible / isolated raster
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

## Architecture Map Rules

- Every node, group, label, and connection must be traceable to supplied method content.
- Record the reader scan path, topology, and edge semantics before choosing visual style.
- Distinguish data flow, control flow, supervision, retrieval, feedback, and gradients when the distinction matters.
- Mark training-only and inference-only elements explicitly; do not collapse them into a misleading single path.
- Use the strongest visual emphasis for the actual contribution, not for generic encoders, databases, or decorative icons.
- Keep an exact label inventory for generation QA and later editable SVG reconstruction.
- Plan icon semantics before rendering. Prefer native primitives or one coherent public SVG family; reserve custom generation for method-specific concepts.
- Record layout references and only the transferable composition principles extracted from them; do not copy exact arrangements, palettes, or icons.
- When PPTX is requested, define which elements must be native-editable and which custom assets may remain separately movable raster objects.

## Stateful Iteration

When a project directory exists and the task is larger than one artifact, keep only the generated state needed to continue or reproduce the deliverable:

```text
visual-composer/visual-contract.md
visual-composer/qa-ledger.md  # only when QA evidence must persist
```

Overwrite each canonical state file on the next iteration. Do not create numbered prompts, attempt folders, render histories, or an iteration log unless the user explicitly requests an audit trail. User inputs and immutable evidence remain outside this overwrite rule. If repeated tweaks do not fix a problem, pivot the structure: split a table, use a full-width float, change the chart family, reduce panel count, or move secondary material to appendix.
