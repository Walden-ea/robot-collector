import math


class Sensor:
    '''
    (todo docs)
    class for robot sensors
    '''
    def __init__(self, length, angle, collision):
        #probably will have to have a rect attached
        self.x = length*math.cos(angle)
        self.y = length*math.sin(angle)
        collision = math.inf #todo check if you are allowed to have int at the first tick


    def update_collision(self):
        # process the collisions here
        pass # collision = 15 etc.
