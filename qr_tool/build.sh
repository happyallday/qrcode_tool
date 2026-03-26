#!/bin/bash
cd "$(dirname "$0")"

echo "正在安装打包依赖..."
pip install --break-system-packages PyInstaller==6.3.0

echo "正在打包exe..."
pyinstaller --onefile --windowed --name QRCodeTool --add-data "main.py:." main.py

echo "打包完成！"
echo "exe文件位于: dist/QRCodeTool.exe"
