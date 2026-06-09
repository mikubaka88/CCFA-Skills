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
