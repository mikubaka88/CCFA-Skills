# 在 Cursor 中使用 CCFA Skills

[返回主页](../../README.md) · [Codex](CODEX.md) · [Claude Code](CLAUDE_CODE.md) · [Gemini CLI](GEMINI_CLI.md) · [其他 Agent](OTHER_AGENTS.md)

## 安装

```bash
npx skills add mikubaka88/CCFA-Skills --global --agent cursor --skill '*' --yes --copy
npx skills list --global --agent cursor
```

重启 Cursor 或开启新的 Agent 会话，然后直接描述研究任务。部分安装必须包含 `ccf-common`，并保留完整 skill 目录。

## 更新与自动更新

```bash
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

更新后的内容在下一次 Agent 会话生效。详见 [自动更新说明](AUTO_UPDATE.md)。
