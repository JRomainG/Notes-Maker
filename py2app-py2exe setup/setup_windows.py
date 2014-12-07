from distutils.core import setup
import py2exe
import os

DATA_FILES = [('LICENSE'),

              ('ext', ['ext/__init__.py']),
              ('ext', ['ext/datetime.py']),
              ('ext', ['ext/find.py']),
              ('ext', ['ext/table.py']),
              ('ext', ['ext/wordcount.py']),

              ('icons', ['icons/abbreviations.png']),
              ('icons', ['icons/align-center.png']),
              ('icons', ['icons/align-center.png']),
              ('icons', ['icons/align-justify.png']),
              ('icons', ['icons/align-left.png']),
              ('icons', ['icons/align-right.png']),
              ('icons', ['icons/bold.png']),
              ('icons', ['icons/bullet.png']),
              ('icons', ['icons/calender.png']),
              ('icons', ['icons/count.png']),
              ('icons', ['icons/dedent.png']),
              ('icons', ['icons/find.png']),
              ('icons', ['icons/font-color.png']),
              ('icons', ['icons/font-size.png']),
              ('icons', ['icons/highlight.png']),
              ('icons', ['icons/icon.png']),
              ('icons', ['icons/image.png']),
              ('icons', ['icons/indent.png']),
              ('icons', ['icons/italic.png']),
              ('icons', ['icons/new.png']),
              ('icons', ['icons/number.png']),
              ('icons', ['icons/open.png']),
              ('icons', ['icons/preview.png']),
              ('icons', ['icons/print.png']),
              ('icons', ['icons/redo.png']),
              ('icons', ['icons/save.png']),
              ('icons', ['icons/strike.png']),
              ('icons', ['icons/subscript.png']),
              ('icons', ['icons/superscript.png']),
              ('icons', ['icons/table.png']),
              ('icons', ['icons/underline.png']),
              ('icons', ['icons/undo.png'])]

OPTIONS = {'includes': ['re', 'PyQt4', 'PyQt4.QtCore', 'PyQt4.QtGui', 'sip'],
           'excludes': ['PyQt4.QtDesigner', 'PyQt4.QtNetwork', 'PyQt4.QtOpenGL', 'PyQt4.QtScript',
                        'PyQt4.QtSql', 'PyQt4.QtTest', 'PyQt4.QtWebKit', 'PyQt4.QtXml', 'PyQt4.phonon'],
           'dll_excludes': ['MSVCP90.dll'],
           'optimize': 2,
           'bundle_files': 1,
           'compressed': True}


setup(name="Notes Maker",
      version="1.0",
      author="Jean-Romain Garnier",
      data_files=DATA_FILES,
      options={"py2exe": OPTIONS},
      scripts=["NotesMaker.py"],
      windows=[{"script": "NotesMaker.py",
                "icon_resources": [(0, 'icon.ico')]}])
