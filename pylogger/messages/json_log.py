from pylogger.messages import Log
import json


class JsonLog(Log):
    def __init__(self):
        super().__init__()

    def get_log(self) -> str:
        data = dict()
        data.update({'log': self.message.replace('"', "'")})

        for fmt in self._additional_info:
            key = fmt.get_name()
            info = fmt.get_format()

            data.update({key: info})

        return str(json.dumps(data))
