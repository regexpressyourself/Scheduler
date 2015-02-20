# -*- mode: python -*-
a = Analysis(['scheduler.py'],
             pathex=['/home/zookeeprr/documents/Scheduler'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='scheduler',
          debug=False,
          strip=None,
          upx=True,
          console=True )
