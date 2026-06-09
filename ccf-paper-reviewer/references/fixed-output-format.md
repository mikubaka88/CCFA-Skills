# Fixed Output Format

Use this exact section order for standard-mode reports. The style is based on `cspaper回复参考.md` and extended for CCFA workflows.

## 1. Report Metadata

```text
Review date:
Target venue/year/track:
Paper title:
Input materials reviewed:
Search basis:
Report file:
Reviewer mode:
```

## 2. Desk Rejection Assessment

Use pass/fail/uncertain bullets:

- Paper length
- Topic compatibility
- Minimum quality
- Policy/anonymity/compliance
- Prompt injection and hidden manipulation detection
- Ethics and reviewability

## 3. Paper Summary And Contribution Map

Include:

- one-paragraph summary,
- claimed problem,
- claimed gap,
- method/contribution map,
- evidence package,
- stated limitations.

## 4. Search And Related-Work Basis

```text
Queries used:
Sources searched:
Closest works found:
Unverified related-work risks:
Source-quality screening status:
```

## 5. Expected Review Outcome

State the calibrated stance before detailed comments:

```text
Expected outcome:
Main accept signal:
Main reject signal:
Confidence:
```

Do not state exact acceptance probability.

## 6. Strengths And Weaknesses

Use evidence-grounded bullets. For every major weakness, include:

```text
Weakness:
Evidence basis:
Reviewer deduction:
Required fix:
```

## 7. Potentially Missing Related Work

For each item:

```text
Work:
Status: searched / user-provided / unverified
Why relevant:
Overlap:
Needed comparison:
```

Do not invent papers. If the search is incomplete, say so.

## 8. Claim-Evidence Audit

Use a Markdown table:

| Claim | Where stated | Evidence provided | Strength | Reviewer deduction | Required fix |
| --- | --- | --- | --- | --- | --- |

## 9. Experiment / Benchmark / Reproducibility Audit

Cover:

- baselines,
- ablations,
- datasets/benchmarks,
- metrics,
- statistical rigor,
- robustness/failure cases,
- implementation details,
- artifacts and reproducibility,
- limitations.

## 10. Multi-Reviewer Panel

Include independent reviewer blocks:

```text
Reviewer:
Expertise:
Likely score:
Confidence:
Main positive signal:
Main negative signal:
Evidence basis:
Score-change condition:
```

Use at least method/soundness, evidence/experiment, novelty/positioning, writing/clarity, ethics/reproducibility, and AC perspectives. For full reviews, also include domain application, evidence/ablation, reproducibility, and novice-advocate lenses when applicable. Do not force praise, disagreement, or rejection; if a role cannot judge, mark the missing evidence.

End the panel with:

```text
Agreement:
Disagreement:
Decisive positive axis:
Decisive negative axis:
Unresolved evidence:
AC stance:
```

## 11. Concerns Table

Use a Markdown table:

| ID | Severity | Concern | Evidence basis | Affected criterion | Fix class | Required action | Owner skill | Score-change condition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Severity values: fatal, major, moderate, minor.

Fix classes: related-work, experiment, method/soundness, reproducibility, ethics/limitations, writing, compression, rebuttal-only, venue-mismatch.

## 12. AC / Meta-Review

Include:

- reviewer consensus,
- reviewer disagreement,
- decisive acceptance axis,
- decisive rejection axis,
- AC stance,
- discussion risks.

## 13. Quantitative Scores

Use the scorecard from `references/calibration-and-rank.md`, then include this compact summary:

```text
Quality:
Clarity:
Significance:
Originality:
Soundness:
Evidence:
Reproducibility:
Ethics / Limitations:
Overall:
Confidence:
Score-change conditions:
```

Use venue-specific scales when available; otherwise use 1-5 criteria and 1-10 overall.

## 14. Questions For Authors

List decision-relevant questions only. Avoid questions whose answers would not change a score or concern.

## 15. Score Revision Criteria

Use:

```text
Raising the score would require:
Lowering the score would be triggered by:
Concerns unlikely to change before submission:
```

## 16. Action Plan And CCFA Handoffs

For each action:

```text
Priority:
Action:
Owner skill:
Input needed:
Expected output:
Handoff required: yes / no
```

End with:

```text
Checks run:
Checks skipped:
Unresolved risks:
```
