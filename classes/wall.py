import pygame as pg
from .helper import item_picture


class Wall(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y,
                 x: float = 0,
                 y: float = 0,):
        self.pos_x = pos_x
        self.pos_y = pos_y
        #pg.sprite.Sprite.__init__(self)
        #self.image = pg.transform.scale(pg.image.load('wall.png').convert_alpha(), (x, y))
        #self.rect = self.image.get_rect()
        #self.mask = pg.mask.from_surface(self.image)
        super().__init__()
        self.image = pg.transform.scale(pg.image.load('wall.png').convert_alpha(), (x, y))
        self.rect = self.image.get_rect(center=(pos_x+x//2, pos_y+y//2))
        self.mask = pg.mask.from_surface(self.image)

