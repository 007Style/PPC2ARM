# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for PPC2ARM — macOS .app bundle

import sys
from pathlib import Path

block_cipher = None

a = Analysis(
    ['ppc2arm.py'],
    pathex=['.'],
    binaries=[],
    datas=[],
    hiddenimports=[
        'wx',
        'wx.aui',
        'wx.richtext',
        'core.engine',
        'core.fuzzy',
        'core.registry',
        'data.ppc_instructions',
        'data.arm_instructions',
        'data.mappings',
        'data.isa_trivia',
        'data.isa_schema',
        'gui.app',
        'gui.theme',
        'gui.mode_bar',
        'gui.main_panel',
        'gui.result_panel',
        'gui.isa_museum',
        'gui.easter_eggs',
        'gui.widgets.searchable_list',
        'gui.widgets.ticker_bar',
        'gui.widgets.about_dialog',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ppc2arm',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ppc2arm',
)

app = BUNDLE(
    coll,
    name='PPC2ARM.app',
    icon=None,
    bundle_identifier='com.daneyand.ppc2arm',
    info_plist={
        'CFBundleName': 'PPC2ARM',
        'CFBundleDisplayName': 'PPC2ARM',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSHighResolutionCapable': True,
        'NSPrincipalClass': 'NSApplication',
        'CFBundleDocumentTypes': [],
    },
)
