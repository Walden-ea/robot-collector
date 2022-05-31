import pygame as pg
from .helper import item_picture

class Wall():
    def __init__(self,
                 x: float = 0,
                 y: float = 0):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load('wall.png').convert_alpha(), (x,y))
        self.rect = self.image.get_rect()