# 在 Claude Code 中使用 CCFA Skills

[返回主页](../../README.md) · [Codex](CODEX.md) · [Cursor](CURSOR.md) · [Gemini CLI](GEMINI_CLI.md) · [其他 Agent](OTHER_AGENTS.md)

## 安装

需要 Node.js 22.20.0 或更高版本（本地核验 `skills` CLI 1.5.22 的要求；其他版本以安装器的 `engines` 声明为准）。安装全部 17 个 skills：

```bash
npx skills add mikubaka88/CCFA-Skills --global --agent claude-code --skill '*' --yes --copy
```

验证：

```bash
npx skills list --global --agent claude-code
```

重新开启 Claude Code 会话后，自然描述科研任务即可：

```text
Use CCFA Skills to review this manuscript without rewriting it, and keep absolute readiness separate from relative revision progress.
```

部分安装必须同时安装 `ccf-humanization` 和 `ccf-common`，执行时先启用 Humanization，再启用 Common。不要仅复制单个 `SKILL.md`。

上述 CLI 命令仅安装 skill 目录。LaTeX 模板及部分安装需要的相邻资源，请从同一版本的仓库按[安装矩阵](../INSTALLATION_MATRIX.zh-CN.md#sibling-resources)补齐，并将复制目标改为本客户端的实际安装根目录。

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

更新后的 skill 在下一次 Claude Code 会话生效。相邻资源和本地 clone 的 `--copy` 副本也需同步，详见[自动更新说明](AUTO_UPDATE.md)。
