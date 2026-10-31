# Codebase And Implementation

Use the sections needed for code selection, method implementation, or environment repair. Source provenance for this guidance belongs in Common's `references/source-registry.yaml`; inspect current official project documentation when an API or compatibility decision depends on it.

## Inspect The Existing Project

Locate the actual repository root, current revision and user changes, training/evaluation entry points, configuration composition, dataset preprocessing, model/loss/optimizer construction, and outputs relevant to the task. Follow an actual sample or tensor through the changed path rather than inferring the whole architecture from filenames. Read the applicable project instructions and existing tests. Do not treat an untracked file or dirty tree as disposable.

Identify who writes each shared surface. Use the current checkout for compatible scoped edits; an isolated worktree or environment is useful for competing candidates or incompatible dependencies when the host supports it. Isolation is a concrete execution choice, not a reason to duplicate datasets, model weights, or the entire project into a task folder. Keep outputs distinct and serialize edits that cannot be isolated. Inspect branch/worktree state before reuse or cleanup.

## Select A Starting Point

First assess whether the supplied code can support the target mechanism and workload. When alternatives matter, compare enough actual candidates to decide; do not require a fixed count or select by stars, newest release, or brevity alone. Prefer an official or well-maintained implementation when its behavior and dependencies fit, while checking the code and configuration behind that label.

| Decision | Inspectable evidence |
| --- | --- |
| Scientific fit | Required model components, loss, supervision, preprocessing, tokenizer/feature definitions, training stages, and evaluation semantics; identify omissions that would change the method. |
| Working baseline | Relevant recipe, checkpoint and data availability, executable train/eval path, reported configuration, and available reproduction evidence. An import or demo is not a reproduced baseline. |
| Extension cost | Concrete modules/interfaces to change, registry or plugin support, configuration propagation, and coupling to training, inference, checkpointing, or distributed layout. |
| Environment and hardware fit | Supported language/framework/runtime versions, accelerator and precision requirements, custom kernels, memory needs, and whether the available environment can execute the relevant path. |
| Reuse and maintenance | License/access constraints, pinned revision or release, meaningful tests, known issues affecting this task, and the cost of carrying a fork or patch. |

Choose the route from these observations: extend the current project, adopt a better-fitting codebase, migrate a bounded component, or implement missing code. A rewrite is justified by a concrete incompatibility, unavailable suitable implementation, or the research question itself; name which mature components remain reusable and how method fidelity will be checked. Do not silently discard essential components to fit a preferred framework or resource limit. Preserve an explicitly requested small research system when it answers the user's actual question.

Keep the decision and decisive source anchors in the existing task context or requested artifact. Do not generate a ranking table or selection report unless it helps the requested decision. Missing external method/data provenance can be resolved with `ccf-literature-searcher`; code compatibility remains this skill's responsibility.

## Preserve The Environment And Execution Identity

Use the project's existing lockfile, environment specification, container recipe, or validated setup when available. Inspect installed versions and the failing import/build/runtime path before changing dependencies. Pin the chosen code revision and material dependencies for reproducible runs; retain the actual interpreter, framework/runtime, accelerator, data/split, and configuration identity relevant to the result. Record unavailable information as unavailable.

For conflicting packages, incompatible kernels, or divergent candidates, choose a project-scoped environment or container if available. Compare the proposed dependency change with the code's supported versions and test its affected path. Avoid broad upgrades, global package replacement, or editing unrelated projects to make one experiment import. Changing a framework, runtime, compiler, or kernel can change numerical behavior and invalidate prior performance evidence; recheck affected comparisons.

Inspect configuration precedence and the resolved runtime values, including overrides and environment variables. Preserve established data/checkpoint paths. Reuse immutable shared inputs where supported; separate run outputs and writable caches when they would collide. Retain meaningful dependency and configuration changes with the code, without exposing credentials or private machine details in public artifacts.

Before a local helper establishes its first comparison, map the command's actual code/configuration inputs to its contract: candidate-varying surfaces are editable; fixed evaluator helpers, preprocessing/configuration and environment lockfiles belong in `protected_files` or existing evaluator/data declarations. Resolve its literal dependency-preflight findings by adding the real omitted inputs, not by changing a displayed score or discarding a necessary module. The preflight checks straightforward local imports and literal reads; it does not establish dynamic dependency closure. For a known intentional exception, `dependency_preflight=report` keeps the diagnostic visible while the owner checks its effect. Optional selected environment identities supplement the actual lockfile/host setup, and a fast status receipt never replaces current-input checks before execution or promotion. See the orchestrator's [input and budget contracts](../../ccf-pipeline-orchestrator/references/autonomous-research.md#bind-the-inputs-actually-used).

## Map The Mechanism To Code

For a substantial method change, connect the supplied mechanism or equations to the actual implementation. Record this compactly in code comments, an existing specification, or task context; do not create another architecture document by default.

| Mapping | Resolve for the changed path |
| --- | --- |
| Objects and state | Modules, parameters/buffers, initialization, checkpoints, and train/eval state. |
| Computation | Inputs/outputs, tensor axes and shapes, masks, normalization, broadcasting, and numerical precision. |
| Learning signal | Loss terms and reductions, labels/supervision, weighting, gradient paths, detach/freeze boundaries, optimizer membership, and update timing. |
| Integration | Preprocessing, model forward, training loop, evaluation/inference, serialization, and any distributed sharding or communication contract the change affects. |
| Distinguishing behavior | What observation would show the mechanism is actually active, and what reference, invariant, or controlled intervention checks it. |

Prefer established extension points, component substitution, and explicit configuration deltas over copying an entire model/trainer. Carry untouched configuration fields through a replacement; a hand-copied constructor can silently reset method details. Detect overlapping overrides or duplicate registrations, and make activation observable through resolved configuration or existing logs. Use deeper structural changes when the mechanism requires them, preserving the relevant surrounding contracts.

Check the path the real entry point uses, not an isolated class that training never instantiates. A feature flag must reach the computation; an added parameter must receive its intended gradient and optimizer update. Verify meaningful changes with a reference computation, limiting case, numerical comparison, or a targeted training step as appropriate. Do not add tests that only repeat the implementation or run an unrelated full suite to validate a local change.

Treat architecture or training optimizations as hypotheses about a measured constraint. Kernel fusion, precision, batching, checkpointing, or parallelization may affect numerics, RNG, normalization, or effective updates; verify those effects where material. Changes to the scientific mechanism or comparison conditions return to the optimizer/designer rather than being hidden as implementation details.
