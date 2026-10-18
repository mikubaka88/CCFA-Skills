# Experiment Debugging Protocol

Read the relevant fault-family section after locating the first meaningful failure. Preserve the original run's evidence; temporary diagnostics and repairs must remain distinguishable from the reported experiment.

## Evidence And Check Selection

| Status | Required basis | Example |
| --- | --- | --- |
| Confirmed | Evidence distinguishes the claimed cause from plausible alternatives under stated conditions. | The traceback and inspected tensor shapes show an incompatible matrix multiplication. |
| Likely | Fits available observations; an alternative remains untested. | A CUDA extension fails to load after a PyTorch upgrade; the build/runtime mismatch still needs inspection. |
| Possible | Plausible but lacks a discriminating observation. | A loader stall could involve worker startup; a single-worker reproduction has not run. |
| Ruled out | A relevant check contradicts the explanation for the tested conditions. | The same interpreter imports the package successfully, ruling out package absence there, not in another worker environment. |

`CUDA out of memory` confirms an allocation failure at that point, not a memory leak. `ModuleNotFoundError` confirms failed module resolution in that process, not that installation is the sole remedy. Keep the observed error and the causal hypothesis separate.

Prefer high-information, low-cost checks: inspect the failing line and active interpreter, test one batch/process/device, then change one variable. For every suggested command, state the expected observation and decision branch. Retain raw output locally when useful; redact credentials, private dataset paths, hostnames, and identifying details before sharing. Do not paste private logs into external searches.

## Python And Dependency Installation

- Check interpreter identity (`python -c "import sys; print(sys.executable); print(sys.version)"`) and the matching installer (`python -m pip --version`). Different environment paths support an interpreter/installer mismatch; matching paths require checking import names, module shadowing, and the traceback next.
- For missing imports, inspect the named module, its distribution name, project-local files, and package metadata. An import name need not equal its installation name. Check whether a local file shadows a dependency before reinstalling.
- For installation failures, isolate the first resolver/build/network error. Distinguish incompatible requirements, missing wheels for the Python/platform combination, failed compiler/build prerequisites, and index/network access. `python -m pip check` tests declared installed requirements; success does not prove ABI compatibility or importability.
- Prefer the project's lockfile or documented compatible versions. Inspect the environment before proposing pins. Do not invent a version combination or treat the latest release as universally compatible. When needed, verify the relevant official compatibility documentation for the exact versions/platform.

## PyTorch And CUDA

- Read `torch.__version__`, `torch.version.cuda`, `torch.cuda.is_available()`, the selected device and GPU model when torch imports. Inspect import failure first if it does not. Check `nvidia-smi` separately if available; its absence alone does not prove there is no GPU.
- Distinguish the installed driver, PyTorch's built CUDA runtime, and a local toolkit used to compile extensions. The CUDA version displayed by `nvidia-smi` is driver capability, not necessarily the toolkit or runtime in use. Do not demand all displayed versions match or recommend reinstalling a system toolkit from that difference alone.
- For extension/ABI errors, inspect the complete missing-symbol/load message, torch/Python/platform versions, and extension build provenance. Rebuild or select a documented compatible binary in the affected environment; verify import and the failing operation separately.
- For asynchronous device errors, use a fresh minimal process with launch blocking set before startup, scoped to that diagnostic command. For example, POSIX shells support `CUDA_LAUNCH_BLOCKING=1 python repro.py`; adapt for other shells and restore any changed session environment afterward. It can locate the failing operation but does not itself fix the bug. Inspect index ranges, shapes, dtype, and device alignment at that operation.
- For OOM, inspect tensor/batch sizes, memory allocated/reserved at the failure, and relevant process usage. Compare a short repeated-step trace before asserting accumulation or a leak. Lowering batch size or precision is a diagnostic/protocol change to record, not proof of the root cause. Cache release cannot free tensors that remain live; do not kill unrelated GPU processes.

## Data, Model, And Numerical Failures

- Check a single failing sample/batch: keys, shape, dtype, device, label range, finite values, preprocessing, and loss input contract. Trace the first operation whose inputs violate its contract. Avoid logging private samples when metadata suffices.
- For NaN/Inf, find the first nonfinite input, activation, loss, or gradient in a bounded run. Check loss scaling, divisions/log domains, learning rate, and mixed precision only as implicated by evidence. A lower learning rate or full-precision run can discriminate hypotheses; do not label either as a verified universal fix.
- For loader failures/stalls, preserve the worker traceback; test a small input with `num_workers=0` to expose the underlying error. A single-process pass narrows the issue toward worker behavior but does not prove a specific multiprocessing cause.
- For distributed hangs, retain the first meaningful error from each relevant rank and inspect launch/world-size/rank/device mapping. A later communication timeout may be a secondary symptom. Compare a one-process reproduction when feasible; do not infer network failure from a timeout alone.

## Reproduction Differences

Compare code revision/local diff, command, config, dataset version/split/preprocessing, checkpoint, evaluation mode, metric implementation, seeds, deterministic settings, library/hardware versions, and run duration. Start with fields that actually differ. A fixed seed alone does not guarantee identical outcomes across platforms or releases.

Separate exact rerun, successful execution, and matching scientific results. Check the author's protocol before interpreting a metric gap. Keep training completion, evaluation correctness, and agreement with a published number as distinct outcomes. Record a debugging change that alters batch size, gradient accumulation, optimizer steps, precision, augmentation, or preprocessing; route unresolved protocol equivalence to experiment designer.

## Reproduction Record Template

Use inline for small cases or update the established issue record for file-based work. Omit irrelevant fields and leave unavailable evidence explicitly unknown.

```text
Issue / expected behavior:
Code revision and relevant local changes:
Working directory and exact failing command:
Environment: OS, Python/interpreter, dependency versions, GPU/driver/runtime (as relevant)
Config / dataset split and version / checkpoint identity:
Seeds and deterministic settings (if relevant):
Original symptom and evidence anchors:
Confirmed causes and supporting evidence (or none confirmed):
Hypotheses: status, evidence, next discriminator
Checks: action | expected observation | branch decision | proposed/executed | actual result
Repair: change | rationale | rollback | protocol impact
Verification: exact command | exit status | observed result | coverage and limits
Before/after evidence:
Unresolved facts and next action:
```
