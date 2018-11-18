from pylogger.transporters.transporter import Transporter
from ..levels import Levels


class Console(Transporter):
    def __init__(self, level: Levels=None, same_level: bool=True):
        super().__init__(level, same_level)

    def transport(self, message: object) -> None:
        print(str(message))
