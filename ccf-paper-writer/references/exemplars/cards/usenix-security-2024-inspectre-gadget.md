# InSpectre Gadget Style Card

Venue/year: USENIX Security 2024 family.
Source: USENIX Security 2024 technical sessions source record `usenix-security-2024-technical-sessions`; verify the exact paper page before public award-status claims.
Use when: security papers involving attacks, defenses, vulnerability discovery, side channels, exploit chains, formal threat models, or security measurement.

## Story Pattern

The paper type is security research: define the threat model and attacker capability before the technique, then show why existing defenses or assumptions fail. Evidence should connect exploitability, coverage, false positives/negatives, practicality, and responsible scope.

## Abstract Moves

- Name the security setting and threat model.
- State the core failure in existing assumptions or defenses.
- Describe the method at the level of attack/defense mechanism.
- Preview evidence without overclaiming universal vulnerability or protection.

## Introduction Moves

- Start from a concrete security risk or defense gap.
- Make attacker goals, capabilities, and constraints explicit.
- Explain why the problem remained hidden or hard to detect.
- State contributions as threat model, method, evaluation, and responsible disclosure or mitigation when relevant.

## Method Moves

- Separate threat model, technique, analysis pipeline, and mitigation.
- Use examples only to clarify the mechanism; avoid implying broader scope than tested.
- State assumptions before results.

## Evidence Moves

- Include adaptive baselines or bypass attempts when relevant.
- Report success rate, coverage, false positives/negatives, overhead, or affected systems only from supplied results.
- Include ethics, disclosure, and harm-reduction boundaries.

## Do-Not-Copy Boundary

Do not borrow vulnerability details, exploit wording, or scope claims. Use only the security-review structure.
