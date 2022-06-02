from time import sleep

import pygame as pg
import sys
import random
import array as arr
import classes.robot as rb
import classes.window as ww

import classes.map_item as mi
import classes.wall as wl


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


WINDOW_WIDTH = 1300
WINDOW_HIGHT = 800
pg.init()
screen = pg.display.set_mode((1300, 800))

num = random.randint(3, 5)
coords = ([0, 0] * num)

for i in range(num):
    coords[i] = ww.generate_coords()

player = pg.sprite.GroupSingle(Player())

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
    for i in range(num):
        garb.append(mi.Map_item(random.randint(0, 2)))

    pg.display.set_caption("Робот-сборщик мусора")
    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
        ww.draw_background(screen, WINDOW_WIDTH, WINDOW_HIGHT)
        ww.draw_robot(screen, robot)
        #ww.draw_walls(screen, wall1, 98, 100)
        #ww.draw_walls(screen, wall2, 650, 200)
        #ww.draw_walls(screen, wall3, 100, 450)
        for i in range(num):
            garb[i].update(screen, coords[i][0], coords[i][1]) # todo ЗАМЕНИТЕ АПДЕЙТ НА ЧТО-НИБУДЬ ЧТОБЫ ОНО НЕ МИГАЛО АПДЕЙТ МИГАЕТ
        for sensor in robot.sensors:
            sensor.check_collide([wall1, wall2, wall3])
        robot.go()
        player.update()
        player.draw(screen)
        #obstacle.draw(screen)
        for wall in walls.sprites():
            pg.sprite.GroupSingle(wall).draw(screen)
        # collision

        if pg.sprite.spritecollide(player.sprite, walls, False, pg.sprite.collide_mask):
            player.sprite.image.fill('green')
        else:
            player.sprite.image.fill('red')
        clock.tick(fps)
        pg.display.update()
        #sleep(3)


if __name__ == '__main__':
    main()
