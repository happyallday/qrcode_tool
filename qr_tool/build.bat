@echo off
echo Installing dependencies...
pip install PyInstaller==5.13.2

echo Building exe...
pyinstaller --onefile --windowed --name QRCodeTool main.py

echo Done!
echo Exe file: dist\QRCodeTool.exe
pause
