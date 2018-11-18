from .format import Format


class LoggerName(Format):
    def __init__(self, name: str=None):
        self.name = name

    @staticmethod
    def get_name() -> str:
        return 'Logger Name'

    def get_format(self) -> str:
        return self.name
