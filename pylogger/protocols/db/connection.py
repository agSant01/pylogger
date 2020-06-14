from typing_extensions import Protocol
from pylogger.protocols.db.cursor import Cursor


class Connection(Protocol):
    def close(self) -> None:
        ...

    def commit(self) -> None:
        ...

    def cursor(self) -> Cursor:
        ...
