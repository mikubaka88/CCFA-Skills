# 在 Gemini CLI 中使用 CCFA Skills

[返回主页](../../README.md) · [Codex](CODEX.md) · [Claude Code](CLAUDE_CODE.md) · [Cursor](CURSOR.md) · [其他 Agent](OTHER_AGENTS.md)

## 安装

```bash
npx skills add mikubaka88/CCFA-Skills --global --agent gemini-cli --skill '*' --yes --copy
npx skills list --global --agent gemini-cli
```

开启新的 Gemini CLI 会话后直接描述任务。部分安装必须包含 `ccf-common`，并保留完整 skill 目录。

## 更新与自动更新

```bash
npx skills update --global --yes
```

macOS/Linux 每周自动更新：

```bash
(crontab -l 2>/dev/null; echo '0 9 * * 1 cd "$HOME" && /usr/bin/env npx skills update --global --yes >> "$HOME/.ccfa-skills-update.log" 2>&1') | crontab -
```

Windows 每周自动更新：

```powershell
schtasks /Create /SC WEEKLY /D SUN /TN "CCFA Skills Update" /TR "cmd.exe /c npx skills update --global --yes" /ST 09:00 /F
```

更新后的内容在下一次会话生效。详见 [自动更新说明](AUTO_UPDATE.md)。
