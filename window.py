import pygame as pg

def draw_background(screen, x, y):
    # todo можно юзать относительные величины а не абсолютные если понадобится
    screen.fill((242, 208, 202))
    pg.draw.rect(screen, (163, 178, 217), (40, 40, 850,710))
    pg.draw.rect(screen, (0, 0, 0), (40, 40, 850, 710),2)
    pg.draw.rect(screen, (250, 236, 234), (950, 40, 300, 710))
    pg.draw.rect(screen, (0, 0, 0), (950, 40, 300, 710), 2)
    pg.font.init()
    my_font = pg.font.SysFont('Comic Sans MS', 30)
    text_log = my_font.render('Лог', True, (0, 0, 0))
    screen.blit(text_log, (1075 , 40))
    pg.display.update()