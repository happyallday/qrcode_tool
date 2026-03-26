@echo off
echo Installing dependencies...
pip install pyinstaller

echo Cleaning previous build...
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build
if exist *.spec del /q *.spec

echo Building exe...
pyinstaller QRCodeTool.spec

echo Done!
pause
