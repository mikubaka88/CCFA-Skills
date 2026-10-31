# Autonomous Research

Use this mode when the user explicitly asks to carry scientific work through iterative hypothesis development, experiments, observed feedback, and further improvement, including `autonomous research`, `autoresearch`, or `自主科研迭代`. A request to explain such a workflow, review an idea, or give a plan does not start execution. Reuse the active Humanization -> Common preflights.

## Scope And Ownership

Coordinate the full requested research loop through its owners. The orchestrator integrates evidence, controls the run contract, and invokes actual execution tools exposed by the host. It does not replace scientific owners or stop at naming them. Loading specialist guidance does not require a separate model call or agent; use actual delegation only when it helps this task.

| Contribution | Owner and return |
| --- | --- |
| Candidate mechanism, changed assumption, or search strategy | `ccf-idea-optimizer`; return the hypothesis and a discriminating prediction. Use `ccf-idea-reviewer` for a consequential concept judgment when needed, without imposing experiment requirements on concept review. |
| Closest work, dataset/baseline provenance, or missing external evidence | `ccf-literature-searcher`; use current sources where the decision needs them and preserve source anchors. |
| Comparison protocol, execution specification, interpretation of measured feedback | `ccf-experiment-designer`; apply its `references/evidence-design.md` iteration guidance. |
| Codebase fit, task-owned implementation, baseline reproduction, training diagnosis and performance | `ccf-research-engineer`; return code, inspected runtime configuration, actual execution evidence and resource observations. Use available host tools within authorized edit surfaces and resources. A specialist specification is not an executed run. |
| Material result conflicts, requested figures, or supported manuscript text | The relevant integrity, visual, or writing owner; run only the contribution needed for this deliverable. |

Within the authorized task, the agent may revise hypotheses, methods, research code, search queries, and candidate-selection strategy in response to evidence. Preserve the scientific objective and hard constraints while changing the route when warranted. A stable goal does not freeze the initial mechanism or restrict innovation to small module additions.

Persistent changes to installed/public skills, global prompts, personal preferences, or cross-project behavior require a separate authorized maintenance task. This workflow does not automatically train or upgrade the foundation model running the agent, or establish recursive capability gains. Training candidate research models is valid when the task explicitly authorizes it and actual commands, data, and resources support it. The `maintenance_evolution` one-extra-candidate limit does not govern a requested research campaign; `alternative_routes=off` does not suppress its authorized exploration. Optional additional whole research branches and task-owned policy comparisons follow research_branching and research_policy_evolution in Common preferences. Ordinary research execution needs neither switch; no switch starts a background task or upgrades the foundation model.

## Resolve The Run Contract Once

Reuse the latest user request, existing research plan, project configuration, and verified available resources. Resolve only missing decisions that affect execution; do not ask again at each candidate.

- The scientific objective, acceptance conditions, hard constraints, and requested deliverables.
- The editable research surface, protected inputs and evaluator, and which tool/data transfers are already authorized.
- A usable starting point or baseline, candidate mechanism, evaluation protocol, and evidence locations. A missing empirical baseline need not prevent developing the hypothesis or preparing its implementation.
- The actual command/environment/data dependencies, a finite allowance for the whole campaign, and a timeout for each external run. Reuse applicable limits on total attempts, elapsed time, compute or API use; a per-command timeout alone does not bound the campaign. State which values are measured, estimated, or unavailable. Include preparation, failures, evaluation, retries, and final verification where they consume the authorized allowance.
- The conditions for stopping successfully, stopping with an unresolved/negative outcome, or requesting a material resource/scope decision.

Use an existing authorized budget. If the necessary data, command, access, or execution allowance is missing, continue independent source inspection, hypothesis development, protocol design, and implementation preparation; block only the dependent run and name the precise missing input. Do not invent an unlimited budget, fabricate a command, or request a new full intake. A user request for a bounded local campaign already authorizes its ordinary internal steps, subject to host permissions.

Keep the contract and current state in the existing task record or established artifact mapping. Reuse `ccfa.yaml` according to the [shared contract](../../ccf-common/references/ccfa-yaml-contract.md), without silently adding top-level fields or forcing project scaffolding. A persisted helper record belongs under the existing task directory; the [artifact contract](../../ccf-common/references/artifact-contracts.md) governs its paths and retained evidence. Do not create both a generic continuity record and a second equivalent research record.

## Execute And Learn

1. **Orient.** Check the current objective, actual baseline/current candidate, relevant evidence versions, available execution capabilities, and remaining allowance. Reuse applicable prior checks. Do not require every research stage before an early hypothesis can be explored.
2. **Propose.** State the mechanism or assumption being changed and the observation that distinguishes it from the current explanation. Choose candidates for decision-relevant scientific value, not only easy implementation or likely metric gains. When useful and authorized, explore a different causal mechanism rather than renaming similar module combinations.
3. **Prepare.** Have the experiment designer connect the hypothesis to a sufficient comparison and expected evidence. Use the research engineer for needed codebase selection, mechanism implementation, baseline reproduction, or training diagnosis and the inspected executable configuration. Reuse valid groundwork; a local fix need not restart codebase selection or full baseline training. Protect original measurements and the comparison definition; isolate candidate changes from the usable baseline. Use checks for changed critical paths and meaningful controlled diagnostics without presenting them as unexecuted full-method results.
4. **Run.** Have the engineering owner execute through an available, authorized host tool with the applicable allowance, or reuse an applicable run already completed for this contract. Record actual command/configuration, source and environment versions, output locations, and observed consumption. Profile or tune the training path when the requested decision, cost, or observed failure justifies it. Starting a command is not completion; a zero exit code does not establish a valid measurement. Missing or partial outputs remain unresolved.
5. **Interpret.** Read the relevant actual evidence and check comparability. Separate infrastructure failure, invalid protocol, a valid negative result, and an inconclusive measurement. The designer explains which hypothesis each outcome supports or weakens; the optimizer can then revise the mechanism or strategy.
6. **Select.** The integrating owner chooses keep, discard, branch, repair, or stop against the current contract. Judge baseline replacement separately from scientific value: an informative negative result or a promising branch can guide the next experiment without replacing the best measured candidate. Promote a candidate only when its evidence supports the relevant criteria and hard constraints; distinguish further study from achieving the research goal.
7. **Continue or close.** If scope and resources remain, take the next informative step. Deliver the best supported result, necessary evidence and code, observed cost, and remaining uncertainty when the stopping condition is reached. Do not stop an authorized end-to-end request after returning only a plan when execution is available.

Keep evaluation criteria stable while comparing candidates. A corrected evaluator or an explicit user goal change can justify a new comparison contract; record the reason and rerun affected comparisons. Scores from different conditions are not a single improvement sequence. An unfavorable result alone is not a reason to change the metric or hide a failed candidate. New candidate IDs, branches, records, or protocol versions do not reset the user's campaign allowance.

## Escape Unproductive Loops

Apply Common's progress test across all contributors: each continuation should add a relevant observation, test a distinct prediction, resolve an execution defect, or change a justified assumption. Repeated critique, rephrased hypotheses, and owner changes are not progress.

When a branch repeats the same failure without new information, stop that branch. If the goal and remaining allowance support it, compare a different mechanism or take the smallest observation that can change the decision. A scientifically uninformative search direction may be replaced within the task without changing the user's goal. Do not keep a poor route because work has already been spent on it, and do not replace an ambitious goal with an easier claim merely to finish.

Stop the campaign when its requested result and applicable checks are complete, its allowance is exhausted, a required decision/input blocks further meaningful execution, or no informative next step remains within scope. Preserve and deliver supported independent work. Budget exhaustion is not scientific success. A negative result can be the result of a completed investigation; an unresolved claim must remain unresolved. Continuing beyond the approved allowance requires the missing scope/resource decision, not another renamed iteration.

## Research Memory And Context

Reuse the campaign records as working memory: user objective, current working question, best measured candidate, relevant contrary observations, and the next discriminating action. Retrieve older attempts by mechanism or finding when revisiting a route; do not reload every log or create a second narrative ledger. The helper's `context --query` returns compact records and evidence paths. Literal matching is a retrieval aid, not a scientific ranking.

Interpret the actual run before changing the idea. Environment failures call for environment repair; broken implementations do not refute hypotheses; invalid comparisons need corrected protocols. A valid negative result can reject an explanation without rejecting the broader objective. Use `note` for a reusable finding or corrected interpretation not already clear from the decision reason. It adds no model call and preserves raw measurements and earlier interpretations. Host annotations remain judgments, distinct from observed measurements.

## Complete Research Branches

Use `research_branching` for optional additional branches; explicit multi-direction requests remain authorized with it off. Delegate complete questions with a mechanism, implementation, observation, and interpretation. Share verified results while retaining each branch's unfinished reasoning. Give contributors finite allowances and separate candidate areas for concurrent edits; keep the evaluator and comparison definition common. Do not split one tightly coupled architecture into independently invented pieces. Without actual host delegation, execute useful branches serially.

Keep one integrating owner and serialize changes to shared artifacts. Carry the goal revision, candidate version, remaining allowance, evidence anchors, and completion condition. Check delayed findings against changed inputs. Choose the next opportunity from observed progress: repair a fault, repeat an uncertain measurement, deepen a promising mechanism, or test a different explanation. Preserve the strongest route while exploring; recent score alone and obligatory round-robin scheduling are both insufficient. Stop a branch whose decisive assumption fails or whose allowance is exhausted, retaining its result.

## Optional Research-Policy Evolution

When `research_policy_evolution` is enabled for an authorized campaign, optimize a task-owned search, context-selection, or tool-use policy in an outer loop. Keep its file in the established campaign directory. Ordinary task corrections need no policy trial; installed skills and personal defaults remain under their separate maintenance authorization.

1. Identify an observed process failure and a policy change intended to correct it. Freeze editable surfaces, reference policy, task starts, available model/tool settings, evaluation criteria, and total cost allowance.
2. Separate development, selection, and final held-out tasks. Protect evaluators and final answers from candidate edits. A final test used to select the next policy is no longer held out. Establish the actual trial command with the engineer; absent execution inputs block only the dependent trial.
3. Run reference and candidate policies under comparable total allowances, including failures, context construction, model calls, and checks. Record output validity, scientific progress, and actual costs separately. An unknown token count remains unknown.
4. Apply the frozen selection rule and retain the incumbent if required quality or constraints regress. Reuse an accepted task policy in the next trial. Broader adoption needs independent-task results and authorized maintenance. The next iteration edits the retained policy, not an unevaluated proposal.

The existing helper can track a policy file against an external trial evaluator using the same frozen contract. Use the optional evaluation stages below to bind selection and final tasks to their declared split content; final measurements report a frozen selected candidate without promoting or tuning it. It supplies execution records and bounded selection, not a model service, benchmark dataset, external sandbox, or automatic scheduler. Extra trials consume the campaign budget. Do not add an always-on judge or import an entire agent platform to perform this loop.

## Sequential Experiment Helper

Use [research_loop.py](../scripts/research_loop.py) when the task has a local, independently evaluated foreground command that waits for all its workers and needs bounded execution, managed-file rollback, and recoverable records. Commands that detach background workers are unsupported. The standard-library helper does not generate hypotheses, edit candidate code, search branches, judge novelty, or call a model. The agent performs those steps through the scientific and engineering owners. It also does not provide an OS sandbox: its file checks detect changes, while command permissions, network/GPU access, environment, and side effects remain the host's responsibility. It supplies no codebase selection, training-state resume, cluster scheduler, or GPU cost meter; use the engineer and real host capabilities where needed. Do not simplify the research project merely to fit this helper.

Prepare the execution contract from inspected project files. For example, the following assumes an existing `research/evaluate.py` independently evaluates `research/candidate.py` on `data/dev.jsonl`, accepts the shown arguments, and writes a fresh top-level JSON object such as `{"accuracy": 0.72}` to `--metrics`. These example paths and values are not supplied results or a ready-made experiment.

```json
{
  "objective": "Improve retrieval accuracy within the fixed retrieval budget",
  "constraints": ["Keep the retrieval budget and evaluation split unchanged"],
  "scientific_value": "Test whether allocating retrieval to uncertain queries explains an improvement",
  "editable_files": ["research/candidate.py"],
  "evaluator_files": ["research/evaluate.py"],
  "data_files": ["data/dev.jsonl"],
  "command": ["python", "research/evaluate.py", "--candidate", "research/candidate.py", "--data", "data/dev.jsonl", "--metrics", "{metrics}"],
  "metric": {"name": "accuracy", "direction": "max", "min_delta": 0.0},
  "budgets": {"max_attempts": 4, "max_seconds": 120, "timeout_seconds": 30}
}
```

The three budget values are illustrative, not defaults or recommended research scale. Local `max_attempts` covers this comparison's baseline, candidates, replications and failed attempts; an attached shared campaign record additionally limits all its participating contracts. `max_seconds` budgets cumulative elapsed time of direct foreground commands, including startup, and `timeout_seconds` sets one run's timeout, capped by the remaining execution allowance. This is not total process-tree CPU usage and excludes model tokens, host planning time, and other external charges; track these against the broader user allowance separately. Timeout termination is best effort and cannot guarantee that orphan processes have stopped or undo external side effects. If the process-tree termination tool fails or termination cannot be confirmed, the run stays pending and managed files are preserved until the host checks workers and explicitly recovers it. `scientific_value` and `constraints` record the host's scientific contract; the script cannot judge their fulfillment from text.

Declared evaluator/data files and optional `protected_files` are hashed before and after execution. Large datasets can make these checks expensive, and their time is outside the command timer. Prefer this helper for manageable local inputs; a separately verified immutable dataset version may use a manifest only when the host actually enforces that version. Hashing a manifest alone does not protect mutable data behind it. For repeated state reads, `status --fast` and `context --fast` return the last recorded verification identity/time and explicitly mark `integrity=not_rechecked`; they do not rehash data or evidence. Normal execution, promotion and recovery still check current declared inputs. A fast receipt never establishes that current files remain valid.

### Bind The Inputs Actually Used

Before the first comparison, the engineer follows the inspected command through local imports, resolved configuration, preprocessing, evaluator helpers and material environment dependencies. Put candidate-varying code/config in `editable_files`; keep fixed evaluation helpers/configuration, environment lockfiles and split manifests in `protected_files` or the existing evaluator/data lists. Every path remains a unique project-relative file. Do not freeze a candidate setting that the experiment intentionally changes.

The default literal preflight catches existing local Python imports, straightforward `Path(...).read_text/read_bytes/open` and read-mode `open(...)`, plus existing file arguments in argv. It reports the source and omitted input and stops a new comparison until those files are declared. It does not execute imports, crawl the environment, resolve arbitrary configuration languages, trace dynamic file access, or provide a sandbox. For a known intentional exception, `dependency_preflight: "report"` preserves the diagnostic while allowing execution; the owner still resolves comparison-relevant omissions. `declared_integrity` in status makes this boundary explicit. Add a missing helper to the contract before establishing a new baseline; do not retrofit a changed evaluator into an old comparison.

Optional contract additions, using actual inspected paths rather than these examples:

```json
{
  "protected_files": ["research/evaluator_helper.py", "configs/eval-resolved.json", "requirements.lock"],
  "dependency_preflight": "strict",
  "environment": {"variables": ["OMP_NUM_THREADS"], "packages": ["numpy"]}
}
```

`environment` is opt-in. It binds the resolved command executable, selected environment-variable hashes and selected installed package versions. Package checks require the same Python interpreter as this controller; another interpreter/container needs its real lockfile and host verification. Choose material nonsecret variables, not credentials. An omitted environment field keeps the old contract behavior. These checks identify declared conditions; they do not prove that all training behavior or remote resources are unchanged.

### Share A Campaign Allowance Across Contracts

For concurrent branches or a campaign spanning corrected protocols, create one project-local budget record once and reference it from every participating contract:

```text
python <orchestrator>/scripts/research_loop.py campaign-init --project . --record ccfa-workfiles/experiments/retrieval-campaign/source/campaign-budget.json --id retrieval-campaign --max-attempts 8 --max-seconds 600
```

```json
{"campaign": {"id": "retrieval-campaign", "record": "ccfa-workfiles/experiments/retrieval-campaign/source/campaign-budget.json"}}
```

The record's OS lock serializes reservation and settlement. Every reserved run consumes one shared attempt slot and reserves foreground-command seconds before execution. A branch, new workdir or corrected contract keeps the same allowance; it does not create a fresh campaign budget. Completed execution settles measured elapsed seconds, including failed commands. A preparation failure after reservation keeps its attempt slot and settles zero execution seconds. Model tokens remain unknown; the helper does not invent usage for owner/subagent reasoning or measure preparation time. Keep those costs against the user's broader allowance through actual host receipts when available. This optional record is not created for ordinary single-contract work.

Initialization checks the destination before shared registration and commits its local snapshot and event first. If interrupted after that event but before shared registration/cache completion, inspect `status` and use the initialized record; the next `run` completes its idempotent registration before reserving or starting a command. Failed input checks or snapshot creation do not register task content. A nonempty destination is never reinitialized.

Normal `recover` also settles its attached shared reservation. If the controller died between reservation and recording a run, no subprocess is replayed: after checking all workers, use `recover-reservation --workdir <branch-dir> --id <run-id> --confirm-stopped --reason "<checks performed>"`. Unknown duration closes the remaining campaign execution allowance; a durable known settlement is preserved. Managed inputs and partial evidence remain intact. Reconcile real costs before authorizing another campaign; do not delete/reinitialize the old record to reset usage.

### Bind Development, Selection And Final Tasks

Evaluation stages are opt-in contract fields. A selection contract may add:

```json
{"evaluation": {"split_role": "selection", "task_set_id": "retrieval-selection-v1", "task_files": ["data/selection-index.json"]}}
```

`task_files` must name declared immutable input files and defaults to `data_files`. Use the actual small split/index or fixed dataset-version manifest that the project uses to select its tasks; public corpora and model assets can remain shared. File-content identity is recorded, so changing a display name or copying identical task bytes under another filename does not make a new held-out set. This distinguishes declared task identities; it does not prove semantic non-overlap or protect mutable remote data behind an unenforced manifest.

After selection, prepare an independently inspected final command and final split, and reference the selected record's `best.candidate_id`:

```json
{
  "evaluation": {
    "split_role": "final",
    "task_set_id": "retrieval-final-v1",
    "task_files": ["data/final-index.json"],
    "frozen_candidate": {"workdir": "ccfa-workfiles/experiments/retrieval-selection", "candidate_id": "<selected candidate ID>"}
  }
}
```

The final contract's declared task content must differ from the selection tasks, and its managed bytes must match that retained candidate. A successful final run is `reported`, has no eligible promotion, and closes that record to further runs. Repeated measurements needed by the frozen final protocol belong inside its evaluator; do not decide keep/discard or adaptively replicate on final scores. Failed execution can be repaired only while preserving the frozen candidate and protocol. Development/selection stages retain ordinary bounded comparison behavior.

```text
python <orchestrator>/scripts/research_loop.py init --project . --workdir ccfa-workfiles/experiments/retrieval-final --contract <inspected-final-contract.json>
python <orchestrator>/scripts/research_loop.py run --workdir ccfa-workfiles/experiments/retrieval-final --id final-report
python <orchestrator>/scripts/research_loop.py status --workdir ccfa-workfiles/experiments/retrieval-final --fast
python <orchestrator>/scripts/research_loop.py context --workdir ccfa-workfiles/experiments/retrieval-final --query final --limit 1 --fast
```

Within a shared campaign, recorded final task content cannot silently reappear as development/selection under a different label. If the user explicitly chooses to reuse it, use a new non-final `task_set_id` and add `reused_final: {"task_set_id": "retrieval-final-v1", "reason": "<actual authorization and loss of held-out status>"}`. The record marks it non-held-out. It cannot later be restored to held-out status by renaming. This local control does not isolate model context or prevent the owner from seeing a result; the owner must avoid feeding final observations into policy tuning or run a genuinely new final set.

The first final reservation also binds its task-content hash, frozen candidate and declared evaluator/environment protocol under that campaign's lock. A completed final use cannot run again through another directory or task-set label; report the existing result. A failed command may retry only the unchanged frozen candidate/protocol within the remaining allowance. Predefined repeated samples stay inside that evaluator. Unknown execution keeps use closed until its records are reconciled. `campaign_budget.final_task_uses` shows these bindings and statuses. Legacy campaign records containing final task identities but no final-use history are marked `legacy_unknown`; inspect their prior runs and use genuinely new final tasks or explicit non-final reuse rather than treating missing history as unused tests. Contracts without a shared campaign retain their single-record final limit.

Run from the research project root, replacing `<orchestrator>` with the resolved skill directory and `<approved-contract.json>` with the prepared contract path. Reuse an established work directory; the path below is an example.

```text
python <orchestrator>/scripts/research_loop.py init --project . --workdir ccfa-workfiles/experiments/retrieval-allocation --contract <approved-contract.json>
python <orchestrator>/scripts/research_loop.py status --workdir ccfa-workfiles/experiments/retrieval-allocation
python <orchestrator>/scripts/research_loop.py run --workdir ccfa-workfiles/experiments/retrieval-allocation --id baseline
```

After inspecting the successful baseline, the host edits only the permitted candidate surface for a specific hypothesis, then executes:

```text
python <orchestrator>/scripts/research_loop.py run --workdir ccfa-workfiles/experiments/retrieval-allocation --id uncertainty-allocation --hypothesis "Retrieval allocated to uncertain queries improves accuracy at the same total budget"
```

Read the actual result and relevant logs before deciding. The frozen independent evaluator must generate the measurement; candidate code reporting its own score is not trustworthy scientific evaluation. The metric must be a finite JSON number. By default, `keep` requires improvement strictly beyond `min_delta`. Optional frozen `metric_guards` enforce measured quality/resource bounds, and `tie_breaker` allows lower cost or another secondary improvement within an explicit primary-quality tolerance. The owner still checks scientific meaning and constraints not encoded in measurements; never alter the contract to admit a favored candidate. Record the actual basis:

```text
python <orchestrator>/scripts/research_loop.py decide --workdir ccfa-workfiles/experiments/retrieval-allocation --id uncertainty-allocation --action keep --reason "<observed comparison and verified constraints>"
```

For example, add `"metric_guards": [{"name": "balanced_accuracy", "min": 0.8}]` only when that bound belongs to the agreed protocol. A favorable scalar with accuracy below the floor cannot replace the baseline. Add `"tie_breaker": {"name": "latency_ms", "direction": "min", "min_delta": 0.0, "max_primary_loss": 0.0}` to admit lower latency at equal primary quality. All declared metrics must come from the same independent evaluator output. The primary-loss allowance is anchored to the best accepted primary value within this frozen comparison, preventing cumulative small regressions; shared budget accounting does not make results from different protocols comparable. These numbers are examples, not scientific defaults. A guard-violating candidate remains a valid measured negative result when its execution and measurements were valid; an inadmissible initial baseline cannot establish the comparison.

Use `--action discard` with the actual reason when a candidate should not replace the retained baseline. Its snapshot and observations remain available for scientific interpretation or later exploration. A successful candidate awaits this decision before another run. Failure handling and discard restore only the helper-managed candidate files; they do not authorize repository-wide reset/clean or overwriting intervening edits. Branching is a new host-chosen hypothesis and unique run ID under the remaining allowance, not an automatic tree search. The recorded `parent` is the comparison baseline, not code ancestry; when developing an older snapshot, cite its attempt ID in `hypothesis` or the decision reason.

Ordinary `run` still rejects a candidate identical to its current best. To repeat a valid measured candidate, including the baseline/incumbent, use an explicit reason and source attempt ID or `best`:

```text
python <orchestrator>/scripts/research_loop.py replicate --workdir ccfa-workfiles/experiments/retrieval-allocation --id baseline-repeat --of best --reason "<why another measurement resolves the current uncertainty>"
```

Replication requires the source candidate's identical managed bytes, records its measurement parent and original candidate identity, and consumes the same local/shared allowance. It retains the fresh raw measurement as `reported`; it cannot be promoted by `decide` even if one sample is higher. When measuring an older candidate, restore only its intended managed inputs through the authorized engineering workflow before the call; a completed replication restores the retained incumbent without overwriting intervening edits. Means, variance and seeds remain the protocol's responsibility. Necessary repeated seeds can instead be part of one frozen evaluator command; include their full compute/time in that command's allowance. No repetitions are added by default.

Other previously evaluated candidates may still be run as ordinary candidates when their bytes differ from the current best; `previous_evaluations` points to prior evidence. Inspect those observations and explain why the next attempt is informative. Do not change irrelevant bytes to bypass the ordinary unchanged-candidate check. Invalid execution is not a negative result; retry after a relevant repair or justified transient failure. A failed initial baseline can be retried under the unchanged initial snapshot rules; a protocol correction starts a new comparison within the same campaign allowance.

The helper keeps one frozen `contract.json`, an authoritative append-only `events.jsonl`, and a compact `state.json` cache inside the run directory. `initial/snapshot/` and `attempts/<id>/` contain managed snapshots and necessary execution evidence such as `stdout.log`, `stderr.log`, and `metrics.json`. These are task-local experimental records, not per-agent copies or a second generic continuity ledger. Do not edit the event history to improve a result. `status` exposes compact current state and pointers to raw evidence; read the latter when interpreting a result. The retained baseline's raw metric evidence must remain intact before another comparison or promotion. Recent decisions include valid discarded results as well as execution failures; older observations remain in the event history and attempt directories. Inspect relevant prior conditions before reviving a branch instead of treating absence from the compact recent list as an untested idea.

Reusing an existing run ID returns its recorded outcome rather than rerunning it. After interruption, first inspect `status` and actual processes/artifacts. The host must confirm that the interrupted command and any residual workers have stopped before reconciling its unfinished record:

```text
python <orchestrator>/scripts/research_loop.py recover --workdir ccfa-workfiles/experiments/retrieval-allocation --id uncertainty-allocation --confirm-stopped --reason "<how process termination and artifacts were checked>"
```

`recover` reconciles an unfinished transaction without repeating the command or automatically promoting it. For a record still marked `running`, a residual process may have outlived its reserved timeout: actual elapsed time is marked unknown and the helper closes the remaining execution budget for this experiment. That budget charge is not a measured duration. Further execution needs the host to reconcile residual processes and actual costs, then establish a new contract within the user's remaining campaign allowance; a new directory does not reset that allowance. If `run_finished` was already recorded and status is `evaluated`, recovery retains the known outcome, metrics, and charged duration while discarding an unfinished ordinary candidate. A valid final/replication measurement instead completes its report after checking its original raw metrics; a final report also closes the final-use record. Recovery does not charge the same run again or label a completed measurement as a runtime failure. A `rollback_conflict` requires reconciling the affected managed files and retrying discard. `status` identifies the applicable next action. Recovery is not a resume daemon, and a new session must explicitly inspect state and choose the next authorized action.

### Reusable Findings And Targeted Recall

```text
python <orchestrator>/scripts/research_loop.py note --workdir <campaign-dir> --id <completed-attempt> --category negative_result --finding "<actual interpretation>" --next-action "<discriminating next step>" --evidence attempts/<completed-attempt>/metrics.json
python <orchestrator>/scripts/research_loop.py context --workdir <campaign-dir> --query "<mechanism or finding>" --limit 3
```

Categories separate `environment_error`, `implementation_error`, `invalid_comparison`, `negative_result`, `supports_prediction`, and `inconclusive`. A failed execution cannot be annotated as a scientific result. Findings append to the existing event history, retain original measurements and budget use, and reference actual task files. Revising a finding preserves its earlier event. Context retrieval reports changed or missing evidence instead of silently treating it as current; all summary and retrieval fields use the returned `event_seq` snapshot.

An invalidation persists through ordinary later notes. If reinspection shows that the interpretation itself was mistaken, use `note --corrects <invalidated_by-event>` with the applicable evidence and a finding explaining the correction. This records an explicit host judgment, not an automated scientific verification. A real measurement or protocol defect requires a corrected comparison; a positive label cannot repair it. Every historical accepted result used as a quality anchor must retain its original valid evidence.

## Recovery And Delivery

Repeating a recorded `run` or `keep` request does not repeat execution or promotion. Before returning a successful recorded evaluation for reuse, the helper rechecks the frozen inputs and that evaluation's original metrics and invalidation state, including an older accepted result. Changed evidence requires reconciliation; an old ID is not a fresh validation receipt.

After lost context, a tool interruption, or a session change, recover the current contract from the latest instruction and actual artifacts. Inspect command status, output files and receipts before repeating work. Preserve completed comparable experiments and check the first unresolved dependency. A result whose execution outcome is unknown must not be silently marked failed, rerun, or promoted.

Use the host's real job status/cancellation facilities where available; a local state file is not a running process. Do not claim that work continued in the background or resumed automatically when no such job exists. Restart only the affected step after reconciling side effects and remaining budget. Restore discovery or execution as appropriate instead of remaining indefinitely in a cautious recovery mode.

Update current plans and reports in place. Retain source versions, measurements and logs needed to interpret or reproduce selected and decision-changing failed experiments, using the established task directory. Remove only verified disposable build products owned by this task; do not overwrite evidence merely to keep one attractive result. Return canonical paths, the outcome, the evidence-supported choice, actual execution limits/costs, and any precise remaining decision. Additional process detail follows `detailed_reports`; necessary evidence does not.
