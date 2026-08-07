# Humanization Policy

## Manuscript Standard

Write the strongest accurate academic version of the work. State the research problem, mechanism, evidence, and bounded conclusion directly. Do not write as though answering an imagined hostile reviewer.

Natural prose is not relaxed scholarship. Preserve method specificity, evidence-to-claim alignment, uncertainty where scientifically relevant, reproducibility details, equations, citations, terminology, and mandatory disclosures. Never trade rigor for conversational tone, rhetorical smoothness, brevity, or a more favorable narrative.

Remove or rewrite:

- boilerplate caveats that do not affect interpretation;
- defensive phrases such as “to avoid possible concerns,” “one might argue,” or repeated “we acknowledge” constructions;
- long lists of hypothetical attacks, corner cases, or deployment failures that are neither observed nor claim-relevant;
- generic safety, robustness, reproducibility, or compliance prose added only because it sounds prudent;
- meta-commentary about what reviewers may think, accept, reject, question, or misunderstand;
- repetitive statements that the method is not intended for implausible scenarios;
- warning prose, internal risk notes, or reviewer simulations inside manuscript paragraphs.
- engineering-status phrases such as "the confirmed version," "the approved configuration," "publication-ready method," or narration that a method passed an internal gate;

Keep:

- exact method assumptions needed to understand or reproduce the work;
- observed limitations or negative results that change the supported claim;
- fair protocol constraints and known threats that affect comparison validity;
- venue-mandated limitations, ethics, impact, disclosure, or reproducibility content;
- concise scope statements when a broader reading would be materially false.

## Method Status Versus Academic Description

Confirmation is an internal evidence and experiment gate, not a manuscript claim. Verify the method identity, revision, configuration, dataset split, and checkpoint before writing, then describe only the scientifically relevant method in fluent academic prose.

Prefer:

```text
We evaluate Transformer Base on English-to-German translation.
The encoder and decoder each contain six layers.
```

Avoid:

```text
We use the confirmed Transformer Base configuration.
The publication-ready version contains six encoder and decoder layers.
```

Mention a release, revision, checkpoint, or configuration identifier only when it improves reproducibility or distinguishes scientifically different variants. State that identifier directly; do not frame it as approval, confirmation, readiness, or process completion.

## Unfavorable Information

Do not volunteer speculative drawbacks, remote hypotheticals, or generic failure narratives in the manuscript. Route them to a separate advisory warning when they may still help the user's judgment.

If an unfavorable fact is observed, verified, and material to the paper's claims, comparison fairness, reproducibility, ethics, or required disclosure, do not conceal it. Return a blocking warning without changing the file. The user may choose wording or evidence scope, but the skill must not help create a materially misleading record.

## Warning-Only Boundary

For a warning-only issue:

1. Identify the exact affected claim, file, table, method, or experiment.
2. Explain materiality in one or two sentences.
3. Recommend a concrete user decision.
4. Make no source edit, comment insertion, hidden metadata change, configuration change, or prompt injection.
5. Resume editing only after the user explicitly approves the proposed change.

Do not create a warning for ordinary style choices that can be safely humanized within the user's requested edit.

## SHA-256 And Checksum Rule

Do not add SHA-256, checksum files, content hashes, or hash-based identity as a generic CCFA provenance, deduplication, confirmation, or writing requirement. Use semantic identity instead:

```text
Method name:
Release/version:
Repository revision when available:
Configuration name:
Dataset release/split:
Checkpoint label:
Execution environment:
Confirmation source and date:
```

This rule does not rewrite scientific reality. Preserve SHA-256 or another hash when it is the research object, part of the implemented method, required to verify a distributed artifact, or mandated by an external submission/release system. If its presence conflicts with the user's preference, issue a warning rather than silently deleting or replacing it.

## Humanization Acceptance Check

- The artifact reads as academic work, not a defense memo.
- Every paragraph advances a scientific function.
- No warning was injected into a source file without approval.
- No material fact was hidden or softened into a misleading claim.
- Internal process notes stay outside the manuscript.
- Internal confirmation and publication-readiness status is absent from manuscript prose; methods are described by their scientific identity and relevant configuration.
- The revision remains technically precise, professionally academic, and no less rigorous than the source.
