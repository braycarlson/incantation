from __future__ import annotations

import logging
import subprocess

from abc import ABC, abstractmethod
from constant import (
    ROAMING_APPDATA,
    LOCAL_APPDATA,
    PROGRAM_FILES,
    PROGRAM_FILES_x86
)
from pathlib import Path


log = logging.getLogger(__name__)


class BaseInstaller(ABC):
    def __init__(self) -> None:
        self.roaming_appdata = Path(ROAMING_APPDATA)
        self.local_appdata = Path(LOCAL_APPDATA)
        self.program_files = Path(PROGRAM_FILES)
        self.program_files_x86 = Path(PROGRAM_FILES_x86)

    @abstractmethod
    def download(self) -> None:
        raise NotImplementedError

    def preinstall(self) -> None:
        pass

    @abstractmethod
    def install(self) -> None:
        raise NotImplementedError

    def postinstall(self) -> None:
        pass

    def run(self, command: list[str]) -> None:
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as exception:
            message = f"There was an error while running the command: {command}"

            log.warning(message)
            log.warning(exception)
