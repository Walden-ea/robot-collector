from time import sleep

import pygame as pg
import math
import sys
import random
import array as arr
import classes.robot as rb
import classes.window as ww

import classes.map_item as mi
import classes.wall as wl
import classes.container as ct

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((40, 40))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=(300, 300))
        self.mask = pg.mask.from_surface(self.image)

    def update(self):
        if pg.mouse.get_pos():
            self.rect.center = pg.mouse.get_pos()

# а может тут это в класс painter завернуть чтобы не передавать постоянно х и у not my business tho
# from classes import robot
# from classes import window


WINDOW_WIDTH = 900
WINDOW_HIGHT = 800
pg.init()
screen = pg.display.set_mode((1300, 800))
player = pg.sprite.GroupSingle(Player())

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
        garb.append(mi.Map_item(random.randint(0, 2),coords[i][0], coords[i][1]))
    for i in range(3):
        cont.append(ct.Container(i, ww.generate_coords()[0],ww.generate_coords()[1]))
    container_group = pg.sprite.Group()
    for c in cont:
        container_group.add(c)

    pg.display.set_caption("Робот-сборщик мусора")

    new_garb = []
    new_garb_coords = []
    garb_group = pg.sprite.Group()
    garb_group.add(garb)
    while True:

        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
            if i.type == pg.MOUSEBUTTONUP:
                mouse_pos = pg.mouse.get_pos()
                new_garb_coords.append(mouse_pos)
                new_garb.append(mi.Map_item(random.randint(0, 2), mouse_pos[0], mouse_pos[1]))
                garb_group.add(new_garb[len(new_garb)-1])
                pass
        ww.draw_background(screen, WINDOW_WIDTH, WINDOW_HIGHT)
        ww.draw_robot(screen, robot)
        ww.draw_walls(screen, wall1)
        ww.draw_walls(screen, wall2)
        ww.draw_walls(screen, wall3)
        for i_g in range(num):
            if garb[i_g] in garb_group:
                garb[i_g].update(screen, coords[i_g][0], coords[i_g][1])
        for i_g in range(len(new_garb)):
            if new_garb[i_g] in garb_group:
                new_garb[i_g].update(screen, new_garb_coords[i_g][0], new_garb_coords[i_g][1]) #todo проверить почему не больше 4х
            #print("i_g: "+str(i_g))
            #print("ngc: " + str(len(new_garb_coords)))
        for c in cont:
            screen.blit(c.image, [c.pos_x, c.pos_y])

        for sensor in robot.sensors:
            sensor.check_collide(walls)
        robot.go()
        #obstacle.draw(screen)
        # for wall in walls.sprites():
        #     pg.sprite.GroupSingle(wall).draw(screen)
        # collision
        # updating and drawing
        player.update()
        player.draw(screen)

        # collision
        for s in robot.sensors:
            if pg.sprite.spritecollide(s, walls, False, pg.sprite.collide_mask):
                W1 = pg.sprite.collide_mask(sensor, wall1)
                W2 = pg.sprite.collide_mask(sensor, wall2)
                W3 = pg.sprite.collide_mask(sensor, wall3)

                print('COLLIDE ', W1, W2, W3)
                player.sprite.image.fill('green')
            elif pg.sprite.spritecollide(s, garb_group, True, pg.sprite.collide_mask):
                print("COLLIDES")
                player.sprite.image.fill('blue')
            elif pg.sprite.spritecollide(s, container_group, False, pg.sprite.collide_mask):
                print("CONTAINER")
                player.sprite.image.fill('yellow')
            else:
                player.sprite.image.fill('red')


        #это мышкой проверка
        # if pg.sprite.spritecollide(player.sprite, walls, False, pg.sprite.collide_mask):
        #     print("collides")
        #     player.sprite.image.fill('green')
        # elif pg.sprite.spritecollide(player.sprite, garb_group, False, pg.sprite.collide_mask):
        #     print("COLLIDES")
        #     player.sprite.image.fill('blue')
        # elif pg.sprite.spritecollide(player.sprite, container_group, False, pg.sprite.collide_mask):
        #     print("CONTAINER")
        #     player.sprite.image.fill('yellow')
        # else:
        #     player.sprite.image.fill('red')

        clock.tick(fps)
        pg.display.update()
        #sleep(3)


if __name__ == '__main__':
    main()
