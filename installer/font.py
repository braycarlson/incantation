from __future__ import annotations

import logging

from constant import DOWNLOAD, FONT
from installer.base import BaseInstaller


log = logging.getLogger(__name__)


class FontInstaller(BaseInstaller):
    def __init__(self) -> None:
        super().__init__()

        self.url = "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/FiraCode.zip"
        self.zip = DOWNLOAD / 'FiraCode.zip'
        self.extraction = DOWNLOAD / 'FiraCode'

    def __repr__(self) -> str:
        return 'font'

    def __str__(self) -> str:
        return 'font'

    def download(self) -> None:
        log.info(f"Downloading FiraCode Nerd Font from {self.url}...")

        command = [
            'curl',
            '-L',
            self.url,
            '-o',
            str(self.zip)
        ]

        self.run(command)

    def install(self) -> None:
        self.preinstall()

        log.info("Extracting and installing FiraCode Nerd Font...")

        self.extraction.mkdir(parents=True, exist_ok=True)

        command = [
            'tar',
            '-xf',
            str(self.zip),
            '-C',
            str(self.extraction)
        ]

        self.run(command)

        command = [
            'xcopy',
            str(self.extraction / '*.ttf'),
            str(FONT),
            '/Y'
        ]

        self.run(command)

        self.postinstall()

    def postinstall(self) -> None:
        for file in self.extraction.glob("*"):
            file.unlink()

        self.extraction.rmdir()
        self.zip.unlink()
