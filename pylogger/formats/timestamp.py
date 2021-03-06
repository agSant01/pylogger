from pylogger.formats.format import Format
import time


class Timestamp(Format):
        @staticmethod
        def get_name() -> str:
            return 'timestamp'

        @staticmethod
        def get_format() -> str:
            return time.asctime(time.gmtime(time.time()))
