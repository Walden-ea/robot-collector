import pygame as pg
from classes import helper


class Container(pg.sprite.Sprite):
    def __init__(self, tag: int, pos_x, pos_y, x = 50, y = 50):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = pg.transform.scale(pg.image.load(helper.container_picture[tag]).convert_alpha(), (x, y))
        self.rect = self.image.get_rect(center=(pos_x + x // 2, pos_y + y // 2))
        self.mask = pg.mask.from_surface(self.image)
