from __future__ import annotations

import logging

from installer.base import BaseInstaller


log = logging.getLogger(__name__)


class GitInstaller(BaseInstaller):
    def __init__(self) -> None:
        super().__init__()

        self.url = 'https://git-scm.com/download/win'
        self.installer = 'Git-setup.exe'

    def __repr__(self) -> str:
        return 'git'

    def __str__(self) -> str:
        return 'git'

    def download(self) -> None:
        log.info(f"Downloading Git from {self.url}...")

        command = [
            'curl',
            '-o',
            self.installer,
            self.url
        ]

        self.run(command)

    def install(self) -> None:
        log.info(f"Installing Git from {self.installer}...")

        command = [
            self.installer,
            '/VERYSILENT'
        ]

        self.run(command)
