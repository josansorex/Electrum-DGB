# -*- mode: python -*-
a = Analysis(['C:\\Users\\USer\\Desktop\\digielectrum\\digielectrum'],
             pathex=['C:\\Users\\USer\\Desktop\\digielectrum'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'DigiElectrum.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name=os.path.join('dist', 'DigiElectrum.exe.app'))
