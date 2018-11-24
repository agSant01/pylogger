from pylogger.protocols.db import Cursor, Connection, DbSchema
from pylogger.transporters import Transporter, FileTransporter
from pylogger.pylogger import PyLogger
from pylogger.messages import Log
from pylogger.levels import Levels
from pylogger import formats


class DbTransporter(Transporter):
    _db_conn: Connection
    insert_query = "INSERT INTO {table}({columns}) VALUES('{value}');"

    def __init__(self, db_conn: Connection, schema: DbSchema,
                 level: Levels = None, same_level: bool = True, trans_id: str = None):
        super().__init__(level, same_level, trans_id)
        self._db_schema = schema
        self._db_conn = db_conn

    # noinspection PyBroadException
    def transport(self, log: Log):

        # add log column
        column_str: str = self._db_schema.log_column
        values_str: str = log.message

        # add log type column
        column_str += ', ' + self._db_schema.log_type_column
        values_str += "','" + log.level

        column_str += ', ' + ', '.join(column.name for column in self._db_schema.column_metadata() if log.has_format(column.type))
        values_str += "','" + "','".join(
            column.type.get_format()
            .replace(";", '[semicolon]')
            .replace('--', '[doubledash]')
            .replace("'", '"')
            for column in self._db_schema.column_metadata()
            if log.has_format(column.type)
        )

        try:
            cursor: Cursor = self._db_conn.cursor()

            query = DbTransporter.insert_query.format(
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
