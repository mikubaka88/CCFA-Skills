# Paper Writing Review Rubric

Use this rubric when reviewing a manuscript from the perspective of writing quality, reviewer readability, format discipline, and idea presentation. This file is not a replacement for scientific validation; it diagnoses how the paper communicates its scientific value.

## Review Dimensions

Score each dimension on 1-5 when enough text is available.

| Dimension | Weight | What To Inspect |
| --- | ---: | --- |
| Storyline and motivation | 10 | Whether the paper makes the problem, gap, and stakes unavoidable before presenting the method. |
| Contribution display | 10 | Whether contributions are specific, non-overlapping, evidence-backed, and visible in abstract/introduction/conclusion. |
| Paragraph logic | 10 | Whether each paragraph has one job, a clear topic sentence, causal flow, and no mixed objectives. |
| Claim-evidence alignment | 12 | Whether every strong claim is supported by experiment, proof, citation, example, or qualified language. |
| Method readability | 9 | Whether notation, modules, algorithm steps, assumptions, and design choices are introduced in the right order. |
| Experiment narration | 9 | Whether tables/figures are introduced before interpretation and whether the text explains what each result proves. |
| Related-work positioning | 8 | Whether closest work is compared on technical axes rather than listed chronologically. |
| Terminology and notation consistency | 8 | Whether key terms, symbols, dataset names, model names, and claims stay stable across sections. |
| Prose discipline and voice | 10 | Whether the paper avoids defensive/incremental framing, label-heavy symbols, number-only abstracts, formula dumping, third-person manuscript narration, punctuation-driven structure, unsupported hype, and overlong compound sentences. |
| LaTeX and format discipline | 6 | Whether the manuscript follows venue style, references, captions, labels, equations, algorithms, and page/line constraints. |
| Reviewer-facing risk | 8 | Whether the writing creates avoidable rejection risks: hidden contribution, exaggerated claim, missing limitation, unclear baseline, or inconsistent story. |

Weights sum to 100. Compute:

```text
Writing score (1-5) = sum(dimension score * weight) / 100
Writing risk band = low / moderate / high / severe
```

Do not present the writing score as an acceptance probability. It measures communication risk and reviewer readability, not scientific validity.

## Quantitative Writing Feedback

Include this scorecard in standard writing review:

| Dimension | Weight | Score (1-5) | Confidence (1-5) | Evidence basis | Concrete repair |
| --- | ---: | ---: | ---: | --- | --- |
| Storyline and motivation | 10 |  |  |  |  |
| Contribution display | 10 |  |  |  |  |
| Paragraph logic | 10 |  |  |  |  |
| Claim-evidence alignment | 12 |  |  |  |  |
| Method readability | 9 |  |  |  |  |
| Experiment narration | 9 |  |  |  |  |
| Related-work positioning | 8 |  |  |  |  |
| Terminology and notation consistency | 8 |  |  |  |  |
| Prose discipline and voice | 10 |  |  |  |  |
| LaTeX and format discipline | 6 |  |  |  |  |
| Reviewer-facing risk | 8 |  |  |  |  |

For each score of 3 or below, name the location, the reviewer confusion it creates, and the smallest edit that would raise the score.

## Score Anchors

### 5

The section or paper reads like a strong venue submission: the story is precise, claims are supported, transitions are natural, figures/tables carry evidence, and formatting does not distract.

### 4

Readable and mostly reviewer-proof, but one or two issues still weaken emphasis, evidence alignment, or consistency.

### 3

Understandable but not review-ready. A strict reviewer can follow the work, yet the presentation leaves avoidable doubts about contribution, motivation, evidence, or scope.

### 2

Hard to review fairly. The writing hides the actual contribution, mixes claims, breaks logical order, or leaves major claims unsupported.

### 1

Submission-risk level. The manuscript is incoherent, format-noncompliant, internally inconsistent, or impossible to evaluate from the provided text.

## No-Filler Deduction Format

Every material issue must use:

```text
Location:
Problem:
Why a reviewer deducts:
Concrete edit:
Expected effect:
```

Do not write "improve clarity", "strengthen motivation", "add details", or "polish language" without naming the exact sentence/paragraph role, missing information, and edit action.

## Prose Anti-Pattern Deductions

Apply `../../../ccf-paper-writer/references/prose-quality-guardrails.md`. Flag these as writing risks even when the science is otherwise plausible:

- Defensive or incremental framing that makes the contribution sound like a patch instead of a scientific insight.
- `Q1`/`C1`/`RQ1`-style labels used as the main narrative structure.
- Abstracts dominated by numbers before the task, gap, insight, and method are clear.
- Dense theorem, formula, or notation blocks with no explanation of why they matter.
- Excessive quotation marks, colons, dashes, slash stacks, arrows, or custom symbols replacing natural transitions.
- Third-person manuscript voice, such as "this paper proposes" or "the authors show", in text meant to be the manuscript itself.
- Repeated concepts or inconsistent terms that make the argument feel mechanically generated.
- Paragraphs whose sentences have the same length, template, or rhetorical rhythm.

## Writing Review Panel

Use these independent roles for standard writing review:

- **Storyline reviewer:** checks problem -> gap -> root challenge -> insight -> evidence progression.
- **Skeptical reviewer-reader:** checks where the prose makes the work look weaker, more incremental, or less supported than it is.
- **Claim-evidence reviewer:** checks unsupported, over-broad, or misplaced claims.
- **Paragraph-logic reviewer:** checks topic sentences, paragraph jobs, transitions, and redundancy.
- **Venue-style reviewer:** checks target-venue expectations, contribution display, and figure/table narration.
- **LaTeX/format reviewer:** checks captions, labels, equations, algorithms, references, anonymity markers, and page-risk signals.

Each role must output:

```text
Role:
Writing score tendency:
Confidence:
Main readability gain:
Main reviewer-confusion risk:
Evidence basis:
Concrete edit:
Expected score movement:
```

Do not force praise or criticism. If a role finds the section acceptable on its axis, state why and move to the next role.

## Writing-Only Boundaries

- Do not invent results, citations, baselines, or theorem claims.
- Do not silently rewrite the idea. When a scientific claim is too strong for the evidence, recommend weakening, qualifying, moving, or requesting evidence.
- Do not give acceptance probabilities. Report writing risk and likely reviewer confusion.
- If the user asks for actual rewriting, follow CCFA handoff mode before using `ccf-paper-writer`.
