from .transporter import Transporter
from ..levels import Levels
from ..messages.log import Log


class Console(Transporter):
    def __init__(self, level: Levels=None, same_level: bool=True, trans_id: str=None):
        super().__init__(level, same_level, trans_id)

    def transport(self, log: Log) -> None:
        print(log.get_log() + ',')
