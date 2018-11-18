from pylogger.transporters import Console
from pylogger.messages import Log, JsonLog
from pylogger.levels import Levels
from pylogger.transporters.transporter import Transporter
from pylogger.formats.format import Format
from pylogger.formats.loggername import LoggerName
from typing import List


class PyLogger:
    def __init__(self, input_formats: Format or List[Format]=None,
                 transporters: List[Transporter]=Console(),
                 json: bool=False, level: Levels=Levels.INFO, name: str=None):
        if json is False:
            self._msg = Log()
        else:
            self._msg = JsonLog()
        self._fmts = PyLogger.__to_list(input_formats)
        self._trans = PyLogger.__to_list(transporters)
        self._level = level
        self._name = name

    def log(self, message: str, level: Levels=None) -> None:
        if level is None:
            raise ValueError("No level assigned")

        if self.__is_level_valid__(level) is False:
            return

        if self._name is not None:
            self._fmts.append(LoggerName(self._name))

        self._msg.add_info(self._fmts)
        for t in self._trans:
            if t.is_level_valid(level):
                t.transport(self._msg.get_log(message))

    def add_transporter(self, transport: Transporter) -> None:
        if not isinstance(transport, Transporter):
            raise TypeError('Not instance of Transport.class')

        if isinstance(self._trans, list):
            self._trans.append(transport)
        else:
            temp = self._trans
            self._trans = []
            self._trans.append(temp)
            self._trans.append(transport)

    def error(self, message: str) -> None:
        self.log(message, Levels.ERROR)

    def warn(self, message: str) -> None:
        self.log(message, Levels.WARN)

    def info(self, message: str) -> None:
        self.log(message, Levels.INFO)

    def verbose(self, message: str) -> None:
        self.log(message, Levels.VERBOSE)

    def debug(self, message: str) -> None:
        self.log(message, Levels.DEBUG)

    def __is_level_valid__(self, level: Levels) -> bool:
        if level < self._level:
            return False
        return True

    @staticmethod
    def __to_list(o: object or List[object]) -> list:
        ltr = list()
        if isinstance(o, list):
            ltr.extend(o)
        else:
            ltr.append(o)
        return ltr
