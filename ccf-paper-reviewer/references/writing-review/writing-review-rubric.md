# Paper Writing Review Rubric

Use this rubric when reviewing a manuscript from the perspective of writing quality, reviewer readability, format discipline, and idea presentation. This file is not a replacement for scientific validation; it diagnoses how the paper communicates its scientific value.

## Review Dimensions

Score applicable dimensions on 1-5 when enough text is available, or use qualitative judgments for a no-score request. Carry the manuscript phase and assigned scope into the criteria; an internal alignment check does not become a submission assessment.

| Dimension | Weight | What To Inspect |
| --- | ---: | --- |
| Storyline and motivation | 10 | Whether the reader can understand the scientific question, its importance, and how the contribution addresses it, in an order suited to the work. |
| Contribution display | 10 | Whether contributions are specific, non-overlapping, evidence-backed, and visible in abstract/introduction/conclusion. |
| Paragraph logic | 10 | Whether each paragraph develops a clear point through the actual relation between sentences, with intelligible transitions to adjacent paragraphs. |
| Claim-evidence alignment | 12 | Whether claims have the appropriate experiment, proof, citation, or analysis, with wording calibrated to that support. A qualifier alone is not evidence. |
| Method readability | 9 | Whether notation, modules, algorithm steps, assumptions, and design choices are introduced in the right order. |
| Experiment narration | 9 | Whether tables/figures are introduced before interpretation and the text explains what the observations support, without conflating association and causation. |
| Related-work positioning | 8 | Whether the organization explains relevant relationships to closest work; a historical sequence is useful when the development itself matters. |
| Terminology and notation consistency | 8 | Whether key terms, symbols, dataset names, model names, and claims stay stable across sections. |
| Prose discipline and voice | 10 | Whether scientific objects, actions, and relations carry the explanation; diagnose empty self-defense, unsupported hype, or structure that obscures meaning in context. Preserve informative negation, calibrated uncertainty, useful labels, and necessary mathematics. |
| LaTeX and format discipline | 6 | Whether the manuscript follows venue style, references, captions, labels, equations, algorithms, and page/line constraints. |
| Reviewer-facing risk | 8 | Whether the writing creates avoidable rejection risks: hidden contribution, exaggerated claim, missing limitation, unclear baseline, or inconsistent story. |

Weights sum to 100. Compute:

```text
Writing score (1-5) = sum(assessed dimension score * weight) / sum(assessed weights)
Writing risk band = low / moderate / high / severe
```

Mark inapplicable criteria `N/A` and unavailable text `not assessed`; neither is zero. Show assessed weight coverage for a partial score and omit the aggregate if no dimension can be assessed. Preserve frozen weights for an existing version comparison. Do not present the writing score as an acceptance probability. It measures communication risk and reviewer readability, not scientific validity.

## Quantitative Writing Feedback

Include this scorecard in a requested standard writing review when scoring applies; preserve its dimensions with qualitative judgments for a no-score request. A bounded internal contribution returns its relevant findings without a new scorecard.

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

For each score of 3 or below, name the location, the confusion it creates, and the smallest edit that resolves it. Score changes summarize resolved issues; they are not targets for repeated hedging or rewriting.

## Score Anchors

### 5

The section or paper reads like a strong venue submission: the story is precise, claims are supported, transitions are natural, figures/tables carry evidence, and formatting does not distract.

### 4

Readable and coherent, with one or two local issues in emphasis, evidence alignment, or consistency.

### 3

Understandable but not review-ready. A strict reviewer can follow the work, yet the presentation leaves avoidable doubts about contribution, motivation, evidence, or scope.

### 2

Hard to review fairly. The writing hides the actual contribution, mixes claims, breaks logical order, or leaves major claims unsupported.

### 1

Submission-risk level. The manuscript is incoherent, format-noncompliant, internally inconsistent, or impossible to evaluate from the provided text.

## No-Filler Deduction Format

Use the fixed finding record in `../fixed-output-format.md` for material issues. The following questions help develop that record's explanation; they do not create a second mandatory finding format:

```text
Location:
Problem:
Why a reviewer deducts:
Concrete edit:
Expected effect:
```

Do not write "improve clarity", "strengthen motivation", "add details", or "polish language" without naming the exact sentence/paragraph role, missing information, and edit action.

## Prose Anti-Pattern Deductions

Apply `../../../ccf-paper-writer/references/prose-quality-guardrails.md`. Inspect the following signals in context and retain a deduction only when an actual consequence for meaning, support, or readability is established. A phrase match does not establish a scientific or writing defect:

- Empty self-defense or promotional framing that replaces the actual contribution; an accurately described incremental contribution must remain accurately described.
- `Q1`/`C1`/`RQ1`-style labels that displace explanation or leave the reader decoding undefined references; useful study identifiers can remain.
- Abstracts dominated by numbers before the task, gap, insight, and method are clear.
- Dense theorem, formula, or notation blocks with no explanation of why they matter.
- Excessive quotation marks, colons, dashes, slash stacks, arrows, or custom symbols replacing natural transitions.
- Manuscript narration that displaces the scientific object and operation; conventional attribution alone is not a defect.
- Repeated concepts or inconsistent terms that make the argument feel mechanically generated.
- Mechanically repeated sentence structures that obstruct emphasis or reading; useful procedural or comparative parallelism can remain.
- Abstract ability labels with no described operation, repeated contrasts without a real comparator, or added qualifiers with no relevant condition. Preserve genuine technical terms, comparisons, and evidence boundaries.

## Writing Review Panel

Use the relevant perspectives below within the standard report. Call them independent only when separate reviewer calls were actually performed:

- **Storyline reviewer:** checks whether the actual question, contribution, and findings form a coherent argument without imposing a fixed progression.
- **Skeptical reviewer-reader:** checks where the prose makes the work look weaker, more incremental, or less supported than it is.
- **Claim-evidence reviewer:** checks unsupported, over-broad, or misplaced claims.
- **Paragraph-logic reviewer:** checks topic sentences, paragraph jobs, transitions, and redundancy.
- **Venue-style reviewer:** checks target-venue expectations, contribution display, and figure/table narration.
- **LaTeX/format reviewer:** checks captions, labels, equations, algorithms, references, anonymity markers, and page-risk signals.

Consolidate useful role observations inside the fixed writing profile. The following fields are available when they add distinct evidence; no per-role score, repair, or predicted movement is required:

```text
Role:
Writing score tendency:
Confidence:
Main readability gain:
Main reviewer-confusion risk:
Evidence basis:
Concrete edit:
Resolution condition, if a concern remains:
```

Do not force praise or criticism. If a role finds the section acceptable on its axis, state why and move to the next role.

## Writing-Only Boundaries

- Do not invent results, citations, baselines, or theorem claims.
- Do not silently rewrite the idea. When a scientific claim is too strong for the evidence, recommend weakening, qualifying, moving, or requesting evidence.
- Do not reward extra caution by itself. Identify the missing support or misleading implication before recommending a qualification; equally flag unnecessary qualifiers that obscure an adequately supported contribution. Preserve sentence-final synthesis, emphasis, and broader significance; do not penalize a rhetorical ending just because it adds no new measurement or uses a familiar phrase. Judge whether it follows from the paragraph and preserves the distinction between a prospective implication and an observed result.
- Do not give acceptance probabilities. Report writing risk and likely reviewer confusion.
- If the user asks for actual rewriting, follow CCFA handoff mode before using `ccf-paper-writer`.
