# Research Writing Patterns

Use this file for full-paper drafting, section-specific rewriting, and exemplar-mode adaptation. It consolidates section-level writing patterns for CCFA while keeping venue routing, evidence policy, and artifact contracts in CCFA.

These are transferable writing patterns, not copied examples. Do not reuse sentence templates, distinctive wording, examples, claims, or confidence from any source paper or external skill. Adapt the logic to the user's actual problem, method, and evidence.

## Dense Output Rule

For broad writing tasks, produce the artifact first and make it substantial:

- Full manuscript request: write a full LaTeX/Markdown manuscript, not only an abstract or outline.
- Section request: write the section, not only paragraph roles.
- Revision request: provide revised text in source format plus only the necessary edit notes.
- Exemplar request: show the source writing pattern, then adapt it into original text.

Avoid empty "next steps" and generic warnings. A warning is useful only if it names the unsupported claim, missing evidence, affected section, and concrete fix.

## Exemplar And Source-Paper Mode

When the user asks to learn from a source paper or exemplar:

1. Extract the source paper's writing mode:
   - abstract arc,
   - introduction paragraph roles,
   - technical challenge chain,
   - insight sentence,
   - method module decomposition,
   - experiment evidence sequence,
   - limitation framing.
2. Map that mode to the user's paper:
   - which roles fit,
   - which roles would distort the contribution,
   - what evidence is missing,
   - what should be rewritten rather than copied.
3. Draft original text using the mapped roles.

Visible output should include the adapted artifact. The source-mode map can be concise unless the user asks for a detailed style audit.

## Abstract Patterns

Pick one pattern, not all three.

### Challenge -> Contribution

Use when the core contribution solves one sharp technical challenge.

1. Task and why it matters.
2. Prior-method challenge and root reason.
3. Contribution that directly addresses the challenge.
4. Technical advantage.
5. Evidence summary.

### Challenge -> Insight -> Contribution

Use when the paper's value is a clear conceptual insight.

1. Task.
2. Technical challenge.
3. One sentence with the insight.
4. Method that implements the insight.
5. Benefits and evidence.

### Multiple Contributions

Use when the paper has several independent technical pieces.

1. Task and setting.
2. Short prior-work contrast if needed.
3. Contribution 1 plus advantage.
4. Contribution 2 plus advantage.
5. Contribution 3 plus advantage.
6. Evidence summary.

Abstract checks:

- A reader can identify task, challenge, insight/method, and evidence in one pass.
- Every result claim is later supported.
- Method names are readable before details are introduced.
- No sentence carries several unrelated messages.

## Introduction Patterns

Use backward reasoning before drafting:

1. What problem is solved?
2. Why do existing solutions fail?
3. What root technical reason causes the failure?
4. What insight makes the proposed method plausible?
5. What evidence will convince reviewers?

Then write forward:

1. Task/application/value.
2. Prior methods and their progress.
3. Remaining technical challenge with root reason.
4. Insight and method preview.
5. Contributions and evidence preview.

Task-opening variants:

- Niche task: define the task, then name applications.
- Familiar task: start from application or scientific importance.
- New setting: start broad, then narrow to the exact input/output setting.
- Challenge-first opening: expose the failure case in the first paragraph when it makes the paper more compelling.

Challenge-chain variants:

- Existing task: general challenge -> traditional line -> recent line -> remaining challenge.
- Existing task with historical insight: modern limitation -> classical insight -> why old line is insufficient -> new method.
- Novel task: define the challenge and decompose it into two or three concrete obstacles.

Avoid naive-baseline framing. Do not make the paper sound like "we tried an obvious baseline and patched it." Frame the root technical issue and the non-obvious insight instead.

## Related Work Pattern

Use 2-4 focused topic groups:

1. Topic scope.
2. Representative methods and shared assumptions.
3. Limitation tied to this paper's exact challenge.
4. Technical distinction.

Do not hide the closest competitor. If the closest work is unknown, route to `ccf-literature-searcher` or mark the gap as unsearched.

## Method Pattern

Before writing Method, build a module table:

| Module | Input | Operation | Output | Motivation | Technical advantage | Validated by |
| --- | --- | --- | --- | --- | --- | --- |

Each module subsection should contain:

1. Motivation: why the module is needed.
2. Design: representation, architecture, equation, algorithm, or data structure.
3. Forward process: input -> step -> output.
4. Technical advantage: why this design addresses the challenge.
5. Validation pointer: ablation, theorem, analysis, or qualitative result.

Method clarity checks:

- The overview gives the task setting, core contribution, and subsection map.
- Notation appears before use.
- Every module has a reason to exist.
- Implementation details are sufficient for reproduction or explicitly deferred to appendix.
- The method does not rely on claims that experiments never test.

## Experiment Pattern

Experiments should answer three reviewer questions:

1. Effectiveness: is the method better than strong baselines under fair protocols?
2. Causality: which modules/design choices create the gain?
3. Generalization and limits: when does it work, fail, or become costly?

Recommended section order:

1. Setup: datasets, preprocessing, metrics, baselines, implementation.
2. Main results: one table per primary claim.
3. Ablation: remove/replace/disable major modules.
4. Analysis: robustness, efficiency, sensitivity, qualitative examples, or failure cases.
5. Limitations tied to evaluation scope.

Table/figure rules:

- One table/figure, one message.
- Captions state setting and takeaway.
- Use `booktabs`; avoid vertical rules and dense line stacks.
- Mark metric direction and units.
- Keep numeric precision consistent.
- Group multi-dataset results with clean headers.
- Do not highlight too many cells.

## Conclusion Pattern

1. Restate problem and method.
2. State the key insight.
3. Summarize strongest evidence.
4. Bound limitations as scope boundaries, not hidden fatal flaws.
5. Name a concrete future direction without adding unsupported claims.

## End-Of-Draft Self-Review

For full-paper drafts, run this internally and surface only unresolved issues unless the user asks for the review:

| Dimension | Question | Status | Required fix |
| --- | --- | --- | --- |
| Contribution | What new knowledge does the paper provide? | pass / revise / needs evidence | |
| Clarity | Can a reader reproduce the method? | pass / revise / needs evidence | |
| Empirical strength | Are main claims backed by strong results? | pass / revise / needs evidence | |
| Evaluation completeness | Are baselines, ablations, and metrics sufficient? | pass / revise / needs evidence | |
| Method soundness | Do benefits outweigh assumptions and limitations? | pass / revise / needs evidence | |
