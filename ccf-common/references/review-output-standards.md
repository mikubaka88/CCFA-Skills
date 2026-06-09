# CCFA Review And Output Standards

Use this shared reference when a CCFA skill produces review, scoring, risk diagnosis, revision priorities, or monitor-to-review handoff signals.

## Quantitative Feedback

Every review-style output must separate three values:

- **Criterion score:** how strong the artifact is on one dimension, normally 1-5 unless the venue defines another scale.
- **Overall score or stance:** the calibrated decision-level result, normally 1-10 for paper review and weighted 1-5 or 1-10 for idea review.
- **Confidence:** how much inspectable evidence was available for the judgment; low confidence does not automatically mean a low score.

For each score of 3 or below, include the deduction and the condition that would move the score. Do not give a number without an evidence basis.

```text
Dimension:
Score:
Confidence:
Evidence basis:
Deduction:
Repair condition:
Expected score movement:
```

Use score movement conservatively. Prefer ranges such as `+0.5 to +1 overall` only when a concrete change is likely to affect the calibrated stance. Do not claim acceptance probability.

## Multi-Reviewer Panel

Panel reviewers must be independent before synthesis. Each role should inspect a different failure mode, use evidence from the idea, paper, manuscript text, or searched source, and state uncertainty when evidence is missing.

Required discipline:

- Do not force every reviewer to disagree.
- Do not force praise when no real strength is visible.
- Do not force rejection when the evidence does not support it.
- If a role finds no serious concern, say why and name the supporting evidence.
- If a role cannot judge, mark `insufficient evidence` and state what input would change that.
- Synthesis must not average away fatal flaws; the final stance follows the strongest unresolved decision-relevant concern.

Per-reviewer block:

```text
Reviewer:
Lens:
Score / score tendency:
Confidence:
Main positive signal:
Main negative signal:
Evidence basis:
Score-change condition:
```

Panel synthesis should include:

```text
Agreement:
Disagreement:
Decisive accept axis:
Decisive reject axis:
Unresolved evidence:
Final calibrated stance:
```

## Output Quality Gate

Before returning a visible artifact, read the answer once as if it were going to the user unchanged.

Check:

1. The section order matches the promised output contract.
2. Every table has valid Markdown separators and the same number of columns in each row.
3. Scores, confidence, and recommendations are internally consistent.
4. Bullet lists use parallel grammar where possible: same part of speech, same level of detail, same action style.
5. Causal or progressive logic is explicit: problem -> reason -> consequence -> action.
6. Punctuation is consistent within the chosen language; avoid mixed full-width and half-width punctuation when it distracts from the result.
7. No placeholder such as `TBD`, `TODO`, `[fill]`, or empty heading remains unless it is intentionally marking missing user evidence.
8. No generic filler remains, such as "improve clarity", "needs more experiments", or "strengthen motivation" without the exact location, missing evidence, and action.

For Chinese outputs, prefer concise headings, complete table labels, and direct action verbs. For English outputs, prefer short declarative sentences and avoid inflated reviewer language.
