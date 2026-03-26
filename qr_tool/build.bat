@echo off
echo Installing dependencies...
pip install PyInstaller==6.3.0

echo Building exe...
pyinstaller --onefile --windowed --name QRCodeTool --add-data "main.py;." main.py

echo Done!
echo Exe file: dist\QRCodeTool.exe
pause
