# 在其他 Agent 中使用 CCFA Skills

[返回主页](../../README.md) · [Codex](CODEX.md) · [Claude Code](CLAUDE_CODE.md) · [Cursor](CURSOR.md) · [Gemini CLI](GEMINI_CLI.md)

CCFA Skills 遵循以 `SKILL.md` 为入口的 Agent Skills 目录结构。对于 OpenCode、GitHub Copilot、Cline、Roo Code、OpenHands 等受 `npx skills` 支持的客户端，将 `<agent-id>` 替换为对应标识：

```bash
npx skills add mikubaka88/CCFA-Skills --global --agent <agent-id> --skill '*' --yes --copy
npx skills list --global --agent <agent-id>
```

安装到所有已检测到的 Agent：

```bash
npx skills add mikubaka88/CCFA-Skills --all
```

部分安装必须包含 `ccf-humanization` 和 `ccf-common`；不要只复制 `SKILL.md`。

上述 CLI 命令仅安装 skill 目录。LaTeX 模板及部分安装需要的相邻资源，请从同一版本的仓库按[安装矩阵](../INSTALLATION_MATRIX.zh-CN.md#sibling-resources)补齐，并将复制目标改为本客户端的实际安装根目录。

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

若目标 Agent 不受 CLI 支持，请稳定 clone 本仓库，并通过该 Agent 的 skill、subagent 或 command wrapper 指向 clone 内完整的 `ccf-*/` 目录，并保留相邻的 `ccf-latex-templates/`。直接引用 clone 时执行 `git pull --ff-only` 即可更新引用内容；复制安装则还需刷新副本。相邻资源和本地 clone 的 `--copy` 副本也需同步，详见[自动更新说明](AUTO_UPDATE.md)。
