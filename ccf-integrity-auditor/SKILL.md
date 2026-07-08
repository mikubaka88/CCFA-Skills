---
name: ccf-integrity-auditor
description: "Audit CCF paper integrity: claim-support alignment, result-to-claim consistency, numeric consistency, terminology consistency, figure/table-to-text consistency, existing citation existence, BibTeX metadata, and citation-context support. Use for evidence audit, citation audit, consistency check, 引用核验, claim审计, 数字一致性. Do not perform full scientific review or broad literature search."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Integrity Auditor

## Core Rule

Trace each important claim to supplied evidence, each number to supplied results, and each citation to a real cited work and a supported citation context. Mark unsupported items instead of repairing them by invention.

## Modes

- `claim-audit`: claim-support and result-to-claim consistency.
- `numeric-audit`: numbers, units, table/figure/text agreement, deltas, and metric direction.
- `citation-audit`: already cited papers, BibTeX metadata, duplicate keys, DOI/arXiv/venue sanity, and citation-context support.
- `full`: all integrity checks.

## Workflow

1. Identify supplied manuscript, figures/tables/results, bibliography, `ccfa.yaml`, and requested audit mode.
2. Build a claim-evidence matrix and mark each claim as supported, partially supported, unsupported, overstated, or unclear.
3. Cross-check all reported values across text, tables, figures, captions, abstracts, and conclusions.
4. For citation audit, verify only existing citations unless the user asks for new literature; broad search belongs to `ccf-literature-searcher`.
5. For any questionable citation, separate metadata problems from context-support problems.
6. Hand off to `ccf-paper-reviewer` for full scientific judgment and to `ccf-paper-writer` for safe wording edits.
7. If the numbers and claims are consistent but the figure/table layout, caption placement, palette, float order, or rendered readability is weak, hand off to `ccf-visual-composer`.

## Output Contract

```text
Mode:
Artifacts checked:
Claim-evidence matrix:
Numeric consistency findings:
Citation metadata findings:
Citation-context findings:
Severity:
Safe edit suggestions:
Next CCFA owner:
No-invention status:
```
