import math
import pygame as pg

from . import nav_system
from .sensor import Sensor
from pygame import Vector2
from . import helper


class Robot(pg.sprite.Sprite):
    '''
    (todo docs)
     classes for a robot
    '''

    def __init__(self,
                 item_count: int,  # todo я забыла что такое айтем каунт и зачем он нужен
                 radius: float,
                 sensor_count: int = 3,
                 sensor_length: float = 10.0,
                 x: float = 0,
                 y: float = 0,
                 velocity: Vector2 = (0, 0),
                 capacity: int = 10):
        pg.sprite.Sprite.__init__(self)
        if item_count > 0:
            self.item_count = item_count
        if radius > 0:
            self.radius = radius
        if sensor_count >= 0:
            self.sensors = [Sensor(sensor_length, math.pi / 4), Sensor(sensor_length, 0), Sensor(sensor_length, -math.pi / 4)]

        # if (is_free(location,mask(self),radius)): TODO free space checker func if needed in future

        self.x = x
        self.y = y
        # self.direction = direction
        # if speed >= 0:
        #    self.speed = speed
        self.velocity = velocity
        if capacity > 0:
            self.capacity = capacity
        self.image = pg.transform.scale(pg.image.load('robot.png').convert_alpha(), (50,50))
        self.rect = self.image.get_rect()

    def decide_on_rubbish(self):
        pass  # TODO implement

    def perform_movement(self):
        self.x = self.x + self.velocity.x
        self.y = self.y + self.velocity.y

    def tick(self):
        for sensor in self.sensors:
            sensor.update_collision()
        self.velocity = helper.to_velosity(nav_system.calc())
        # self.speed, self.direction = calc()
        self.decide_on_rubbish()
        self.perform_movement()

# TODO enum for patrol/going to container modes
