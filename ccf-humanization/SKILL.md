---
name: ccf-humanization
description: "Humanize and de-defend publication-facing CCF/AI prose and artifacts as a sidecar preflight, never as the primary task owner. Use before manuscript drafting/revision and before final manuscript experiment text, tables, captions, or method descriptions when Codex must remove defensive writing, boilerplate disclaimers, repetitive improbable edge cases, unnecessary safeguards, generic SHA-256/checksum requirements, duplicated smoke tests, simplified/toy methods, or AI-like risk narration. Do not auto-load as the sole owner for raw experiment planning, retrieval, review, auditing, routing, visual rendering, or assessment-only tasks without publication prose. Keep necessary concerns in a separate user-review warning instead of silently injecting them into files. Do not conceal material evidence, fabricate results, or override venue-mandated disclosures."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Humanization

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, and `../ccf-common/references/task-modes.md`.

Apply this skill before manuscript-facing work by `ccf-paper-writer` and before publication-facing experiment work by `ccf-experiment-designer`. It is the highest-priority preflight as a sidecar quality layer, not a substitute for either owner. Respect the user's requested format and do not broaden the research scope.

## Core Rule

Produce direct academic content, not prose that argues with hypothetical reviewers. Remove defensive framing, generic disclaimers, repeated low-probability cases, ritual safeguards, and process narration that do not change the scientific claim or evidence. Keep a concern outside the artifact as a user-review warning when it needs judgment. Do not edit a source file merely to encode a warning.

Humanization must never dilute academic rigor. Preserve technical precision, evidence boundaries, causal and comparative logic, reproducibility-relevant details, calibrated claims, terminology, equations, citations, and venue-required disclosures. Improve the prose by making the scientific argument clearer and more natural, not by making it vaguer, more promotional, or less complete.

Keep method confirmation and version-gate status internal. A method must pass the confirmed-full-method gate before publication use, but manuscript prose must not say that a method, baseline, configuration, or checkpoint is "confirmed," "approved," "publication-ready," or otherwise cleared by an engineering process. State the actual method name, scientifically relevant structure, configuration, data, and protocol directly and naturally. For example, write `We evaluate Transformer Base on English-to-German translation`, not `We use the confirmed Transformer Base configuration`.

Never hide an observed result, known failure, assumption, conflict of interest, ethical issue, reproducibility fact, or venue-required disclosure when omission would make the paper materially misleading. Flag it as a blocking warning and wait for the user's decision; do not silently insert it or help conceal it.

## Modes

- `manuscript-humanization`: remove defensive or AI-like prose while preserving claims, evidence, terminology, citations, equations, and user format.
- `experiment-humanization`: deduplicate smoke tests, remove hypothetical test sprawl, and prevent simplified development variants from entering publication artifacts.
- `warning-only`: return a separate review warning without modifying manuscript, experiment, code, table, or configuration files.

## Workflow

1. Identify the target artifact, owning CCFA skill, requested change, and whether edits are already authorized.
2. Classify each candidate issue as `remove`, `keep`, or `warn-only` using `references/humanization-policy.md`.
3. For manuscript prose, remove defensive positioning, boilerplate caveats, reviewer simulation, improbable case lists, and internal process/status language. Keep only content that advances problem, method, evidence, interpretation, or a required disclosure. Rewrite version-gate phrases as natural academic descriptions of the actual method and relevant configuration.
4. Apply the manuscript pattern controls in `references/humanization-policy.md`. Prefer zero em dashes in new academic prose and never exceed three in a full paper, excluding direct quotations. Remove throat-clearing openers, forced three-item structures, synonym cycling, and metronomic sentence patterns when they do not serve the science.
5. For experiment work, load `references/experiment-discipline.md`. Require each publication method to have a verified identity and full configuration in the internal gate; do not place simplified, toy, approximate, proxy, reduced, or debug variants in manuscript text, final tables, or claimed comparisons, and do not expose the gate status in manuscript wording.
6. Minimize smoke testing to changed, executable, decision-relevant paths. Do not repeat equivalent smoke tests or treat smoke success as publication evidence.
7. Do not introduce SHA-256/checksum boilerplate for generic provenance, version confirmation, deduplication, or paper-writing workflow. Preserve it only when cryptographic hashing is the research subject, a real implementation dependency, or an external system requirement; surface that exception as a warning when it conflicts with the user's preference.
8. Put any unresolved concern in the warning format below. Do not patch files, add comments, inject disclaimers, or alter method configuration for a warning-only issue until the user explicitly approves a concrete change.
9. Return the requested artifact first, followed only by a compact warning block when one exists. Then hand back to the owning CCFA skill.

## Warning Contract

```text
CCF Humanization Warning: not inserted into artifacts
Issue:
Why user review is required:
Affected claim / file / experiment:
Materiality: advisory / blocking
Recommended decision:
File changes made for this warning: none
```

Use `blocking` only when omission or substitution would materially misstate the method, evidence, reproducibility, ethics, or venue compliance. Otherwise keep the warning advisory and concise.

## Output Contract

```text
Mode:
Artifact returned:
Defensive content removed:
Smoke tests retained / removed:
Publication method version status:
Warnings not inserted into artifacts:
Next CCFA owner:
```

Return only fields that help the user verify the task; do not turn a normal edit into a process report.

## References

- `references/humanization-policy.md`: read for manuscript humanization, consolidated writing constraints, warning classification, non-injection rules, unfavorable information, and SHA-256/checksum handling.
- `references/experiment-discipline.md`: read for smoke-test scope, confirmed method identity, prohibited simplified publication variants, and experiment-to-paper gates.
