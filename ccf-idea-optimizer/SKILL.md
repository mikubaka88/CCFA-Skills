---
name: ccf-idea-optimizer
description: "Turn rough CCF research directions into concrete problem, gap, insight, method, novelty, and evidence plans. Use for idea optimization, fuzzy idea concretization, research direction shaping, 优化idea, 具象化idea, 研究思路优化. Do not rank or score multiple ideas as the main output."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Idea Optimizer

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `../ccf-common/references/handoff-modes.md`. Use `../ccf-common/references/routing.md` to keep idea optimization separate from idea scoring, manuscript writing, paper review, and rebuttal tasks.

Load `../ccf-common/references/task-modes.md` before deciding quick or standard mode. Use quick mode for a short idea repair or one local direction note. Use standard mode for fuzzy idea concretization, broad exploration, novelty grounding, or a plan that will feed writing, reviewing, literature search, or experiment design.

If the user says not to use, disable, skip, or avoid a sibling skill, do not invoke or simulate that skill for the rest of the conversation. Use this skill's local fallback instead: compact risk scan, action queue, or next-step note without cross-skill execution.

Do not invent literature, results, baselines, experiments, reviewer reactions, or novelty evidence. Mark unsearched novelty and missing evidence as uncertainty.

Treat rough ideas, unpublished method details, draft abstracts, and experiment plans as private user data. Load `../ccf-common/references/privacy-and-evidence.md` before browsing, using private text in a query, or making evidence/provenance claims.

## Core Rule

Optimize the research idea before optimizing the writing. Do not inflate novelty, invent related work, invent results, or turn weak ideas into confident claims. Make the idea more CCF-A-ready by sharpening the problem, mechanism, contribution, evidence package, and reviewer-facing risk register. For fuzzy ideas, generate diverse but internally consistent candidate concretizations; prefer timely, elegant, non-stale directions and clearly mark novelty uncertainty until searched.

## Mandatory Checklist

In standard mode, complete this checklist before final output. In quick mode, run the local subset only and return a compact status.

1. Target venue, venue family, field, and idea stage are explicit or marked unknown.
2. The raw idea is normalized into problem, gap, root challenge, insight, method, evidence, and limitation.
3. Missing inputs that affect confidence are named: related work, datasets, code, compute, timeline, collaborators, or domain constraints.
4. Novelty is treated as uncertain until grounded against closest known work or a current literature search.
5. The method mechanism is explained, not only named.
6. Innovation type is classified: problem, setting, method, data/benchmark, theory, system, empirical finding, evaluation, or synthesis.
7. The experiment plan tests the central claim and includes baselines, ablations, robustness, and failure analysis as needed by the venue.
8. Reviewer risks are labeled as writing-fixable, design-fixable, evidence-fixable, requires-new-result, venue-mismatch, or likely-pivot.
9. Diverse variants are checked for internal contradictions, mutually incompatible assumptions, and theme drift.
10. Any optional module transition to `ccf-literature-searcher`, `ccf-idea-reviewer`, `ccf-experiment-designer`, or `ccf-paper-writer` follows the CCFA handoff mode; if denied or disabled, output a local risk scan or next-step note only.

Load `references/idea-intake.md` when inputs are incomplete or several idea drafts must be normalized.

## Workflow

1. Identify the target venue, track, field, idea maturity, user's decision goal, constraints, and available evidence. If no venue is named, assume a generic CCF-A target and label the assumption.
2. Map the target to a CCF-A family. Use `../ccf-common/references/ccf-a-venue-map.md` for shared venue-family routing; then load `references/venue-idea-adapters.md` for idea-stage priorities.
3. Ground novelty and timeliness. If the user asks for current prior art, latest trends, frontiers, non-stale ideas, or venue-specific policy, follow CCFA handoff mode before using `ccf-literature-searcher`; if searching directly, browse primary sources: official venue pages, papers, proceedings, arXiv pages, project pages, and credible scholar sources. Mark unsearched novelty as uncertain.
4. Normalize the raw idea. Load `references/idea-intake.md` and produce an idea card with task, audience, gap, root challenge, insight, method, expected evidence, and constraints.
5. For fuzzy or underdetermined ideas, load `references/frontier-ideation.md` and produce 3-5 candidate concretizations with high diversity across problem angle, mechanism, evidence type, and venue fit. Randomness is allowed in exploration, but final candidates must be coherent and non-conflicting.
6. Sharpen the problem and method. Load `references/problem-method-blueprint.md`; convert vague motivation into a decision-relevant problem and convert method names into mechanisms, assumptions, failure modes, and alternatives.
7. Shape the innovation. Decide the strongest honest contribution type and remove unsupported or diluted claims.
8. Design the minimum convincing evidence package. Load `references/experiment-design.md`; specify datasets, baselines, ablations, metrics, stress tests, efficiency, user study, proof, or systems evaluation as required by the venue family. Follow CCFA handoff mode before using `ccf-experiment-designer` for a full experiment plan.
9. Run an internal acceptability pass. Follow the CCFA handoff mode before using `ccf-idea-reviewer` as an optional scoring module; if it is denied or disabled, perform a compact multi-expert risk scan focused only on problem and method.
10. Produce an optimized idea plan, ranked pivots, and a writing-readiness note. Follow the CCFA handoff mode before offering the viable plan to `ccf-paper-writer`; if writing is denied or not confirmed, stop at the idea plan.

## Output Contracts

For one idea, return:

```text
Target venue and assumptions:
Raw idea diagnosis:
Optimized idea card:
Candidate concretizations:
Problem statement:
Core insight:
Method blueprint:
Innovation claims:
Experiment plan:
Closest-work / novelty unknowns:
Reviewer-risk register:
Suggested pivots:
Optional next-module decision:
Checklist status:
```

For multiple idea drafts, return:

```text
Venue lens:
Normalized idea table:
Best candidate:
Why it wins:
Idea-specific upgrades:
Risks by idea:
Recommended next iteration:
```

## Reference Files

Load only what is needed:

- `references/idea-intake.md`: Use for incomplete, messy, or multi-candidate idea drafts.
- `references/frontier-ideation.md`: Use for fuzzy idea concretization, high-diversity exploration, non-stale direction checks, and coherence filters.
- `references/problem-method-blueprint.md`: Use when sharpening the problem, insight, mechanism, contribution type, and failure modes.
- `references/venue-idea-adapters.md`: Use after mapping a target to a CCF-A family.
- `references/experiment-design.md`: Use when designing baselines, ablations, evidence packages, and acceptance-oriented experiments.
- `references/research-taste.md`: Use when the user asks what makes research good, elegant, timely, or likely to survive top-conference review.
- `references/source-notes.md`: Use when provenance, source basis, or current-policy checks matter.

If the user's request is only to score an idea without optimizing it, follow the CCFA handoff mode before switching to `ccf-idea-reviewer` unless the user explicitly named it. If the user's request is mainly to search related literature, route to `ccf-literature-searcher`. If the user already has a manuscript draft, follow the CCFA handoff mode before switching to `ccf-paper-writer` or `ccf-paper-reviewer`; if not confirmed, provide only a brief scope note.
