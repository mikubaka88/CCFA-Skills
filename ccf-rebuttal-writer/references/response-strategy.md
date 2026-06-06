# Response Strategy

Use this file to classify reviewer concerns and choose a response tactic.

## Concern Types

- Misunderstanding: the paper already contains the answer but it was easy to miss.
- Missing clarity: the work is sound, but the explanation is incomplete or buried.
- Valid weakness: the reviewer is right and the response should concede, bound, and revise.
- Missing evidence: existing evidence is insufficient or not visible enough.
- Requested new result: the reviewer asks for a baseline, ablation, theorem, dataset, user study, or analysis.
- Scope or limitation: the issue is outside the paper's claim or should be bounded honestly.
- Venue-fit or significance concern: the reviewer is unsure why the work matters to the venue.
- Policy or ethics concern: the response must be factual, cautious, and compliance-oriented.
- Hostile or guideline-violating review: the review appears dismissive, inappropriate, or inconsistent with venue rules.

## Global Response Pattern

For a full rebuttal, use this high-level order:

1. Positive opening: begin with strengths, agreement, or reviewer-recognized value.
2. Common concerns: merge repeated high-impact issues across reviewers.
3. Reviewer-specific clarifications: answer individual comments with reviewer color labels.
4. Closing signal: emphasize shared goals, concrete clarifications, and remaining transparency.

Within each issue, use:

```text
Quote -> Direct answer -> Evidence -> Deeper intent -> Exact change or transparent limitation
```

Prefer answers that give concrete data, paper locations, or already-completed analyses over argumentative prose.

## Response Tactics

### Positive opening

Use when reviewers acknowledge strengths, novelty, clarity, usefulness, strong experiments, or practical value.

Rules:

- Start by thanking reviewers and restating the strongest positive signals.
- Do not sound self-congratulatory.
- Tie the positive signal to the paper's central contribution.
- Use this to keep the committee aware of the work's upside while reading criticisms.

### Quote then direct answer

Use for every material concern.

Structure:

```text
\reviewerquote{R2}{"...why was GLORP3 not evaluated?"}
\directanswer{Direct answer: GLORP3 is not in the task scope because [...]. We additionally report results on [datasets], which test the same completeness concern.}
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

Answer the literal question first, then address the deeper concern so other committee members do not inherit the doubt.

### Merge common concerns

Use when multiple reviewers raise the same underlying concern.

Rules:

- Create one common-concern response before reviewer-specific details.
- Name the reviewers with color labels.
- Explain the shared concern once, then refer back in individual clarifications.
- This saves budget and reduces repeated defensive language.

### Clarify

Use when the evidence exists but was hard to find.

Structure:

```text
Thank you for pointing this out. The paper addresses this in [location], where we show [evidence]. To make this clearer, we will revise [section/figure/table] to state [specific change].
```

### Correct misunderstanding

Use when the reviewer inferred something incorrect.

Rules:

- Do not say the reviewer is wrong.
- State the correct interpretation and why the manuscript may have caused confusion.
- Promise a precise wording or figure change.

### Concede and revise

Use when the reviewer identified a real weakness that can be fixed in text or analysis.

Structure:

```text
We agree this was insufficiently clear. We will revise [section] to [specific action], and we will add [evidence/detail] to support [claim].
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

- Prefer "We tested ... and found ..." over "We will test ...".
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
- Promise a limitation or discussion update.

### Decline infeasible request

Use sparingly when requested work cannot be completed before the response deadline.

Rules:

- Be respectful.
- Explain why the existing evidence still supports the central claim.
- State whether the issue will be added as a limitation or future work.

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

1. Positive opening and shared strengths.
2. AC/meta-review decisive concerns.
3. High-confidence answers to fatal soundness, novelty, evidence, or completeness concerns.
4. Shared concerns raised by multiple reviewers.
5. Misunderstandings that can change score or confidence.
6. Missing baselines, ablations, or reproducibility details.
7. Harder secondary issues and transparent limitations.
8. Local clarity, formatting, minor suggestions, and future-work items.

## Tone Rules

- Thank the reviewer without over-apologizing.
- Be direct and evidence-specific.
- Avoid emotional language and defensiveness.
- Avoid "we believe" when a factual result can be cited.
- Avoid promising more than can be done.
- Prefer "we will revise" only for concrete manuscript changes.
- Re-explain acronyms, datasets, settings, and key assumptions because committee members may not remember the paper.
- Emphasize shared goals: fair comparison, reproducibility, complete evaluation, or clearer claims.
