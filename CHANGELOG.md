# Changelog

## v0.4.0 - 2026-06-06

### Added

- 10 new workflow skills: `ccf-pipeline-orchestrator`, `ccf-paper-project-scaffold`, `ccf-integrity-auditor`, `ccf-citation-auditor`, `ccf-submission-checker`, `ccf-figure-table-builder`, `ccf-artifact-reproducibility`, `ccf-revision-ledger`, `ccf-resubmission-adapter`, and `ccf-paper-talk`.
- New `ccf-conference-guides` entry skill for venue LaTeX, page limit, anonymity, template, and camera-ready questions.
- `ccfa.yaml` project-state contract and scaffold template.
- Artifact contracts, trigger registry, architecture docs, agent guide, and skills catalog.
- Codex and Claude plugin manifests.
- GitHub Actions validation for v0.4 routing and structure.

### Changed

- Renamed `forge-skills` to `ccf-forge-skills`.
- Migrated 109 legacy venue runtime skills into `ccf-writing-skills/references/venue-guides/`.
- Updated routing so venue requirements are a writing/reference branch rather than 109 standalone runtime skills.

### Compatibility

- Core research-chain skill names are preserved.
- Legacy `ccf-conference-skills/<venue>/SKILL.md` no longer exists as installable skills. Use `ccf-conference-guides` or the venue guide reference branch.
