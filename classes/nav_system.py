# mock for a navigation system
import math
from scipy import integrate

from .map_item import Map_item
#from .robot import Robot


def calc(robot, map_item: Map_item):
    # Checking sensors when map_item is a piece of garbage
    # Returning fast speed
    if robot.sensors[0] <= 40 & robot.sensors[0] >= 18 & robot.sensors[1] <= 40 \
            & robot.sensors[1] >= 18 & robot.sensors[2] <= 40 & robot.sensors[2] >= 18 \
            & map_item.tag != 0:
        return fast_speed, no_angle()

    # Returning medium speed
    if robot.sensors[0] <= 40 & robot.sensors[0] >= 18 & robot.sensors[1] <= 40 \
            & robot.sensors[1] >= 18 & robot.sensors[2] <= 20 & robot.sensors[2] >= 13 \
            & map_item.tag != 0:
        return medium_speed, turn_right()
    if robot.sensors[0] <= 40 & robot.sensors[0] >= 18 & robot.sensors[1] <= 20 \
            & robot.sensors[1] >= 13 & robot.sensors[2] <= 40 & robot.sensors[2] >= 18 \
            & map_item.tag != 0:
        return medium_speed, no_angle()
    if robot.sensors[0] <= 20 & robot.sensors[0] >= 13 & robot.sensors[1] <= 40 \
            & robot.sensors[1] >= 18 & robot.sensors[2] <= 40 & robot.sensors[2] >= 18 \
            & map_item.tag != 0:
        return medium_speed, turn_left()
    if robot.sensors[0] <= 20 & robot.sensors[0] >= 13 & robot.sensors[1] <= 20 \
            & robot.sensors[1] >= 13 & robot.sensors[2] <= 40 & robot.sensors[2] >= 18 \
            & map_item.tag != 0:
        return medium_speed, turn_left()
    if robot.sensors[0] <= 20 & robot.sensors[0] >= 13 & robot.sensors[1] <= 40 \
            & robot.sensors[1] >= 18 & robot.sensors[2] <= 20 & robot.sensors[2] >= 13 \
            & map_item.tag != 0:
        return medium_speed, no_angle()
    if robot.sensors[0] <= 40 & robot.sensors[0] >= 18 & robot.sensors[1] <= 20 \
            & robot.sensors[1] >= 13 & robot.sensors[2] <= 20 & robot.sensors[2] >= 13 \
            & map_item.tag != 0:
        return medium_speed, turn_right()

    # Returning slow speed
    if robot.sensors[0] <= 20 & robot.sensors[0] >= 13 & robot.sensors[1] <= 20 \
            & robot.sensors[1] >= 13 & robot.sensors[2] <= 20 & robot.sensors[2] >= 13 \
            & map_item.tag != 0:
        return slow_speed, no_angle()
    if robot.sensors[0] <= 20 & robot.sensors[0] >= 13 & robot.sensors[1] <= 20 \
            & robot.sensors[1] >= 13 & robot.sensors[2] <= 15 & robot.sensors[2] >= 4 \
            & map_item.tag != 0:
        return slow_speed, turn_right()
    if robot.sensors[0] <= 20 & robot.sensors[0] >= 13 & robot.sensors[1] <= 15 \
            & robot.sensors[1] >= 4 & robot.sensors[2] <= 20 & robot.sensors[2] >= 13 \
            & map_item.tag != 0:
        return slow_speed, no_angle()
    if robot.sensors[0] <= 15 & robot.sensors[0] >= 4 & robot.sensors[1] <= 20 \
            & robot.sensors[1] >= 13 & robot.sensors[2] <= 20 & robot.sensors[2] >= 13 \
            & map_item.tag != 0:
        return slow_speed, turn_left()
    if robot.sensors[0] <= 15 & robot.sensors[0] >= 4 & robot.sensors[1] <= 15 \
            & robot.sensors[1] >= 4 & robot.sensors[2] <= 20 & robot.sensors[2] >= 13 \
            & map_item.tag != 0:
        return slow_speed, turn_left()
    if robot.sensors[0] <= 15 & robot.sensors[0] >= 4 & robot.sensors[1] <= 20 \
            & robot.sensors[1] >= 13 & robot.sensors[2] <= 15 & robot.sensors[2] >= 4 \
            & map_item.tag != 0:
        return slow_speed, no_angle()
    if robot.sensors[0] <= 20 & robot.sensors[0] >= 13 & robot.sensors[1] <= 15 \
            & robot.sensors[1] >= 4 & robot.sensors[2] <= 15 & robot.sensors[2] >= 4 \
            & map_item.tag != 0:
        return slow_speed, turn_right()

    # Returning very slow speed
    if robot.sensors[0] <= 15 & robot.sensors[0] >= 4 & robot.sensors[1] <= 15 \
            & robot.sensors[1] >= 4 & robot.sensors[2] <= 15 & robot.sensors[2] >= 4 \
            & map_item.tag != 0:
        return very_slow_speed, no_angle()
    if robot.sensors[0] <= 8 & robot.sensors[0] >= 0 & robot.sensors[1] <= 15 \
            & robot.sensors[1] >= 4 & robot.sensors[2] <= 15 & robot.sensors[2] >= 4 \
            & map_item.tag != 0:
        return very_slow_speed, turn_left()
    if robot.sensors[0] <= 15 & robot.sensors[0] >= 4 & robot.sensors[1] <= 8 \
            & robot.sensors[1] >= 0 & robot.sensors[2] <= 15 & robot.sensors[2] >= 4 \
            & map_item.tag != 0:
        return very_slow_speed, no_angle()
    if robot.sensors[0] <= 15 & robot.sensors[0] >= 4 & robot.sensors[1] <= 15 \
            & robot.sensors[1] >= 4 & robot.sensors[2] <= 8 & robot.sensors[2] >= 0 \
            & map_item.tag != 0:
        return very_slow_speed, turn_right()
    if robot.sensors[0] <= 8 & robot.sensors[0] >= 0 & robot.sensors[1] <= 8 \
            & robot.sensors[1] >= 0 & robot.sensors[2] <= 15 & robot.sensors[2] >= 4 \
            & map_item.tag != 0:
        return very_slow_speed, turn_left()
    if robot.sensors[0] <= 8 & robot.sensors[0] >= 0 & robot.sensors[1] <= 15 \
            & robot.sensors[1] >= 4 & robot.sensors[2] <= 8 & robot.sensors[2] >= 0 \
            & map_item.tag != 0:
        return very_slow_speed, no_angle()
    if robot.sensors[0] <= 15 & robot.sensors[0] >= 4 & robot.sensors[1] <= 8 \
            & robot.sensors[1] >= 0 & robot.sensors[2] <= 8 & robot.sensors[2] >= 0 \
            & map_item.tag != 0:
        return very_slow_speed, turn_right()
    if robot.sensors[0] <= 8 & robot.sensors[0] >= 0 & robot.sensors[1] <= 8 \
            & robot.sensors[1] >= 0 & robot.sensors[2] <= 8 & robot.sensors[2] >= 0 \
            & map_item.tag != 0:
        return very_slow_speed, no_angle()

    # Now checking when map_item is actually a wall
    if robot.sensors[0] <= 8 & robot.sensors[0] >= 0 & robot.sensors[1] <= 15 \
            & robot.sensors[1] >= 4 & robot.sensors[2] <= 15 & robot.sensors[2] >= 4 \
            & map_item.tag == 0:
        return very_slow_speed, rapidly_right()
    if robot.sensors[0] <= 15 & robot.sensors[0] >= 4 & robot.sensors[1] <= 8 \
            & robot.sensors[1] >= 0 & robot.sensors[2] <= 15 & robot.sensors[2] >= 4 \
            & map_item.tag == 0:
        return very_slow_speed, rapidly_right()
    if robot.sensors[0] <= 15 & robot.sensors[0] >= 4 & robot.sensors[1] <= 15 \
            & robot.sensors[1] >= 4 & robot.sensors[2] <= 8 & robot.sensors[2] >= 0 \
            & map_item.tag == 0:
        return very_slow_speed, rapidly_left()
    if robot.sensors[0] <= 8 & robot.sensors[0] >= 0 & robot.sensors[1] <= 8 \
            & robot.sensors[1] >= 0 & robot.sensors[2] <= 15 & robot.sensors[2] >= 4 \
            & map_item.tag != 0:
        return very_slow_speed, rapidly_right()
    if robot.sensors[0] <= 8 & robot.sensors[0] >= 0 & robot.sensors[1] <= 15 \
            & robot.sensors[1] >= 4 & robot.sensors[2] <= 8 & robot.sensors[2] >= 0 \
            & map_item.tag == 0:
        return very_slow_speed, turnaround()
    if robot.sensors[0] <= 15 & robot.sensors[0] >= 4 & robot.sensors[1] <= 8 \
            & robot.sensors[1] >= 0 & robot.sensors[2] <= 8 & robot.sensors[2] >= 0 \
            & map_item.tag == 0:
        return very_slow_speed, rapidly_left()
    if robot.sensors[0] <= 8 & robot.sensors[0] >= 0 & robot.sensors[1] <= 8 \
            & robot.sensors[1] >= 0 & robot.sensors[2] <= 8 & robot.sensors[2] >= 0 \
            & map_item.tag == 0:
        return very_slow_speed, turnaround()


v_min = 0
v1 = 7
v2 = 6
v3 = 15
v4 = 12
v5 = 20
v6 = 18
v_max = 30


# Functions for speed
def speed_fast():
    s = 1 / 2 * (v_max - v6 + v_max - v5)

    def f1(x):
        return x

    def f2(x):
        return x * (x - v6) / 2

    integral1 = integrate.quad(func=f1, a=v5, b=v_max)
    integral2 = integrate.quad(func=f2, a=v6, b=v5)
    return (integral1[0] + integral2[0]) / s


def speed_medium():
    s = 1 / 2 * (v5 - v4 + v6 - v3)

    def f1(x):
        return x

    def f2(x):
        return x * (v5 - x) / 2

    def f3(x):
        return x * (x - v3) / 2

    integral1 = integrate.quad(func=f1, a=v3, b=v6)
    integral2 = integrate.quad(func=f2, a=v6, b=v5)
    integral3 = integrate.quad(func=f3, a=v4, b=v3)
    return (integral1[0] + integral2[0] + integral3[0]) / s


def speed_slow():
    s = 1 / 2 * (v3 - v2 + v4 - v1)

    def f1(x):
        return x

    def f2(x):
        return x * (v4 - x) / 2

    def f3(x):
        return x * (x - v2) / 2

    integral1 = integrate.quad(func=f1, a=v1, b=v4)
    integral2 = integrate.quad(func=f2, a=v4, b=v3)
    integral3 = integrate.quad(func=f3, a=v2, b=v1)
    return (integral1[0] + integral2[0] + integral3[0]) / s


def speed_very_slow():
    s = 1 / 2 * (v2 + v1)

    def f1(x):
        return x

    def f2(x):
        return x * (v1 - x) / 2

    integral1 = integrate.quad(func=f1, a=v_min, b=v2)
    integral2 = integrate.quad(func=f2, a=v2, b=v1)
    return (integral1[0] + integral2[0]) / s


fast_speed = speed_fast()
medium_speed = speed_medium()
slow_speed = speed_slow()
very_slow_speed = speed_very_slow()


# functions for angle
def no_angle():
    return math.radians(0)


def turn_left():
    return math.radians(-40)


def turn_right():
    return math.radians(40)


def rapidly_left():
    return math.radians(-90)


def rapidly_right():
    return math.radians(90)


def turnaround():
    return math.radians(180)
