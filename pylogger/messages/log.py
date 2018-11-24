from pylogger.formats.format import Format
from pylogger.levels import Levels
from typing import List


class Log:
    def __init__(self):
        self._additional_info: List[Format] = []
        self.message: str = None
        self._level: Levels = None

    def has_format(self, fmt: Format) -> bool:
        return fmt.get_name() in [f.get_name() for f in self._additional_info]

    def set_message(self, message, level: Levels):
        self.message = message
        self._level = level

    @property
    def level(self):
        return self._level.name.lower()

    def add_info(self, info_format: List[Format]):
        if info_format is None:
            return

        self._additional_info = info_format

    def get_log(self) -> str:
        msg = 'Log: "{}"'.format(self.message)

        for fmt in self._additional_info:
            name = fmt.get_name()
            data = fmt.get_format()
            info_to_add: str = '{}: {}'.format(name, data)

            msg += ', ' + info_to_add
        return msg
