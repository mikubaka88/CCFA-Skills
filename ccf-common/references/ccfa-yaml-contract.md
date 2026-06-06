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
