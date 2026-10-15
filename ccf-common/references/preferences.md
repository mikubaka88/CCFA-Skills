# Personal Preferences

Preferences control optional extra work, not required prerequisites, factual accuracy, review coverage, privacy, file contracts, or the Humanization -> Common preflight. They do not select the model, change host permissions, or replace `quick/standard/exploratory` and `partial/full/off` modes.

## Resolve Once

During Common's preflight, reuse an applicable resolved preference set. Otherwise run `python <ccf-common>/scripts/preferences.py resolve` once, adding `--project <established-project-root>` only when a project root is known. The script reads no manuscript, contacts no service, and creates no files. If Python is unavailable, read the two known JSON paths below directly and apply the same precedence. A missing file means defaults; an invalid file is a configuration error, not a remembered refusal or permission. Continue unaffected required work, report the affected configuration problem, and do not silently overwrite it.

Precedence: current explicit user instruction > project overrides > user overrides > defaults, within host constraints. Pass the resolved choices to contributors instead of rerunning the resolver at every handoff. Refresh only after a preference, project, or explicit instruction changes. UI language affects the configurator; it does not override the user's requested artifact language.

| Key | Default | Optional work and trigger |
| --- | --- | --- |
| `independent_review` | `off` | A second independent assessment of a consequential unresolved finding, competing interpretations, or a requested pre-submission check. Use one bounded pass over relevant evidence; broaden only if the finding requires it. Requires actual independent execution permitted by the host; role-play is not independence. |
| `extended_search` | `auto` | Additional query clusters or citation-neighborhood traversal when a specific closest-work or evidence gap could change the answer. Stop when covered or when further queries add no decision-relevant evidence. |
| `enhanced_document_parsing` | `auto` | Additional OCR, visual interpretation, or a heavier parser for relevant pages whose tables, formulae, reading order, or glyphs remain unclear. Prefer existing tools and inspected source pages before new dependencies. |
| `figure_variants` | `off` | An additional candidate when comparing a materially different composition or visual hierarchy helps choose the requested figure. Share the approved content and assets; a local label/spacing correction does not trigger alternatives. |
| `detailed_reports` | `off` | Extra execution/provenance detail useful for a complex handoff, replication, or explicit audit. Extend the existing canonical report; do not create per-step reports. Required structured reviews remain unchanged. |
| `alternative_routes` | `off` | Add at most one optional alternative to a task with a selected route when a concrete unresolved choice could change the result. Reuse evidence and compare mechanisms before switching. Requested brainstorming, multiple directions, and necessary route corrections remain core work with this off. Extra experiments or services still need applicable authorization. |
| `maintenance_evolution` | `off` | During explicitly requested skill maintenance only, evaluate at most one additional candidate rule revision against fixed representative cases when a diagnosed rule failure remains unresolved. Keep acceptance criteria fixed and retain the stable version if the candidate fails. Never edit skills or model weights automatically during research tasks. |

`off` skips only unrequested optional extensions. `auto` enables a listed extension only for a concrete trigger with expected benefit. `on` remembers the user's preference for that extension on relevant tasks; it does not run every enhancement for every task, authorize a new experiment campaign, or permit unrelated rewrites. Explicit requests such as “compare two figure designs” override a saved `off` for that task without changing the saved preference. An unavailable optional tool does not block the underlying deliverable or justify pretending the extension ran.

Necessary evidence lookup, source-page inspection, material verification, and prerequisite collaboration still happen with optional extensions off. Retain concept-only idea review unless the user requests experiments. Extra work is bounded by its question and completion condition, not a quota of agents, papers, or retries. If required evidence remains unavailable, identify that gap rather than declaring completion to meet an optional-work budget.

The two route/maintenance extensions default to `off`; existing version-1 files that omit them remain valid and inherit `off`. `auto` requires the concrete trigger above; `on` is a preference for relevant comparisons, not a permanent exploration or self-modification loop. The optional extensions add at most one candidate per unresolved decision or maintenance task; changing owners or renaming the same problem does not reset this allowance. Additional unrequested rounds need an agreed scope and budget. A user request such as "find five directions" or "explore more ambitious mechanisms" already authorizes that breadth: do not cap it at one, ask for a budget form, or require turning on this switch. Necessary fixes, recovery checks, and required comparisons also remain part of the base workflow. The Lean and Balanced UI presets keep these extensions `off`; Deep sets them to `auto`.

## Ask Once And Remember

Use existing explicit choices first. If an optional extension needs a preference decision, ask once for the relevant choices and whether they apply to this project or future tasks. Bundle related choices; do not show an intake form on every activation. An unanswered question uses the default and is not saved as consent. Saving preference settings is authorized when the user explicitly asks to remember their selection or presses Save in the configurator. A one-task instruction is not a permanent preference unless requested.

Do not ask again when the choice and scope are unchanged. A material change in external service, data destination, extra charges, or scope may require a new decision for that affected action; a general enhancement preference does not authorize uploading a private manuscript. Preserve existing authorization and `privacy-and-evidence.md` boundaries.

## Storage And Web Configuration

- User file: `$CODEX_HOME/ccfa/preferences.json`, or `~/.codex/ccfa/preferences.json` when `CODEX_HOME` is unset. It stays outside installed skills and survives their replacement.
- Project file: `<project-root>/.ccfa/preferences.json`. The root is explicit/established, never discovered by scanning unrelated parent directories. Personal project preferences are local by default; share them only intentionally.
- Configuration format: `{"version":1,"preferences":{},"ui":{}}`. Preference values are `off`, `auto`, or `on`; `ui.language` is `zh-CN`, `zh-TW`, or `en`; `ui.theme` is `system`, `light`, or `dark`. Omitted entries inherit. Unknown fields, values, duplicate JSON keys, and unsupported versions are errors.
- Keep only chosen overrides. Deleting an override restores inheritance, not a snapshot of today's inherited value. Do not write resolved settings back to every project or store manuscript content, credentials, source paths, or task logs in this file.

Run `python <ccf-common>/scripts/preferences.py serve [--project <project-root>]` to open the local configurator. `--no-browser` prints a launch URL instead. It binds to loopback and saves to the two fixed destinations only. A static copy of `assets/configurator/index.html` supports JSON import/export; an exported download is not an applied configuration until it is placed at the selected destination. Reading a skill never launches the web server.

The local page reads/saves through the authenticated service. Unsaved edits, successful writes, invalid settings, and conflicting edits must be distinguished. Browser theme/preview storage alone cannot claim skills are configured. The `ccfa.yaml` research-state schema remains unchanged; these preferences live in a separate optional personal configuration.

## Cost And Quality

Show qualitative marginal impact with the actual extra operation: a second assessment reads evidence again; expanded retrieval adds requests and source text; visual parsing adds page/image processing; additional figures add generation calls; detailed reporting adds output; a route comparison adds reasoning and evidence checks; a maintenance candidate adds a rule revision and fixed-case comparison. Exact latency, tokens, or price depend on the host/model/input and are not known from a toggle. Do not display invented percentages or describe a cost estimate as metering.

Default-path efficiency comes from targeted fields, valid evidence reuse, current-artifact edits, and compact tool returns. Preserve full diagnostics when needed for reproduction; summarize their actionable locations instead of repeatedly loading raw logs. Keep useful context and scientific evidence intact. Evaluate changes on representative tasks during skill maintenance, not by running a benchmark or an extra judge for every user request.
