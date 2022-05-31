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

def generate_garbage(screen,Map_item):
    x1=0
    y1=0
    x2 = 0
    y2 = 0
    x3 = 0
    y3 = 0
    ok = False;
    while (not(ok)):
        x1 = random.randint(42, 838)
        y1 = random.randint(42, 698)
        if (not((y1 == 450 and 150 <= x1 <= 350) or (y1 == 100 and x1 >= 148 and x1 <= 698) or (
                    x1 == 650 and y1 >= 250 and y1 <= 500))):
            ok = True
    ok = False
    while (not(ok)):
        x2 = random.randint(42, 838)
        y2 = random.randint(42, 698)
        if (not(y2 == 450 and 100 <= x2 <= 400) and not(y2 == 100 and x2 >= 98 and x2 <= 748) and not(
                    x2 == 650 and y2 >= 200 and y2 <= 550)):
            ok = True

    ok = False
    while (not(ok)):
        x3 = random.randint(42, 838)
        y3 = random.randint(42, 698)
        if (not(y3 == 450 and 100 <= x3 <= 400) and not(y3 == 100 and x3 >= 98 and x3 <= 748) and not(
                    x3 == 650 and y3 >= 200 and y3 <= 550)):
            ok = True
    screen.blit(Map_item.image, [x1, y1])
    screen.blit(Map_item.image, [x2, y2])
    screen.blit(Map_item.image, [x3, y3])
    pg.display.update()