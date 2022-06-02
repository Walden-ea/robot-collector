import pygame as pg
import random
from .helper import item_picture


class Map_item(pg.sprite.Sprite):
    '''
    (todo docs)
    classes for a garbage
    '''

    # initializing garbage
    def __init__(self, tag, image = 0, volume=0):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load(item_picture[tag]).convert_alpha(),(50,50))
        self.rect = self.image.get_rect()
        self.tag = tag
        self.volume = tag+1

    def update(self, screen, x, y):
        screen.blit(self.image, [x, y])
        #pg.display.update()




