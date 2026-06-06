# Section Modules

Use this file when drafting, rewriting, or checking a specific paper section. Always connect section writing back to `references/storyline-blueprint.md`.

Use the steps below as internal writing control unless the user asks to see the plan. For direct polishing, line editing, compression, or LaTeX revision, return the revised text in the user's original format rather than exposing paragraph-role analysis.

## Module Template

For any section:

1. Determine the section role in the whole-paper story.
2. Decide paragraph roles before writing.
3. Draft paragraphs one role at a time.
4. Check local flow: one paragraph, one message.
5. Check global flow: section supports the main story and venue plan.
6. Update claim-evidence and reviewer-risk maps.

Show steps 1-2 only when the user requested a plan, outline, diagnosis, or explanation.

## Abstract

Goal: give reviewers the whole paper in one pass.

Recommended moves:

1. Task and importance.
2. Specific gap or technical challenge.
3. Core insight or contribution.
4. Method mechanism at a high level.
5. Evidence summary with cautious claims.

Checks:

- Does every major abstract claim appear later with evidence?
- Is the method name understandable without hidden context?
- Does the abstract fit target venue style: concise for systems, precise for theory, contribution/evidence-balanced for AI/CV/NLP?

## Introduction

Goal: create reviewer curiosity and make the contribution feel necessary.

Recommended paragraph roles:

1. Task/application/value.
2. Existing methods and their progress.
3. Remaining gap and root technical reason.
4. Insight and proposed method.
5. Contributions and evidence preview.

Checks:

- Does the core challenge appear early enough?
- Is the root technical reason explicit?
- Are prior methods used to motivate the gap rather than dumped as citations?
- Do contribution bullets map to Method and Experiments?
- Would a skeptical reviewer understand why the work is not a small patch?

## Related Work

Goal: make novelty easy to verify.

Recommended structure:

1. 2-4 topic groups.
2. For each group: paradigm -> representative methods -> limitation tied to this paper -> distinction.
3. End with the closest gap the paper fills.

Checks:

- Are strongest and recent competitors included?
- If closest work is unknown or fast-moving, use `ccf-literature-searcher` through the CCFA handoff mode rather than inventing citations.
- Is the distinction technical, not marketing language?
- Does Related Work prepare the reader for the Method?
- Are citations complete for all background claims?

## Method

Goal: make the mechanism auditable and reproducible.

Pre-writing questions:

1. What modules exist?
2. For each module, what is the workflow?
3. Why is the module needed?
4. Why should it work?
5. What assumptions, hyperparameters, or implementation details matter?

Recommended structure:

1. Overview: setting, core idea, pipeline figure, section map.
2. Module sections: motivation -> design -> forward process -> technical advantage.
3. Implementation details: reproducible specifics.
4. Complexity, assumptions, or proof sketch when relevant.

Checks:

- Can a reviewer reconstruct the pipeline from text and figure?
- Does each module have motivation and technical advantage?
- Are inputs, outputs, notation, and symbols defined before use?
- Are design choices later validated by ablation, theorem, analysis, or user study?

## Experiments

Goal: prove the claims reviewers care about.

Recommended structure:

1. Setup: datasets, metrics, baselines, protocol, implementation.
2. Main comparison: answer whether the method works.
3. Ablation: answer why it works.
4. Analysis: answer when it works, when it fails, and how robust it is.
5. Qualitative or case studies when the venue expects them.
6. Limitations or failure cases if not placed elsewhere.

Checks:

- Does each claimed contribution have a corresponding experiment?
- If the user needs datasets, baselines, ablations, benchmark design, or fill-in result tables, use `ccf-experiment-designer` through the CCFA handoff mode.
- Are baselines strong, recent, and fair?
- Are metrics standard and sufficient?
- Are ablations tied to modules and design choices?
- Do tables and figures each have one message?
- Are negative or boundary results handled honestly?

## Figures And Tables

Goal: make the paper inspectable before close reading.

Rules:

1. Every figure/table should answer one reviewer question.
2. Captions should state setting and main takeaway.
3. Tables should use clean grouping, consistent precision, metric direction, and minimal visual noise.
4. Pipeline figures should show data flow, modules, and outputs without overcrowding.
5. Qualitative figures should avoid cherry-picking by showing representative successes and failures when possible.

Checks:

- Can the paper's contribution be understood from figures and captions?
- Are key claims visible in tables or figures?
- Are visual examples aligned with the text discussion?

## Conclusion

Goal: leave a precise final takeaway.

Recommended moves:

1. Restate problem and core method.
2. State the key insight or contribution.
3. Summarize strongest evidence.
4. Bound limitations.
5. Point to future work without adding new claims.

Checks:

- Does it match the paper's actual evidence?
- Does it avoid introducing new technical material?
- Does the limitation sound like scope boundary rather than hidden fatal flaw?

## Limitations, Ethics, Broader Impact

Use when the venue requires or expects these sections.

Checks:

- Are limitations specific and bounded?
- Are datasets, human subjects, privacy, security, misuse, bias, or environmental concerns addressed when relevant?
- Are claims weakened where the limitation narrows validity?
- Does the section improve reviewer trust rather than read like boilerplate?

## Small Paragraph Edit Mode

When the user gives one paragraph:

1. Identify paragraph role.
2. State the intended message in one sentence.
3. Check sentence flow.
4. Check term consistency.
5. Check whether claims are supported or need softer wording.
6. Rewrite with the same technical meaning unless the user asks for structural changes.

Visible output default: the rewritten paragraph only, preserving Markdown/LaTeX/citation formatting. Add a short note only if a claim was softened, a citation/result looked unsupported, or the user asked for explanation.

## LaTeX Drafting Mode

When the user supplies only an idea and asks for a paper draft:

1. Read the target venue guide from `venue-guides/index.md`; if the target venue is missing or unspecified, use the NeurIPS guide as the fallback.
2. Use the venue's template path and section conventions for the visible LaTeX draft.
3. Keep missing results, citations, figures, and theorem/proof details as `TBD` placeholders instead of inventing them.
4. Prefer a compilable skeleton with real section content over a checklist report.
5. Include venue-freshness or missing-evidence notes after the LaTeX output, not before it.
