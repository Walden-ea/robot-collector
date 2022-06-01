# mock for a navigation system
import math
from scipy import integrate

from .map_item import Map_item


# from .robot import Robot

def check_sensors(robot):
    # возвращаем 0 - стен нет, 1 - стена у первого сенсора, 2 - у второго,
    # 3 - у третьего, 4 - стены у всех трёх сенсоров
    if robot.sensors[0].collide_object is None and robot.sensors[1].collide_object is None \
            and robot.sensors[2].collide_object is None:
        return 0
    elif robot.sensors[0].collide_object is not None and robot.sensors[1].collide_object is not None \
            and robot.sensors[2].collide_object is not None:
        return 4
    elif robot.sensors[0].collide_object is not None and robot.sensors[1].collide_object is None \
            and robot.sensors[2].collide_object is None:
        return 1
    elif robot.sensors[0].collide_object is None and robot.sensors[1].collide_object is not None \
            and robot.sensors[2].collide_object is None:
        return 2
    else:
        return 3


def calc(robot):
    # Checking sensors when map_item is a piece of garbage
    # Returning fast speed
    # todo а есть какие-нибудь доки для тегов(??)
    if 40.0 >= robot.sensors[0].distance >= 18.0 and 40.0 >= robot.sensors[1].distance >= 18.0 and \
            40.0 >= robot.sensors[2].distance >= 18.0:
        return fast_speed, no_angle()

    # Returning medium speed
    if 40.0 >= robot.sensors[0].distance >= 18.0 and 40.0 >= robot.sensors[1].distance >= 18.0 and 20.0 >= \
            robot.sensors[2].distance >= 13.0 and (check_sensors(robot) != 0 or check_sensors(robot) != 3):
        return medium_speed, turn_right()
    if 40.0 >= robot.sensors[0].distance >= 18.0 and 20.0 >= robot.sensors[1].distance >= 13.0 and 40.0 >= \
            robot.sensors[2].distance >= 18.0 and (check_sensors(robot) != 0 or check_sensors(robot) != 2):
        return medium_speed, no_angle()
    if 20.0 >= robot.sensors[0].distance >= 13.0 and 40.0 >= robot.sensors[1].distance >= 18.0 and 40.0 >= \
            robot.sensors[2].distance >= 18.0 and (check_sensors(robot) != 0 or check_sensors(robot) != 1):
        return medium_speed, turn_left()
    if 20.0 >= robot.sensors[0].distance >= 13.0 and 20.0 >= robot.sensors[1].distance >= 13.0 and 40.0 >= \
            robot.sensors[2].distance >= 18.0 and \
            (check_sensors(robot) != 0 or check_sensors(robot) != 1 or check_sensors(robot) != 2):
        return medium_speed, turn_left()
    if 20.0 >= robot.sensors[0].distance >= 13.0 and 40.0 >= robot.sensors[1].distance >= 18.0 and 20.0 >= \
            robot.sensors[2].distance >= 13.0 and (check_sensors(robot) != 0 or check_sensors(robot) != 2):
        return medium_speed, no_angle()
    if 40.0 >= robot.sensors[0].distance >= 18.0 and 20.0 >= robot.sensors[1].distance >= 13.0 and 20.0 >= \
            robot.sensors[2].distance >= 13.0 and \
            (check_sensors(robot) != 0 or check_sensors(robot) != 2 or check_sensors(robot) != 3):
        return medium_speed, turn_right()

    # Returning slow speed
    if 20.0 >= robot.sensors[0].distance >= 13.0 and 20.0 >= robot.sensors[1].distance >= 13.0 and 20.0 >= \
            robot.sensors[2].distance >= 13.0 and (check_sensors(robot) != 0 or check_sensors(robot) != 2):
        return slow_speed, no_angle()
    if 20.0 >= robot.sensors[0].distance >= 13.0 and 20.0 >= robot.sensors[1].distance >= 13.0 and 15.0 >= \
            robot.sensors[2].distance >= 4.0 and (check_sensors(robot) != 0 or check_sensors(robot) != 3):
        return slow_speed, turn_right()
    if 20.0 >= robot.sensors[0].distance >= 13.0 and 15.0 >= robot.sensors[1].distance >= 4.0 and 20.0 >= \
            robot.sensors[2].distance >= 13.0 and (check_sensors(robot) != 0 and check_sensors(robot) != 2):
        return slow_speed, no_angle()
    if 15.0 >= robot.sensors[0].distance >= 4.0 and 20.0 >= robot.sensors[1].distance >= 13.0 and 20.0 >= \
            robot.sensors[2].distance >= 13.0 and (check_sensors(robot) != 0 or check_sensors(robot) != 1):
        return slow_speed, turn_left()
    if 15.0 >= robot.sensors[0].distance >= 4.0 and 15.0 >= robot.sensors[1].distance >= 4.0 and 20.0 >= \
            robot.sensors[2].distance >= 13.0 and \
            (check_sensors(robot) != 0 or check_sensors(robot) != 1 or check_sensors(robot) != 2):
        return slow_speed, turn_left()
    if 15.0 >= robot.sensors[0].distance >= 4.0 and 20.0 >= robot.sensors[1].distance >= 13.0 and 15.0 >= \
            robot.sensors[2].distance >= 4.0 and (check_sensors(robot) != 0 or check_sensors(robot) != 2):
        return slow_speed, no_angle()
    if 20.0 >= robot.sensors[0].distance >= 13.0 and 15.0 >= robot.sensors[1].distance >= 4.0 and 15.0 >= \
            robot.sensors[2].distance >= 4.0 and \
            (check_sensors(robot) != 0 or check_sensors(robot) != 2 or check_sensors(robot) != 3):
        return slow_speed, turn_right()

    # Returning very slow speed
    if 15.0 >= robot.sensors[0].distance >= 4.0 and 15.0 >= robot.sensors[1].distance >= 4.0 and 15.0 >= \
            robot.sensors[2].distance >= 4.0 and (check_sensors(robot) != 0 or check_sensors(robot) != 2):
        return very_slow_speed, no_angle()
    if 8.0 >= robot.sensors[0].distance >= 0 and 15.0 >= robot.sensors[1].distance >= 4.0 and 15.0 >= \
            robot.sensors[2].distance >= 4.0 and (check_sensors(robot) != 0 or check_sensors(robot) != 1):
        return very_slow_speed, turn_left()
    if 15.0 >= robot.sensors[0].distance >= 4.0 and 8.0 >= robot.sensors[1].distance >= 0 and 15.0 >= \
            robot.sensors[2].distance >= 4.0 and (check_sensors(robot) != 0 and check_sensors(robot) != 2):
        return very_slow_speed, no_angle()
    if 15.0 >= robot.sensors[0].distance >= 4.0 and 15.0 >= robot.sensors[1].distance >= 4.0 and 8.0 >= \
            robot.sensors[2].distance >= 0 and (check_sensors(robot) != 0 or check_sensors(robot) != 3):
        return very_slow_speed, turn_right()
    if 8.0 >= robot.sensors[0].distance >= 0 and 8.0 >= robot.sensors[1].distance >= 0 and 15.0 >= \
            robot.sensors[2].distance >= 4.0 and \
            (check_sensors(robot) != 0 or check_sensors(robot) != 1 or check_sensors(robot) != 2):
        return very_slow_speed, turn_left()
    if 8.0 >= robot.sensors[0].distance >= 0 and 15.0 >= robot.sensors[1].distance >= 4.0 and 8.0 >= \
            robot.sensors[2].distance >= 0 and (check_sensors(robot) != 0 or check_sensors(robot) != 2):
        return very_slow_speed, no_angle()
    if 15.0 >= robot.sensors[0].distance >= 4.0 and 8.0 >= robot.sensors[1].distance >= 0 and 8.0 >= \
            robot.sensors[2].distance >= 0 and \
            (check_sensors(robot) != 0 or check_sensors(robot) != 2 or check_sensors(robot) != 3):
        return very_slow_speed, turn_right()
    if 8.0 >= robot.sensors[0].distance >= 0 and 8.0 >= robot.sensors[1].distance >= 0 and 8.0 >= \
            robot.sensors[2].distance >= 0 and (check_sensors(robot) != 0 or check_sensors(robot) != 2):
        return very_slow_speed, no_angle()

    # Now checking when map_item is actually a wall
    if 8.0 >= robot.sensors[0].distance >= 0 and 15.0 >= robot.sensors[1].distance >= 4.0 and 15.0 >= \
            robot.sensors[2].distance >= 4.0 and check_sensors(robot) == 1:
        return very_slow_speed, rapidly_right()
    if 15.0 >= robot.sensors[0].distance >= 4.0 and 8.0 >= robot.sensors[1].distance >= 0 and 15.0 >= \
            robot.sensors[2].distance >= 4.0 and check_sensors(robot) == 2:
        return very_slow_speed, rapidly_right()
    if 15.0 >= robot.sensors[0].distance >= 4.0 and 15.0 >= robot.sensors[1].distance >= 4.0 and 8.0 >= \
            robot.sensors[2].distance >= 0 and check_sensors(robot) == 3:
        return very_slow_speed, rapidly_left()
    if 8.0 >= robot.sensors[0].distance >= 0 and 8.0 >= robot.sensors[1].distance >= 0 and 15.0 >= \
            robot.sensors[2].distance >= 4.0 and check_sensors(robot) == 1 and check_sensors(robot) == 2:
        return very_slow_speed, rapidly_right()
    if 8.0 >= robot.sensors[0].distance >= 0 and 15.0 >= robot.sensors[1].distance >= 4.0 and 8.0 >= \
            robot.sensors[2].distance >= 0 and \
            (check_sensors(robot) == 4 or check_sensors(robot) == 1 and check_sensors(robot) == 3):
        return very_slow_speed, turnaround()
    if 15.0 >= robot.sensors[0].distance >= 4.0 and 8.0 >= robot.sensors[1].distance >= 0 and 8.0 >= \
            robot.sensors[2].distance >= 0 and check_sensors(robot) == 2 and check_sensors(robot) == 3:
        return very_slow_speed, rapidly_left()
    if 8.0 >= robot.sensors[0].distance >= 0 and 8.0 >= robot.sensors[1].distance >= 0 and 8.0 >= \
            robot.sensors[2].distance >= 0 and check_sensors(robot) == 4:
        return very_slow_speed, turnaround()


v_min = 0
v1 = 7
v2 = 6
v3 = 15.0
v4 = 12
v5 = 20.0
v6 = 18.0
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
