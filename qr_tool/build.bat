@echo off
echo Installing dependencies...
pip install --upgrade setuptools
pip install pyinstaller

echo Cleaning previous build...
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build
if exist *.spec del /q *.spec

echo Creating spec file...
pyi-makespec --onefile --console --name QRCodeTool --hidden-import=PyQt5 --hidden-import=PyQt5.QtCore --hidden-import=PyQt5.QtGui --hidden-import=PyQt5.QtWidgets --hidden-import=qrcode --hidden-import=PIL --hidden-import=pyzbar --hidden-import=pyzbar.pyzbar main.py

echo Manually editing spec file...
echo a = Analysis(
echo     ['main.py'],
echo     pathex=[],
echo     binaries=[],
echo     datas=[],
echo     hiddenimports=['PyQt5', 'PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets', 'qrcode', 'PIL', 'pyzbar', 'pyzbar.pyzbar'],
echo     hookspath=[],
echo     hooksconfig={},
echo     runtime_hooks=[],
echo     excludes=['pkg_resources'],
echo     noarchive=False,
echo )
echo pyz = PYZ(a.pure)
echo exe = EXE(pyz,
echo      a.scripts,
echo      [],
echo      exclude_binaries=True,
echo      name='QRCodeTool',
echo      debug=False,
echo      bootloader_ignore_signals=False,
echo      strip=False,
echo      upx=True,
echo      console=True,
echo      disable_windowed_traceback=False,
echo      argv_emulation=False,
echo      target_arch=None,
echo      codesign_identity=None,
echo      entitlements_file=None )
echo coll = COLLECT(exe,
echo        a.binaries,
echo        a.zipfiles,
echo        a.datas,
echo        strip=False,
echo        upx=True,
echo        upx_exclude=[],
echo        name='QRCodeTool')
> QRCodeTool.spec

echo Building exe...
pyinstaller QRCodeTool.spec

echo Done!
pause
