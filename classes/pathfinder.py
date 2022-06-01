import enum
import classes.window
from pygame import math

from classes import helper

class Mode(enum.Enum):
    #   todo можно вынести в отдельный класс с конфигом
    ROAMING = 0  # патрулирует
    CARRYING = 1  # несет мусор к контейнеру


class Pathfinder:
    '''
    todo docs
    '''
    def __init__(self, robot):
        self.mode = Mode.ROAMING
        #self.spiral_count = 1 -- если пытаться протащить его по спирали, то какой-то говнокод получается так что я не буду
        x = robot.radius//2 + 1
        y = robot.radius // 2 + 1
        if helper.can_be_placed_at(x, y):
            self.target_x = x
            self.target_y = y
        else: #todo надо тогда двигать, чо ниже заготовка чтобы оно не ругалось
            self.target_x = x
            self.target_y = y


    def start_roaming(self):
        self.mode = Mode.ROAMING

    def start_carrying(self):
        self.mode = Mode.CARRYING

    #def set_up_spiral_movement(self, Robot): куда разумнее вбить метод движения к цели (любой) и потом уже отдельно выбирать цель

    def go_to_target(self,robot):  # todo возможно проще координаты робота хранить в виде вектора я хз
        v = (math.Vector2(self.target_x, self.target_y) - math.Vector2(robot.x, robot.y))
        print("dest: "+ str(v.x)+", "+str(v.y))
        # v.scale_to_length((math.Vector2(robot.velocity)).length()) todo раскомментировать когда разберемся с навсистемой
        v.scale_to_length(10)
        print("dest scaled: "+ str(v.x)+", "+str(v.y))
        robot.velocity = v
        print(self.target_x)
        print(self.target_y)
        print(robot.velocity)
