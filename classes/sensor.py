import math
import pygame as pg
from . import window


class Sensor(pg.sprite.Sprite):
    '''
    (todo docs)
    classes for robot sensors
    '''

    def __init__(self, length, angle, robot, collision=math.inf):
        self.x = length * math.cos(angle)
        self.y = length * math.sin(angle)
        self.image = pg.Surface((850, 710))
        self.rect = self.image.get_rect(center=(465, 395))
        self.start_x = robot.x
        self.start_y = robot.y - robot.radius
        self.robot_radius = robot.radius
        self.angle = angle
        self.length = length
        self.distance = length
        pg.draw.line(self.image, (255, 255, 0), (self.start_x, self.start_y), (self.start_x + self.x, self.start_y - robot.radius - self.y))
        self.collide_object = None
        # collision = math.inf #todo check if you are allowed to have int at the first tick

    def update(self, rotate_angle, velocity):
        self.image.fill(0)
        h = self.robot_radius * math.sin(rotate_angle)
        self.start_x += h * abs(math.sin((180 - rotate_angle) / 2))
        self.start_y += h * abs(math.cos((180 - rotate_angle) / 2))
        new_x = self.start_x + (self.x * math.sin(self.angle + self.y * math.cos(self.angle))) + velocity.x
        new_y = self.start_y - self.y + self.length * math.sin(90 - rotate_angle - self.angle) + velocity.y
        pg.draw.line(self.image, (255, 255, 0), (self.start_x, self.start_y), new_x, new_y)
        self.mask = pg.mask.from_surface(self.image)

    def check_collide(self, walls):
        pass
        for wall in walls:
            collide = pg.sprite.collide_mask(self, wall)
            if collide:
                self.distance = self.length - collide[0]*collide[1]/2
                self.collide_object = wall
        # process the collisions here
        pass  # collision = 15 etc.