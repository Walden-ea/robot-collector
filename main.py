import pygame as pg
import sys



# you may refactor it however you please

# а может тут это в класс painter завернуть чтобы не передавать постоянно х и у not my business tho
from classes.window import draw_background

WINDOW_WIDTH = 900
WINDOW_HIGHT = 800


def main():
    screen = pg.display.set_mode((1300, 800))
    fps = 60
    clock = pg.time.Clock()



    pg.display.set_caption("Робот-сборщик мусора")
    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
            draw_background(screen,WINDOW_WIDTH,WINDOW_HIGHT)
            clock.tick(fps)


if __name__ == '__main__':
    main()
