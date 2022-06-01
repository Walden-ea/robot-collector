import pygame as pg
import sys
import random
import array as arr
import classes.robot as rb
import classes.window as ww

import classes.map_item as mi
import classes.wall as wl

# you may refactor it however you please

# а может тут это в класс painter завернуть чтобы не передавать постоянно х и у not my business tho
# from classes import robot
# from classes import window


WINDOW_WIDTH = 900
WINDOW_HIGHT = 800

num = random.randint(3, 5)
coords = ([0, 0] * num)

for i in range(num):
    coords[i] = ww.generate_coords()


def main():
    screen = pg.display.set_mode((1300, 800))
    fps = 60
    clock = pg.time.Clock()

    robot = rb.Robot(5, 75.0, WINDOW_WIDTH, WINDOW_HIGHT, x=WINDOW_WIDTH / 2, y=WINDOW_HIGHT / 2)
    wall1 = wl.Wall(700, 50)
    wall2 = wl.Wall(50, 400)
    wall3 = wl.Wall(350, 50)

    garb = []
    for i in range(num):
        garb.append(mi.Map_item(random.randint(0, 2)))

    pg.display.set_caption("Робот-сборщик мусора")
    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
            ww.draw_background(screen, WINDOW_WIDTH, WINDOW_HIGHT)
            ww.draw_robot(screen, robot)
            #ww.draw_walls(screen, wall1, 98, 100) todo раскомментить
            #ww.draw_walls(screen, wall2, 650, 200)
            #ww.draw_walls(screen, wall3, 100, 450)
            #for i in range(num):
            #    garb[i].update(screen, coords[i][0], coords[i][1])
            #for sensor in robot.sensors:
            #    print(pg.sprite.collide_mask(sensor, wall1))
            #    sensor.check_collide([wall1, wall2, wall3])
            robot.tick(WINDOW_HIGHT,WINDOW_WIDTH)
        clock.tick(fps)


if __name__ == '__main__':
    main()
