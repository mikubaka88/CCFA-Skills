# Expert Review Loop

Use this before submission, after a full section is drafted, or whenever the user asks for reviewer-style critique. Pair it with `references/score-lifting-loop.md` when the goal is reducing weak-score risks or rejection risk.

## Review Roles

Simulate multiple reviewer perspectives:

1. Area-chair view: venue fit, contribution level, fatal risks.
2. Method expert: soundness, novelty, assumptions, technical clarity.
3. Experiment expert: baselines, metrics, ablations, significance, robustness.
4. Writing expert: storyline, paragraph flow, terminology, figure/table readability.
5. Target-venue reviewer: alignment with the conference's review culture and expected evidence.
6. Ethics/reproducibility reviewer when relevant.

## Closed-Loop Workflow

1. Calibrate the review target:
   - target venue and track,
   - likely review form or scoring scale,
   - current known scores if available,
   - target threshold, defaulting to no fatal reject risk and at least weak-accept stance.
2. Triage for fatal risks:
   - unclear contribution,
   - unsupported central claim,
   - weak baseline,
   - missing ablation/proof/study,
   - overclaim,
   - venue mismatch,
   - reproducibility gap,
   - ethical or policy issue.
3. Produce expert reviews using the review form below, including numeric score, confidence, and criterion-level deductions.
4. Convert each weakness into a revision action:
   - rewrite,
   - add evidence,
   - weaken claim,
   - add experiment,
   - add citation,
   - reorganize section,
   - improve figure/table,
   - add limitation.
5. Classify each action as writing-fixable, analysis-fixable, citation/positioning, figure/table, reproducibility, requires-new-result, accepted-limitation, or venue-mismatch.
6. Revise the draft or provide exact edit instructions.
7. Re-review and re-score the revised version.
8. Repeat until all high-severity issues are resolved, or explicitly listed as requiring new results or accepted limitations.

## Review Form

```text
Summary:
Contribution:
Strengths:
Weaknesses:
Questions for authors:
Claim-evidence risks:
Missing experiments/proofs/studies:
Clarity and organization issues:
Venue-fit concerns:
Ethics/reproducibility concerns:
Severity: high / medium / low
Recommended action:
Confidence:
Likely score:
Per-criterion deductions:
Score-change condition:
```

## Revision Plan Format

```text
Issue:
Reviewer concern:
Evidence in current draft:
Required change:
Where to revise:
Suggested rewrite or experiment:
Fix class:
Risk-reduction condition:
Status: open / fixed / requires new result / accepted limitation
```

## Severity Rules

High severity:

- Central contribution is unclear or unsupported.
- Main experiment/proof/study does not validate the claimed novelty.
- Strongest baseline is missing.
- Method cannot be reproduced from the paper.
- Threat model, dataset, or evaluation protocol invalidates the claim.
- Writing makes the paper look incremental when the idea is stronger.

Medium severity:

- A module motivation is weak.
- A paragraph is hard to follow.
- A table needs clearer caption or grouping.
- A limitation should be bounded more carefully.
- Related Work lacks a close citation but not a core competitor.

Low severity:

- Local wording, style, ordering, or formatting improvements.

## Re-Review Gate

After revision, ask:

1. Would the same reviewer repeat the same high-severity criticism?
2. Does the revised story explain why the method is needed?
3. Does each contribution have explicit evidence?
4. Are overclaims removed or supported?
5. Has the target venue adapter been respected?
6. Is the remaining risk acceptable and honestly disclosed?

Do not call the paper ready while any central claim remains unsupported.

## Score Consistency Gate

Before finalizing the review, ask:

1. Does the overall score match the severity of the listed weaknesses?
2. Would the most skeptical reviewer still have a fatal concern after the proposed revision?
3. Are conditional diagnostic changes tied to concrete edits or evidence?
4. Are required new experiments, proofs, studies, or baselines clearly separated from writing-only fixes?
5. Does the review use the target venue's taste instead of a generic positive tone?

## Output Modes

For a full draft:

1. Give a concise meta-review first.
2. List high-severity issues before line edits.
3. Provide a revision plan.
4. Then rewrite selected sections if requested.

For a section:

1. Review section role in the whole story.
2. Identify local weaknesses.
3. Rewrite or annotate paragraph-by-paragraph.
4. Update cross-section risks.

For a paragraph:

1. Identify paragraph role.
2. Give one or two key problems.
3. Provide a revised paragraph.
4. Explain which reviewer risk the revision reduces.
