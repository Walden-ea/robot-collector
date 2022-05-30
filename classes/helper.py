import math
import pygame as pg


def to_velosity(speed: float, direction: float):
    return pg.Vector2(speed * math.cos(direction), speed * math.sine(direction))


def can_be_placed_at(x,y):  # нам много где нужна будет функция которая будет проверять
    # есть ли свободное место чтобы куда-то поставить
    return True  # todo logic


item_picture = []  # массив с картинками для спрайтов мусора
