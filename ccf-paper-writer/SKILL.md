---
name: ccf-paper-writer
description: "Plan, draft, revise, polish, compress, and presentation-adapt CCF research paper text while preserving user-supplied idea scope and evidence. Use for paper writing, abstract/introduction/related work/method/experiment writing, polishing, page/word compression, slides/poster/talk/Q&A preparation, 润色论文, 写作, 压缩论文, 报告展示. Do not perform full review, evidence audit, submission-package checks, or rebuttal as the main task."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Paper Writer

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, and `../ccf-common/references/task-modes.md`.

This is the manuscript text owner. It also owns local compression and presentation adaptation because both change paper wording or paper-derived communication. Keep idea scope, method mechanism, experiments, numbers, and conclusions unchanged unless the user explicitly authorizes a research-scope change.

Do not invent results, citations, baselines, experiments, reviewer impact, or missing evidence. Unsupported claims must be weakened, marked as needing evidence, or left unchanged with a risk note.

## Core Rule

Write for the target CCF venue, not for a generic paper. Improve structure, section logic, paragraph roles, contribution framing, claim-evidence alignment, reviewer-facing clarity, and concise presentation. Do not use reference papers to copy wording, claims, examples, technical content, or distinctive phrasing.

## Modes

- `draft`: create or revise paper sections.
- `polish`: improve clarity, flow, terminology, and claim-evidence presentation.
- `compress`: shorten text to word/page limits using `references/compression-rules.md` without changing claims or numbers.
- `presentation`: convert a completed or near-completed paper into slides, poster, talk script, figure narration, and Q&A, without replacing submission review.

## Workflow

1. Identify mode, target venue, paper type, draft state, available evidence, and whether idea-scope changes are authorized.
2. If a target venue is named, read `references/venue-guides/index.md` and the specific venue guide for LaTeX/page/anonymity/template constraints; use `references/venue-adapters.md` for reviewer priorities.
3. Build or update the global story with `references/storyline-blueprint.md`: task -> gap -> root challenge -> insight -> method -> evidence -> limitation.
4. Draft or revise section by section using `references/section-modules.md` and `references/writing-checklists.md`.
5. For compression, load `references/compression-rules.md`; rank content by claim importance, remove repetition, preserve evidence and limitations, and mark cuts that require author approval.
6. For presentation adaptation, derive slides/poster/talk/Q&A only from the manuscript and supplied evidence.
7. If current literature, baselines, or experiments are missing, hand off to `ccf-literature-searcher` or `ccf-experiment-designer`; do not fill gaps by invention.
8. Before calling text ready, run a local score-risk check and, when needed, hand off to `ccf-paper-reviewer`.

## Output Contract

```text
Mode:
Target venue and assumptions:
Global story:
Section/paragraph plan:
Draft or revised text:
Compression or presentation notes:
Claim-evidence risks:
Reviewer-facing risks:
Next CCFA owner:
Checklist status:
```

## Reference Files

- `references/venue-guides/index.md` and `references/venue-guides/<venue>.md`: venue writing and format constraints.
- `references/storyline-blueprint.md`: whole-paper story.
- `references/section-modules.md`: section drafting.
- `references/writing-checklists.md`: readiness checks.
- `references/score-lifting-loop.md`: score-risk improvement loop.
- `references/expert-review-loop.md`: reviewer-style self-check.
- `references/compression-rules.md`: page/word compression.
- `references/exemplars/`: style-move references; never copy content.
