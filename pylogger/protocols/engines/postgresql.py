from pylogger.protocols.engines.engine import DBEngine


class PostgreSQL(DBEngine):
    @staticmethod
    def db_version_statement() -> str:
        return 'select version();'

    @staticmethod
    def create_table_statement() -> str:
        return 'if not exists(select * ' \
               'from   pg_tables'\
                'where  schemaname = "Public"'\
                'and    tablename = "?")' \
                'then' \
               'Create Table ?({columns});' \
               'end if;'

    @staticmethod
    def create_column_query() -> str:
        return '? ? Not Null'               # column_name type not_null

    @staticmethod
    def autoincrement_keyword() -> str:
        return 'Serial'

    @staticmethod
    def string_keyword() -> str:
        return 'Varchar'

    @staticmethod
    def timestamp_keyword() -> str:
        return 'Timestamp'

    @staticmethod
    def int_keyword() -> str:
        return 'Integer'
