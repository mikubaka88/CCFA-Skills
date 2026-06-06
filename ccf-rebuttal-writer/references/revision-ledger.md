# Revision Ledger

Use this reference when rebuttal, response-letter, resubmission, or camera-ready work needs a traceable ledger. The ledger is now part of `ccf-rebuttal-writer`; it is not a separate runtime skill.

## Ledger Columns

| Column | Meaning |
| --- | --- |
| `comment_id` | Stable ID such as `R1-C2` or `AC-C1`. |
| `source` | Reviewer, AC, meta-review, shepherd, or internal audit. |
| `concern` | Short neutral summary of the issue. |
| `response_claim` | What the author response says or will say. |
| `manuscript_action` | Concrete edit, experiment, clarification, limitation, or no-change rationale. |
| `location` | Section, paragraph, line, figure, table, appendix, or TeX file. |
| `owner_skill` | Usually `ccf-rebuttal-writer`, `ccf-paper-writer`, `ccf-experiment-designer`, or `ccf-submission-checker`. |
| `status` | `open`, `planned`, `drafted`, `done`, `blocked`, or `accepted_limit`. |
| `evidence` | Existing result, citation, table, figure, code, or explanation supporting the action. |
| `risk` | Remaining reviewer or submission risk. |

## Rules

1. Do not mark an action `done` unless the manuscript location or artifact exists.
2. Do not let response text promise an action that is absent from the ledger.
3. Use `accepted_limit` when the right response is to acknowledge a limitation rather than hide it.
4. Use `blocked` only when the missing artifact, result, permission, or policy cannot be resolved inside this skill.
5. Keep wording factual; persuasive tone belongs in the response draft, not in the ledger.

## Compact Template

```markdown
| ID | Concern | Response claim | Manuscript action | Location | Status | Evidence | Risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R1-C1 |  |  |  |  | open |  |  |
```
