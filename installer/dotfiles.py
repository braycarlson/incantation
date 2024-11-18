from __future__ import annotations

import logging

from constant import (
    DOTFILES,
    LOCALAPPDATA,
    PERSONAL,
    ROAMING_APPDATA
)
from installer.base import BaseInstaller


log = logging.getLogger(__name__)


class DotfilesInstaller(BaseInstaller):
    def __init__(self) -> None:
        super().__init__()

        self.url = 'https://github.com/braycarlson/dotfiles'

    def __repr__(self) -> str:
        return 'dotfiles'

    def __str__(self) -> str:
        return 'dotfiles'

    def download(self) -> None:
        log.info('Cloning the dotfiles repository...')

        if not DOTFILES.exists():
            command = [
                'git',
                'clone',
                self.url,
                str(DOTFILES)
            ]

            self.run(command)
        else:
            log.info("Dotfiles repository already exists.")

    def install(self) -> None:
        log.info('Preparing directories for symbolic links...')

        symlinks = {
            LOCALAPPDATA / 'nvim': self.dotfiles_dir / 'nvim',
            ROAMING_APPDATA / 'alacritty': self.dotfiles_dir / 'alacritty',
            PERSONAL / 'backup/registry': self.dotfiles_dir / 'registry',
            PERSONAL / 'backup/aliases.bat': self.dotfiles_dir / 'aliases.bat',
        }

        for symlink in symlinks:
            if symlink.exists() or symlink.is_symlink():
                log.info(f"Removing existing directory or link: {symlink}")

                if symlink.is_dir():
                    symlink.rmdir()
                else:
                    symlink.unlink()

        for target, source in symlinks.items():
            log.info(f"Creating symbolic link: {target} -> {source}")

            target.parent.mkdir(parents=True, exist_ok=True)

            target.symlink_to(
                source,
                target.is_dir()
            )

        log.info('Dotfiles installation and symlink creation complete.')
