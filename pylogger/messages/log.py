from pylogger.formats.format import Format


class Log:
    def __init__(self):
        self._additional_info = []

    def add_info(self, info_format):
        if info_format is None:
            return

        if isinstance(info_format, list):
            for fmt in info_format:
                self.__add_format__(fmt)
        else:
            self.__add_format__(info_format)

    def get_log(self, message):
        msg = 'Log: "{}"'.format(message)
        for info in self._additional_info:
            msg += ', ' + info
        return msg

    def __add_format__(self, fmt):
        if not isinstance(fmt, type(Format)):
            raise TypeError('Argument is not of type Format')
        info_to_add = '{}: {}'.format(fmt.get_name(), fmt.get_format())
        self._additional_info.append(info_to_add)
