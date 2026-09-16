# Calibration And Rank

Use this file for scores, calibrated stance, confidence, and cohort-relative interpretation.

## Default Overall Scale

Use 1-10 when the venue does not specify a scale:

- 10: award-level or clear top-tier accept.
- 9: strong accept.
- 8: accept.
- 7: weak accept.
- 6: borderline positive.
- 5: borderline negative.
- 4: weak reject.
- 3: reject.
- 2: strong reject.
- 1: desk-reject-level or unreviewable.

## Canonical Scientific Criteria

This is the single definition of the `generic-7` scientific rubric, including its order and display names. Use integer criterion scores of 1-5. The report template, universal audit, and validator refer here; do not maintain another dimension list or weight these dimensions by default.

| Key | English label | 中文名称 | Evidence for a strong assessment | Evidence for a weak assessment |
| --- | --- | --- | --- | --- |
| novelty | Novelty | 新颖性 | A nontrivial new contribution or insight, with a verified difference from the closest work. | Demonstrated overlap, an overstated novelty claim, or an unclear contribution. |
| soundness | Soundness | 正确性 | Valid assumptions, derivations, algorithms, implementation, or study design for the stated claim. | An identified logical contradiction, invalid assumption, proof gap, or flawed evaluation protocol. |
| evidence | Evidence | 证据 | Adequate, inspectable support matched to the claims and contribution type: proofs, experiments, analysis, studies, or workloads. | A central asserted claim is unsupported or contradicted by the inspected material. |
| significance | Significance | 意义 | Meaningful new knowledge, capability, framing, data, or practical value for the target community. | A substantiated mismatch between the claimed importance and the actual contribution. |
| clarity | Clarity | 清晰度 | The contribution, mechanism, evidence, and boundaries are recoverable from the manuscript. | Specific organization, notation, or explanation defects obstruct understanding. |
| reproducibility | Reproducibility | 可复核性 | Enough definitions, proof steps, protocols, data/artifact details, or study documentation to check the claims. | Identified omissions prevent a relevant claim from being independently assessed. |
| ethics_limitations | Ethics / Limitations | 伦理与局限 | Relevant risks and material limitations are handled in the work and its disclosure. | An observed material risk or limitation is unaddressed; a policy concern cites an applicable verified rule. |

`Originality` is an alias for `Novelty`, not an extra score. `Positioning / Related work` supplies evidence for Novelty; do not deduct twice for the same overlap. `Quality` is a synthesis in the overall judgment, not an eighth generic criterion. A verified venue form may use these names or different scales; preserve that form, label its venue/year/track, and do not silently convert it into generic scores. Historical frozen comparison rubrics remain unchanged.

## Criterion Scale

Anchors:

- 5: clear strength,
- 4: good,
- 3: mixed,
- 2: weak,
- 1: fatal or near-fatal.

## Stance Bands

- Clear accept: no fatal risk; most criteria 4-5; overall usually 8-10.
- Lean accept: no fatal risk; one or two moderate concerns; overall usually 7.
- Borderline: merits and risks balanced; overall usually 5-6.
- Lean reject: one major concern or multiple moderate concerns; overall usually 4.
- Clear reject: fatal technical, novelty, evidence, policy, or venue issue; overall usually 1-3.

## Cohort-Relative Interpretation

When the user asks for rank or cohort-relative quality, require an inspectable comparable set, common rubric, and declared cohort. Report only the rank supported by those inputs. Without them, use the absolute stance anchors above and omit relative bands, percentiles, outperformed counts, and distribution plots. Scores from different cohorts or calibration methods are not interchangeable.

## Confidence

Use integer confidence scores of 1-5 for the judgment actually made:

- 5: decisive evidence and counterarguments were checked; relevant domain knowledge supports the assessment and little material uncertainty remains.
- 4: the main judgment is well checked; minor uncertainty is unlikely to change it.
- 3: a material assumption, source, or interpretation remains unresolved and could change the judgment.
- 2: substantial uncertainty remains about a decisive point or the reviewer's relevant expertise.
- 1: the available basis is too weak for more than a tentative assessment.

State materials inspected and unavailable separately in report scope. A complete PDF does not establish high confidence by itself; a short excerpt can support a high-confidence local finding without supporting a whole-paper verdict. Identify which judgment a missing appendix, source, or artifact prevents. Low confidence changes certainty, not automatically the quality score. Use `not assessed` when no judgment was made.

## Cross-Version Calibration

For re-review or manuscript-version comparison, load `version-comparison.md`. Freeze dimensions, weights, anchors, reviewer roles, thresholds, and evidence standard before comparing versions. Report relative progress, current absolute readiness, and comparison confidence separately. Every decrease must be traceable to a current-version regression or newly revealed evidence. Previously undetected issues apply consistently to both versions rather than silently lowering only the current score.

## Consistency Check

Before finalizing scores:

1. Does the overall score match the strongest unresolved weakness?
2. Would a skeptical reviewer repeat a fatal concern?
3. Are strength claims backed by exact manuscript evidence?
4. Are score-change conditions concrete and feasible?
5. Is the score calibrated to the named venue rather than generic positivity?
6. For version comparison, did both versions use the same frozen contract and did every decrease pass the provenance rule?

## Mandatory Scorecard Output

For standard scientific/full review, put this scorecard inside the Critical Reviewer Ratings section of `fixed-output-format.md`. Use an explicit venue form when available. A scientific review of a narrow excerpt retains all seven rows, marking unassessed or inapplicable criteria with their status and reason. Writing-only assessment uses the separate writing rubric, never this scientific scorecard. Honor no-score requests with qualitative judgments. If available material cannot support an overall numerical judgment, put `not assessed` in Overall and explain the evidence-limited stance and coverage. A verified central contradiction can support a negative stance even when other dimensions remain unassessed.

```markdown
### Scorecard

| Dimension | Score (1-5) | Confidence (1-5) | Evidence basis | Deduction / score-change condition |
|:---|:---:|:---:|:---|:---|
| [canonical dimension] | [1-5 or status] | [1-5 or status] | [section/paragraph/line ref] | [deduction and repair condition] |

**Overall:** [1-10]  | **Scholarly Confidence:** [1-5]

**Recommendation:** [accept/weak-accept/borderline/weak-reject/reject]
**Verdict:** [What evidence would change the judgment, and why?]
```

Expand the row into exactly the seven dimensions in the canonical table, in that order, using its English label, Chinese label, or `English label / 中文名称`. Keep all seven rows in a generic detailed scientific/full report. Use `N/A` with a reason for an inapplicable dimension and `not assessed` with a reason for an unassessed one; never use 0. In a no-score report, replace the Score column with Judgment and keep the same rows with qualitative findings. A detailed report retains one Overall field and one Scholarly Confidence field, qualitative when requested. In version comparison, the current-readiness confidence may instead appear once under Confidence And Comparability; do not duplicate it. Brief reports may summarize applicable ratings without reproducing the full table. Writing reports use their writing rubric instead.

## Scoring Rules

1. Assess each applicable dimension. Use `N/A` for an inapplicable criterion and `not assessed` when necessary material was not supplied; neither is zero. Do not invent a substitute score for a criterion outside scope. Missing support for an actual manuscript claim can justify a low Evidence score; unavailable excerpts do not establish a whole-paper defect.
2. Each score must be backed by at least one verifiable manuscript reference. Do not write "The paper is not well organized." Write "Section 3.1 (para 2) introduces a method without naming or motivating the insight and fails to separate the differential contribution from the components. 3/5 clarity."
3. Evidence means inspected support, not a promise. A high score requires support sufficient for the central claims and contribution type. A theory paper may earn it through rigorous proofs; a qualitative study through appropriate analysis; an empirical mechanism claim may need a decisive ablation. Do not impose ablations, robustness tests, dataset counts, or SOTA wins on every contribution. Unavailable input alone is not evidence of a missing result.
4. Confidence reflects how well the relevant claims could be checked and familiarity with the closest work. Identify which decisive judgment an unavailable appendix or code prevents; its absence alone does not force confidence to 1/5. Separate confidence from quality and scientific stance.
5. Select one anchored integer for generic criterion, overall, and confidence scores; do not round an average of reviewer votes. If the paper is between 6 and 7, explain the decisive tie-breaker. A venue's verified scale takes precedence. Weighted progress deltas and writing composites may be fractional; they are not generic overall ratings.

## Score-Change Conditions

After the scorecard, include a compact condition table:

| Change | Condition | Likely affected dimensions | Expected movement |
| --- | --- | --- | --- |
| Raise score | [concrete evidence/edit] | [dimensions] | [could move to the next stated anchor; not guaranteed] |
| Lower score | [failure revealed by closer inspection] | [dimensions] | [could move to a lower stated anchor or change the stance] |
| No quick change | [issue requiring new result or new method] | [dimensions] | [unlikely before submission] |
