# Changelog

## Unreleased - Naming consistency pass

- Unified runtime skill names to the `ccf-<object>-<role/action>` style.
- Renamed ambiguous legacy names such as `ccf-paper-writer`, `ccf-scientific-reviewer`, `ccf-writing-reviewer`, `ccf-venue-format-guide`, and `ccf-skill-forger`.
- Merged `ccf-revision-ledger` into `ccf-rebuttal-writer` as `references/revision-ledger.md`.
- Rewrote README EN/zh-CN/zh-TW, catalog, routing, architecture, and agent guide around the new names.
- Added detailed catalog, routing, and artifact SVG diagrams in English, Simplified Chinese, and Traditional Chinese.


## v0.4.0 - 2026-06-06

### Added

- 10 new workflow skills: `ccf-pipeline-orchestrator`, `ccf-project-scaffolder`, `ccf-integrity-auditor`, `ccf-citation-auditor`, `ccf-submission-checker`, `ccf-figure-table-builder`, `ccf-artifact-packager`, `ccf-rebuttal-writer`, `ccf-resubmission-adapter`, and `ccf-paper-presenter`.
- New `ccf-venue-format-guide` entry skill for venue LaTeX, page limit, anonymity, template, and camera-ready questions.
- `ccfa.yaml` project-state contract and scaffold template.
- Artifact contracts, trigger registry, architecture docs, agent guide, and skills catalog.
- Codex and Claude plugin manifests.
- GitHub Actions validation for v0.4 routing and structure.

### Changed

- Renamed `forge-skills` to `ccf-skill-forger`.
- Migrated 109 legacy venue runtime skills into `ccf-paper-writer/references/venue-guides/`.
- Updated routing so venue requirements are a writing/reference branch rather than 109 standalone runtime skills.

### Compatibility

- Core research-chain skill names are preserved.
- Legacy `ccf-conference-skills/<venue>/SKILL.md` no longer exists as installable skills. Use `ccf-venue-format-guide` or the venue guide reference branch.
