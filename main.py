import pygame as pg
import sys
import classes.robot as rb
import classes.window as ww


# you may refactor it however you please

# а может тут это в класс painter завернуть чтобы не передавать постоянно х и у not my business tho
#from classes import robot
#from classes import window



WINDOW_WIDTH = 900
WINDOW_HIGHT = 800


def main():
    screen = pg.display.set_mode((1300, 800))
    fps = 60
    clock = pg.time.Clock()

    robot = rb.Robot(5, 75.0, x=WINDOW_WIDTH/2, y=WINDOW_HIGHT/2)


    pg.display.set_caption("Робот-сборщик мусора")
    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
            ww.draw_background(screen, WINDOW_WIDTH, WINDOW_HIGHT)
            ww.draw_robot(screen, robot)
            clock.tick(fps)


if __name__ == '__main__':
    main()
