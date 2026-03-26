@echo off
echo Installing dependencies...
pip install PyInstaller==6.3.0

echo Building exe...
pyinstaller --onefile --windowed --name QRCodeTool --collect-all pyzbar --hidden-import=PyQt5 --hidden-import=qrcode --hidden-import=PIL main.py

echo Done!
echo Exe file: dist\QRCodeTool.exe
pause
