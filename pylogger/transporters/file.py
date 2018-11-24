from .transporter import Transporter
from ..levels import Levels
from ..messages.log import Log


class FileTransporter(Transporter):
    def __init__(self, filename: str, level: Levels=None, same_level: bool=True, trans_id: str=None):
        super().__init__(level, same_level, trans_id)
        self.filename = filename

    def transport(self, log: Log) -> None:
        f = open(self.filename, '+a')
        f.write(log.get_log() + ',\n')
        f.close()
