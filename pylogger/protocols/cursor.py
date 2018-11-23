from abc import abstractmethod
from typing_extensions import Protocol


class Cursor(Protocol):
    @abstractmethod
    def close(self) -> None:
        ...

    @abstractmethod
    def execute(self, *args) -> object:
        raise NotImplementedError()

    @abstractmethod
    def executemany(self) -> None:
        ...
