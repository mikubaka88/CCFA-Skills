# 在 Codex 中使用 CCFA Skills

[返回主页](../../README.md) · [Claude Code](CLAUDE_CODE.md) · [Cursor](CURSOR.md) · [Gemini CLI](GEMINI_CLI.md) · [其他 Agent](OTHER_AGENTS.md)

## 前置条件

- Git。
- Node.js 18 或更高版本。`npx skills` 无需全局安装。
- Codex 会自动检测 skill 变化；如果更新未显示，再重启 Codex。官方加载规则见 [Build skills](https://learn.chatgpt.com/docs/build-skills)。

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

确认列表中已显示所需 skills 后，直接描述任务：

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

更新后检查 skill 列表；若仍显示旧内容，再重启 Codex。取消方法与日志建议见 [自动更新说明](AUTO_UPDATE.md)。

## 稳定 clone 方案

需要审阅源码、固定版本或自行修改时，可从稳定 clone 安装：

```powershell
git clone https://github.com/mikubaka88/CCFA-Skills.git
Set-Location CCFA-Skills
git pull --ff-only
npx skills add . --global --agent codex --skill '*' --yes --copy
```

不要只复制 `SKILL.md`；`references/`、`scripts/`、`resources/` 与 `ccf-common` 都是家族的一部分。部分模式还读取相邻 skill 的参考文件，以及仓库根目录的 `ccf-latex-templates/`。安装器若仅复制 skill 目录，须在实际安装根目录保留相同的相邻资源关系；只在源码 clone 中存在模板不足以保证安装副本可用。依赖说明见 [安装矩阵](../INSTALLATION_MATRIX.zh-CN.md)。

手动安装按当前 Codex 文档使用项目或用户的 `.agents/skills` 路径；旧版兼容路径以实际客户端为准。仓库的 Codex 插件清单通过 `skills: "./"` 指向现有根目录，保留全部家族和相邻模板；插件分发方式见 [Build plugins](https://learn.chatgpt.com/docs/build-plugins)。本次静态验证不等同于在每个客户端完成安装测试。
