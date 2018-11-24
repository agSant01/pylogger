from pylogger.formats import Format
from typing import Type


class ColumnMeta:
    def __init__(self, column_name: str, column_data_type: Type[Format]):
        self.name: str = column_name
        self.type: Format = column_data_type

    def __repr__(self):
        return '[ Name: {}, Type: {} ]'.format(self.name, self.type)
