from ..levels import Levels


class Transporter:
    def __init__(self, level: Levels=None, same_level: bool=True, trans_id: str=None):
        self.logger = None
        self.trans_id: str = trans_id
        self.level: Levels = level
        self.same_level: bool = same_level

    def transport(self, message: object):
        raise NotImplementedError()

    def get_id(self):
        return self.trans_id

    def set_id(self, trans_id: str):
        if self.trans_id is None:
            self.trans_id = trans_id
        else:
            raise ValueError('ID for transporter is already set. Cannot modify')

    def set_owner(self, owner):
        self.logger = owner

    def get_type(self) -> str:
        return str(type(self).__name__)

    def is_level_valid(self, level: Levels) -> bool:
        if self.level is None:
            return True

        if self.same_level:
            if self.level is level:
                return True
            else:
                return False

        if self.level > level:
            return False

        return True
