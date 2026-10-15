# Prose Quality Guardrails

Use this file for manuscript drafting, polishing, compression, abstract writing, introduction writing, paragraph review, and response text that may be copied into a paper. The goal is not to make prose decorative. The goal is to make every sentence serve the scientific argument.

Humanization's family baseline is active for both writing and assessment. For manuscript drafting or revision, apply `../../ccf-humanization/references/humanization-policy.md` and its sentence-decision procedure and bilingual repairs. Preserve material limitations; keep only unresolved scientific decisions in an external warning. For assessment-only review, use prose criteria diagnostically without rewriting assessed text or creating a warning artifact merely because this reference is loaded.

These checks improve precision, rhythm, and readability. They are writing-quality controls, not detector-evasion methods.

## Core Principle

Write from inside the research contribution. A manuscript should sound like a coherent scientific argument made by the authors, not a detached report about "the paper", "the reviewers", or a checklist of isolated claims.

Default voice:

- Prefer direct scientific prose: "We study...", "We propose...", "The results show...", or a direct subject such as "The bottleneck arises because..."
- Avoid third-person manuscript narration: "This paper proposes...", "The authors demonstrate...", "The reviewer will think...", or "The paper argues..." unless discussing another paper.
- Keep reviewer-facing reasoning internal. The visible paper should persuade through logic and evidence, not through comments about what reviewers may want.

## Contextual Prose Signals

Inspect the following for their scientific function and effect on the reader. They are not a word blacklist or automatic rewrite triggers. Change a pattern when it adds empty defense, overstates evidence, or obscures the argument; preserve accurate uncertainty, negative findings, standard terminology, and useful disciplinary conventions.

- Defensive or incremental framing: "we merely", "we only", "a simple extension", "despite being limited", "not much worse", or apology-like motivation when these substitute self-deprecation for a scientific point. State the scientific reason and evidence instead; keep terms such as "only" when they express a real condition or bound.
- Label-heavy writing: `Q1`, `Q2`, `C1`, `C2`, `RQ1`, `H1`, `P1`, or similar symbols in running prose. Use natural names such as "the invariance question" or "the efficiency claim". If labels are necessary for a study, define them once and keep them out of ordinary narrative.
- Formula and theorem dumping: dense theorem blocks, equation chains, or notation-heavy paragraphs without explanation. Each theorem, equation, and symbol must answer a specific question in the story.
- Abstracts that are mostly numbers: numbers should validate the contribution, not replace motivation, insight, method, and scope.
- Punctuation as structure: repeated quotation marks, colon chains, em-dash interruptions, slash stacks, arrows, or bracketed labels used instead of sentences.
- Overlong compound sentences that carry several unrelated ideas. Split when a sentence contains more than one claim, mechanism, and evidence item.
- Strange symbols replacing natural language: arrows, mathematical shorthand, custom markers, or abbreviations that are not needed for the method.
- Empty intensifiers and hype: "significant", "substantial", "powerful", "novel", "first", "dramatically", "obviously", or "clearly" without evidence and scope.
- Repeated redefinition: once a concept is named, use the same term unless a narrower subcase is introduced.

## Measurable Pattern Controls

The punctuation and pattern definitions live in `../../ccf-humanization/references/humanization-policy.md`. Load only the relevant definitions when a specific writing judgment needs them. Apply its editing procedure only during authorized prose changes; assessment-only review reports the diagnosed issue without entering that workflow.

For a full section or paper, run `../scripts/check_prose_quality.py`. The script is non-mutating and can read a path or standard input, so it does not require an intermediate report file. Treat its findings as writing signals governed by the humanization policy, not as detector-evasion targets.

## Positive Writing Rules

### Argument And Cohesion

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

Inspect empty importance announcements, `not merely ... but ...` contrasts, significance tails such as `highlighting its effectiveness`, abstract benefit stacks, nominalized actions, anonymous authority, mechanical three-part lists, and repeated rhetorical questions. State the concrete relationship or evidence; delete text with no scientific payload. Avoid changing passive voice, sentence lengths, or common words merely to simulate a human writer.

Use each section at its proper level. Abstract and introduction give a readable scientific position, not a catalogue of all module acronyms and protocol fields. Contributions can begin with `We` and state actual work; experimental contribution language requires results. Prefer one canonical name per concept and a small number of meaningful abbreviations. Use bold and italics selectively, and retain useful brief run-in headings rather than multiplying numbered sublevels.

### Sentence Rhythm

Use varied sentence lengths. A strong paragraph usually mixes short signpost sentences with longer explanatory sentences. Avoid paragraphs where every sentence has the same template, length, or grammatical shape.

### Evidence-Bounded Claims

Claims must match the available support:

- Use strong verbs only when evidence is strong.
- Prefer scoped claims over universal claims.
- State only material or required scope boundaries, not apologetic disclaimers or speculative failure lists.
- Replace unsupported assertions with mechanism, evidence, or a narrower claim.

## Section-Specific Checks

### Abstract

The abstract should connect task, gap, insight or method, and evidence. Express scope in these statements when needed; do not append a mandatory disclaimer. It may include key numbers, but the abstract should not read like a results table in prose. If more than half of the abstract is numeric comparison, rewrite it around the scientific contribution and keep only the decisive evidence.

### Introduction

Avoid defensive novelty positioning. Do not frame the contribution as a patch over a naive baseline. Explain the root reason prior approaches leave the gap unresolved, then show why the proposed insight changes the situation.

### Method

Equations and theorems must be narrated:

- Introduce what the equation represents before displaying it.
- Explain why the definition is needed after displaying it.
- Name symbols once and reuse them consistently.
- Move derivation detail to the appendix when it interrupts the mechanism.

### Experiments

Do not list results as disconnected numbers. Each paragraph should answer a question: effectiveness, causality, generalization, efficiency, robustness, or a material scope boundary.

### Conclusion

Do not introduce new claims or return to broad motivation. Close on the core insight and strongest support within the studied setting. Add a limitation or future-work sentence only if it contributes a specific material point or is required.

## Final Prose Self-Audit

Before calling writing ready, scan for:

- Any paragraph with no single retained message.
- Any sentence that repeats an already established concept without adding logic.
- Any term that has multiple names.
- Any strong adjective or adverb not grounded in evidence.
- Any abstract dominated by numbers.
- Any unnecessary `Q1`/`C1`-style labels.
- Any formula or theorem block that lacks narrative purpose.
- Any visible third-person narration about the paper or reviewer.
- Any punctuation pattern doing the work of logic.
- Any paragraph whose sentences all have the same length or template.
- Any denial-led positioning, empty assurance, stacked hedge, imagined reviewer, or repeated cautionary ending flagged by `scripts/check_prose_quality.py`; inspect its scientific function before changing it.
- Any real assumption, negative result, comparison constraint, or uncertainty lost during revision.
