import pygame as pg
import random
from .helper import item_picture


class Map_item(pg.sprite.Sprite):
    '''
    (todo docs)
    classes for a garbage
    '''

    # initializing garbage
    def __init__(self, tag,pos_x,pos_y, image = 0, volume=0):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(item_picture[tag]).convert_alpha(),(50,50))
        self.rect = self.image.get_rect(center=(pos_x+50//2, pos_y+50//2))
        self.mask = pg.mask.from_surface(self.image)
        self.tag = tag
        self.volume = tag+1

    def update(self, screen, x, y):
        screen.blit(self.image, [x, y])
        #pg.display.update()




