from pylogger.transporters.transporter import Transporter
from ..levels import Levels


class FileTransporter(Transporter):
    def __init__(self, filename: str, level: Levels=None, same_level: bool=True):
        super().__init__(level, same_level)
        self.filename = filename

    def transport(self, message: object) -> None:
        f = open(self.filename, '+a')
        f.write(str(message) + '\n')
        f.close()
