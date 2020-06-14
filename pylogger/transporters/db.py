from pylogger.protocols.db import Cursor, Connection, DbSchema, ColumnMeta
from pylogger.transporters import Transporter, FileTransporter
from pylogger.pylogger import PyLogger
from pylogger.messages import Log
from pylogger.levels import Levels
from pylogger import formats
from typing import List


class DbTransporter(Transporter):
    _log_column_length = 200
    _db_conn: Connection
    _insert_query = "INSERT INTO {table}({columns}) VALUES('{value}');"
    _create_table_query = "Create Table {table}({columns});"
    _create_column_query = "? ? ? NOT NULL"

    def __init__(self, db_conn: Connection, schema: DbSchema=None,
                 level: Levels = None, same_level: bool = True, trans_id: str = None):
        super().__init__(level, same_level, trans_id)
        self._db_schema = schema or DbSchema()
        self._db_conn = db_conn

    def __create_table__(self):
        cursor: Cursor = self._db_conn.cursor()

        query = "Create Table {table} (" \
                "  {name1} VARCHAR(200)" \
                ");"


    # noinspection PyBroadException
    def transport(self, log: Log):
        columns_data: List[ColumnMeta] = self._db_schema.column_metadata()

        if columns_data is None:
            columns_data = [ColumnMeta(_format.get_name(), _format) for _format in log.formats()]

        # add log column
        column_str: str = self._db_schema.log_column
        values_str: str = log.message

        # add log type column
        column_str += ', ' + self._db_schema.log_type_column
        values_str += "','" + log.level

        column_str += ', ' + ', '.join(column.name for column in columns_data)
        values_str += "','" + "','".join(
            column.type.get_format()
            .replace(";", '[semicolon]')
            .replace('--', '[doubledash]')
            .replace("'", '"')
            for column in columns_data
            if log.has_format(column.type)
        )

        try:
            cursor: Cursor = self._db_conn.cursor()

            query = DbTransporter._insert_query.format(
                columns=column_str,
                table=self._db_schema.table(),
                value=values_str

            )
            cursor.execute(query)

            self._db_conn.commit()
            cursor.close()
            cursor = None
            del cursor
        except Exception as e:
            data = {
                'message': log.get_log(),
                'not_logged_because': e
            }
            PyLogger(
                input_formats=[
                    formats.Timestamp,
                    formats.FileLine,
                    formats.FileCaller,
                    formats.ClassCaller
                ],
                transporters=FileTransporter('txt/db_error.log'),
                json=True,
                level=Levels.ERROR
            ).error(str(data))
