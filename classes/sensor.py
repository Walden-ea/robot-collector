import math
import pygame as pg
from . import window


class Sensor(pg.sprite.Sprite):
    '''
    (todo docs)
    classes for robot sensors
    '''

    def __init__(self, length, angle, robot, collision=math.inf):
        super().__init__()
        self.x = length * math.cos(angle)
        self.y = length * math.sin(angle)
        self.image = pg.Surface((850, 710)).convert_alpha()
        self.image.fill(0)
        self.rect = self.image.get_rect(center=(425, 355))
        self.start_x = robot.x + robot.radius
        self.start_y = robot.y
        self.robot_position = pg.math.Vector2(robot.x,robot.y)
        self.robot_radius = robot.radius
        self.robot_rotate = math.radians(0)
        self.angle = angle
        self.length = length
        self.distance = length
        pg.draw.line(self.image, (255, 255, 0), (self.start_x, self.start_y), (self.start_x + self.x, self.start_y - self.y))
        self.collide_object = None
        self.mask = pg.mask.from_surface(self.image)

        # class Player(pg.sprite.Sprite):
        #     def __init__(self):
        #         super().__init__()
        #         self.image = pg.Surface((40, 40))
        #         self.image.fill('red')
        #         self.rect = self.image.get_rect(center=(300, 300))
        #         self.mask = pg.mask.from_surface(self.image)
        #
        #     def update(self):
        #         if pg.mouse.get_pos():
        #             self.rect.center = pg.mouse.get_pos()

    def update(self, rotate_angle, velocity):
        self.image.fill(0)
        # self.start_x = math.cos(rotate_angle)*(self.start_x - self.robot_position.x) - math.sin(rotate_angle) *\
        #                (self.start_y - self.robot_position.y) + self.robot_position.x
        # self.start_y = math.sin(rotate_angle) * (self.start_x - self.robot_position.x) + math.cos(rotate_angle) * \
        #                (self.start_y - self.robot_position.y) + self.robot_position.x
        #
        # self.x = math.cos(rotate_angle)*(self.x - self.robot_position.x) - math.sin(rotate_angle) *\
        #                (self.y - self.robot_position.y) + self.robot_position.x
        # self.y = math.sin(rotate_angle) * (self.x - self.robot_position.x) + math.cos(rotate_angle) * \
        #                (self.y - self.robot_position.y) + self.robot_position.x
        self.robot_rotate += rotate_angle
        self.angle += rotate_angle
        h = 2 * self.robot_radius * math.sin(abs(rotate_angle) / 2)
        self.start_x += h * math.cos((180 - abs(rotate_angle)) / 2) + velocity.x
        self.start_y += h * math.sin((180 - abs(rotate_angle)) / 2) + velocity.y
        self.x = self.length * math.cos(self.angle)
        self.y = self.length * math.sin(self.angle)
        pg.draw.line(self.image, (255, 255, 0), (self.start_x, self.start_y), (self.start_x + self.x, self.start_y + self.y),2)
        self.mask = pg.mask.from_surface(self.image)

    def check_collide(self, walls):
            if pg.sprite.spritecollide(self, walls, False, pg.sprite.collide_mask):
                W = walls.sprites()
                W1 = pg.sprite.collide_mask(self, W[0])
                W2 = pg.sprite.collide_mask(self, W[1])
                W3 = pg.sprite.collide_mask(self, W[2])

                print('COLLIDE ', W1, W2, W3)
                wall = W1 or W2 or W3

                self.collide_object = wall
                if math.pi / 2 <= self.robot_rotate < 3 * math.pi / 2:
                    self.distance = self.length - math.sqrt(wall[0] ^ 2 + wall[1] ^ 2)
                elif 3 * math.pi / 2 <= self.robot_rotate <= math.radians(0) or math.radians(0) <= self.robot_rotate <= math.pi / 2:
                    self.distance = math.sqrt(wall[0] ^ 2 + wall[1] ^ 2)
                    # collision = 15 etc.
