# Response Strategy

Use this file to classify reviewer concerns and choose a response tactic.

## Concern Types

- Misunderstanding: the review's interpretation conflicts with the inspected manuscript or evidence; check whether the wording contributed to it.
- Missing clarity: an explanation is incomplete or buried; clarity alone does not establish scientific soundness.
- Valid weakness: the criticism is supported; acknowledge the exact defect and its consequence, then state the appropriate repair or remaining gap.
- Missing evidence: existing evidence is insufficient or not visible enough.
- Requested new result: the reviewer asks for a baseline, ablation, theorem, dataset, user study, or analysis.
- Scope or limitation: the issue is outside the paper's claim or should be bounded honestly.
- Venue-fit or significance concern: the reviewer is unsure why the work matters to the venue.
- Policy or ethics concern: establish the applicable requirement, actual conduct, and any necessary correction.
- Hostile or guideline-violating review: the review appears dismissive, inappropriate, or inconsistent with venue rules.

## Global Response Pattern

For a full rebuttal, organize the supplied concerns in this order, adapting to the required response form:

1. Main answer: address the decisive issue; include a brief acknowledgement or reviewer-recognized strength when useful and actually present.
2. Common concerns: merge repeated high-impact issues across reviewers when doing so preserves attribution and answer coverage.
3. Reviewer-specific clarifications: answer remaining individual comments using the venue's identifiers.
4. Closing: include only a useful summary of the answer or an actual outstanding decision.

Within each issue, identify the concern, answer it directly, and give the supporting evidence. Quote only when needed for attribution. Address a broader concern when the review supports that interpretation; include an exact change or material limitation only when one exists:

```text
Concern -> Direct answer -> Evidence -> Applicable change or unresolved point
```

Prefer answers that give concrete data, paper locations, or already-completed analyses over argumentative prose.

## Response Tactics

### Positive opening

Use when reviewers acknowledge strengths, novelty, clarity, usefulness, strong experiments, or practical value.

Rules:

- A brief acknowledgement may introduce the response; restate a positive signal only when the review actually contains it and it helps explain the contribution.
- Do not sound self-congratulatory.
- Tie the positive signal to the paper's central contribution.
- Keep it shorter than the substantive answer. A review without praise does not require an invented positive opening.

### Quote then direct answer

Identify every material concern. Use a short quote when it helps identify or distinguish the issue; otherwise use its reviewer ID or a faithful summary.

Structure:

```text
\reviewerquote{revtwo}{R2}{Why was [baseline] not evaluated?}
\directanswer{[Explain whether the baseline tests the stated claim, using the actual task and protocol. Cite an existing comparison or state the specific unresolved gap.]}
```

Rules:

- Quote only the core concern, not the full review.
- Give a direct answer before background.
- Keep the reply conversational and evidence-grounded.

### Deeper intent

Use when a literal question points to a broader concern.

Examples:

- "Why no GLORP3?" may mean "Is the evaluation complete?"
- "Why this baseline?" may mean "Are comparisons fair?"
- "What is the mechanism?" may mean "Is the method sound?"

Answer the literal question first. Address a broader concern only when the comment or its context supports that reading; do not invent a hidden objection to answer.

### Merge common concerns

Use when multiple reviewers raise the same underlying concern.

Rules:

- Create one common-concern response before reviewer-specific details.
- Name the reviewers with the required identifiers; color is an optional TeX aid when permitted.
- Explain the shared concern once, then refer back in individual clarifications.
- This saves budget and reduces repeated defensive language.

### Clarify

Use when the evidence exists but was hard to find.

Structure:

```text
The paper addresses this in [location], where [evidence]. [If clarification is needed and authorized: We will revise the relevant passage to state the specific missing distinction.]
```

### Correct misunderstanding

Use when the reviewer inferred something incorrect.

Rules:

- State the factual disagreement directly and respectfully, with the manuscript location or evidence that resolves it.
- Identify ambiguous manuscript wording when it exists; do not concede a writing defect merely because an interpretation was incorrect.
- Promise a wording or figure change only when it resolves an identified problem and is within scope. An accurate clarification may need no manuscript change.

### Concede and revise

Use when the reviewer identified a real weakness that can be fixed in text or analysis.

Structure:

```text
The current [claim/protocol/explanation] has [specific defect and consequence]. [Describe the supported correction, or the evidence still needed. Distinguish a completed change from an authorized plan.]
```

### Add existing evidence

Use only when the result already exists.

Rules:

- Name the exact result, metric, dataset, table, figure, appendix, or experiment.
- Say where it will be moved or highlighted.
- Do not claim a new experiment is complete unless it is.

### Deliver now, not vague promise

Use when the response can include a new analysis, number, table summary, or explanation immediately.

Rules:

- Use "We tested ... and found ..." only for an actual completed test. Give an available derivation, explanation, or evidence location directly when that answers the concern.
- Include the key result in the response itself.
- If manuscript changes are promised, still give the substantive answer now.

### Use emphasis

Use sparingly to guide busy committee readers.

Rules:

- Bold only the decisive answer, dataset, result, or limitation.
- Avoid all-caps except for short labels such as `DIRECT ANSWER`.
- Do not use emphasis to compensate for weak evidence.

### Narrow claim

Use when the paper overclaims.

Structure:

```text
We agree the original wording was too broad. We will revise the claim from [broad claim] to [scoped claim], which is supported by [evidence].
```

### Bound limitation

Use when the concern is real but not fatal.

Rules:

- Admit the limitation plainly.
- Explain why it does not invalidate the central contribution.
- Add a limitation or discussion update when the manuscript omits this material boundary and revision is authorized; an already accurate statement needs only its location.

### Decline infeasible request

Use sparingly when requested work cannot be completed before the response deadline.

Rules:

- Be respectful.
- State what the existing evidence supports and whether the unperformed work leaves a material claim unresolved. Do not assert adequacy merely because the deadline prevents a test.
- Add a limitation or future-work commitment only when the scientific gap and authorized plan warrant it; inability to perform a requested test is not itself a scientific limitation.

### Handle hostile or inappropriate review

Use only when the review appears to violate reviewing norms or contains unsupported hostile claims.

Rules:

- Do not retaliate in the public response.
- Calmly correct factual errors and point to evidence.
- Ask the committee to evaluate the concern against the evidence.
- If necessary, suggest a confidential note to the program chairs rather than escalating in the rebuttal text.

### Thank constructive reviewers

Use when a reviewer provides careful suggestions or helpful analysis.

Rules:

- Thank them specifically.
- If their suggestion was tried, report what happened.
- If it cannot be done, explain transparently and preserve goodwill.

## Priority Rules

Answer in this order:

1. AC/meta-review decisive concerns.
2. Soundness, novelty, evidence, or completeness issues that could change the paper-level judgment, including unresolved ones.
3. Available evidence that answers those concerns.
4. Shared concerns raised by multiple reviewers.
5. Misunderstandings that can change score or confidence.
6. Missing comparisons or reproducibility details that matter to the stated claims.
7. Harder secondary issues and transparent limitations.
8. Local clarity, formatting, minor suggestions, and future-work items.

## Tone Rules

- Thank the reviewer without over-apologizing.
- Be direct and evidence-specific.
- Avoid emotional language and defensiveness.
- Avoid "we believe" when a factual result can be cited.
- Avoid promising more than can be done.
- Prefer "we will revise" only for concrete manuscript changes.
- Define acronyms, settings, or assumptions needed to understand the answer within the response budget.
- Explain the actual comparison, protocol, or claim instead of appending a generic assurance about shared goals.
