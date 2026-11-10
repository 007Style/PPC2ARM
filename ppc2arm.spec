# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for PPC2ARM — macOS .app bundle

import sys
from pathlib import Path

block_cipher = None

a = Analysis(
    ['src/ppc2arm/__main__.py'],
    pathex=['src'],
    binaries=[],
    datas=[],
    hiddenimports=[
        'wx',
        'wx.aui',
        'wx.richtext',
        'ppc2arm.core.engine',
        'ppc2arm.core.fuzzy',
        'ppc2arm.core.registry',
        'ppc2arm.data.ppc_instructions',
        'ppc2arm.data.arm_instructions',
        'ppc2arm.data.mappings',
        'ppc2arm.data.isa_trivia',
        'ppc2arm.data.isa_schema',
        'ppc2arm.gui.app',
        'ppc2arm.gui.theme',
        'ppc2arm.gui.mode_bar',
        'ppc2arm.gui.main_panel',
        'ppc2arm.gui.result_panel',
        'ppc2arm.gui.isa_museum',
        'ppc2arm.gui.easter_eggs',
        'ppc2arm.gui.widgets.searchable_list',
        'ppc2arm.gui.widgets.ticker_bar',
        'ppc2arm.gui.widgets.about_dialog',
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
