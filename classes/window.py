import pygame as pg
import random

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
    screen.blit(robot.image, [300,300])
    pg.display.update()

def draw_walls(screen,wall,x,y):
    screen.blit(wall.image, [x, y])
    pg.display.update()

def generate_coords():
    ok = False
    while (not (ok)):
        x = random.randint(42, 838)
        y = random.randint(42, 698)
        if (not (51 <= x <= 451 and 399 <= y <= 501) and not (49 <= y <= 151 and 45 <= x <= 801) and not (
                149 <= y <= 602 and 599 <= x <= 701)):
            ok = True
    return (x, y)