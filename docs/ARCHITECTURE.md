# CCFA v0.4 Architecture

CCFA is now a paper-project workflow family rather than a loose writing-skill set. The architecture has four layers:

1. Governance: `ccf-common`, `ccf-forge-skills`, trigger registry, artifact contracts, and validation scripts.
2. Project state: `ccf-paper-project-scaffold`, `ccf-pipeline-orchestrator`, and `ccfa.yaml`.
3. Research pipeline: idea, literature, experiments, writing, compression, review, rebuttal, resubmission, and talk skills.
4. Venue branch: `ccf-conference-guides` plus `109` migrated venue guides under `ccf-writing-skills/references/venue-guides/`.

## Design References

v0.4 uses ARS, nature-skills, and ARIS as workflow references, not as authoritative venue or review sources. The adopted lessons are:

- ARS-style research workflow decomposition is useful, but CCFA keeps stronger routing boundaries and a public trigger catalog.
- nature-skills-style high-standard writing guidance is useful, but CCFA separates writing, writing review, full scientific review, and submission checks.
- ARIS-style automation/orchestration is useful, but CCFA keeps generated content, project state, and evidence claims auditable through `ccfa.yaml` and artifact contracts.

The result should avoid three common conflicts: citation audit versus literature search, integrity audit versus scientific review, and venue-format lookup versus manuscript writing.

## Conflict Policy

- Route by the user's current primary intent.
- Keep venue-format lookup separate from paper-content writing.
- Use `ccf-citation-auditor` for already-cited-paper verification and `ccf-literature-search` for discovering new papers.
- Use `ccf-integrity-auditor` for evidence/number/claim consistency and `ccf-conference-reviewer` for full scientific review.
- Use `ccf-submission-checker` for package compliance and `ccf-conference-writing-reviewer` for manuscript-facing format/writing review.

## Source Of Truth

`SKILL.md` is authoritative. `docs/SKILLS_CATALOG.md`, `ccf-common/references/routing.md`, and `ccf-common/references/skill-trigger-registry.yaml` are audit indexes.
