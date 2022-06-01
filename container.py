import pygame as pg
from .helper import item_picture

class Container():
    def __init__(self,
                 x: float = 0,
                 y: float = 0,
                 capacity: float = 100,
                 container_type: int =0 ):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load('container.png').convert_alpha(), (x,y))
        self.rect = self.image.get_rect()
