from pylogger.formats import Format
from pylogger.levels import Levels


class LogType(Format):
    def __init__(self):
        self.log_type = None

    def set_type(self, level: Levels):
        self.log_type = level

    @staticmethod
    def get_name() -> str:
        return 'Log type'

    def get_format(self) -> str:
        return self.log_type.name.lower()
