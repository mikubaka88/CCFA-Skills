---
name: ccf-paper-compressor
description: "Compress CCF paper drafts, sections, abstracts, related work, methods, experiments, and camera-ready text to fit word or page limits while preserving claims and evidence. Use for ????, ??, shorten paper. Do not change results, claims, or limitations."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Paper Compressor

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `../ccf-common/references/handoff-modes.md`. Use `../ccf-common/references/routing.md` to keep compression separate from general manuscript drafting, paper review, experiment design, and rebuttal.

Load `../ccf-common/references/task-modes.md` before deciding quick or standard mode. Use quick mode for one paragraph, one subsection, or a local polish/shortening pass. Use standard mode for page-limit compression, full-section restructuring, camera-ready shortening, or decisions about appendix/delete.

Default to writing-only compression. Preserve the user's research topic, core problem, method mechanism, experimental setting, numerical results, conclusion direction, and limitations unless the user explicitly authorizes a scope change. Do not invent citations, results, baselines, or reviewer impact.

For content that may be moved to appendix or deleted, ask the user once with a concise recommendation unless the user already gave an instruction such as "delete aggressively" or "move details to appendix." After that one decision, apply it consistently.

## Core Rule

Compress by protecting the paper's story, not by trimming random words. Keep text that supports task -> gap -> root challenge -> insight -> method -> evidence -> limitation. Remove or move text that does not change reviewer understanding, duplicate earlier points, over-explain background, or hide the central claim.

## Mandatory Compression Checklist

In standard mode, complete this checklist before final output. In quick mode, run only the local subset and return a compact status.

1. Target length, section, venue, and allowed operations are explicit or assumed.
2. The section's role in the global story is identified.
3. Claims, evidence, results, and limitations are preserved unless explicitly removed by the user.
4. Redundant background, repeated motivation, excess implementation detail, and weak transition prose are identified.
5. Appendix/delete candidates are separated from mandatory main-text content.
6. One user decision is requested for appendix-vs-delete when that choice affects content ownership or paper strategy.
7. The compressed version keeps terminology stable and does not create unsupported stronger claims.
8. Any optional handoff to `ccf-paper-writer`, `ccf-scientific-reviewer`, `ccf-writing-reviewer`, or `ccf-experiment-designer` follows CCFA handoff mode.

## Workflow

1. Identify mode:
   - Quick: one paragraph/subsection, local shortening, no full checklist.
   - Standard: full section or manuscript-level compression with a content decision table.
2. Identify constraints: target venue, page/word limit, target percentage reduction, must-keep items, appendix allowed, citation policy, and whether technical details can be moved.
3. Load `references/compression-rules.md` and, if needed, `../ccf-paper-writer/references/storyline-blueprint.md` to preserve the paper story.
4. Build a content inventory:

```text
Unit:
Role:
Keep / compress / merge / move to appendix / delete:
Reason:
Risk if removed:
```

5. Ask once before moving material to appendix or deleting nontrivial content when the user's preference is unknown. Recommended default: move reproducibility detail, extra derivations, extended tables, and secondary analyses to appendix; delete repeated motivation, generic claims, and unsupported filler.
6. Rewrite at the requested granularity. Preserve facts and numbers exactly. If a claim becomes unsupported after compression, either keep the support, weaken the claim, or flag the risk.
7. Produce a before/after compression report with word or page estimates when possible.
8. If compression reveals a structural writing issue, follow CCFA handoff mode before using `ccf-paper-writer` or `ccf-writing-reviewer`. If it reveals missing evidence or experiment overload, follow CCFA handoff mode before using `ccf-experiment-designer` or `ccf-scientific-reviewer`.

## Output Contracts

For standard compression, return:

```text
Target and assumptions:
Storyline protected:
Compression plan:
Appendix/delete decision:
Compressed text:
Content movement table:
Claim-evidence preservation:
Estimated reduction:
Remaining risks:
Checklist status:
```

For quick compression, return:

```text
Quick mode:
Compressed text:
What changed:
Risk note:
Compact checklist status:
```

## Reference Files

Load only what is needed:

- `references/compression-rules.md`: Use for compression hierarchy, appendix/delete decision rules, venue style, and quick/standard workflows.
