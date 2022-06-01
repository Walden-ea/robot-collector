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
        self.image = pg.Surface((850, 710)).convert_alpha()
        self.image.fill(0)
        self.rect = self.image.get_rect(center=(425, 355))
        self.start_x = robot.x + robot.radius
        self.start_y = robot.y
        self.robot_radius = robot.radius
        self.robot_rotate = math.radians(0)
        self.angle = angle
        self.length = length
        self.distance = length
        pg.draw.line(self.image, (255, 255, 0), (self.start_x, self.start_y), (self.start_x + self.x, self.start_y - self.y))
        self.collide_object = None

    def update(self, rotate_angle, velocity):
        self.image.fill(0)
        self.robot_rotate += rotate_angle
        self.angle += rotate_angle
        h = 2 * self.robot_radius * math.sin(abs(rotate_angle) / 2)
        self.start_x += h * math.cos((180 - abs(rotate_angle)) / 2) + velocity.x
        self.start_y += h * math.sin((180 - abs(rotate_angle)) / 2) + velocity.y
        self.x = self.length * math.cos(self.angle)
        self.y = self.length * math.sin(self.angle)
        pg.draw.line(self.image, (255, 255, 0), (self.start_x, self.start_y), (self.start_x + self.x, self.start_y + self.y))
        self.mask = pg.mask.from_surface(self.image)

    def check_collide(self, walls):
        for wall in walls:
            collide = pg.sprite.collide_mask(self, wall)
            if pg.sprite.collide_mask(self, wall):
                self.collide_object = wall
                if math.pi / 2 <= self.robot_rotate < 3 * math.pi / 2:
                    self.distance = self.length - math.sqrt(collide[0] ^ 2 + collide[1] ^ 2)
                elif 3 * math.pi / 2 <= self.robot_rotate <= math.radians(0) or math.radians(0) <= self.robot_rotate <= math.pi / 2:
                    self.distance = math.sqrt(collide[0] ^ 2 + collide[1] ^ 2)
        pass  # collision = 15 etc.
