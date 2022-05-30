import pygame as pg
from .helper import item_picture


class Map_item(pg.sprite.Sprite):
    '''
    (todo docs)
    classes for a garbage
    '''

    # initializing garbage
    def __init__(self, tag, volume=0):
        pg.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.tag = tag
        self.volume = volume
