# 在 Codex 中使用 CCFA Skills

[返回主页](../../README.md) · [Claude Code](CLAUDE_CODE.md) · [Cursor](CURSOR.md) · [Gemini CLI](GEMINI_CLI.md) · [其他 Agent](OTHER_AGENTS.md)

## 前置条件

- Git。
- Node.js 18 或更高版本。`npx skills` 无需全局安装。
- 一个新的 Codex 会话；已启动的会话不会自动重载刚安装的 skill。

## 推荐安装

先查看仓库中可安装的 skills：

```powershell
npx skills add mikubaka88/CCFA-Skills --list
```

将完整家族安装到 Codex：

```powershell
npx skills add mikubaka88/CCFA-Skills --global --agent codex --skill '*' --yes --copy
```

只安装部分 skills 时必须包含 `ccf-common`。例如：

```powershell
npx skills add mikubaka88/CCFA-Skills --global --agent codex --skill ccf-common --skill ccf-humanization --skill ccf-paper-writer --skill ccf-visual-composer --yes --copy
```

验证：

```powershell
npx skills list --global --agent codex
```

开启新的 Codex 会话后直接描述任务：

```text
使用 CCFA Skills 检索这个方向的公开 benchmark，并设计主实验与消融；不要虚构结果。
```

## 更新与自动更新

```powershell
npx skills update --global --yes
```

Windows 每周自动更新：

```powershell
schtasks /Create /SC WEEKLY /D SUN /TN "CCFA Skills Update" /TR "cmd.exe /c npx skills update --global --yes" /ST 09:00 /F
```

macOS/Linux 每周自动更新：

```bash
(crontab -l 2>/dev/null; echo '0 9 * * 1 cd "$HOME" && /usr/bin/env npx skills update --global --yes >> "$HOME/.ccfa-skills-update.log" 2>&1') | crontab -
```

更新后的内容通常在下一次会话完整生效。取消方法与日志建议见 [自动更新说明](AUTO_UPDATE.md)。

## 稳定 clone 方案

需要审阅源码、固定版本或自行修改时，可从稳定 clone 安装：

```powershell
git clone https://github.com/mikubaka88/CCFA-Skills.git
Set-Location CCFA-Skills
git pull --ff-only
npx skills add . --global --agent codex --skill '*' --yes --copy
```

不要只复制 `SKILL.md`；`references/`、`scripts/`、`resources/` 与 `ccf-common` 都是家族的一部分。
