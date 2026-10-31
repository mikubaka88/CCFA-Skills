# Training And Validation

Use the relevant sections for baseline reproduction, training correctness, performance, or run delivery. Reuse Common's evidence rules and the designer's comparison protocol. The primary-source inventory is Common's `references/source-registry.yaml`; this reference supplies engineering decisions, not a universal training recipe.

## Establish The Necessary Baseline

A comparative improvement needs an applicable baseline, not necessarily a fresh full training run. Reuse prior evidence only when code/configuration, data/split, evaluator, and material environment assumptions still support the current comparison. Inspect its actual outputs and provenance. A paper's published number can be a disclosed reference under its protocol; it is not a run performed here.

When evidence is missing or stale, choose the verification needed by the task:

- Checkpoint evaluation can establish inference/evaluation behavior when training reproduction is not the question.
- An original training recipe can establish the training baseline; retain preprocessing, initialization, optimizer/schedule, effective batch, steps or data exposure, and checkpoint-selection rule that affect its meaning.
- A short run or reduced configuration can diagnose execution, learning signals, memory, or a specific controlled hypothesis. Identify the changed scale and what it can establish; do not report its metric as the unexecuted full-method baseline.
- Full retraining or repeated seeds are needed when the requested claim or unresolved variance depends on them. Reuse valid evidence for a local code repair and avoid imposing this cost automatically.

For the local sequential helper, `replicate --of <measured-attempt-id|best> --reason <specific-purpose>` can repeat identical baseline/incumbent or earlier candidate bytes under the existing budget. It saves a fresh raw measurement and its source identity, restores the retained incumbent after an older-candidate repeat, and never promotes from a single favorable sample. The protocol still owns seeds, aggregation and interpretation; a frozen multi-seed evaluator is another valid route. Ordinary `run` keeps its unchanged-candidate guard, so do not edit irrelevant bytes just to obtain a repeat.

Agree with the designer on the relevant result-matching tolerance or comparison criterion before interpreting improvement. If reference results disagree, inspect data processing, evaluator, configuration, initialization and checkpoints before changing the target metric or tuning only the candidate. Preserve valid discrepancies and failed runs. A baseline gap does not prevent independent mechanism implementation, but remains a dependency for the comparison it supports.

## Choose And Diagnose The Training Configuration

Start from the working recipe closest to the actual model/task, preserving its scientific requirements. Resolve optimizer and parameter groups, learning-rate schedule, warmup, regularization, precision, clipping, effective batch, gradient accumulation, steps/data exposure, evaluation cadence, and checkpoint/resume behavior only where relevant. Avoid silently trading model fidelity, sequence length, resolution, supervision, or training stages for convenience.

Use observed symptoms to choose a targeted diagnostic. Examples below are conditional; they are not a checklist for every run:

| Observation or changed path | Useful next check |
| --- | --- |
| A new module has no effect | Trace its activation from the real entry point; inspect loss contribution, parameter registration, gradients, optimizer membership and update. |
| Loss or gradients become non-finite | Locate the first affected batch/operation; inspect data/masks/reductions, precision, scale, learning rate and clipping before changing unrelated modules. |
| Training does not learn | Check labels, sampling, loss normalization and updates; a tiny-subset fit or controlled reference can distinguish plumbing errors from a poor mechanism. Some stochastic or constrained objectives need a different diagnostic than perfect overfitting. |
| Train/eval or checkpoint behavior disagrees | Inspect preprocessing, mode switches, state/weight loading, RNG, and evaluator configuration; test the changed state transition. |
| Restart differs materially from continuation | Check model, optimizer, scheduler, scaler, random state, data position and distributed state as relevant; resuming weights alone is not resuming the full training process. |
| Multi-device results differ unexpectedly | Compare the relevant reference path under controlled inputs; inspect reductions, effective batch, normalization, RNG and sharding/communication semantics. |

Use the smallest diagnostic that can resolve the observed uncertainty while preserving its relevant mechanism. Keep diagnostics separate from publication comparisons. Retest the affected real path after a fix. Repeating the same unsuccessful run needs changed evidence, a justified transient-failure retry, or a concrete repair.

## Profile Before Choosing Performance Changes

Profile when the requested goal concerns efficiency, a run is costly enough that measurement can change the resource decision, or symptoms suggest memory/throughput problems. A short inexpensive correctness fix does not need a profiling campaign. Use available tools on representative inputs and the relevant model/training path, with warmup/compilation separated from steady-state measurement. Report hardware, shapes, precision, batch/accumulation, device count, and timing scope needed to interpret the comparison.

Measure the bottleneck that matters: step time or examples/tokens per second, data wait, CPU/device overlap, peak allocated/reserved memory, optimizer/state memory, and communication where applicable. Use a trace or memory snapshot when aggregate utilization cannot distinguish the cause. A utilization percentage alone does not show which optimization will help. GPU timing requires correct synchronization or device events; include compilation, preprocessing, checkpointing and evaluation costs when they affect total task cost.

| Measured cause | Candidate response and relevant tradeoff |
| --- | --- |
| Data loading or host-device transfer dominates | Inspect preprocessing, sampling, caching, worker configuration, batching and transfer overlap; preserve data semantics and ordering where required. |
| Compute-bound operators or Python/launch overhead | Consider supported kernels, vectorization, compilation or fusion on the affected region; check numerical behavior and amortization of startup cost. |
| Memory capacity or fragmentation | Identify parameters, optimizer state, activations, temporary buffers or allocator behavior; consider precision, microbatching, recomputation or sharding as appropriate. A smaller scientific model is a separate configuration decision. |
| Communication or synchronization dominates | Inspect topology, collective timing, partitioning and overlap; choose parallelism from workload/device constraints rather than enabling every available strategy. |
| Low throughput despite larger batches | Check the actual limiting stage and useful scaling range. Gradient accumulation changes effective updates and memory use; it does not inherently increase throughput. |

Compare the change against the relevant baseline on equivalent inputs and a stated timing scope, then recheck affected loss/gradient/convergence behavior. Effective-batch changes may require retuning learning rate, schedule or regularization and revisiting the comparison budget. A short numerical check can validate a kernel replacement locally; it cannot establish unchanged final convergence when that remains in question. Make quality/cost tradeoffs explicit and return protocol changes to the designer.

## Execute And Deliver Within The Actual Resources

Inspect the real command, working directory, environment, data access, output paths and execution allowance before launching. Reuse a supplied budget; when a material allowance or required resource is missing, continue independent code/protocol work and identify that dependency. Do not invent unlimited retries or estimate GPU-hours from wall time without known device allocation. Track measured and estimated consumption separately, including failed runs and required verification.

Use existing host job controls for remote or distributed work. Verify launch, completion, cancellation and residual workers through actual status and artifacts. A checkpoint file alone does not prove that training resumed, and a terminal disconnect does not prove that a job stopped. Check completed work before retrying after interruption. Never roll back source files under a live worker or reset unrelated repository changes.

For a bounded local foreground comparison, the orchestrator's [sequential helper](../../ccf-pipeline-orchestrator/references/autonomous-research.md#sequential-experiment-helper) can manage its declared files and evidence. It supports a primary metric, optional measured guards and a bounded secondary tie-breaker, together with direct-command timing and snapshot recovery. Broader scientific selection, GPU billing, environment isolation and training-state recovery remain with the owner and a suitable host workflow; do not force a real training project into a toy runner example.

For multiple contracts/branches, attach the same optional campaign ID and budget record; reserve before launch and settle the actual foreground duration. A new directory or corrected protocol does not renew the campaign allowance. Use `status/context --fast` only for reading the last known state; execution, promotion and recovery still check declared inputs. Opt-in `evaluation` stages bind actual task/split manifests: a final stage runs a frozen selection candidate once for reporting, with no keep/discard or tuning from its score. Shared corpora may remain common while the actual selection and final split indices differ. Task-file hashes establish declared identity, not semantic disjointness or an execution sandbox.

Retain the code/revision, resolved configuration, relevant environment/data identity, commands, logs, measurements, selected checkpoint and restart information needed to reproduce or continue the requested result. Preserve baseline and decision-changing failed evidence in the existing run directory; do not copy entire datasets or make a second per-skill ledger. Validate from a clean or independently reconstructed environment when reproducible delivery is requested and resources permit; disclose what was actually reconstructed and executed.

Report separately what was implemented, what ran, what matched its baseline/target, and what scientific conclusion the evidence supports. For a training diagnosis, the completed result may be a localized cause and verified repair. For requested full reproduction, code presence and a successful smoke run remain partial progress.
