from pylogger.formats.format import Format
import time


class Timestamp(Format):
        @staticmethod
        def get_name():
            return 'timestamp'

        @staticmethod
        def get_format():
            return time.asctime(time.gmtime(time.time()))
