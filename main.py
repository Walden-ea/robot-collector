import pygame as pg
import sys

#you may refactor it however you please


# а может тут это в класс painter завернуть чтобы не передавать постоянно х и у not my business tho
def draw(screen, x, y):
    screen.fill((255, 255, 255))
    pg.draw.rect(screen, (0, 0, 255), (300, 200, 70,70)) #example of a blue rectangle
    pg.display.update()


def main():
    screen = pg.display.set_mode((600, 400))
    fps = 60
    clock = pg.time.Clock()
    x = 300
    y = 300


    pg.display.set_caption("Робот-сборщик мусора")
    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
            draw(screen,x,y)
            clock.tick(fps)


if __name__ == '__main__':
    main()