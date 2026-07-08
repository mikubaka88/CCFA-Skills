# Prose Quality Guardrails

Use this file for manuscript drafting, polishing, compression, abstract writing, introduction writing, paragraph review, and response text that may be copied into a paper. The goal is not to make prose decorative. The goal is to make every sentence serve the scientific argument.

## Core Principle

Write from inside the research contribution. A manuscript should sound like a coherent scientific argument made by the authors, not a detached report about "the paper", "the reviewers", or a checklist of isolated claims.

Default voice:

- Prefer direct scientific prose: "We study...", "We propose...", "The results show...", or a direct subject such as "The bottleneck arises because..."
- Avoid third-person manuscript narration: "This paper proposes...", "The authors demonstrate...", "The reviewer will think...", or "The paper argues..." unless discussing another paper.
- Keep reviewer-facing reasoning internal. The visible paper should persuade through logic and evidence, not through comments about what reviewers may want.

## Forbidden Or High-Risk Patterns

Avoid these unless the venue, discipline, or user explicitly requires them:

- Defensive or incremental framing: "we merely", "we only", "a simple extension", "despite being limited", "not much worse", or apology-like motivation. State the scientific reason and evidence instead.
- Label-heavy writing: `Q1`, `Q2`, `C1`, `C2`, `RQ1`, `H1`, `P1`, or similar symbols in running prose. Use natural names such as "the invariance question" or "the efficiency claim". If labels are necessary for a study, define them once and keep them out of ordinary narrative.
- Formula and theorem dumping: dense theorem blocks, equation chains, or notation-heavy paragraphs without explanation. Each theorem, equation, and symbol must answer a specific question in the story.
- Abstracts that are mostly numbers: numbers should validate the contribution, not replace motivation, insight, method, and scope.
- Punctuation as structure: repeated quotation marks, colon chains, em-dash interruptions, slash stacks, arrows, or bracketed labels used instead of sentences.
- Overlong compound sentences that carry several unrelated ideas. Split when a sentence contains more than one claim, mechanism, and evidence item.
- Strange symbols replacing natural language: arrows, mathematical shorthand, custom markers, or abbreviations that are not needed for the method.
- Empty intensifiers and hype: "significant", "substantial", "powerful", "novel", "first", "dramatically", "obviously", or "clearly" without evidence and scope.
- Repeated redefinition: once a concept is named, use the same term unless a narrower subcase is introduced.

## Positive Writing Rules

### Cohesion

Every paragraph should have one retained message. Each sentence must do one of five jobs:

1. State or narrow the message.
2. Explain the mechanism or reason.
3. Provide evidence, citation, or example.
4. Contrast with an alternative.
5. Transition to the next needed idea.

If a sentence does none of these, cut it or rewrite it.

### Logical Progression

Build sections as progressive arguments:

```text
known context -> unresolved gap -> root cause -> insight -> method mechanism -> evidence -> bounded claim
```

Do not jump from motivation directly to method names. Do not assert a claim before the reader has seen the reason it should be true.

### Terminology Discipline

- Keep one canonical term for each concept, module, dataset, metric, assumption, and claim.
- Do not alternate synonyms just to avoid repetition.
- Repeat a term only when needed for clarity; otherwise use sentence structure to carry continuity.
- Align abstract, introduction, method, experiments, and conclusion wording for the same contribution.

### Sentence Rhythm

Use varied sentence lengths. A strong paragraph usually mixes short signpost sentences with longer explanatory sentences. Avoid paragraphs where every sentence has the same template, length, or grammatical shape.

### Evidence-Bounded Claims

Claims must match the available support:

- Use strong verbs only when evidence is strong.
- Prefer scoped claims over universal claims.
- State limitations as boundaries of validity, not as apologetic disclaimers.
- Replace unsupported assertions with mechanism, evidence, or a narrower claim.

## Section-Specific Checks

### Abstract

The abstract must include task, gap, insight or method, evidence, and scope. It may include key numbers, but the abstract should not read like a results table in prose. If more than half of the abstract is numeric comparison, rewrite it around the scientific contribution and keep only the decisive evidence.

### Introduction

Avoid defensive novelty positioning. Do not frame the contribution as a patch over a naive baseline. Explain the root reason prior approaches leave the gap unresolved, then show why the proposed insight changes the situation.

### Method

Equations and theorems must be narrated:

- Introduce what the equation represents before displaying it.
- Explain why the definition is needed after displaying it.
- Name symbols once and reuse them consistently.
- Move derivation detail to the appendix when it interrupts the mechanism.

### Experiments

Do not list results as disconnected numbers. Each paragraph should answer a question: effectiveness, causality, generalization, efficiency, robustness, or limitation.

### Conclusion

Do not introduce new claims or return to broad motivation. Close on the core insight, strongest support, and honest scope.

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
