# Version Comparison And Re-Review

Use this reference when two or more manuscript versions, review rounds, score changes, or a moving-target concern must be compared. Keep this mode distinct from an independent review of the current manuscript.

## Two Questions, Two Scorecards

Report these judgments separately:

1. **Relative progress:** Is the current version better than the historical version under the same comparison contract?
2. **Absolute readiness:** Does the current version meet the target venue's present publication standard?

A revision can improve materially and remain below the acceptance threshold. Do not treat those statements as inconsistent. Report confidence and version comparability as a third field, not as a score dimension.

### Relative-progress scorecard

Use the frozen comparison contract for both versions. For each dimension, report `historical score`, `current score`, `delta`, `weight`, and the issue IDs that explain the delta. Sum the weighted deltas and classify the result as `regressed`, `unchanged`, or `improved` using thresholds fixed in the contract. This is a revision-effect score, not an acceptance score.

### Absolute-readiness scorecard

Review only the current version against the stated target venue, year, track, and paper type. Report the current per-dimension scores, calibrated overall score or stance, decision threshold, and remaining blocking evidence. If the venue standard has changed since the historical review, disclose that change here. Do not retroactively alter the relative-progress scorecard.

The current generic readiness assessment uses `generic-7` from `calibration-and-rank.md`; a verified venue form may replace it. Historical comparison dimensions, labels, weights, and scores stay frozen even when they predate this rubric. The two scorecards may therefore have different dimensions; disclose the mapping or difference rather than migrating historical scores.

Do not combine the scorecards into a single number. The readiness score may stay flat or fall while the progress score is positive, but every difference must be explained by the distinct question, evidence, or external standard used.

## Frozen Comparison Contract

Record or inherit the comparison contract before scoring, and before inspecting the revision when materials can be separated. If both versions are already in the prompt, do not claim a blinded comparison; establish the common rubric before assigning scores:

- target venue, year, track, and paper type;
- rubric dimensions and anchors;
- dimension weights and overall-score mapping;
- reviewer roles and synthesis rule;
- decision thresholds;
- required evidence standard;
- materials available for each version.

Use the same contract for both versions. If current venue policy must be applied in a new independent review, disclose it as an external standard change. Do not retroactively penalize only the revised version in the historical comparison.

## Three-Phase Comparison

1. **Freeze:** Lock the comparison contract and inherited issue definitions.
2. **Evidence-only comparison:** Read the historical manuscript, current manuscript, and their diff. Score both versions independently under the frozen contract before reading persuasive author explanations when the artifacts permit this separation.
3. **Response reconciliation:** Use the response letter or revision summary only to locate manuscript evidence. It may clarify where a change appears, but it cannot silently relax a criterion or substitute a promise for manuscript evidence.

For subjective pairwise judgments, inspect both orders when feasible: historical/current and current/historical. Resolve any order-dependent result from manuscript evidence rather than averaging it away.

## Ledger-Ready Issue Records

Retain stable issue records in the canonical review report. When a revision ledger already belongs to the authorized workflow or the user requests one, the reviewer returns ledger-ready rows and `ccf-rebuttal-writer` updates that ledger in place. Review or review-plus-revision alone does not require a new ledger or response stage. Each issue record needs these fields:

| Field | Allowed values or meaning |
| --- | --- |
| `first_seen_version` | First manuscript or review round where the issue was recorded. |
| `status` | `unresolved`, `partially_resolved`, `resolved`, or `not_applicable`. |
| `origin` | `inherited`, `revision_regression`, `previously_undetected`, `newly_revealed_by_evidence`, or `external_standard_change`. |
| `applies_to` | `historical`, `current`, or `both`. |
| `affected_dimensions` | Frozen rubric dimensions changed by the issue. |
| `evidence` | Section, paragraph, line, figure, table, result, or diff anchor. |
| `score_effect` | Per-version dimension or overall delta, if any. |

Apply provenance consistently:

- `revision_regression` affects the current version because the revision introduced a concrete defect.
- `previously_undetected` describes a weakness already present in the historical manuscript. It applies to both versions unless the current version resolves it.
- `newly_revealed_by_evidence` may lower the current assessment when new experiments expose a contradiction, instability, or invalid conclusion. Cite that evidence.
- `external_standard_change` belongs to a new absolute-readiness review, not to the frozen historical comparison.

## Score Continuity Rules

- If an inherited issue is resolved and the revision introduces no corresponding defect or contradictory evidence, the affected dimension must not decrease.
- Every decrease must cite an issue ID, current-version evidence, origin, affected dimension, and score delta.
- A newly noticed latent issue cannot penalize only the current version in the comparison.
- Do not guarantee a higher overall score after every revision. New evidence may legitimately expose a serious defect.
- Do not change weights, reviewer roles, anchors, or thresholds mid-comparison. If a change is unavoidable, run a separate review and label it non-comparable.

## Compact Output

```text
Comparison contract:
Relative-progress scorecard:
  Historical / current / delta / weight by dimension:
  Weighted progress delta and classification:
Inherited issues resolved / partial / unresolved:
New issue provenance:
Traceable score decreases:
Absolute-readiness scorecard:
  Current dimension scores:
  Overall score or stance and threshold:
  Remaining blocking evidence:
Confidence and comparability:
```

Write the comparison and issue status into the canonical review report. If ledger maintenance is in scope, send those rows to `ccf-rebuttal-writer` for the existing canonical ledger; otherwise preserve them in the report and pass relevant findings directly to the revision owner. Do not create phase reports, response-reconciliation sidecars, or per-round copies unless requested.

When structured validation is useful, pass an internal JSON object to `../scripts/validate_version_comparison.py` through standard input. The validator does not create files. For a new comparison with partial materials, freeze the common assessable dimensions for the numeric contract and report omitted criteria and coverage separately. Do not encode `N/A` as zero or silently drop dimensions from an inherited contract; when inherited criteria cannot be assessed, report that numeric comparison is unavailable and provide the scoped findings.

For existing structured comparison inputs, omitted readiness rubric metadata retains the legacy validator behavior. For a new generic readiness scorecard with different historical dimensions, set `absolute_readiness_scorecard.rubric` to `generic-7` and use the canonical keys from `calibration-and-rank.md` in `current_dimension_scores`; inapplicable/unassessed values may be `N/A` / `not assessed`, never zero. Its overall score may be `not assessed` if only a scoped stance is supported. Keep the historical/current progress dimensions numeric and unchanged. For a verified external readiness rubric, set `rubric: external` and supply its separate `dimensions`; describe its scale and evidence standard.

The Markdown report can be checked directly with `--report --mode version-comparison`, using the fixed two-scorecard subheadings in `fixed-output-format.md`. This checks presentation and the generic current-readiness table; the original `validate(data)` comparison checks still handle arithmetic and score-decrease provenance when structured data is available internally. Neither route requires a persisted JSON file.
