import math
import pygame as pg

from . import nav_system
from .sensor import Sensor
from pygame import Vector2
from . import helper

from classes import pathfinder as pf
from classes import map_item


class Robot(pg.sprite.Sprite):
    '''
    (todo docs)
     classes for a robot
    '''

    def __init__(self,
                 item_count: int,  # todo я забыла что такое айтем каунт и зачем он нужен
                 radius: float,
                 win_width: int,
                 win_height: int,
                 sensor_count: int = 3,
                 sensor_length: float = 10.0,
                 x: float = 0,
                 y: float = 0,
                 velocity: Vector2 = (0, 0),
                 capacity: int = 10):
        # pg.sprite.Sprite.__init__(self)
        super().__init__()
        if item_count > 0:
            self.item_count = item_count
        if radius > 0:
            self.radius = radius
        self.pfs  = pf.Pathfinder(self, win_height, win_width)

        # if (is_free(location,mask(self),radius)): TODO free space checker func if needed in future
        self.x = x - 40
        self.y = y - 40
        # self.direction = direction
        # if speed >= 0:
        #    self.speed = speed
        self.velocity = velocity
        if capacity > 0:
            self.capacity = capacity
        self.image = pg.Surface((850, 710), pg.SRCALPHA, 32).convert_alpha()
        self.rect = self.image.get_rect(center=(850+self.radius//2, 300+self.radius//2))
        pg.draw.circle(self.image, (255, 255, 0), (self.x, self.y), self.radius)
        if sensor_count >= 0:
            self.sensors = [Sensor(sensor_length, math.radians(45), self), Sensor(sensor_length, math.radians(0), self),
                            Sensor(sensor_length, math.radians(-45), self)]

    def decide_on_rubbish(self):
        pass

    def perform_movement(self):
        self.x = self.x + self.velocity.x
        self.y = self.y + self.velocity.y

    def go(self):
        #calc_result = nav_system.calc(self)
        #self.velocity = helper.to_velosity(calc_result)
        #for sensor in self.sensors:
        #    sensor.update(calc_result[1], self.velocity)
        # пока не разберемся с сенсорами мап айтемами (и логикой подбора хехе) -- придется закомментить
        #self.pfs.go_to_target(self)
        #self.pfs.set_velocity(self)
        calc_result = nav_system.calc(self)
        self.velocity = helper.to_velosity(calc_result)
        self.pfs.set_velocity(self)
        self.perform_movement()
        self.image.fill(0)
        pg.draw.circle(self.image, (255, 255, 0), (self.x, self.y), self.radius)
        for sensor in self.sensors:
            sensor.update(calc_result[1], self.velocity)

        print("x loc:" + str(self.x))
        print("y loc:" + str(self.y))
