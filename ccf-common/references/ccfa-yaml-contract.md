# ccfa.yaml Contract

`ccfa.yaml` is the shared paper-project state file introduced in v0.4.0.

Required top-level fields:

- `version`
- `project`
- `target_venue`
- `stage`
- `artifacts`
- `claims`
- `experiments`
- `reviews`
- `revision_ledger`
- `submission_checks`

Only `ccf-project-scaffolder` should create it by default. `ccf-pipeline-orchestrator` may update stage and gate state. Other skills may read it and propose updates unless the user explicitly grants write permission.

Optional monitoring fields:

- `literature_monitor`
- `tracked_competitors`
- `watch_queries`
- `last_monitoring_report`

`ccf-literature-monitor` may propose updates to these fields after a watch run. It must not silently overwrite project state unless the user explicitly asks it to persist the monitoring summary.

## Path Resolution And Iteration

Keep the existing schema version and top-level fields. Resolve `project.root` relative to the directory containing `ccfa.yaml`, then resolve relative artifact paths against that project root. Existing mappings and explicit user paths take precedence over default folders. Do not change paths merely to adopt a new naming convention.

Use `artifact-contracts.md` for canonical outputs, one working directory per artifact, on-demand source/cache/build placement, and update-in-place rules. Only store a path in project state when the artifact actually exists or is clearly marked as planned; do not claim an old export is refreshed after a failed rebuild. Reuse existing state/report fields rather than introducing a new schema or per-step manifest.
