from time import sleep

import pygame as pg
import sys
import random
import array as arr
import classes.robot as rb
import classes.window as ww

import classes.map_item as mi
import classes.wall as wl
import classes.container as ct



# а может тут это в класс painter завернуть чтобы не передавать постоянно х и у not my business tho
# from classes import robot
# from classes import window


WINDOW_WIDTH = 900
WINDOW_HIGHT = 800
pg.init()
screen = pg.display.set_mode((1300, 800))

num = random.randint(3, 5)
coords = ([0, 0] * num)

for i in range(num):
    coords[i] = ww.generate_coords()



def main():

    fps = 60
    clock = pg.time.Clock()

    robot = rb.Robot(5, 20.0,WINDOW_WIDTH, WINDOW_HIGHT, sensor_length=40, x=WINDOW_WIDTH / 2, y=WINDOW_HIGHT / 2)
    wall1 = wl.Wall(98, 100,700, 50)
    wall2 = wl.Wall( 650, 200, 50, 400)
    wall3 = wl.Wall( 100, 450, 350, 50)
    walls = pg.sprite.Group()
    walls.add(wall1,wall2,wall3)


    garb = []
    cont = []
    for i in range(num):
        garb.append(mi.Map_item(random.randint(0, 2)))
    for i in range(3):
        cont.append(ct.Container(i, ww.generate_coords()[0],ww.generate_coords()[1]))

    pg.display.set_caption("Робот-сборщик мусора")

    new_garb = []
    new_garb_coords = []
    while True:

        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
            if i.type == pg.MOUSEBUTTONUP:
                new_garb.append(mi.Map_item(random.randint(0, 2)))
                new_garb_coords.append(pg.mouse.get_pos())
                pass
        ww.draw_background(screen, WINDOW_WIDTH, WINDOW_HIGHT)
        ww.draw_robot(screen, robot)
        ww.draw_walls(screen, wall1)
        ww.draw_walls(screen, wall2)
        ww.draw_walls(screen, wall3)
        for i_g in range(num):
            garb[i_g].update(screen, coords[i_g][0], coords[i_g][1])
        for i_g in range(len(new_garb)):
            garb[i_g].update(screen, new_garb_coords[i_g][0], new_garb_coords[i_g][1]) #todo проверить почему не больше 4х
            print("i_g: "+str(i_g))
            print("ngc: " + str(len(new_garb_coords)))
        for c in cont:
            screen.blit(c.image, [c.pos_x, c.pos_y])
        for sensor in robot.sensors:
            sensor.check_collide([wall1, wall2, wall3])
        robot.go()
        #obstacle.draw(screen)
        # for wall in walls.sprites():
        #     pg.sprite.GroupSingle(wall).draw(screen)
        # collision
        for s in robot.sensors:
            if pg.sprite.spritecollide(s, walls, False, pg.sprite.collide_mask):
                print("collides")
            else:
                print("doesn't collide")
        clock.tick(fps)
        pg.display.update()
        #sleep(3)


if __name__ == '__main__':
    main()
