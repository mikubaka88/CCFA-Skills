# Local Commands

## No Personal Absolute Paths

Do not write machine-specific absolute paths, usernames, home directories, or expanded local skill paths into committed skills, README files, source registries, SVGs, scripts, or examples. Use `$CODEX_HOME`, `$HOME`, repo-relative paths, or variables such as `$SkillsRoot` and `$SkillCreatorScripts`.

Before finishing a skill-family maintenance task, search for path leaks:

```powershell
python 'ccf-common/scripts/check_path_privacy.py' .
```

Any match should be replaced with a variable, repo-relative path, or non-identifying local reference.

## Locate Skill Tools

Locate the system `skill-creator` scripts without expanding a personal home path:

```powershell
$SkillsRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $HOME '.codex/skills' }
$SkillCreatorScripts = Join-Path $SkillsRoot '.system/skill-creator/scripts'
```

If the path changes, locate them with:

```powershell
Get-ChildItem -Force -Recurse -Filter init_skill.py $SkillsRoot
Get-ChildItem -Force -Recurse -Filter quick_validate.py $SkillsRoot
```

## Initialize A Skill

Use the initializer for new skills:

```powershell
python (Join-Path $SkillCreatorScripts 'init_skill.py') my-skill --path $SkillsRoot --resources references
```

Add only resource directories that are needed:

```powershell
python (Join-Path $SkillCreatorScripts 'init_skill.py') my-skill --path $SkillsRoot --resources scripts,references,assets
```

## PowerShell Quoting

In PowerShell, `$skill-name` inside double quotes can be treated as a variable expression. Use single quotes for interface values that contain `$`:

```powershell
python (Join-Path $SkillCreatorScripts 'init_skill.py') my-skill --path $SkillsRoot --interface display_name='My Skill' --interface short_description='Create a focused skill' --interface default_prompt='Use $my-skill to create a focused skill.'
```

If a generated `agents/openai.yaml` loses the skill name, edit it so the prompt explicitly includes `$my-skill`.

## Validate

Run the validator when available:

```powershell
python (Join-Path $SkillCreatorScripts 'quick_validate.py') (Join-Path $SkillsRoot 'my-skill')
```

If validation fails because Python package `yaml` is missing, report the dependency issue and perform the manual validation checklist in `references/design-checklist.md`. Install dependencies only when the user has asked for a fully automated local validator or the environment policy allows it.

## Inspect Created Files

Use these commands to review a skill without noisy output:

```powershell
$SkillPath = Join-Path $SkillsRoot 'my-skill'
Get-ChildItem -Force -Recurse -Name -LiteralPath $SkillPath
Get-Content -Raw -LiteralPath (Join-Path $SkillPath 'SKILL.md')
Get-Content -Raw -LiteralPath (Join-Path $SkillPath 'agents/openai.yaml')
```
