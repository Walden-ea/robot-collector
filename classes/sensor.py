import math


class Sensor:
    '''
    (todo docs)
    class for robot sensors
    '''
    def __init__(self, length, angle):
        self.x = length*math.cos(angle)
        self.y = length*math.sin(angle)
