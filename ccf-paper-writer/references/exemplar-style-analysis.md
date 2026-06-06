# Exemplar Style Analysis

Use this file when the user provides strong papers as writing references or when a built-in exemplar card is selected from `references/exemplars/index.md`. Extract transferable writing technique only. Do not copy content, claims, examples, terminology, or distinctive phrasing.

## Inputs

Ask for or infer:

- Target venue and year if known.
- 2-5 reference papers the user considers well written.
- Built-in exemplar cards from `references/exemplars/cards/` when the user has not supplied papers or wants venue-specific best-paper style.
- The user's current draft, outline, experiment table, figures, or raw idea.
- Which sections need imitation at the writing-technique level.

## Non-Copying Rule

Reference papers may guide:

- Section ordering.
- Paragraph roles.
- Transition strategies.
- How challenges are framed.
- How contributions are announced.
- How methods are decomposed.
- How figures/tables are introduced.
- How experiments are sequenced.
- How limitations are disclosed.

Reference papers must not provide:

- Reused sentences or sentence templates with only noun replacement.
- The same technical claim.
- The same novelty framing if it does not fit the user's work.
- Distinctive examples, metaphors, or phrasings.
- Unsupported confidence borrowed from another paper's evidence.

## Extraction Workflow

0. If using built-in exemplars, load `references/exemplars/index.md`, pick at most 2-4 cards that match the target venue, paper type, and evidence style, then read only those card files.
1. Read the paper at the section level first. Identify the macro story:
   - task/application,
   - pain point,
   - prior gap,
   - insight,
   - method mechanism,
   - evidence,
   - limitation or discussion.
2. Build a paragraph-role map for each relevant section:
   - `context`,
   - `gap`,
   - `root cause`,
   - `insight`,
   - `method preview`,
   - `contribution`,
   - `evidence`,
   - `transition`,
   - `limitation`.
3. Extract writing moves rather than words:
   - how the paragraph opens,
   - what contrast or causal relation it uses,
   - where it places evidence,
   - how it reduces reviewer uncertainty,
   - how it transitions to the next paragraph.
4. Compare multiple papers and synthesize common patterns. Prefer patterns repeated across papers over one paper's idiosyncratic style.
5. Adapt the pattern to the user's story blueprint, not the other way around.

## Extraction Table

Use this format:

```text
Paper:
Venue/year:
Section:
Paragraph role:
Writing move:
Transition pattern:
Evidence pattern:
Why this works for reviewers:
Reusable technique:
How to adapt to our paper:
Do-not-copy boundary:
```

## Section-Specific Signals

### Abstract

Look for:

- How the first sentence positions the task.
- Whether the gap is framed as technical limitation, practical need, or missing capability.
- How the method is named without overloading details.
- Whether results are presented as numerical gains, broad validation, or qualitative improvement.

### Introduction

Look for:

- The paragraph where the core challenge appears.
- Whether prior work is used as a ladder toward the gap or as a citation list.
- The sentence that introduces the insight.
- The contribution bullets and whether each contribution maps to later evidence.

### Method

Look for:

- Overview figure placement.
- How modules are named.
- Whether each module starts with motivation or design.
- How forward process is described.
- Where assumptions and implementation details appear.

### Experiments

Look for:

- Experiment sequence: setup -> comparison -> ablation -> analysis -> limitation.
- Table/figure message per result.
- How baselines are described.
- How qualitative examples support quantitative findings.
- Whether claims in Introduction are revisited.

## Adaptation Output

After analyzing exemplars, produce:

1. `Reference style summary`: 5-10 writing techniques.
2. `Our story alignment`: which techniques fit the user's paper.
3. `Section pattern`: paragraph roles for the target section.
4. `Drafting warnings`: techniques that should not be used because they would distort the user's contribution or overclaim.
5. `Originality guard`: a reminder that all final prose must be newly written for the user's paper.
