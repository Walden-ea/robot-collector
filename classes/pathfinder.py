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
    def __init__(self, robot, height, width):
        self.mode = Mode.ROAMING
        x = robot.radius + 5
        y = robot.radius + 5
        if helper.can_be_placed_at(x,y):
            self.target_x = x
            self.target_y = y
        else: #todo надо тогда двигать, чо ниже заготовка чтобы оно не ругалось
            self.target_x = x
            self.target_y = y
        self.win_height = height
        self.win_width = width
        self.roaming_targets = []
        self.set_list_of_targets(robot)
        self.target_num = 0

    def set_list_of_targets(self, robot):
        x = robot.radius+ robot.radius//5
        y = robot.radius + robot.radius // 5
        self.roaming_targets.append((x,y))  # robot.radius//5 -- это своего рода припуск
        # экспериментальный
        direction = 1  # направление, 1 -- вправо, -1 -- влево
        while y < self.win_height - (3*robot.radius + robot.radius//5):
            x = x+direction*(self.win_width - robot.radius*2)
            if direction == -1:
                y += robot.radius
            self.roaming_targets.append((x,y))
            direction *= -1

    def start_roaming(self):
        self.mode = Mode.ROAMING

    def start_carrying(self):
        self.mode = Mode.CARRYING

    #def set_up_spiral_movement(self, Robot): куда разумнее вбить метод движения к цели (любой) и потом уже отдельно выбирать цель

    def go_to_target(self, robot):  # todo возможно проще координаты робота хранить в виде вектора я хз
        v = (math.Vector2(self.target_x, self.target_y) - math.Vector2(robot.x, robot.y))
        print("dest: "+ str(v.x)+", "+str(v.y))
        # v.scale_to_length((math.Vector2(robot.velocity)).length()) todo раскомментировать когда разберемся с навсистемой
        v.scale_to_length(10)
        print("dest scaled: " + str(v.x)+", "+str(v.y))
        robot.velocity = v
        print(self.target_x)
        print(self.target_y)
        print(robot.velocity)

    def roam(self, robot):
        if math.Vector2(self.target_x, self.target_y).distance_to(math.Vector2(robot.x, robot.y)) < (robot.radius//4):
            self.target_x, self.target_y = self.roaming_targets[self.target_num]
            if self.target_num == len(self.roaming_targets)-1:
                self.roaming_targets.reverse()
                self.target_num = 0
            else:
                self.target_num += 1
        self.go_to_target(robot)

    def carry(self):
        pass

    def set_velocity(self, robot):
        if self.mode == Mode.ROAMING:
            self.roam(robot)
        else:
            self.carry()

