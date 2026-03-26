@echo off
echo Installing dependencies...
pip install --upgrade setuptools
pip install pyinstaller

echo Cleaning previous build...
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build
if exist *.spec del /q *.spec

echo Building exe...
pyinstaller --onefile --console --name QRCodeTool --hidden-import=PyQt5 --hidden-import=PyQt5.QtCore --hidden-import=PyQt5.QtGui --hidden-import=PyQt5.QtWidgets --hidden-import=qrcode --hidden-import=PIL --hidden-import=pyzbar --hidden-import=pyzbar.pyzbar main.py

echo Done!
pause
