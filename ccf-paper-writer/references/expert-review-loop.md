# Writer Revision Bridge

This compatibility reference preserves the v0.7 revision workflow without duplicating the independent reviewer. Use it only when the writer applies review findings to manuscript text or performs a narrow, unscored writing-quality pass.

## Ownership Boundary

- `ccf-paper-reviewer` owns simulated reviewers, AC/meta-review, scientific scoring, version comparison, and both cross-version scorecards.
- `ccf-paper-writer` owns manuscript edits, section restructuring, compression, and prose polish.
- `ccf-experiment-designer`, `ccf-literature-searcher`, `ccf-visual-composer`, and `ccf-integrity-auditor` own evidence, literature, figures, and integrity checks respectively.

If the user asks for reviewer-style critique or a score, hand the manuscript to `ccf-paper-reviewer`. Do not simulate a parallel reviewer panel inside the writing task.

## Writer-Side Revision Loop

1. Read the supplied reviewer finding, canonical review report, or explicit user request.
2. Locate the affected claim, paragraph, section, figure reference, or table narrative.
3. Classify the action as `rewrite`, `reorganize`, `compress`, `clarify evidence`, `citation handoff`, `experiment handoff`, `visual handoff`, or `requires user decision`.
4. Edit only writing-owned content. Do not invent results, citations, experiments, reviewer consensus, or score movement.
5. Apply `references/prose-quality-guardrails.md` and the `ccf-humanization` policy.
6. Preserve the user's source format and overwrite the canonical artifact in place.
7. Run one internal quality pass for meaning, evidence bounds, terminology, flow, and format fidelity.

## Revision Record

Keep the visible output compact unless the user requests rationale:

```text
Finding or request:
Affected location:
Writing action:
Evidence preserved:
External handoff, if any:
Status: applied / needs evidence / needs user decision
```

Formal issue provenance, historical/current score deltas, and the canonical revision ledger remain with `ccf-paper-reviewer` and `ccf-rebuttal-writer`. Do not create writer-owned review scores or per-pass critique files.
