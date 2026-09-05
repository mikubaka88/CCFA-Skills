# Visual Contract

Start every non-trivial figure or table with a contract. The contract keeps scientific meaning ahead of decoration and prevents panels from becoming disconnected result dumps.

## Relevant Fields Only

Reuse the existing source/specification. For a new non-trivial artifact, establish the core fields below internally; save them only for continuation or reproduction. A one-label or one-color edit does not require a new contract.

```text
Artifact and canonical paths:
Scientific question / takeaway:
Source data or method, with evidence locations:
Final size / destination / requested formats:
Relevant panel map or topology:
Exact labels, units, and visual encodings:
```

Add only mode-specific information: uncertainty and metric direction for quantitative evidence; node/edge semantics for architectures; float/caption placement for manuscript integration; icon provenance or editability levels when those assets are used; reference-layout principles only when a reference is actually used. Do not emit empty fields for unrelated formats. The architecture specification and this contract are the same state, not two documents to maintain.

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
- Group rows/columns by scientific question, dataset family, method family, or claim.
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

Follow `../../ccf-common/references/artifact-contracts.md` for path resolution. Reuse established `visual-composer/` paths; otherwise use `output/visual-composer/<figure-id>/`. For multiple figures, use distinct stable IDs. Preserve one current specification/source, reusable assets, and build preview per figure. Record a source path rather than duplicating supplied data. Keep QA findings in this specification only when persistence is needed; reuse an existing separate ledger if the project already has one.

Update the relevant fields and exports after a change. Do not create numbered prompts, attempt folders, render histories, or an iteration log unless requested. Preserve user inputs and scientific evidence. Resolve repeated failures by changing the relevant structure or rendering approach; do not alter the scientific content to make the layout fit.
