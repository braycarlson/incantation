from __future__ import annotations

import os

from constant import CWD
from installer.alacritty import AlacrittyInstaller
from installer.dotfiles import DotfilesInstaller
from installer.font import FontInstaller
from installer.firefox import FirefoxInstaller
from installer.git import GitInstaller
from log import logger


def main() -> None:
    os.environ.setdefault(
        'PYTHONPATH',
        str(CWD)
    )

    installers = [
        GitInstaller(),
        AlacrittyInstaller(),
        FirefoxInstaller(),
        FontInstaller(),
        DotfilesInstaller()
    ]

    for installer in installers:
        installer.download()
        installer.install()


if __name__ == '__main__':
    with logger():
        main()
