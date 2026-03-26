#!/bin/bash
cd "$(dirname "$0")"

# 检查依赖
if ! python3 -c "import PyQt5" 2>/dev/null; then
    echo "正在安装依赖..."
    pip install --break-system-packages -r requirements.txt
fi

# 运行程序
python3 main.py
