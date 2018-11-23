from abc import abstractmethod
from typing_extensions import Protocol
from .connection import Connection


class DbModule(Protocol):
    @abstractmethod
    def connect(self) -> Connection:
        ...
