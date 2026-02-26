# Ouroboros 本地运行 - 快速参考

## 🚀 启动步骤

```bash
# 1. 编辑配置
nano .env

# 2. 检查配置
python3 check_config.py

# 3. 启动
./run.sh
```

## 📝 必填配置项

在 `.env` 文件中填写：

```bash
LLM_API_KEY=sk-...              # OpenAI 或兼容接口的 API Key
TELEGRAM_BOT_TOKEN=123456:ABC...  # 从 @BotFather 获取
GITHUB_TOKEN=ghp_...            # GitHub Token (repo 权限)
GITHUB_USER=your_username       # 你的 GitHub 用户名
GITHUB_REPO=ouroboros           # 仓库名
TOTAL_BUDGET=10                 # 预算上限（USD）

# 可选：自定义 API 端点
LLM_BASE_URL=https://...        # LLM 兼容接口地址
ANTHROPIC_BASE_URL=https://...  # Claude Code CLI 兼容接口地址
```

## 🔧 常用命令

```bash
# 启动
./run.sh

# 检查配置
python3 check_config.py

# 查看日志
tail -f ~/.ouroboros/logs/supervisor.jsonl

# 停止（Ctrl+C 或发送 /panic 到 Telegram）

# 清理状态
rm -rf ~/.ouroboros/
```

## 💬 Telegram 命令

- `/status` - 查看状态
- `/panic` - 紧急停止
- `/restart` - 重启
- `/evolve` - 启动进化模式
- `/bg start` - 启动后台意识

## 📂 文件说明

- `.env` - 配置文件（必须填写）
- `local_launcher.py` - 本地启动器
- `run.sh` - 启动脚本
- `check_config.py` - 配置检查工具
- `LOCAL_SETUP.md` - 详细设置指南

## 🆘 获取 API Keys

1. **Telegram Bot Token**:
   - 打开 Telegram，搜索 @BotFather
   - 发送 `/newbot` 创建新 bot
   - 复制 token

2. **GitHub Token**:
   - 访问 https://github.com/settings/tokens
   - Generate new token (classic)
   - 勾选 `repo` 权限

3. **LLM API Key**:
   - OpenAI: https://platform.openai.com/api-keys
   - OpenRouter: https://openrouter.ai/keys
   - 其他兼容接口

## ⚠️ 注意事项

- 首次运行会自动创建 `~/.ouroboros/` 目录
- 进化模式会持续消耗 API 调用
- 预算限制由 `TOTAL_BUDGET` 控制
- 所有状态保存在本地，重启后会恢复
