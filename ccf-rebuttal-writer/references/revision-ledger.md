# Revision Ledger

Use this reference when rebuttal, response-letter, resubmission, or camera-ready work needs a traceable ledger. The ledger is now part of `ccf-rebuttal-writer`; it is not a separate runtime skill.

## Ledger Columns

| Column | Meaning |
| --- | --- |
| `comment_id` | Stable ID such as `R1-C2` or `AC-C1`. |
| `source` | Reviewer, AC, meta-review, shepherd, or internal audit. |
| `first_seen_version` | First manuscript version or review round where the issue was recorded. |
| `current_version` | Manuscript version against which status is currently assessed. |
| `concern` | Short neutral summary of the issue. |
| `response_claim` | What the author response says or will say. |
| `manuscript_action` | Concrete edit, experiment, clarification, limitation, or no-change rationale. |
| `location` | Section, paragraph, line, figure, table, appendix, or TeX file. |
| `owner_skill` | Usually `ccf-rebuttal-writer`, `ccf-paper-writer`, `ccf-experiment-designer`, or `ccf-submission-checker`. |
| `status` | Revision work: `open`, `planned`, `drafted`, `done`, `blocked`, or `accepted_limit`. Comparative review: `unresolved`, `partially_resolved`, `resolved`, or `not_applicable`. |
| `origin` | `inherited`, `revision_regression`, `previously_undetected`, `newly_revealed_by_evidence`, or `external_standard_change`. |
| `applies_to` | `historical`, `current`, or `both` for version comparisons. |
| `affected_dimensions` | Frozen review dimensions affected by the issue. |
| `comparative_score_effect` | Per-version score effect, with a reason and evidence anchor when nonzero. |
| `evidence` | Existing result, citation, table, figure, code, or explanation supporting the action. |
| `risk` | Remaining reviewer or submission risk. |

## Rules

1. Do not mark an action `done` unless the manuscript location or artifact exists.
2. Do not let response text promise an action that is absent from the ledger.
3. Use `accepted_limit` when the right response is to acknowledge a limitation rather than hide it.
4. Use `blocked` only when the missing artifact, result, permission, or policy cannot be resolved inside this skill.
5. Keep wording factual; persuasive tone belongs in the response draft, not in the ledger.
6. Maintain one canonical ledger, normally `reviews/revision-ledger.md`, and update it in place. Do not create dated or per-round copies unless the user or an external submission record requires them.
7. A `previously_undetected` issue applies to both versions in a frozen comparison unless the current revision resolves it. A current-only score decrease requires `revision_regression` or `newly_revealed_by_evidence` plus a concrete evidence anchor.

## Compact Template

```markdown
| ID | First seen | Current version | Concern | Origin | Applies to | Affected dimension | Status | Action / location | Evidence | Score effect | Risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R1-C1 |  |  |  | inherited | both |  | unresolved |  |  |  |  |
```
