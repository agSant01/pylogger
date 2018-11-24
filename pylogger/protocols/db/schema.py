from typing import List, Dict, Type
from ..db import ColumnMeta
from ...formats import Format


class DbSchema:
    def __init__(self, table: str, log_column: str, log_type_column: str, columns: Dict[str, Type[Format]]):
        self._table_name: str = table
        self.log_column: str = log_column
        self.log_type_column = log_type_column

        self._column_metadata: List[ColumnMeta] = list()
        for name, fmt in columns.items():
            self._column_metadata.append(ColumnMeta(name, fmt))

    def table(self) -> str:
        return self._table_name

    def column_metadata(self) -> List[ColumnMeta]:
        return self._column_metadata

    def __repr__(self):
        return 'Table: {}\nLog Column: {}\nLog Type Column: {}\nColumns: {}'.format(
            self._table_name,
            self.log_column,
            self.log_type_column,
            self._column_metadata
        )
