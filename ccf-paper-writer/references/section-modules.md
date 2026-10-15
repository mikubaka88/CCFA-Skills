# Section Modules

Use this file when drafting, rewriting, or checking a specific paper section. Use `storyline-blueprint.md` only when global narrative decisions are needed; reuse an established story for local edits.

Use the steps below as internal writing control unless the user asks to see the plan. For direct polishing, line editing, compression, or LaTeX revision, return the revised text in the user's original format rather than exposing paragraph-role analysis.

For a complete initial draft, apply `materials-to-manuscript.md` before these section guides. The moves below are functional roles, not fixed sentence counts or compulsory paragraph templates. Several related observations can support one theme. Choose sections by the actual contribution; a new task, benchmark, and method are not required in every paper.

Also apply `references/prose-quality-guardrails.md`. Section drafting must avoid defensive framing, symbolic question/claim labels in prose, formula dumping, number-only abstracts, third-person manuscript narration, and punctuation used as a substitute for logic.

## Module Template

For any section:

1. Determine the section role in the whole-paper story.
2. Decide paragraph roles before writing.
3. Draft paragraphs one role at a time.
4. Check local flow: one paragraph, one message.
5. Check global flow: section supports the main story and venue plan.
6. Check prose quality: stable terminology, no unsupported hype, no unnecessary repeated concepts, and varied sentence rhythm.
7. Check affected claim-evidence links. Do not create a reviewer-risk map for ordinary section writing.

Show steps 1-2 only when the user requested a plan, outline, diagnosis, or explanation.

## Section-Length Guidance (ICLR/NeurIPS/ICML, ~9-page main text)

These are later fitting heuristics for an illustrative AI/ML manuscript, not initial-draft quotas. Use only after the content/alignment phase and when length fitting is requested. Adapt to the actual venue, paper type, and supplied content.

| Section | Typical Range | Notes |
| --- | --- | --- |
| Abstract |0.15--0.25 page | Approximately150--250 words. |
| Introduction |1.0--1.5 pages | Must include motivation, gap, insight, contributions. |
| Related Work |0.75--1.25 pages | Optional before or after Method; can merge with Background. |
| Background / Preliminaries |0.5--0.75 page | Formal problem statement, notation, path-length or complexity arguments. |
| Method |2.0--3.5 pages | The largest section. Per-component motivation, equations, architecture details. |
| Experiments |2.0--3.0 pages | Setup (0.5p), main results (1.0p), ablations and analysis (1.0--1.5p). |
| Discussion / Analysis |0.5--1.0 page | Architecture-level analysis, failure modes, limitations. |
| Conclusion |0.2--0.4 page | Restate insight and evidence; no new claims. |

Give Method and Experiments enough space to explain the work and its evidence. Their length depends on the contribution; page occupancy alone does not establish completeness.

For an underfilled draft, inspect Method and Experiments for actual explanatory gaps. Expand supported content and clearly planned evidence; do not pad to a fixed page count.

## Abstract

Goal: give reviewers the whole paper in one pass.

Recommended moves:

1. Task and importance.
2. Specific gap or technical challenge.
3. Core insight or contribution.
4. Method mechanism at a high level.
5. Decisive evidence and the interpretation it supports, with calibrated uncertainty only where needed.

Checks:

- Does every major abstract claim appear later with evidence?
- Is the method name understandable without hidden context?
- Does the abstract fit target venue style: concise for systems, precise for theory, contribution/evidence-balanced for AI/CV/NLP?
- Is the abstract built around the scientific contribution rather than a dense list of numeric improvements?
- If results are pending, does it explain the research without claiming an unobserved improvement or validation?

## Introduction

Goal: create reviewer curiosity and make the contribution feel necessary.

Recommended paragraph roles:

1. Task/application/value.
2. Existing methods and their progress.
3. Remaining gap and root technical reason.
4. Insight and proposed method.
5. Contributions and evidence preview.

Citation rules:

- Every prior-work claim in the introduction must have a citation. A paragraph that describes what "existing methods" do without citing any is incomplete.
- Cover the relevant foundations, closest approaches, and gap with verified citations. Citation count alone is not a completeness criterion.
- Use natural citation weaving: claim first, citation second. "Large-scale pretraining on web-scale data [4,5] has become the dominant paradigm..." not "Brown et al. [4] and Chowdhery et al. [5] proposed..."
- Prefer scientific subjects and retain author-name attribution when informative, following `citation-workflow.md` without a per-paragraph quota.

Checks:

- Does the core challenge appear early enough?
- Is the root technical reason explicit?
- Does the introduction avoid defensive or incremental framing?
- Do cited prior methods explain the actual gap and closest alternatives? Avoid expanding literature only to meet a citation count.
- Do contribution bullets map to Method and Experiments?
- Does the reader understand the mechanism-level difference and what it enables?

## Related Work

Goal: make novelty easy to verify.

Recommended structure:

Group sources by the ideas, assumptions, or capabilities relevant to the scientific question. Explain representative work and the closest technical relationships with accurate attribution. Group count follows coverage needs. A meaningful distinction can be explicit, but do not require every group to end with a limitation or a claim of superiority.

Citation rules:

- Each topic group needs the works that support its argument; a narrow topic may need only one decisive source.
- Size Related Work by relevant coverage, not a fixed citation quota.
- Every factual claim about a research thread must be supported by specific citations, not vague references to "prior work."
- Do not cite a paper simply because it is famous in the field. Every cited paper must be relevant to the specific point being made.
- The closest competitor must be cited and discussed explicitly in its own sentence or paragraph. Do not bury it in a citation list.

Checks:

- Are strongest and recent competitors included?
- If closest work is unknown or fast-moving, use `ccf-literature-searcher` through the CCFA handoff mode rather than inventing citations.
- Is the distinction technical, not marketing language?
- Does Related Work prepare the reader for the Method?
- Are factual prior-work claims supported and the closest competitor discussed explicitly?

## Task And Benchmark

Use when the actual contribution defines a task, dataset, or evaluation resource. Establish the scientific object, required inputs and outputs, and conditions before describing construction. Separate task semantics from one method's interfaces and training labels from inference inputs.

Explain the sample unit, category meanings, source coverage, annotation formation, important construction decisions, quality checks, and split policy. Distinguish task categories, output fields, difficulty axes, and metric groups. Report verified statistics with units and counting scope; target sizes or illustrative examples are not completed dataset counts.

Give primary metrics their scientific meaning and necessary definitions, including applicability, denominator, units, and aggregation. Main text contains what readers need to interpret the evidence; the appendix can carry detailed rules. Organize construction around why the resource measures the task, not around scripts, filenames, or operational logs.

## Method

Goal: make the mechanism auditable and reproducible.

Pre-writing questions:

1. What scientific relationship does the method model?
2. What supplied computations realize that relationship?
3. What information and representation does each key mechanism use and produce?
4. Why does that operation address the identified problem?
5. Which definitions, assumptions, training signals, and inference dependencies are necessary to understand it?

Recommended structure:

Establish the setting, central representation, and overall computation. Organize key mechanisms in their actual dependency order, connecting the problem to the operation and its role. Modules can provide useful structure when they exist and have distinct scientific functions; do not invent an encoder/module/decoder architecture or use an interface inventory as the narrative. Explain training and inference, with supporting reproducibility details in the appropriate body or appendix location. Complexity and proofs belong when supplied and relevant, not as decoration.

Citation rules:

- Any borrowed component, architecture, or technique must cite its original source. Do not describe a well-known module as if it were original.
- Cite borrowed modules, the base architecture, and adapted objectives or optimization methods where relevant; use evidence coverage rather than a citation quota.
- When describing a novel module, cite the closest prior module it builds on or replaces. This helps reviewers understand the novelty.

Style rule:

- Do not use bold inline labels (`\textbf{Input:}`, `\textbf{Output:}`, `\textbf{Architecture:}`) in every paragraph. Write prose that flows: "The encoder takes a sequence of tokens and produces contextualized representations through stacked self-attention layers" rather than "`\textbf{Encoder:}` The encoder uses self-attention."
- Do not let theorem statements, equations, or notation blocks replace explanation. Introduce their purpose before the formalism and explain their role afterward.
- Avoid `Q1`/`C1`-style labels for modules or claims unless the venue or task convention requires them.

Checks:

- Can a reader reconstruct the core computation from text and any supplied figure?
- Does each module have motivation and technical advantage?
- Are inputs, outputs, notation, and symbols defined before use?
- Are design rationales distinguished from effects actually supported by ablation, theorem, analysis, or study? Pending tests are not completed validation.
- Are citations present for every borrowed component? If not, search for sources before finishing.

## Experiments

Goal: test the central scientific claims and explain the observations.

Recommended structure:

1. Setup: datasets, metrics, baselines, protocol, implementation.
2. Main comparison: answer whether the method works.
3. Ablation: answer why it works.
4. Analysis: answer when it works, when it fails, and how robust it is.
5. Qualitative or case studies when the venue expects them.
6. Material observed limitations or failure cases at the relevant location, or in a required dedicated section.

Citation rules:

- Cite external datasets, borrowed metrics, and baseline methods actually used. Define newly introduced resources and metrics in the paper; cite their predecessors where relevant, following `citation-workflow.md`.
- When comparing against prior published results, cite both the method paper and the source of the specific numbers being compared.
- In a results-pending draft, cite baselines specified in the supplied design and leave results blank. Their presence in a protocol does not imply a completed comparison. For reported comparisons, trace both the method and the actual result source.

Checks:

- Does each empirical claim have applicable evidence, or remain unasserted while its result is pending? Formal and dataset contributions need the appropriate proof or construction support, not necessarily a model experiment.
- If the user needs datasets, baselines, ablations, benchmark design, or fill-in result tables, use `ccf-experiment-designer` through the CCFA handoff mode.
- Are baselines strong, recent, and fair? Is every baseline cited?
- Are metrics standard and sufficient?
- Are ablations tied to modules and design choices?
- Do tables and figures each have one message?
- Are negative or boundary results handled honestly?

## Figures And Tables

Goal: make the paper inspectable before close reading.

**For LaTeX table beautification details, always load `references/table-style-guide.md`. It covers booktabs rules, number precision, narrow-column fixes, wide-table handling, caption style, and placement.**

Structural rules:

1. Every figure/table should answer one reviewer question.
2. Captions state the evaluated object, necessary setting, and supported takeaway; pending-result captions state scope without a conclusion. Follow the user's established style and venue requirements for placement.
3. Follow `table-style-guide.md` for table rules, with the venue requirements and established user style taking precedence.
4. Numbers in the same column must have the same decimal precision.
5. Actual best results can be bolded under one convention; do not emphasize unknown cells or incomparable protocols as winners.
6. Resolve visible overflow and poor spacing through column widths, readable headers, or line breaks. Inspect warnings in the rendered table; harmless underfull hboxes do not require edits.
7. Fit tables to the actual available width without sacrificing readability or automatically shrinking fonts.
8. Pipeline figures should show data flow, modules, and outputs without overcrowding.
9. Qualitative figures should avoid cherry-picking by showing representative successes and failures when possible.

Checks:

- Can the paper's contribution be understood from figures and captions?
- Are key claims visible in tables or figures?
- Are visual examples aligned with the text discussion?
- Do table rules and caption placement match the applicable template and user style?

## Conclusion

Goal: leave a precise final takeaway.

Recommended moves:

1. Restate problem and core method.
2. State the key insight or contribution.
3. Summarize strongest evidence.
4. Include a specific material boundary only when it changes the takeaway or is required.
5. Include future work only for a concrete useful direction, not as a required closing ritual.

Checks:

- Does it match the paper's actual evidence?
- Does it avoid introducing new technical material?
- Are retained qualifications scientifically necessary, and is the final takeaway supported?

## Limitations, Ethics, Broader Impact

Use when the venue requires or expects these sections.

Checks:

- Are limitations specific and bounded?
- Are datasets, human subjects, privacy, security, misuse, bias, or environmental concerns addressed when relevant?
- Are claims weakened where the limitation narrows validity?
- Does each statement identify a concrete assumption, observation, consequence, or required disclosure?

## Small Paragraph Edit Mode

When the user gives one paragraph:

1. Identify paragraph role.
2. State the intended message in one sentence.
3. Check sentence flow.
4. Check term consistency.
5. Check whether the paragraph repeats a concept without adding logic.
6. Check whether claims are supported or need softer wording.
7. Rewrite with the same technical meaning unless the user asks for structural changes.

Visible output default: the rewritten paragraph only, preserving Markdown/LaTeX/citation formatting. Add a short note only if a claim was softened, a citation/result looked unsupported, or the user asked for explanation.

## LaTeX Drafting Mode

For a paper from an idea or research documents, follow `materials-to-manuscript.md`. Use the requested template, with a disclosed NeurIPS format fallback if needed. Write full content before applying `length-budget-policy.md` to requested fitting. Missing result values use `\emptycell`; unknown citations, core mechanisms, and proofs are not fabricated. Deliver substantive sections and necessary appendices rather than a short compilable skeleton. Report missing evidence and build status outside manuscript prose.
