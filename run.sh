#!/bin/bash
# Ouroboros 本地启动脚本

cd "$(dirname "$0")"

# 检查 .env 文件
if [ ! -f .env ]; then
    echo "❌ 错误: .env 文件不存在"
    echo "请先复制 .env 模板并填写必要的配置："
    echo "  cp .env .env"
    echo "  nano .env  # 或使用其他编辑器"
    exit 1
fi

# 检查必要的配置
if ! grep -q "^LLM_API_KEY=.\+" .env || grep -q "^LLM_API_KEY=your_" .env; then
    echo "❌ 错误: 请在 .env 文件中填写 LLM_API_KEY"
    exit 1
fi

if ! grep -q "^TELEGRAM_BOT_TOKEN=.\+" .env || grep -q "^TELEGRAM_BOT_TOKEN=your_" .env; then
    echo "❌ 错误: 请在 .env 文件中填写 TELEGRAM_BOT_TOKEN"
    exit 1
fi

# 激活虚拟环境
if [ ! -d .venv ]; then
    echo "📦 创建虚拟环境..."
    python3 -m venv .venv
    .venv/bin/pip install -q -r requirements.txt
fi

source .venv/bin/activate

# 启动
echo "🐍 启动 Ouroboros..."
echo "   状态目录: ~/.ouroboros/"
echo "   日志: ~/.ouroboros/logs/"
echo ""
python3 local_launcher.py
