from pylogger.formats.format import Format
from pylogger.messages import Log


class JsonLog(Log):
    def __init__(self):
        super().__init__()
        self._key_dict = dict()

    def get_log(self, message):
        self._key_dict.update({'log': message})
        return self._key_dict

    def __add_format__(self, fmt):
        if not isinstance(fmt, type(Format)):
            raise TypeError('Argument is not of type Format')
        key = fmt.get_name()
        info = fmt.get_format()

        self._key_dict.update({key: info})

