import math
import pygame as pg


def to_velosity(calc_result):
    return pg.Vector2(calc_result[0] * math.cos(calc_result[1]), calc_result[0] * math.sin(calc_result[1]))


def can_be_placed_at(x,y):  # нам много где нужна будет функция которая будет проверять
    # есть ли свободное место чтобы куда-то поставить
    return True  # todo logic


item_picture = ['garbage.png']  # массив с картинками для спрайтов мусора
