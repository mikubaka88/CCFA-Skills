# Prose Quality Guardrails

Use this file for manuscript drafting, polishing, compression, abstract writing, introduction writing, paragraph review, and response text that may be copied into a paper. The goal is not to make prose decorative. The goal is to make every sentence serve the scientific argument.

Humanization's family baseline is active for both writing and assessment. For manuscript drafting or revision, apply `../../ccf-humanization/references/humanization-policy.md` and its sentence-decision procedure and bilingual repairs. Preserve material limitations; keep only unresolved scientific decisions in an external warning. For assessment-only review, use prose criteria diagnostically without rewriting assessed text or creating a warning artifact merely because this reference is loaded.

These checks improve precision, rhythm, and readability. They are writing-quality controls, not detector-evasion methods.

## Core Principle

Write from inside the research contribution. A manuscript should sound like a coherent scientific argument made by the authors, not a detached report about "the paper", "the reviewers", or a checklist of isolated claims.

Separate the scientific writing input from internal preparation fields. The target's message, whole-paper relationship, necessary neighboring text and relevant original passages supply the explanation; source identities, completion states and checks constrain facts without becoming the narrative. For substantial coordinated edits, [writing-execution.md](writing-execution.md) implements that separation and checks edit scope. A packet does not replace source verification or semantic reading, and ordinary small edits do not need one.

Default voice:

- Prefer direct scientific prose: "We study...", "We propose...", "The results show...", or a direct subject such as "The bottleneck arises because..."
- Prefer the scientific object or author action over repeated commentary about the manuscript. Conventional phrases such as "This paper studies..." are not errors by themselves; preserve the author's selected voice and useful attribution. Imagined reviewer reactions do not belong in manuscript prose.
- Keep reviewer-facing reasoning internal. The visible paper should persuade through logic and evidence, not through comments about what reviewers may want.

## Contextual Prose Signals

Inspect the following for their scientific function and effect on the reader. They are not a word blacklist or automatic rewrite triggers. Change a pattern when it adds empty defense, overstates evidence, or obscures the argument; preserve accurate uncertainty, negative findings, standard terminology, and useful disciplinary conventions.

- Defensive or incremental framing: "we merely", "we only", "a simple extension", "despite being limited", "not much worse", or apology-like motivation when these substitute self-deprecation for a scientific point. State the scientific reason and evidence instead; keep terms such as "only" when they express a real condition or bound.
- Label-heavy writing: inspect whether `Q1`, `C1`, `RQ1`, `H1`, or similar identifiers help readers follow the study or force them to decode undefined references. Define useful labels and retain the cross-references that use them; use natural names when a label adds no value.
- Formula and theorem dumping: dense theorem blocks, equation chains, or notation-heavy paragraphs without explanation. Each theorem, equation, and symbol must answer a specific question in the story.
- Abstracts that are mostly numbers: numbers should validate the contribution, not replace motivation, insight, method, and scope.
- Punctuation as structure: repeated quotation marks, colon chains, em-dash interruptions, slash stacks, arrows, or bracketed labels used instead of sentences.
- Overloaded sentences that obscure the relation between ideas or the scope of a modifier. Split at a real change of subject or argument; keep a connected claim, reason, comparison, and qualification together when one sentence expresses their relationship clearly.
- Strange symbols replacing natural language: arrows, mathematical shorthand, custom markers, or abbreviations that are not needed for the method.
- Empty intensifiers and hype: "significant", "substantial", "powerful", "novel", "first", "dramatically", "obviously", or "clearly" without evidence and scope.
- Repeated redefinition: once a concept is named, use the same term unless a narrower subcase is introduced.

## Measurable Pattern Controls

The punctuation and pattern definitions live in `../../ccf-humanization/references/humanization-policy.md`. Load only the relevant definitions when a specific writing judgment needs them. Apply its editing procedure only during authorized prose changes; assessment-only review reports the diagnosed issue without entering that workflow.

For a full section or paper, run `../scripts/check_prose_quality.py`. The script is non-mutating and can read a path or standard input, so it does not require an intermediate report file. Treat its findings as writing signals governed by the humanization policy, not as detector-evasion targets.

## Positive Writing Rules

### Argument And Cohesion

Before composing, choose the scientific point and the supplied content that explains it. Start with the relevant object and what it does, predicts, changes, or reveals. Carry a defined object into the next sentence when that sentence explains its cause, consequence, or unresolved property. A heading such as “evidence,” “capability,” or “validation” does not determine the paragraph's content. For substantive drafting or expression rewriting, use matching originals through `exemplar-style-analysis.md` before drafting; additional discovery follows `reference_style_search`. An explicit request to learn from a supplied paper is not required. Minor corrections can use the established context.

Give each paragraph a retained message and develop its reason, mechanism, evidence, or necessary comparison. For a full section or a passage whose logic is unclear, briefly reconstruct the argument from the actual draft: name each paragraph's main point and check how it advances the section. Merge repetition, repair missing links from supplied material, and remove material with no function. This reverse outline is part of the existing edit, not an extra report, file, or model call. A bounded clear passage needs only a local check.

For adjacent sentences, identify the actual relationship: reason, evidence, consequence, qualification, example, comparison, or necessary transition. If it is unclear, reorder or split the material, or explain the relationship supported by the source. Changing a connector does not repair missing logic; do not invent causality or evidence to make prose flow. Lead claims may precede their supporting explanation when the paragraph develops that support.

Introduce new terms, variables, and comparators intelligibly; give pronouns specific antecedents. Where useful, start from information the reader already has and end on the new point that the next sentence develops. Keep subjects near their main verbs and use concrete actions where noun stacks hide the mechanism. These are repair options, not a required sentence template or a fixed sequence for every section.

When translating Chinese into English, first recover the propositions and their relationships, then compose the English argument. Preserve actors, operations, conditions, negation, comparison direction, quantities and units, citation support, and uncertainty. Do not follow Chinese clause order mechanically or supply an unstated causal link. After an addition, integrate it into the relevant paragraph and remove superseded or duplicate explanation instead of appending another summary of the same point.

Prefer actual dependencies over mechanical ordinal lead-ins such as `First`, `Second`, `Finally`, “第一、第二” and “首先、其次、最后”. Keep clear numbering for real ordered procedures or enumerations. Do not replace these words mechanically with `Moreover`; evaluate the relation conveyed by the sentence, not the presence of a word. Preserve equation indices, algorithm numbering, technical terms, and user or venue conventions.

### Terminology Discipline

- Keep one canonical term for each concept, module, dataset, metric, assumption, and claim.
- Do not alternate synonyms just to avoid repetition.
- Repeat a term only when needed for clarity; otherwise use sentence structure to carry continuity.
- Align abstract, introduction, method, experiments, and conclusion wording for the same contribution.
- Prefer familiar, precise field terminology and natural verb combinations. Do not use rare synonyms, invented compounds, or fashionable terms for sophistication. Keep technical terms even when long if they are necessary and defined.
- Check agency, pronoun reference, modifier scope, comparator, and technical promises. Words such as `causal`, `optimal`, `invariant`, and `consistent` need their actual technical meaning, not a promotional interpretation.

### Scientific Explanation

Explain what is modeled or inferred, what information it depends on, and why the operation addresses the question. Do not substitute a sequence of interfaces, execution events, or names for that explanation. `pipeline`, `readout`, `head`, `stage`, and `component` are context checks, not forbidden standard terminology. Preserve a real structure and necessary reproducibility detail; avoiding engineering narration does not authorize omitting the method.

Use objects and operations in place of empty ability labels: explain what will be compared instead of calling a plan “verifiable,” and how a computation is performed instead of calling a framework “feasible.” Keep feasibility, realizability, and verifiability when they are defined technical properties or real constraints. Apply Humanization's stage distinction: a proposed mechanism needs a clear rationale, while a reported effect needs actual support.

Inspect empty importance announcements, `not merely ... but ...` contrasts, abstract benefit stacks, nominalized actions, anonymous authority, mechanical three-part lists, and repeated rhetorical questions. Repair the relationship or remove empty repetition. Preserve sentence-final synthesis and broader significance that follows from the paragraph, even without a new measurement. Avoid changing passive voice, sentence lengths, or common words merely to simulate a human writer.

Use each section at its proper level. Abstract and introduction give a readable scientific position, not a catalogue of all module acronyms and protocol fields. Contributions can begin with `We` and state actual work; experimental contribution language requires results. Prefer one canonical name per concept and a small number of meaningful abbreviations. Use bold and italics selectively, and retain useful brief run-in headings rather than multiplying numbered sublevels.

### Sentence Rhythm

Let sentence length follow the thought. Repair an actual parsing problem, monotonous emphasis, or unnecessary repetition; do not manufacture alternating lengths or break a connected explanation to make it look less generated. Parallel procedures and comparisons may use parallel grammar.

### Evidence-Bounded Claims

Claims must match the available support:

- Use strong verbs only when evidence is strong.
- Prefer scoped claims over universal claims.
- State only material or required scope boundaries, not apologetic disclaimers or speculative failure lists.
- Replace unsupported assertions with mechanism, evidence, or a narrower claim.
- Before adding a qualifier, identify the specific condition or gap it expresses. Reviewer wording alone does not establish one; retain supported strength and avoid repeating a condition already clear in context.

## Section-Specific Checks

### Abstract

The abstract should make the question, contribution, and supported finding intelligible. Express scope where needed. Numerical results may be central to a measurement or benchmark paper; revise disconnected numbers when their scientific meaning is missing, not when they cross a fixed proportion of the abstract.

### Introduction

Explain the actual scientific question and contribution. A baseline may reveal the decisive failure and an incremental change may solve a real problem; describe that relationship accurately. Do not hide the baseline, exaggerate prior failure, or invent a non-obvious insight to make the story sound stronger. Broader framing remains useful when supported by the materials.

### Method

Equations and theorems must be narrated:

- Introduce the scientific role of an equation or theorem where the reader needs it; a clear definition can provide that context without a separate lead-in.
- Explain non-obvious steps and consequences. Do not surround every display with repetitive paraphrases of symbols the reader already understands.
- Name symbols once and reuse them consistently.
- Move derivation detail to the appendix when it interrupts the mechanism.

### Experiments

Do not list results as disconnected numbers. Each paragraph should answer a question: effectiveness, causality, generalization, efficiency, robustness, or a material scope boundary.

### Conclusion

Close by connecting the core insight and findings to their scientific significance or a broader research question. Preserve the author's rhetorical emphasis and prospective implications without inventing new empirical results. Paragraph endings elsewhere can serve the same synthesis or significance role; they need not supply a new technical fact. Add a limitation or future-work sentence when it serves the passage or is required.

## Final Prose Self-Audit

Before calling writing ready, scan for:

- Any paragraph whose point or relation to the surrounding discussion is unclear.
- Any sentence that repeats an already established concept without adding logic.
- Any term that has multiple names.
- Any strong adjective or adverb not grounded in evidence.
- Any abstract dominated by numbers.
- Any unnecessary `Q1`/`C1`-style labels.
- Any formula or theorem block that lacks narrative purpose.
- Commentary about the paper or an imagined reviewer that replaces the scientific explanation.
- Any punctuation pattern doing the work of logic.
- Repeated sentence templates that obscure the argument or its emphasis.
- Any denial-led positioning, empty assurance, stacked hedge, imagined reviewer, or repeated cautionary ending flagged by `scripts/check_prose_quality.py`; inspect its scientific function before changing it.
- Any real assumption, negative result, comparison constraint, or uncertainty lost during revision.
