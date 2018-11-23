from pylogger.formats.format import Format
import inspect

STEPS_TO_CALLER = 5


class FunctionCaller(Format):
    @staticmethod
    def get_name() -> str:
        return 'Function caller'

    @staticmethod
    def get_format() -> str:
        return str(inspect.stack()[STEPS_TO_CALLER][0].f_code.co_name)


class FileCaller(Format):
    @staticmethod
    def get_name() -> str:
        return 'File caller'

    @staticmethod
    def get_format() -> str:
        return str(inspect.stack()[STEPS_TO_CALLER][1]).split('/').pop()


class ClassCaller(Format):
    @staticmethod
    def get_name() -> str:
        return 'Class caller'

    @staticmethod
    def get_format() -> str:
        return str(type(inspect.stack()[STEPS_TO_CALLER][0].f_locals.get('self')).__name__)


class FileLine(Format):
    @staticmethod
    def get_name() -> str:
        return 'Line Number'

    @staticmethod
    def get_format() -> str:
        return str(inspect.stack()[STEPS_TO_CALLER][2])
