# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['MBPI-inventory.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\Administrator\\PycharmProjects\\3.12\\MBPI-system\\add.png', '.'), ('C:\\Users\\Administrator\\PycharmProjects\\3.12\\MBPI-system\\home_icon.png', '.'), ('C:\\Users\\Administrator\\PycharmProjects\\3.12\\MBPI-system\\update.png', '.'), ('C:\\Users\\Administrator\\PycharmProjects\\3.12\\MBPI-system\\filter.png', '.'), ('C:\\Users\\Administrator\\PycharmProjects\\3.12\\MBPI-system\\delete2.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='MBPI-inventory',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
