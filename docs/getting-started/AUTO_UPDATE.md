# 自动更新 CCFA Skills

[返回主页](../../README.md) · [Codex](CODEX.md) · [Claude Code](CLAUDE_CODE.md) · [Cursor](CURSOR.md) · [Gemini CLI](GEMINI_CLI.md)

## 更新命令

通过 `npx skills` 安装时：

```bash
npx skills update --global --yes
```

更新不会让已运行会话重新加载 skill。完成后请开启新会话。

更新前先比较安装副本中的个人修改与仓库版本，将需要保留的改进合并或另存到明确的维护位置；不要用整目录覆盖代替差异核对。个人偏好保存在安装目录之外的 `$CODEX_HOME/ccfa/preferences.json`（未设置时为 `~/.codex/ccfa/preferences.json`）及项目 `.ccfa/preferences.json`，更新时保留。配置页与解析器随 `ccf-common` 一起更新，普通任务无需启动网页服务。

## Windows 任务计划

```powershell
schtasks /Create /SC WEEKLY /D SUN /TN "CCFA Skills Update" /TR "cmd.exe /c npx skills update --global --yes" /ST 09:00 /F
schtasks /Query /TN "CCFA Skills Update" /V /FO LIST
```

取消：

```powershell
schtasks /Delete /TN "CCFA Skills Update" /F
```

如果计划任务找不到 `npx`，先运行 `Get-Command npx`，再把任务中的命令替换为显示的绝对路径。不要把访问令牌或 API key 写入任务命令。

## macOS/Linux cron

```bash
(crontab -l 2>/dev/null; echo '0 9 * * 1 cd "$HOME" && /usr/bin/env npx skills update --global --yes >> "$HOME/.ccfa-skills-update.log" 2>&1') | crontab -
crontab -l
tail -n 50 "$HOME/.ccfa-skills-update.log"
```

取消时运行 `crontab -e`，删除对应行。

## 稳定 clone

若使用本地 clone 作为单一来源：

```bash
git -C "$HOME/ai-skills/CCFA-Skills" pull --ff-only
```

`--ff-only` 会在本地存在分叉提交时停止，不会静默覆盖修改。开发用 clone 与自动更新 clone 应分开。
