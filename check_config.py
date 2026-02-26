#!/usr/bin/env python3
"""
配置检查工具 - 在启动前验证所有必要的配置
"""
import os
import sys
import pathlib

def load_env():
    env_path = pathlib.Path(__file__).parent / ".env"
    if not env_path.exists():
        return False
    with open(env_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, _, val = line.partition("=")
                key = key.strip()
                val = val.strip()
                if key and key not in os.environ:
                    os.environ[key] = val
    return True

def check_config():
    print("🔍 检查 Ouroboros 配置...\n")

    if not load_env():
        print("❌ .env 文件不存在")
        print("   请先创建 .env 文件并填写配置")
        return False

    required = {
        "LLM_API_KEY": "LLM API Key（OpenAI 或兼容接口）",
        "TELEGRAM_BOT_TOKEN": "Telegram Bot Token",
        "GITHUB_TOKEN": "GitHub Personal Access Token",
        "GITHUB_USER": "GitHub 用户名",
        "GITHUB_REPO": "GitHub 仓库名",
        "TOTAL_BUDGET": "预算上限（USD）",
    }

    optional = {
        "LLM_BASE_URL": "LLM Base URL（可选）",
        "OPENAI_API_KEY": "OpenAI API Key（用于 web search）",
        "ANTHROPIC_API_KEY": "Anthropic API Key（用于 Claude Code）",
        "ANTHROPIC_BASE_URL": "Anthropic Base URL（用于 Claude Code 自定义端点）",
    }

    all_ok = True

    print("必填配置:")
    for key, desc in required.items():
        val = os.environ.get(key, "").strip()
        if not val or val.startswith("your_"):
            print(f"  ❌ {key:20s} - 未配置 ({desc})")
            all_ok = False
        else:
            masked = val[:8] + "..." if len(val) > 8 else "***"
            print(f"  ✅ {key:20s} - {masked}")

    print("\n可选配置:")
    for key, desc in optional.items():
        val = os.environ.get(key, "").strip()
        if val and not val.startswith("your_"):
            masked = val[:8] + "..." if len(val) > 8 else "***"
            print(f"  ✅ {key:20s} - {masked}")
        else:
            print(f"  ⚪ {key:20s} - 未配置 ({desc})")

    print("\n环境:")
    print(f"  Python: {sys.version.split()[0]}")
    print(f"  工作目录: {pathlib.Path.cwd()}")
    print(f"  状态目录: {pathlib.Path.home() / '.ouroboros'}")

    if all_ok:
        print("\n✅ 配置检查通过！可以运行 ./run.sh 启动")
        return True
    else:
        print("\n❌ 配置不完整，请编辑 .env 文件填写缺失的配置")
        return False

if __name__ == "__main__":
    sys.exit(0 if check_config() else 1)
