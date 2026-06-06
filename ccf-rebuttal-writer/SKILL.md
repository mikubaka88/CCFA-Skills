---
name: ccf-rebuttal-writer
description: "Write and organize CCF conference rebuttals, author responses, response letters, revision summaries, reviewer-comment ledgers, and conservative resubmission adaptation plans. Use for rebuttal, author response, AC/meta-review response, revision ledger, resubmission to a new venue, 审稿意见回复, 重投迁移. Do not trigger for ordinary manuscript writing."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Rebuttal Writer

## Core Rule

Handle post-review communication and revision accountability. Responses must be calm, factual, evidence-grounded, and promise only feasible changes. Resubmission adaptation is conservative by default: no new experiments and no bibliography changes unless the user explicitly authorizes them.

## Modes

- `rebuttal`: reviewer/AC response under a word or time budget.
- `revision-ledger`: reviewer comment -> action -> manuscript location -> owner -> status.
- `response-letter`: revision summary or camera-ready response letter.
- `resubmission`: adapt an already written paper to a new venue with conservative defaults.

## Workflow

1. Identify venue, response format, word budget, deadline, review scores/confidence, and whether this is rebuttal, revision, or resubmission.
2. Parse comments into issue groups by reviewer, concern type, severity, available evidence, response strategy, and promised paper change.
3. Load `references/response-strategy.md` and answer high-impact concerns first: soundness, novelty, missing evidence, incorrect assumptions, and shared concerns.
4. Load `references/revision-ledger.md` whenever promised edits, manuscript locations, or resubmission actions must be tracked.
5. For full rebuttals, load `references/tex-templates.md` and use the TeX templates in `assets/templates/` when useful.
6. For resubmission, map old reviewer concerns to the new venue's constraints through `ccf-submission-checker`; do not silently add experiments or bibliography changes.
7. Hand off to `ccf-paper-writer` for manuscript revisions, `ccf-experiment-designer` for authorized new evidence, and `ccf-submission-checker` for venue/package checks.

## Output Contract

```text
Mode:
Venue and constraints:
Issue table:
Response strategy:
Draft response or response file:
Promised paper changes:
Revision ledger:
Resubmission adaptation notes:
Claims/promises to avoid:
Next CCFA owner:
Checklist status:
```

## References

- `references/response-strategy.md`: response tactics.
- `references/response-checklists.md`: tone, evidence, promises, and word-budget checks.
- `references/tex-templates.md`: reusable TeX response templates.
- `references/revision-ledger.md`: tracking reviewer comments and manuscript actions.
