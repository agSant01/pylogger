from typing import List, Dict, Type
from ..db import ColumnMeta
from ...formats import Format


class DbSchema:
    def __init__(self, table: str='Log', log_column: str='log', log_type_column: str='log_type', columns: Dict[str, Type[Format]] or List[ColumnMeta] or List[Format]=None):
        if table is None:
            raise ValueError("Table Name cannot be null")

        if log_column is None:
            raise ValueError("Log column name cannot be null")

        if log_type_column is None:
            raise ValueError("Log type column name cannot be null")

        self._table_name: str = table
        self.log_column: str = log_column
        self.log_type_column = log_type_column

        self._column_metadata: List[ColumnMeta] = list()

        if columns is None:
            return

        if isinstance(columns, list):
            if isinstance(columns[0], ColumnMeta):
                self._column_metadata.extend(columns)
            elif isinstance(columns[0], Format):
                for _format in columns:
                    self._column_metadata.append(ColumnMeta(_format.get_name(), _format))
            else:
                raise ValueError("Not a ColumnMeta object")
        else:
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
