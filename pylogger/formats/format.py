class Format:
    @staticmethod
    def get_name() -> str:
        raise NotImplementedError()

    @staticmethod
    def get_format() -> str:
        raise NotImplementedError()

    @staticmethod
    def get_db_column_length() -> str:
        raise NotImplementedError()

