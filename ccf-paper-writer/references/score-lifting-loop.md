# Review-Risk Revision Loop

Use this reference when the user supplies weak review scores or asks the writer to revise text in response to known review findings. It converts evidence-backed deductions into manuscript actions. It does not create an independent score.

## Boundary

`ccf-paper-reviewer` owns scientific scoring, reviewer simulation, score calibration, and cross-version comparison. For a revision comparison it keeps two separate systems:

1. relative-progress scorecard under a frozen historical/current rubric;
2. absolute-readiness scorecard against the target venue.

The writer may read those scorecards and apply the linked fixes, but must not recompute, combine, or promise movement in them. Conditional score effects remain reviewer findings, not writing claims.

## Revision Loop

1. Read the canonical review report or user-supplied findings.
2. Map each deduction to a manuscript location and evidence anchor. Check whether the alleged defect is present. When feedback asks for a qualifier, narrower objective, or new experiment without a factual or logical gap, retain the supported argument and record the reason in an existing response or action table only if one is requested.
3. Classify the fix:
   - `writing-fixable`;
   - `analysis-fixable`;
   - `citation/positioning`;
   - `experiment-design`;
   - `figure/table`;
   - `reproducibility`;
   - `requires-new-result`;
   - `venue-mismatch`;
   - `needs user decision`.
4. Apply writing-owned fixes in priority order while preserving claims, numbers, citations, equations, and method identity.
5. Route non-writing fixes to their owning skill. Do not replace missing evidence with stronger prose.
6. Apply the humanization and prose-quality rules so revisions read as academic argument rather than a response to an imagined reviewer.
7. Overwrite the canonical manuscript artifact. Do not retain critique passes or numbered revision copies unless the user explicitly requests snapshots.
8. Return unresolved findings to `ccf-paper-reviewer` for re-evaluation when the user requests a new score.

Close a resolved concern when the changed passage and its affected evidence pass the relevant check. Reopen it for a changed source, assumption, artifact, or actual unresolved defect; do not cycle through wording changes and full reviews on unchanged evidence. A requested score target does not authorize endless rewrites or stronger unsupported claims. If the remaining score depends on missing evidence or a research choice, complete supported revisions and identify that dependency. Necessary new fixes continue; optional score chasing stops.

## Compact Action Table

```text
Issue ID:
Affected location:
Evidence basis:
Fix class:
Writing action:
External owner, if any:
Status: applied / needs evidence / needs user decision
```

Do not add generic limitations, speculative failure cases, or defensive caveats to make the paper appear safer. Preserve verified material negative evidence, scientific assumptions, and venue-mandated disclosures directly in the relevant manuscript passage. They are scientific content, not warning-only material. Use a short external note only for a remaining scientific choice that the available evidence or authorization cannot resolve; continue unaffected revisions and do not create a separate warning artifact by default.
