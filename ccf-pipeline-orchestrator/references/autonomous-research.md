# Autonomous Research

Use this mode when the user explicitly asks to carry scientific work through iterative hypothesis development, experiments, observed feedback, and further improvement, including `autonomous research`, `autoresearch`, or `自主科研迭代`. A request to explain such a workflow, review an idea, or give a plan does not start execution. Reuse the active Humanization -> Common preflights.

## Scope And Ownership

Coordinate the full requested research loop through its owners. The orchestrator integrates evidence, controls the run contract, and invokes actual execution tools exposed by the host. It does not replace scientific owners or stop at naming them. Loading specialist guidance does not require a separate model call or agent; use actual delegation only when it helps this task.

| Contribution | Owner and return |
| --- | --- |
| Candidate mechanism, changed assumption, or search strategy | `ccf-idea-optimizer`; return the hypothesis and a discriminating prediction. Use `ccf-idea-reviewer` for a consequential concept judgment when needed, without imposing experiment requirements on concept review. |
| Closest work, dataset/baseline provenance, or missing external evidence | `ccf-literature-searcher`; use current sources where the decision needs them and preserve source anchors. |
| Comparison protocol, execution specification, interpretation of measured feedback | `ccf-experiment-designer`; apply its `references/evidence-design.md` iteration guidance. |
| Task-owned research implementation and actual execution | Host coding/execution tools coordinated by the orchestrator, within authorized edit surfaces and resources. A specialist specification is not an executed run. |
| Material result conflicts, requested figures, or supported manuscript text | The relevant integrity, visual, or writing owner; run only the contribution needed for this deliverable. |

Within the authorized task, the agent may revise hypotheses, methods, research code, search queries, and candidate-selection strategy in response to evidence. Preserve the scientific objective and hard constraints while changing the route when warranted. A stable goal does not freeze the initial mechanism or restrict innovation to small module additions.

Persistent changes to installed/public skills, global prompts, personal preferences, or cross-project behavior require a separate authorized maintenance task. This workflow does not automatically train or upgrade the foundation model running the agent, or establish recursive capability gains. Training candidate research models is valid when the task explicitly authorizes it and actual commands, data, and resources support it. The `maintenance_evolution` one-extra-candidate limit does not govern a requested research campaign; `alternative_routes=off` does not suppress its authorized exploration. Other optional enhancements retain their existing meaning. This mode adds no global switch or automatic background work.

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
3. **Prepare.** Have the experiment designer connect the hypothesis to a sufficient comparison, expected evidence files, and execution specification. Inspect the task's research code before changing it. Protect original measurements and the comparison definition; isolate candidate changes from the usable baseline. Use a local smoke check only for a changed critical path, not as scientific evidence.
4. **Run.** Execute through an available, authorized host tool with the applicable allowance. Record actual command/configuration, source versions, output locations, and observed consumption. Starting a command is not completion; a zero exit code does not establish a valid measurement. Missing or partial outputs remain unresolved.
5. **Interpret.** Read the relevant actual evidence and check comparability. Separate infrastructure failure, invalid protocol, a valid negative result, and an inconclusive measurement. The designer explains which hypothesis each outcome supports or weakens; the optimizer can then revise the mechanism or strategy.
6. **Select.** The integrating owner chooses keep, discard, branch, repair, or stop against the current contract. Preserve a useful baseline while investigating alternatives. Promote a candidate only when its evidence supports the relevant criteria and hard constraints; distinguish keeping a promising candidate for further study from claiming the research goal has been achieved.
7. **Continue or close.** If scope and resources remain, take the next informative step. Deliver the best supported result, necessary evidence and code, observed cost, and remaining uncertainty when the stopping condition is reached. Do not stop an authorized end-to-end request after returning only a plan when execution is available.

Keep evaluation criteria stable while comparing candidates. A corrected evaluator or an explicit user goal change can justify a new comparison contract; record the reason and rerun affected comparisons. Scores from different conditions are not a single improvement sequence. An unfavorable result alone is not a reason to change the metric or hide a failed candidate. New candidate IDs, branches, records, or protocol versions do not reset the user's campaign allowance.

## Escape Unproductive Loops

Apply Common's progress test across all contributors: each continuation should add a relevant observation, test a distinct prediction, resolve an execution defect, or change a justified assumption. Repeated critique, rephrased hypotheses, and owner changes are not progress.

When a branch repeats the same failure without new information, stop that branch. If the goal and remaining allowance support it, compare a different mechanism or take the smallest observation that can change the decision. A scientifically uninformative search direction may be replaced within the task without changing the user's goal. Do not keep a poor route because work has already been spent on it, and do not replace an ambitious goal with an easier claim merely to finish.

Stop the campaign when its requested result and applicable checks are complete, its allowance is exhausted, a required decision/input blocks further meaningful execution, or no informative next step remains within scope. Preserve and deliver supported independent work. Budget exhaustion is not scientific success. A negative result can be the result of a completed investigation; an unresolved claim must remain unresolved. Continuing beyond the approved allowance requires the missing scope/resource decision, not another renamed iteration.

## Context And Parallel Contributions

Keep active context compact: current goal/contract, best supported and current candidate, recent failure conditions that affect the next decision, and the next action. Use stable pointers to raw evidence, code, and older observations and read only the relevant portions. Preserve material quantities, units, conditions, negation, and unknowns when summarizing. Never treat a summary as fresh experimental evidence.

Delegate independent candidate development or source checks only when the host provides real agents and the benefit warrants the coordination cost. Give candidate generators the same goal and constraints while keeping other candidates' preferred answers out of their first pass. Do not copy the full search history or run one agent per skill by default. Parallelism is limited by actual host resources and the shared run allowance; necessary work may queue rather than disappear.

Keep one integrating owner for evaluation and promotion. Serialize writes to shared artifacts. Carry the goal revision, candidate/input versions, write boundary, evidence anchors, remaining allowance, and completion condition when these affect the contribution. Reuse known inputs and send changes on later handoffs. Verify delayed results against the current goal and source versions; integrate valid portions and reject or refresh only stale dependencies. Parallel candidate execution requires isolated outputs and resource accounting that the actual host supports; a sequential helper does not supply those capabilities.

## Sequential Experiment Helper

Use [research_loop.py](../scripts/research_loop.py) when the task has a local, independently evaluated foreground command that waits for all its workers and needs bounded execution, managed-file rollback, and recoverable records. Commands that detach background workers are unsupported. The standard-library helper does not generate hypotheses, edit candidate code, search branches, judge novelty, or call a model. The host performs those steps. It also does not provide an OS sandbox: its file checks detect changes, while command permissions, network/GPU access, environment, and side effects remain the host's responsibility.

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

The three budget values are illustrative, not defaults or recommended research scale. `max_attempts` covers the campaign's baseline and failed attempts. `max_seconds` budgets cumulative elapsed time of direct foreground commands, including startup, and `timeout_seconds` sets one run's timeout, capped by the remaining execution allowance. This is not total process-tree CPU usage and excludes model tokens, host planning time, and other external charges; track these against the broader user allowance separately. Timeout termination is best effort and cannot guarantee that orphan processes have stopped or undo external side effects. `scientific_value` and `constraints` record the host's scientific contract; the script cannot judge their fulfillment from text.

Declared evaluator/data files are hashed before and after execution. Large datasets can make these checks expensive, and their time is outside the command timer. Prefer this helper for manageable local inputs; a separately verified immutable dataset version may use a manifest only when the host actually enforces that version. Hashing a manifest alone does not protect mutable data behind it.

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

Read the actual result and relevant logs before deciding. The frozen independent evaluator must generate the measurement; candidate code reporting its own score is not trustworthy scientific evaluation. The metric must be a finite JSON number. The helper requires a strictly better metric by more than `min_delta` for `keep`; the owner must additionally check scientific meaning, comparison validity, and hard constraints. Record the actual basis, without inventing a successful comparison to fill the command:

```text
python <orchestrator>/scripts/research_loop.py decide --workdir ccfa-workfiles/experiments/retrieval-allocation --id uncertainty-allocation --action keep --reason "<observed comparison and verified constraints>"
```

Use `--action discard` with the actual reason when a candidate should not replace the retained baseline. A successful candidate awaits this decision before another run. Failure handling and discard restore only the helper-managed candidate files; they do not authorize repository-wide reset/clean or overwriting intervening edits. Branching is a new host-chosen hypothesis and unique run ID under the remaining allowance, not an automatic tree search. A failed initial baseline can be retried with a new ID only under the helper's unchanged initial snapshot rules; a protocol/evaluator correction needs an explicit new comparison, without resetting the user's campaign budget.

The helper keeps one frozen `contract.json`, an authoritative append-only `events.jsonl`, and a compact `state.json` cache inside the run directory. `initial/snapshot/` and `attempts/<id>/` contain managed snapshots and necessary execution evidence such as `stdout.log`, `stderr.log`, and `metrics.json`. These are task-local experimental records, not per-agent copies or a second generic continuity ledger. Do not edit the event history to improve a result. `status` exposes compact current state and pointers to raw evidence; read the latter when interpreting a result.

Reusing an existing run ID returns its recorded outcome rather than rerunning it. After interruption, first inspect `status` and actual processes/artifacts. The host must confirm that the interrupted command and any residual workers have stopped before reconciling its unfinished record:

```text
python <orchestrator>/scripts/research_loop.py recover --workdir ccfa-workfiles/experiments/retrieval-allocation --id uncertainty-allocation --confirm-stopped --reason "<how process termination and artifacts were checked>"
```

`recover` records interruption without repeating the command. Because a residual process may have outlived its reserved timeout, actual elapsed time is marked unknown and the helper closes the remaining execution budget for this experiment; that budget charge is not a measured duration. Further execution needs the host to reconcile residual processes and actual costs, then establish a new contract within the user's remaining campaign allowance. A new directory does not reset that allowance. Recovery is not a resume daemon, and a new session must explicitly inspect state and choose the next authorized action.

## Recovery And Delivery

After lost context, a tool interruption, or a session change, recover the current contract from the latest instruction and actual artifacts. Inspect command status, output files and receipts before repeating work. Preserve completed comparable experiments and check the first unresolved dependency. A result whose execution outcome is unknown must not be silently marked failed, rerun, or promoted.

Use the host's real job status/cancellation facilities where available; a local state file is not a running process. Do not claim that work continued in the background or resumed automatically when no such job exists. Restart only the affected step after reconciling side effects and remaining budget. Restore discovery or execution as appropriate instead of remaining indefinitely in a cautious recovery mode.

Update current plans and reports in place. Retain source versions, measurements and logs needed to interpret or reproduce selected and decision-changing failed experiments, using the established task directory. Remove only verified disposable build products owned by this task; do not overwrite evidence merely to keep one attractive result. Return canonical paths, the outcome, the evidence-supported choice, actual execution limits/costs, and any precise remaining decision. Additional process detail follows `detailed_reports`; necessary evidence does not.
