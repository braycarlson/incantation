from __future__ import annotations

import json
import logging

from constant import DOWNLOAD
from installer.base import BaseInstaller


log = logging.getLogger(__name__)


class AlacrittyInstaller(BaseInstaller):
    def __init__(self) -> None:
        super().__init__()

        self.url = 'https://api.github.com/repos/alacritty/alacritty/releases/latest'
        self.installer = DOWNLOAD / 'alacritty-installer.msi'

    def __repr__(self) -> str:
        return 'alacritty'

    def __str__(self) -> str:
        return 'alacritty'

    def download(self) -> None:
        log.info(f"Fetching latest release from {self.url}...")

        release = DOWNLOAD / 'release.json'

        command = [
            'curl',
            '-s',
            self.url,
            '-o',
            str(release)
        ]

        self.run(command)

        with release.open('r', encoding='utf-8') as handle:
            file = json.load(handle)

            download = next(
                asset['browser_download_url']
                for asset in file['assets']
                if asset['name'].endswith('.msi')
            )

        log.info(f"Latest installer URL: {download}")

        command = [
            'curl',
            '-L',
            download,
            '-o',
            str(self.installer)
        ]

        self.run(command)
        release.unlink()

    def install(self) -> None:
        log.info(f"Installing Alacritty from {self.installer}...")

        command = [
            'msiexec',
            '/i',
            str(self.installer)
        ]

        self.run(command)
        self.installer.unlink()
