# -*- coding: utf-8 -*-

# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': ['atexit'],
        'packages': ['modbus_tk']
    }
}

executables = [
    Executable('pyModSlaveQt.py', base=base)
]

setup(name='pyModSlave',
      version='0.3.7',
      description='pyModSlave - Modbus RTU-TCP slave',
      options=options,
      executables=executables
      )