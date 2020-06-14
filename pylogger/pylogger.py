from .transporters import Transporter
from pylogger.transporters import Console

from pylogger.messages import Log, JsonLog
from pylogger.levels import Levels

from pylogger.formats.format import Format
from pylogger.formats.loggername import LoggerName
from pylogger.formats.type import LogType

from typing import List, Dict
from . import utils


class PyLogger:
    def __init__(self, input_formats: List[Format] or Format=None,
                 transporters: List[Transporter] or Format=Console(),
                 json: bool=False, level: Levels=Levels.VERBOSE, name: str=None):
        if json is False:
            self._msg = Log()
        else:
            self._msg = JsonLog()
        self._fmts: List[Format] = utils.to_list(input_formats)
        self._transporters: Dict[str, Transporter] = self.__set_transporters__(utils.to_list(transporters))
        self._level = level

        self._name = name
        self.log_type = LogType()
        if self._name is not None:
            self._fmts.append(LoggerName(self._name))

    def log(self, message: str, level: Levels = None, trans_id: str=None) -> None:
        if level is None:
            raise ValueError("No level assigned")

        if self.__is_level_valid__(level) is False:
            return

        self.log_type.set_type(level)
        self._msg.add_info(self._fmts)
        self._msg.set_message(message, level)

        if trans_id is None:
            self.__log_to_all__(level)
        else:
            self.__log_to_id__(level, trans_id)

    def __log_to_id__(self, level, trans__id):
        transport: Transporter = self._transporters.get(trans__id)
        if transport is None:
            raise ValueError('Transport with ID: {} does not exists'.format(trans__id))

        if transport.is_level_valid(level):
            transport.transport(self._msg)

    def __log_to_all__(self, level):
        for trans_id, trans in self._transporters.items():
            if trans.is_level_valid(level):
                trans.transport(self._msg)

    def add_transporter(self, transport: Transporter) -> None:
        if not isinstance(transport, Transporter):
            raise TypeError('Not instance of Transport.class')
        trans_id: str = transport.get_id()
        if trans_id in self._transporters:
            raise ValueError('ID: `{}` for transporter is already in use'.format(trans_id))
        transport.set_id(utils.id_generator())
        self._transporters.update({transport.get_id(): transport})

    def error(self, message: str, trans_id: str=None) -> None:
        self.log(message, Levels.ERROR, trans_id)

    def warn(self, message: str, trans_id: str=None) -> None:
        self.log(message, Levels.WARN, trans_id)

    def info(self, message: str, trans_id: str=None) -> None:
        self.log(message, Levels.INFO, trans_id)

    def verbose(self, message: str, trans_id: str=None) -> None:
        self.log(message, Levels.VERBOSE, trans_id)

    def debug(self, message: str, trans_id: str=None) -> None:
        self.log(message, Levels.DEBUG, trans_id)

    def __set_transporters__(self, transporters: List[Transporter]) -> Dict[str, Transporter]:
        dict_of_transporters: Dict[str, Transporter] = dict()

        for transporter in transporters:
            trans_id: str = transporter.get_id()
            if trans_id in dict_of_transporters:
                raise ValueError('ID: `{}` for transporter is already in use'.format(trans_id))
            transporter.set_id(utils.id_generator())
            transporter.set_owner(self)
            dict_of_transporters.update({transporter.get_id(): transporter})
        return dict_of_transporters

    def __is_level_valid__(self, level: Levels) -> bool:
        if level < self._level:
            return False
        return True
