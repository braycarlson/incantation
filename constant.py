from __future__ import annotations

import os
import sys

from pathlib import Path


CWD = Path(__file__).resolve().parent

if sys.platform == 'win32':
    VENV = CWD / '.venv' / 'Scripts' / 'python'
else:
    VENV = CWD / '.venv' / 'bin' / 'python'

LOG = CWD / 'log'
LOG.mkdir(exist_ok=True, parents=True)

HOME = Path.home()
DOWNLOAD = HOME / 'Documents'
ROAMING_APPDATA = os.environ.get('APPDATA')
LOCAL_APPDATA = os.environ.get('LOCALAPPDATA')
PROGRAM_FILES = os.environ.get('PROGRAMFILES', 'C:/Program Files')
PROGRAM_FILES_x86 = os.environ.get('PROGRAMFILES(X86)', 'C:/Program Files (x86)')
FONT = Path(LOCAL_APPDATA) / 'Microsoft' / 'Windows' / 'Fonts'

CODE = Path('E:/code')
PERSONAL = CODE / 'personal'
WORK = CODE / 'work'

DOTFILES = PERSONAL / 'dotfiles'
