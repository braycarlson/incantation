from __future__ import annotations

import logging

from constant import LOG
from contextlib import contextmanager
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, Generator


@contextmanager
def logger() -> Generator[None, Any, None]:
    try:
        log = logging.getLogger()
        log.setLevel(logging.DEBUG)

        path = LOG / 'incantation.log'
        path.touch(exist_ok=True)

        file_handler = logging.FileHandler(
            filename=path,
            encoding='utf-8',
        )

        stream_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            '[{asctime}] [{levelname}] {name}: {message}',
            '%Y-%m-%d %I:%M:%S %p',
            style='{',
        )

        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(logging.DEBUG)

        log.addHandler(file_handler)
        log.addHandler(stream_handler)

        yield
    finally:
        for handler in log.handlers:
            handler.close()
            log.removeHandler(handler)
