import pygame as pg
import random
import classes.wall as wl
import classes.container as cn

ROOM_CONSTRAINTS = pg.Rect(40, 40, 850, 710)

def draw_background(screen, x, y):
    # todo можно юзать относительные величины а не абсолютные если понадобится
    screen.fill((242, 208, 202))
    pg.draw.rect(screen, (163, 178, 217), ROOM_CONSTRAINTS)
    pg.draw.rect(screen, (0, 0, 0), (40, 40, 850, 710),2)
    pg.draw.rect(screen, (250, 236, 234), (950, 40, 300, 710))
    pg.draw.rect(screen, (0, 0, 0), (950, 40, 300, 710), 2)
    pg.font.init()
    my_font = pg.font.SysFont('Comic Sans MS', 30)
    text_log = my_font.render('Лог', True, (0, 0, 0))
    screen.blit(text_log, (1075 , 40))
    pg.display.update()

def draw_robot(screen,robot):
    #todo надо заморочиться чтобы он был круглым и вследствие этого придется еще заморочиться над коллизиями
    # эта штука обвиосли временная
    screen.blit(robot.image, [40,40])
    for sensor in robot.sensors:
        screen.blit(sensor.image, [40, 40])
    pg.display.update()

def draw_walls(screen,wall,x,y):
    screen.blit(wall.image, [x, y])
    pg.display.update()



def draw_window_borderline(screen):
       wall10 = wl.Wall(900, 40)
       wall11 = wl.Wall(40, 800)
       draw_walls(screen, wall10, 0, 0)
       draw_walls(screen, wall10, 0, 750)
       draw_walls(screen, wall11, 0, 0)
       draw_walls(screen, wall11, 890, 0)

def draw_container(screen, container ,x,y):
    screen.blit(container.image, [x, y])
    pg.display.update()

def draw_containers(screen):
     container0 = cn.Container(80, 80, 100, 0)
     container1 = cn.Container(80, 80, 100, 1)
     container2 = cn.Container(80, 80, 100, 2)
     draw_container(screen, container0, 150, 150)
     draw_container(screen, container1, 250, 150)
     draw_container(screen, container2, 350, 150)

def generate_coords():
    ok = False
    while (not (ok)):
        x = random.randint(42, 838)
        y = random.randint(42, 698)
        if (not (51 <= x <= 451 and 399 <= y <= 501) and not (49 <= y <= 151 and 45 <= x <= 801) and not (
                99 <= y <= 652 and 549 <= x <= 751) and not (49 <= x <= 201 and 479 <= y <= 721) and not (
                259 <= x <= 401 and 569 <= y <= 721) and not (49 <= x <= 351 and 469 <= y <= 621) and not (
                699 <= x <= 851 and 249 <= y <= 651) and not (699 <= x <= 871 and 249 <= y <= 401) and not (
                469 <= x <= 621 and 249 <= y <= 401) and not (479 <= x <= 621 and 469 <= y <= 721) and not (
                249 <= x <= 351 and 469 <= y <= 721) and not (349 <= x <= 571 and 469 <= y <= 721)):
            ok = True
    return (x, y)
