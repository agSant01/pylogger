from pylogger.protocols.db import Cursor, Connection, DbSchema
from pylogger.transporters import Transporter, FileTransporter
from pylogger.pylogger import PyLogger
from pylogger.messages import Log
from pylogger.levels import Levels
from pylogger import formats


class DbTransporter(Transporter):
    db_conn: Connection
    insert_query = "INSERT INTO {table}({columns}) VALUES('{value}');"

    def __init__(self, db_conn: Connection, table: str, column: str,
                 level: levels.Levels=None, same_level: bool=True, trans_id: str=None):
        super().__init__(level, same_level, trans_id)
        self.table = table
        self.column = column
        self.db_conn = db_conn

    # noinspection PyBroadException
    def transport(self, message: object):
        try:
            cursor: Cursor = self.db_conn.cursor()

            query = DbTransporter.insert_query.format(
                columns=self.column,
                table=self.table,
                value=str(message).replace(";", '[semicolon]').replace('--', '[doubledash]').replace("'", '"')
            )
            cursor.execute(query)

            self.db_conn.commit()
            cursor.close()
            cursor = None
            del cursor
        except Exception as e:
            pylogger.PyLogger(
                input_formats=[
                    pylogger.formats.Timestamp,
                    pylogger.formats.FileLine,
                    pylogger.formats.FileCaller,
                    pylogger.formats.ClassCaller
                ],
                transporters=pylogger.transporters.FileTransporter('txt/db_error.log'),
                json=True,
                level=pylogger.Levels.ERROR
            ).error(str(e))
