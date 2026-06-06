# Self-Test: Default User-Custom Writing Format

Purpose: verify that `references/custom-format/default-user-format.md` is used when no target venue is specified, that it loads the user-custom ICLR/CVPR exemplars, and that it runs a draft -> expert review -> revision -> re-review loop.

Prompt simulated: "帮我写一篇关于动态三维场景记忆的论文摘要和引言结构。"

Assumption: no target venue was specified, so the user-custom writing format is active.

Loaded files:

- `references/custom-format/default-user-format.md`
- `references/exemplars/cards/llava-4d.md`
- `references/exemplars/cards/vggt.md`
- `references/storyline-blueprint.md`
- `references/expert-review-loop.md`

## Draft Pass 1

### Blueprint

Task: dynamic 3D scene memory for embodied visual-language agents.

Gap: existing agents can parse current observations but struggle to remember object motion and viewpoint-dependent geometry over long trajectories.

Root challenge: a dynamic scene representation must bind identity, 3D location, time, and language-grounded attributes while staying compact enough for decision making.

Insight: object-time memory tokens can bridge LLaVA-4D-style spatiotemporal grounding and VGGT-style direct multi-output geometry.

Method: a Dynamic Geometry Memory Transformer that writes object-time geometry tokens and predicts navigation waypoints, temporal object answers, and evidence traces.

Evidence: dynamic relocation benchmark, multi-task geometry grounding, ablations for time encoding, memory compaction, and evidence trace supervision.

### Abstract Draft

Embodied visual-language agents need to reason about dynamic 3D scenes, yet most current systems either describe the present view or maintain static maps. This loses the temporal evidence needed when objects move, disappear, or become visible from a different viewpoint. We propose Dynamic Geometry Memory Transformer, a model that writes compact object-time memory tokens from egocentric video and retrieves them for language-conditioned navigation and temporal question answering. Each token stores semantic attributes, camera-relative geometry, global 3D position, timestamp, and motion cues, allowing the model to predict navigation waypoints, object-state answers, and supporting evidence traces in a single forward pass. We evaluate on a dynamic relocation benchmark with moving-object goals and temporal queries, comparing against static semantic maps, recurrent frame memory, and video-LMM retrieval baselines. The model improves temporal grounding and navigation success while reducing retained visual tokens; ablations isolate the roles of time encoding, memory compaction, and evidence supervision.

## Expert Review Pass 1

Score: 6/10.

High-severity issues:

- The draft sounds plausible but does not define how camera-relative geometry becomes global 3D position.
- The evidence package is broad; without a concrete benchmark construction paragraph, the central claim could look hypothetical.
- "Single forward pass" echoes VGGT but may be unsupported if the memory writer runs over a sequence.

Medium-severity issues:

- The relation between navigation waypoints and question answering needs clearer task boundaries.
- The storage reduction claim needs a metric.

Revision plan:

- Replace "single forward pass" with "one retrieval-and-decision stage" unless the architecture truly supports single-pass inference.
- Define the output triplet before detailed token fields.
- Add a benchmark construction sentence.
- Add a storage metric placeholder tied to retained token count and performance.

## Draft Pass 2

### Revised Abstract

Embodied visual-language agents need to remember dynamic 3D scenes, not only recognize the current view. Static maps lose object motion, while frame-history memories store redundant context without exposing which past observation supports a decision. We propose Dynamic Geometry Memory Transformer, an object-time memory model for language-conditioned relocation and temporal scene queries. Given egocentric video, the model writes compact memory tokens that bind object identity, local geometry, estimated global position, timestamp, and motion state; at query time it retrieves a support set and predicts a waypoint, an answer, and an evidence trace. We introduce a dynamic-room benchmark by replaying object relocations across multi-view trajectories and asking agents to navigate to, describe, or localize moved objects. Experiments compare against static semantic maps, recurrent frame memory, and video-LMM retrieval baselines under matched storage budgets. The proposed memory improves temporal grounding and navigation success, and ablations show that time encoding, motion-aware writing, and evidence-trace supervision each reduce failure on moved-object queries.

## Expert Review Pass 2

Score: 7/10.

Remaining risks:

- Needs exact benchmark details before a real submission.
- Needs baseline names and data-generation protocol.
- The global-position estimate must be described carefully in the method.

Outcome:

- The default custom format loaded the ICLR and CVPR user exemplars.
- The first draft used the desired dynamic-scene and direct-output style.
- The review loop removed a VGGT-like overclaim and clarified evidence.
- The format is ready as a default unspecified-venue workflow, with remaining risks correctly tied to future experimental details.
