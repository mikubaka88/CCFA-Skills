# Research Writing Patterns

Use this file for full-paper drafting, section-specific rewriting, and exemplar-mode adaptation. It consolidates section-level writing patterns for CCFA while keeping venue routing, evidence policy, and artifact contracts in CCFA.

These are transferable writing patterns, not copied examples. Do not reuse sentence templates, distinctive wording, examples, claims, or confidence from any source paper or external skill. Adapt the logic to the user's actual problem, method, and evidence.

Always apply `prose-quality-guardrails.md` with this file. It is the authority for avoiding defensive or incremental prose, label-heavy symbols, formula dumping, number-only abstracts, punctuation-driven structure, overlong compound sentences, strange shorthand, third-person manuscript narration, and unsupported hype.

## Dense Output Rule

For broad writing tasks, produce the artifact first and make it substantial:

- Full manuscript request: write a full LaTeX/Markdown manuscript, not only an abstract or outline.
- Submission manuscript request: target the venue's page budget, not the minimum text needed to compile.
- Section request: write the section, not only paragraph roles.
- Revision request: provide revised text in source format plus only the necessary edit notes.
- Exemplar request: show the source writing pattern, then adapt it into original text.

Avoid empty "next steps" and generic warnings. A warning is useful only if it names the unsupported claim, missing evidence, affected section, and concrete fix.

For underfilled full drafts, add substantive paper content before finishing: deeper problem setup, closest-work contrast, method mechanism, experiment protocol, analysis scaffolds, limitations, and reproducibility notes. Use `TBD` for missing evidence; do not pad with generic background.

## Natural Writing Style

CCF-A papers read as continuous prose arguments, not as annotated outlines. The best papers in CVPR, ICLR, NeurIPS, and ICML share these traits:

### What Best Papers Do

- Each paragraph opens with a claim or observation, then supports it with evidence, reasoning, or citations.
- Citations appear inside sentences as part of the argument, not as parenthetical interruptions.
- Technical terms are defined once, used consistently, and never bolded in running text unless the venue template requires it.
- Method descriptions follow a logical flow: problem, design rationale, mechanism, justification.
- Experiments are narrated to answer reviewer questions, not to list results.

### What To Avoid

- **Bold-label paragraphs:** Do not write paragraphs where every sentence starts with `\textbf{Key:}` or `\textit{Label:}`. Example of forbidden pattern:
 ```
 \textbf{Input:} The model takes images as input. \textbf{Architecture:} We use a transformer. \textbf{Training:} We train with Adam.
 ```
 Instead, write flowing prose: "The model processes images through a transformer backbone, trained end-to-end with Adam optimization."

- **Citation dumps:** Do not list five citations in one bracket with no narrative. Group related work with a shared observation: "Contrastive objectives [9,10,11] share the goal of learning invariant representations, but differ in how negative pairs are constructed."

- **Empty transitions:** Do not use "Recently, ..." or "In recent years, ..." as a paragraph opener more than once per paper. Start with the specific development that matters.

- **Repeated motivation:** State the paper's core motivation once in the introduction and once in the conclusion. Do not re-motivate in every section.

- **Over-bolded terms:** Do not bold every technical term. Use italics sparingly for the first definition only. Reserve bold for venue-mandated formatting (e.g., NeurIPS checklist headings).

- **Question/claim labels as prose:** Avoid `Q1`, `Q2`, `C1`, `C2`, `RQ1`, and similar shorthand in the main narrative. Use natural names and sentence-level transitions unless the venue or study design explicitly requires labels.

- **Number-led abstracts:** Do not let the abstract become a list of gains. Put task, gap, insight, method, and scope before numeric evidence.

- **Formula-first paragraphs:** Do not introduce a method through dense symbols before explaining the scientific role of the quantity being defined.

- **Third-person manuscript voice:** Do not write manuscript text as "this paper proposes" or "the authors show". Use direct scientific voice or make the concept itself the subject.

### Citation Weaving

Load `references/citation-workflow.md` for the full workflow. In the writing itself, citations must feel woven into the argument:

**Good:**
- "The shift from recurrent to self-attentive architectures [1] eliminated the sequential dependency that limited training parallelism."
- "Residual connections [2] address vanishing gradients by providing identity shortcuts through deep networks."
- "Several works have since extended this idea to dense prediction [3,4], video understanding [5], and multimodal fusion [6]."

**Bad:**
- "Vaswani et al. [1] proposed the Transformer. He et al. [2] proposed ResNet."
- "Many methods have been proposed [1,2,3,4,5,6,7,8]."
- "In [1], the authors show that attention improves translation quality."

The claim comes first, then the citation. The sentence should make sense without the brackets. See `references/citation-workflow.md` for the complete rules.

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
- The abstract is not dominated by numeric comparisons; numbers appear only as decisive evidence after the contribution is clear.

## Introduction Patterns

Use backward reasoning before drafting:

1. What problem is solved?
2. Why do existing solutions fail?
3. What root technical reason causes the failure?
4. What insight makes the proposed method plausible?
5. What evidence will convince reviewers?

Then write forward:

1. **Task/application/value** (cite2-4 field-defining works): Open with what the field can now do and why it matters. Do not use "Recently" or "In recent years" as the first words.
2. **Prior methods and their progress** (cite3-6 works): Show the ladder of progress, not a flat list. Each sentence should name a capability gained, then cite the works that contributed it.
3. **Remaining technical challenge with root reason** (cite1-2 closest works): Identify the gap and explain why it persists. The root reason must be technical, not just "nobody has tried this."
4. **Insight and method preview** (0-1 citation if building on a known architecture): State the key observation that makes the solution possible. Preview the method in2-3 sentences.
5. **Contributions and evidence preview:** Map each contribution to the experiment or analysis that validates it.

An introduction should carry12-20 citations total. A well-cited introduction signals that the authors understand the field and have positioned their work honestly.

Task-opening variants:

- Niche task: define the task, then name applications. Cite the works that established the task.
- Familiar task: start from application or scientific importance. Cite the breakthrough papers that created the current momentum.
- New setting: start broad, then narrow to the exact input/output setting. Cite the closest related settings.
- Challenge-first opening: expose the failure case in the first paragraph. Cite the work that reveals the failure or the standard method that fails.

Challenge-chain variants:

- Existing task: general challenge -> traditional line -> recent line -> remaining challenge. Each line gets1-3 citations.
- Existing task with historical insight: modern limitation -> classical insight -> why old line is insufficient -> new method.
- Novel task: define the challenge and decompose it into two or three concrete obstacles.

Avoid naive-baseline framing. Do not make the paper sound like "we tried an obvious baseline and patched it." Frame the root technical issue and the non-obvious insight instead.

## Related Work Pattern

Use2-4 focused topic groups. Each group cites3-8 distinct works. The total related-work section should carry20-35 citations for a typical CCF-A paper.

For each topic group:

1. **Topic scope:** Name the research thread and why it is relevant to this paper.
2. **Representative methods:** Cite3-6 works with a shared observation about what they achieve. Do not list papers one-by-one: "A et al. [1] did X. B et al. [2] did Y." Instead: "Prior work has explored supervised pretraining [1,2], self-supervised objectives [3,4], and hybrid approaches [5,6] to improve feature quality."
3. **Limitation tied to this paper exact challenge:** Explain what the group as a whole does not address, not what each individual paper fails at. The limitation must connect to the gap this paper fills.
4. **Technical distinction:** State how this paper differs, using technical terms, not marketing language. "In contrast, our method eliminates the need for paired data by..." not "Unlike previous work, our method is superior."

**Citation integration rules for Related Work:**

- Every named paradigm or thread gets at least3 citations.
- The closest competitor must be cited and discussed explicitly, not hidden in a list.
- If any claim about prior work cannot be verified, route to `ccf-literature-searcher` before writing.
- Do not cite a paper only because it is famous; every citation must serve the argument.

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
