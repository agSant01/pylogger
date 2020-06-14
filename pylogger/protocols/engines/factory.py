from pylogger.protocols.db.connection import Connection, Cursor
from pylogger.protocols.engines.mysql import MySQL
from pylogger.protocols.engines.mssql import SqlServer
from pylogger.protocols.engines.postgresql import PostgreSQL
from pylogger.protocols.engines.engine import DBEngine

import mysql.connector


def create_engine(connection: Connection) -> DBEngine or None:
    cursor: Cursor = connection.cursor()

    # try PostgresSQL
    try:
        cursor.execute(PostgreSQL.db_version_statement())
        result = cursor.fetchone()

        if result:
            if 'postgresql' in result[0].lower():
                return PostgreSQL()

    except BaseException as e:
        if 'ProgrammingError' in str(repr(e)):
            pass
        else:
            raise e

    # try MySQL
    try:
        cursor = connection.cursor()
        cursor.execute(MySQL.db_version_statement())

        result = cursor.fetchone()

        if result:
            if 'mysql' in result[0].lower():
                return MySQL()

    except BaseException as e:
        if 'ProgrammingError' in str(repr(e)):
            pass
        else:
            raise e

    # try SQL Server
    try:
        cursor.execute(SqlServer.db_version_statement())
        result = cursor.fetchone()
        if result:
            if 'microsoft sql server' in result[0].lower():
                return SqlServer()

    except BaseException as e:
        if 'ProgrammingError' in str(repr(e)):
            pass
        else:
            raise e

    return None


if __name__ == '__main__':

    con = mysql.connector.connect(host='localhost', database='Hi', user='root', password='gab-Santiag0')

    engine = create_engine(con)

    print(engine)

    con.close()
