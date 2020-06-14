from pylogger.protocols.engines.engine import DBEngine


class MySQL(DBEngine):
    @staticmethod
    def db_version_statement() -> str:
        return "select @@version_comment;"

    @staticmethod
    def create_table_statement() -> str:
        return "Create Table If Not Exists {table}({columns});"

    @staticmethod
    def create_column_query() -> str:
        return "? ? Not Null"               # column_name type not_null

    @staticmethod
    def autoincrement_keyword() -> str:
        return "auto_increment"

    @staticmethod
    def string_keyword() -> str:
        return "Varchar"

    @staticmethod
    def timestamp_keyword() -> str:
        return "Timestamp"

    @staticmethod
    def int_keyword() -> str:
        return "Int"
