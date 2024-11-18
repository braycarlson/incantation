from __future__ import annotations

import logging

from constant import DOWNLOAD
from installer.base import BaseInstaller


log = logging.getLogger(__name__)


class FirefoxInstaller(BaseInstaller):
    def __init__(self) -> None:
        super().__init__()

        self.installer = DOWNLOAD / 'firefox.exe'
        self.url = 'https://download.mozilla.org/?product=firefox-stub&os=win64&lang=en-CA'

    def __repr__(self) -> str:
        return 'firefox'

    def __str__(self) -> str:
        return 'firefox'

    def download(self) -> None:
        log.info(f"Downloading Firefox installer from {self.url}...")

        command = [
            'curl',
            '-L',
            self.url,
            '-o',
            str(self.installer)
        ]

        self.run(command)

    def install(self) -> None:
        log.info(f"Installing Firefox from {self.installer}...")

        command = [
            'start',
            '/wait',
            '',
            str(self.installer),
            '/silent',
            '/install'
        ]

        self.run(command)
        self.installer.unlink()
