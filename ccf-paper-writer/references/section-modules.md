# Section Modules

Use this file when drafting, rewriting, or checking a specific paper section. Use `storyline-blueprint.md` only when global narrative decisions are needed; reuse an established story for local edits.

Use the steps below as internal writing control unless the user asks to see the plan. For direct polishing, line editing, compression, or LaTeX revision, return the revised text in the user's original format rather than exposing paragraph-role analysis.

For a complete initial draft, apply `materials-to-manuscript.md` before these section guides. The moves below are functional roles, not fixed sentence counts or compulsory paragraph templates. Several related observations can support one theme. Choose sections by the actual contribution; a new task, benchmark, and method are not required in every paper.

For substantial edits across a long manuscript or several contributors, use [writing-execution.md](writing-execution.md) to preserve the whole-paper relationship, target and necessary neighboring transitions while projecting only relevant source material. A section ID is an editing anchor, not a reason to split every paragraph into a separate agent. Ordinary local polishing stays direct.

Also apply `references/prose-quality-guardrails.md`. Inspect defensive framing, labels, mathematics, abstract numbers, manuscript voice, and punctuation for their actual effect on meaning and readability; their presence alone is not an error.

## Module Template

For any section:

1. Determine the section role in the whole-paper story and select the scientific content that serves it. Missing-result and unresolved-detail notes limit dependent assertions; include them only when needed to interpret a claim or complete the requested specification, not as a routine progress summary.
2. Decide paragraph roles before writing.
3. Compose connected paragraphs; several related roles can develop one point.
4. Check local flow: one developed point per paragraph, with the actual reason, evidence, or consequence connecting its sentences. Keep supporting material with its claim.
5. Check global flow: the section supports the established scientific argument and connects to its necessary neighbors. After a substantive edit, inspect the actual affected definitions, repeated claims and transitions; a title-only outline does not establish whole-paper coherence.
6. Check prose quality: stable terminology, no unsupported hype, no unnecessary repeated concepts, and readable emphasis and sentence relationships.
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
| Method |2.0--3.5 pages | Explain the supplied method at the depth it needs; its size relative to other sections follows the contribution. |
| Experiments |2.0--3.0 pages | Setup, main results, and the mechanism or other analysis needed for the claims; no fixed ablation quota. |
| Discussion / Analysis |0.5--1.0 page | Architecture-level analysis, failure modes, limitations. |
| Conclusion |0.2--0.4 page | Restate insight and evidence; no new claims. |

Give Method and Experiments enough space to explain the work and its evidence. Their length depends on the contribution; page occupancy alone does not establish completeness.

When Method or Experiments has an actual explanatory gap, add the supported explanation or clearly planned setup within the drafting scope. Page occupancy alone does not trigger expansion.

## Abstract

Goal: explain the question, contribution, essential mechanism, and supported finding in one pass.

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

Goal: explain the scientific question, the unresolved relationship, and how the contribution addresses it.

Recommended paragraph roles:

1. Task/application/value.
2. Existing methods and their progress.
3. Remaining gap and root technical reason.
4. Insight and proposed method.
5. Contributions and evidence preview.

Citation rules:

- Every prior-work claim in the introduction must have a citation. A paragraph that describes what "existing methods" do without citing any is incomplete.
- Cover the relevant foundations, closest approaches, and gap with verified citations. Citation count alone is not a completeness criterion.
- Integrate citations with the scientific explanation. A claim-led sentence can summarize a shared finding; author-led attribution is useful when the historical step, disagreement, or specific contribution matters. Neither form is mandatory.
- Prefer scientific subjects and retain author-name attribution when informative, following `citation-workflow.md` without a per-paragraph quota.

Checks:

- Does the core challenge appear early enough?
- Is the root technical reason explicit?
- Does the introduction avoid defensive or incremental framing?
- Do cited prior methods explain the actual gap and closest alternatives? Avoid expanding literature only to meet a citation count.
- Do contribution bullets map to the relevant method, proof, construction, analysis, or study, distinguishing planned evidence from completed findings?
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

Goal: explain the method's definitions, operations, dependencies, and assumptions precisely enough to understand and reproduce it.

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
- When describing a novel module, cite the closest prior module it builds on or replaces and explain the changed operation.

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

Choose the relevant roles below from the actual claims and supplied evidence; do not add an experiment simply to fill a section heading:

1. Setup: datasets, metrics, baselines, protocol, implementation.
2. Main comparison or study: answer the central empirical question.
3. Mechanism analysis: use an ablation or other appropriate evidence when the interpretation depends on it; removing a component does not by itself establish the full causal explanation.
4. Further analysis: resolve a specific scope, robustness, or failure question grounded in the claim or observations.
5. Qualitative or case studies when they answer a relevant question or satisfy a verified venue requirement.
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
- Does each added analysis resolve a claim or decision that the existing evidence leaves open?
- Are the comparisons and takeaways in tables and figures clear, including connected findings shown together?
- Are negative or boundary results handled honestly?

## Figures And Tables

Goal: make the paper inspectable before close reading.

**For LaTeX table beautification details, always load `references/table-style-guide.md`. It covers booktabs rules, number precision, narrow-column fixes, wide-table handling, caption style, and placement.**

Structural rules:

1. Each figure/table should support a concrete scientific question or comparison in the argument.
2. Captions state the evaluated object, necessary setting, and supported takeaway; pending-result captions state scope without a conclusion. Follow the user's established style and venue requirements for placement.
3. Follow `table-style-guide.md` for table rules, with the venue requirements and established user style taking precedence.
4. Apply the precision rules in `table-style-guide.md`; preserve small values, thresholds, and the source's measurement precision.
5. Actual best results can be bolded under one convention; do not emphasize unknown cells or incomparable protocols as winners.
6. Resolve visible overflow and poor spacing through column widths, readable headers, or line breaks. Inspect warnings in the rendered table; harmless underfull hboxes do not require edits.
7. Fit tables to the actual available width without sacrificing readability or automatically shrinking fonts.
8. Pipeline figures should show data flow, modules, and outputs without overcrowding.
9. Qualitative figures should follow a stated selection principle and include material observed failures; do not invent a failure panel or select only favorable examples to support a general claim.

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
6. Match claims to their actual support; change strength only for a concrete overstatement or missing condition, not merely to sound more cautious.
7. Rewrite with the same technical meaning unless the user asks for structural changes.

Visible output default: the rewritten paragraph only, preserving Markdown/LaTeX/citation formatting. Add a short note only if a claim was softened, a citation/result looked unsupported, or the user asked for explanation.

## LaTeX Drafting Mode

For a paper from an idea or research documents, follow `materials-to-manuscript.md`. Use the requested template, with a disclosed NeurIPS format fallback if needed. Write full content before applying `length-budget-policy.md` to requested fitting. Missing result values use `\emptycell`; unknown citations, core mechanisms, and proofs are not fabricated. Deliver substantive sections and necessary appendices rather than a short compilable skeleton. Report missing evidence and build status outside manuscript prose.
