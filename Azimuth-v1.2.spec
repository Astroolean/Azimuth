# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Azimuth-v1.2.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('fonts/americandream.zip', 'fonts'),
        ('fonts/game_of_squids.zip', 'fonts'),
        ('fonts/pixel_calculon.zip', 'fonts'),
        ('fonts/toe_the_lineless.zip', 'fonts'),
        ('LoadingUI/Loading.jpg', 'LoadingUI'),
        ('logo/Azimuth Logo.gif', 'logo'),
        ('Backgrounds/background2.jpg', 'Backgrounds'),
        ('Backgrounds/Primary.jpg', 'Backgrounds'),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Azimuth-v1.2',
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
