from pylogger.formats import Format
from pylogger.levels import Levels


class LogType(Format):
    def __init__(self, log_type: Levels):
        self.log_type = log_type

    @staticmethod
    def get_name() -> str:
        return 'Log type'

    def get_format(self) -> str:
        return self.log_type.name.lower()
