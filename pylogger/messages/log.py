from pylogger.formats.format import Format
from typing import List


class Log:
    def __init__(self):
        self._additional_info: List[str] = []

    def add_info(self, info_format: List[Format]):
        if info_format is None:
            return

        self._additional_info.clear()
        for fmt in info_format:
            self.__add_format__(fmt)

    def get_log(self, message: str) -> str:
        msg = 'Log: "{}"'.format(message)
        for info in self._additional_info:
            msg += ', ' + info
        return msg

    def __add_format__(self, fmt: Format) -> None:
        info_to_add: str = '{}: {}'.format(fmt.get_name(), fmt.get_format())
        self._additional_info.append(info_to_add)
