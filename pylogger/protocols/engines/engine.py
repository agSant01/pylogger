class DBEngine:
    @staticmethod
    def db_version_statement() -> str:
        raise NotImplementedError()

    @staticmethod
    def create_table_statement() -> str:
        raise NotImplementedError()

    @staticmethod
    def create_column_query() -> str:
        raise NotImplementedError()

    @staticmethod
    def autoincrement_keyword() -> str:
        raise NotImplementedError()

    @staticmethod
    def string_keyword() -> str:
        raise NotImplementedError()

    @staticmethod
    def timestamp_keyword() -> str:
        raise NotImplementedError()

    @staticmethod
    def int_keyword() -> str:
        raise NotImplementedError()
