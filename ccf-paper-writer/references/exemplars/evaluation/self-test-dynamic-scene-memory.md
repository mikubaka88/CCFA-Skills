# Self-Test: Dynamic Scene Memory Transformer

Purpose: test whether the exemplar cards help plan, draft, review, and revise a simple CCF A-style paper idea without copying exemplar prose.

Target paper idea: Dynamic Scene Memory Transformer for 4D embodied navigation. The hypothetical method stores object-centric spatiotemporal memories from multi-view egocentric video and uses them for long-horizon navigation queries.

Target venue family: ICLR/CVPR-style AI and vision.

Loaded references:

- `references/exemplars/index.md`
- `references/exemplars/cards/llava-4d.md`
- `references/exemplars/cards/vggt.md`
- `references/exemplars/cards/neurips-2025-1000-layer-ssl-rl.md`
- `references/storyline-blueprint.md`
- `references/expert-review-loop.md`

## Draft Pass 1

### Global Story

Task: answer navigation and interaction queries in dynamic 4D indoor scenes.

Gap: current embodied agents remember static landmarks better than moving objects, so temporal changes are lost across long-horizon reasoning.

Root challenge: moving objects create discontinuous observations; a model must bind object identity, 3D position, and time without rebuilding the entire scene at every step.

Insight: object-centric spatiotemporal memory can preserve dynamic evidence more efficiently than frame-level history.

Method: a transformer that writes object memory tokens with 3D pose, time, motion, and language-aligned attributes, then retrieves them for navigation decisions.

Evidence promise: benchmark on dynamic-object navigation, ablations for memory write/read, comparison against frame history and static maps, qualitative temporal query examples.

### Simple Abstract Draft

Embodied agents increasingly operate in dynamic indoor scenes, yet most visual-language navigation systems store scenes as static maps or frame histories. This makes them brittle when objects move, disappear, or reappear across long trajectories. We propose Dynamic Scene Memory Transformer, an object-centric memory model that writes spatiotemporal tokens from egocentric multi-view video and retrieves them for language-conditioned navigation. The model binds each memory token to 3D position, time, motion state, and semantic attributes, enabling agents to reason over both stable background structure and dynamic objects. We introduce a dynamic navigation benchmark with temporal object queries and evaluate against static-map, frame-history, and 3D-LMM baselines. Across navigation success, temporal grounding, and object relocation tasks, the proposed memory improves dynamic-scene reasoning while reducing stored visual tokens.

## Expert Review Pass 1

Score: 5/10, weak reject.

Findings:

- Novelty is plausible but underspecified. "Object-centric memory" could overlap with existing memory-map and tracking work.
- The benchmark promise is too broad for a simple article. The draft needs a clearer evidence package and task boundary.
- The abstract claims reduced storage but does not say how storage is measured.
- It borrows the 4D dynamic-scene rhythm successfully, but it needs the VGGT-style output definition: what exactly is predicted or retrieved?

Revision Actions:

- Narrow the task to language-conditioned relocation and navigation in dynamic rooms.
- Define outputs: answer, waypoint, and supporting object-time trace.
- Add storage metric and ablation requirement.
- Replace broad "3D-LMM baselines" with precise baseline families.

## Draft Pass 2

### Revised Abstract

Language-conditioned navigation in dynamic rooms requires more than recognizing the current view: an agent must remember where objects were, when they moved, and which past observation supports a decision. Existing static-map and frame-history agents either discard object motion or store redundant visual context. We propose Dynamic Scene Memory Transformer, a retrieval model that writes object-time memory tokens from egocentric video and predicts three outputs for each query: a navigation waypoint, a natural-language answer, and an evidence trace over remembered objects. The model stores 3D position, timestamp, motion cue, and semantic state for each object token, then retrieves a compact temporal support set before action prediction. We evaluate on a language-conditioned relocation benchmark with moving-object goals, comparing against static semantic maps, recurrent frame memory, and video-LMM retrieval baselines. The proposed memory improves temporal grounding and navigation success while using fewer retained tokens; ablations isolate the contributions of time encoding, motion-aware writing, and evidence-trace supervision.

### Section Plan

Introduction:

1. Dynamic navigation need: current view alone is insufficient.
2. Prior map/frame-memory limitation: static maps lose motion, frame histories are redundant.
3. Root challenge: bind object identity, 3D location, and time for query-time evidence.
4. Method preview: object-time memory writes, compact retrieval, waypoint/answer/evidence outputs.
5. Contributions: task benchmark, memory model, evidence-trace supervision, evaluation package.

Experiments:

1. Main comparison on relocation navigation.
2. Temporal grounding and evidence-trace accuracy.
3. Storage-efficiency curve.
4. Ablations: no time, no motion cue, no evidence supervision, full frame memory.
5. Failure analysis for occlusion and identity switches.

## Expert Review Pass 2

Score: 7/10, weak accept if experiments are real.

Remaining risks:

- Must define benchmark construction and annotation quality.
- Needs a strong baseline suite from embodied AI and video retrieval.
- Storage reduction claim must report both token count and accuracy trade-off.

Skill Outcome:

- The exemplar index helped choose a small card bundle instead of overloading context.
- The LLaVA-4D card helped shape the dynamic-scene gap and observation-to-module move.
- The VGGT card exposed the need to define outputs early.
- The review loop caught overclaiming before final prose.
- No exemplar wording or technical claim was copied.
