from pylogger.transporters import Console
from pylogger.messages import Log, JsonLog
from pylogger.levels import Levels


class PyLogger:
    def __init__(self, input_formats=None, transporters=Console(), json=False, level=Levels.INFO):
        if json is False:
            self.msg = Log()
        else:
            self.msg = JsonLog()
        self.fmts = input_formats
        self.trans = transporters
        self.level = level

    def log(self, message, level=None):
        if level is None:
            raise ValueError("No level assigned")

        if self.__is_level_valid__(level) is False:
            return

        self.msg.add_info(self.fmts)
        if isinstance(self.trans, list):
            for t in self.trans:
                t.transport(self.msg.get_log(message))
        else:
            self.trans.transport(self.msg.get_log(message))

    def add(self, transport):
        if not isinstance(transport, transport.Transporter):
            raise TypeError('Not instance of Transport.class')

        if isinstance(self.trans, list):
            self.trans.append(transport)
        else:
            temp = self.trans
            self.trans = []
            self.trans.append(temp)
            self.trans.append(transport)

    def error(self, message):
        self.log(message, Levels.ERROR)

    def warn(self, message):
        self.log(message, Levels.WARN)

    def info(self, message):
        self.log(message, Levels.INFO)

    def verbose(self, message):
        self.log(message, Levels.VERBOSE)

    def debug(self, message):
        self.log(message, Levels.DEBUG)

    def __is_level_valid__(self, level):
        if level < self.level:
            return False
        return True
