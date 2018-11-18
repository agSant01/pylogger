from ..levels import Levels


class Transporter:
    def __init__(self, level: Levels=None, same_level: bool=True):
        self.level = level
        self.same_level = same_level

    def transport(self, message: object):
        raise NotImplementedError()

    def is_level_valid(self, level: Levels) -> bool:
        if self.level is None:
            return True

        if self.same_level:
            if self.level is level:
                return True
            else:
                return False

        if self.level < level:
            return False

        return True
