#!/bin/bash
cd "$(dirname "$0")"

echo "Installing dependencies..."
pip install --break-system-packages PyInstaller==6.3.0

echo "Building exe..."
pyinstaller --onefile --windowed --name QRCodeTool --hidden-import=PyQt5 --hidden-import=qrcode --hidden-import=PIL --hidden-import=pyzbar.pyzbar --collect-all pyzbar main.py

echo "Done!"
echo "Exe file: dist/QRCodeTool.exe"
