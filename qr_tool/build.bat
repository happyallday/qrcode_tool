@echo off
echo Installing dependencies...
pip install PyInstaller==6.3.0

echo Building exe...
pyinstaller --onefile --windowed --name QRCodeTool --hidden-import=PyQt5 --hidden-import=qrcode --hidden-import=PIL --hidden-import=pyzbar.pyzbar --hidden-import=pyzbar --recursive-copy-recursive pyzbar main.py

echo Done!
echo Exe file: dist\QRCodeTool.exe
pause
