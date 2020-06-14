from abc import abstractmethod
from typing_extensions import Protocol


class Cursor(Protocol):
    @abstractmethod
    def close(self) -> None:
        ...

    @abstractmethod
    def execute(self, *args) -> object:
        ...

    @abstractmethod
    def executemany(self) -> None:
        ...

    @abstractmethod
    def fetchone(self):
        ...

    @abstractmethod
    def fetchmany(self):
        ...
