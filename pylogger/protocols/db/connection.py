from typing_extensions import Protocol
from pylogger.protocols.db import cursor


class Connection(Protocol):
    def close(self) -> None:
        ...

    def commit(self) -> None:
        ...

    def cursor(self) -> cursor:
        ...
