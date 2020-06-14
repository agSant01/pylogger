from pylogger.protocols.engines.engine import DBEngine


class SqlServer(DBEngine):

    @staticmethod
    def db_version_statement() -> str:
        return "Select @@version;"

    @staticmethod
    def create_table_statement() -> str:
        return "If Not Exists (Select * from sys.tables where name = ?) create table ? ({columns});"

    @staticmethod
    def create_column_query() -> str:
        return "? ? not null"

    @staticmethod
    def autoincrement_keyword() -> str:
        return "identity(1,1)"

    @staticmethod
    def string_keyword() -> str:
        return "Varchar"

    @staticmethod
    def timestamp_keyword() -> str:
        return "Datetime"

    @staticmethod
    def int_keyword() -> str:
        return "Int"