from pylogger.formats.format import Format
from pylogger.messages import Log
import json


class JsonLog(Log):
    def __init__(self):
        super().__init__()
        self._key_dict = dict()

    def get_log(self, message: str) -> str:
        self._key_dict.update({'log': message.replace('"', "'")})
        return str(json.dumps(self._key_dict))

    def __add_format__(self, fmt: Format) -> None:
        key = fmt.get_name()
        info = fmt.get_format()

        self._key_dict.update({key: info})
