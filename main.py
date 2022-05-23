import pygame as pg
import sys

#you may refactor it however you please

# а может тут это в класс painter завернуть чтобы не передавать постоянно х и у not my business tho
def draw(screen, x, y):
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


def main():
    screen = pg.display.set_mode((1300, 800))
    fps = 60
    clock = pg.time.Clock()
    x = 900
    y = 800


    pg.display.set_caption("Робот-сборщик мусора")
    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
            draw(screen,x,y)
            clock.tick(fps)


if __name__ == '__main__':
    main()