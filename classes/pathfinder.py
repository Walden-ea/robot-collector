import enum
import classes.window

class Mode(enum.Enum):
    #   todo можно вынести в отдельный класс с конфигом
    ROAMING = 0  # патрулирует
    CARRYING = 1  # несет мусор к контейнеру


class Pathfinder:
    '''
    todo docs
    '''
    def __init__(self):
        self.mode = Mode.ROAMING

    def start_roaming(self):
        self.mode = Mode.ROAMING

    def start_carrying(self):
        self.mode = Mode.CARRYING
