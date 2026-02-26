# Ouroboros 本地运行指南

本项目已配置为在本地系统运行（无需 Google Colab）。

## 快速开始

### 1. 配置 API 密钥

编辑 `.env` 文件，填写以下必要信息：

```bash
nano .env  # 或使用其他编辑器
```

必填项：
- `LLM_API_KEY` - OpenAI 或兼容接口的 API Key
- `TELEGRAM_BOT_TOKEN` - 从 [@BotFather](https://t.me/BotFather) 获取
- `GITHUB_TOKEN` - GitHub Personal Access Token（需要 repo 权限）
- `GITHUB_USER` - 你的 GitHub 用户名
- `GITHUB_REPO` - 仓库名（通常是 `ouroboros`）
- `TOTAL_BUDGET` - 预算上限（USD，如 `10`）

可选项：
- `LLM_BASE_URL` - 如使用 OpenRouter 等兼容接口（如 `https://openrouter.ai/api/v1`）
- `OPENAI_API_KEY` - 用于 web search 工具
- `ANTHROPIC_API_KEY` - 用于 Claude Code CLI
- `ANTHROPIC_BASE_URL` - Claude Code CLI 的自定义端点（如使用兼容接口）

### 2. 启动

```bash
./run.sh
```

或手动启动：

```bash
source .venv/bin/activate
python3 local_launcher.py
```

### 3. 使用

1. 打开你的 Telegram，找到你创建的 Bot
2. 发送任意消息，第一个发消息的人将成为 owner
3. 开始与 Ouroboros 对话

## 目录结构

```
~/.ouroboros/          # 状态存储目录（替代 Google Drive）
├── state/             # 状态文件
├── logs/              # 日志文件
│   ├── chat.jsonl     # 聊天记录
│   └── supervisor.jsonl  # 系统日志
├── memory/            # 记忆存储
├── index/             # 索引文件
├── locks/             # 锁文件
└── archive/           # 归档文件
```

## Telegram 命令

| 命令 | 说明 |
|------|------|
| `/panic` | 紧急停止，立即终止所有任务 |
| `/restart` | 软重启，保存状态后重新启动 |
| `/status` | 显示当前状态（workers、任务队列、预算） |
| `/evolve` | 启动自主进化模式（注意：会消耗预算） |
| `/evolve stop` | 停止进化模式 |
| `/review` | 队列深度审查任务 |
| `/bg start` | 启动后台意识循环 |
| `/bg stop` | 停止后台意识循环 |
| `/bg` | 查看后台意识状态 |

其他消息将直接发送给 LLM 处理。

## 故障排查

### 依赖问题

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### 查看日志

```bash
tail -f ~/.ouroboros/logs/supervisor.jsonl
tail -f ~/.ouroboros/logs/chat.jsonl
```

### 清理状态

如需重置所有状态：

```bash
rm -rf ~/.ouroboros/
```

## 与 Colab 版本的区别

- ✅ 无需 Google Colab
- ✅ 无需 Google Drive
- ✅ 状态存储在本地 `~/.ouroboros/`
- ✅ 使用 `.env` 文件管理配置
- ✅ 完全相同的功能和命令

## 注意事项

1. 确保系统有足够的磁盘空间（建议至少 1GB）
2. 首次运行会自动创建必要的目录
3. 所有状态和日志都保存在 `~/.ouroboros/`
4. 预算限制由 `TOTAL_BUDGET` 控制，请谨慎设置
5. 进化模式会持续消耗 API 调用，建议先测试后再启用

## 技术支持

- GitHub Issues: https://github.com/joi-lab/ouroboros/issues
- 文档: 查看项目根目录的 `BIBLE.md` 和 `README.md`
