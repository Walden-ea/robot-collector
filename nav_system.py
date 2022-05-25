# mock for a navigation system
import math
import random

from classes.map_item import Map_item
from classes.robot import Robot


def calc(robot: Robot, map_item: Map_item):
    # Checking sensors when map_item is a piece of garbage
    # Returning fast speed
    if robot.sensors[0] <= 40 & robot.sensors[0] >= 18 & robot.sensors[1] <= 40 \
            & robot.sensors[1] >= 18 & robot.sensors[2] <= 40 & robot.sensors[2] >= 18\
            & map_item.tag != 0:
        return speed_fast(), no_angle()

    # Returning medium speed
    if robot.sensors[0] <= 40 & robot.sensors[0] >= 18 & robot.sensors[1] <= 40 \
            & robot.sensors[1] >= 18 & robot.sensors[2] <= 20 & robot.sensors[2] >= 13\
            & map_item.tag != 0:
        return speed_medium(), turn_right()
    if robot.sensors[0] <= 40 & robot.sensors[0] >= 18 & robot.sensors[1] <= 20 \
            & robot.sensors[1] >= 13 & robot.sensors[2] <= 40 & robot.sensors[2] >= 18\
            & map_item.tag != 0:
        return speed_medium(), no_angle()
    if robot.sensors[0] <= 20 & robot.sensors[0] >= 13 & robot.sensors[1] <= 40 \
            & robot.sensors[1] >= 18 & robot.sensors[2] <= 40 & robot.sensors[2] >= 18\
            & map_item.tag != 0:
        return speed_medium(), turn_left()
    if robot.sensors[0] <= 20 & robot.sensors[0] >= 13 & robot.sensors[1] <= 20 \
            & robot.sensors[1] >= 13 & robot.sensors[2] <= 40 & robot.sensors[2] >= 18\
            & map_item.tag != 0:
        return speed_medium(), turn_left()
    if robot.sensors[0] <= 20 & robot.sensors[0] >= 13 & robot.sensors[1] <= 40 \
            & robot.sensors[1] >= 18 & robot.sensors[2] <= 20 & robot.sensors[2] >= 13\
            & map_item.tag != 0:
        return speed_medium(), no_angle()
    if robot.sensors[0] <= 40 & robot.sensors[0] >= 18 & robot.sensors[1] <= 20 \
            & robot.sensors[1] >= 13 & robot.sensors[2] <= 20 & robot.sensors[2] >= 13\
            & map_item.tag != 0:
        return speed_medium(), turn_right()

    # Returning slow speed
    if robot.sensors[0] <= 20 & robot.sensors[0] >= 13 & robot.sensors[1] <= 20 \
            & robot.sensors[1] >= 13 & robot.sensors[2] <= 20 & robot.sensors[2] >= 13 \
            & map_item.tag != 0:
        return speed_slow(), no_angle()
    if robot.sensors[0] <= 20 & robot.sensors[0] >= 13 & robot.sensors[1] <= 20 \
            & robot.sensors[1] >= 13 & robot.sensors[2] <= 15 & robot.sensors[2] >= 4\
            & map_item.tag != 0:
        return speed_slow(), turn_right()
    if robot.sensors[0] <= 20 & robot.sensors[0] >= 13 & robot.sensors[1] <= 15 \
            & robot.sensors[1] >= 4 & robot.sensors[2] <= 20 & robot.sensors[2] >= 13 \
            & map_item.tag != 0:
        return speed_slow(), no_angle()
    if robot.sensors[0] <= 15 & robot.sensors[0] >= 4 & robot.sensors[1] <= 20 \
            & robot.sensors[1] >= 13 & robot.sensors[2] <= 20 & robot.sensors[2] >= 13 \
            & map_item.tag != 0:
        return speed_slow(), turn_left()
    if robot.sensors[0] <= 15 & robot.sensors[0] >= 4 & robot.sensors[1] <= 15 \
            & robot.sensors[1] >= 4 & robot.sensors[2] <= 20 & robot.sensors[2] >= 13 \
            & map_item.tag != 0:
        return speed_slow(), turn_left()
    if robot.sensors[0] <= 15 & robot.sensors[0] >= 4 & robot.sensors[1] <= 20 \
            & robot.sensors[1] >= 13 & robot.sensors[2] <= 15 & robot.sensors[2] >= 4 \
            & map_item.tag != 0:
        return speed_slow(), no_angle()
    if robot.sensors[0] <= 20 & robot.sensors[0] >= 13 & robot.sensors[1] <= 15 \
            & robot.sensors[1] >= 4 & robot.sensors[2] <= 15 & robot.sensors[2] >= 4 \
            & map_item.tag != 0:
        return speed_slow(), turn_right()

    # Returning very slow speed
    if robot.sensors[0] <= 15 & robot.sensors[0] >= 4 & robot.sensors[1] <= 15 \
            & robot.sensors[1] >= 4 & robot.sensors[2] <= 15 & robot.sensors[2] >= 4 \
            & map_item.tag != 0:
        return speed_very_slow(), no_angle()
    if robot.sensors[0] <= 8 & robot.sensors[0] >= 0 & robot.sensors[1] <= 15 \
            & robot.sensors[1] >= 4 & robot.sensors[2] <= 15 & robot.sensors[2] >= 4 \
            & map_item.tag != 0:
        return speed_very_slow(), turn_left()
    if robot.sensors[0] <= 15 & robot.sensors[0] >= 4 & robot.sensors[1] <= 8 \
            & robot.sensors[1] >= 0 & robot.sensors[2] <= 15 & robot.sensors[2] >= 4 \
            & map_item.tag != 0:
        return speed_very_slow(), no_angle()
    if robot.sensors[0] <= 15 & robot.sensors[0] >= 4 & robot.sensors[1] <= 15 \
            & robot.sensors[1] >= 4 & robot.sensors[2] <= 8 & robot.sensors[2] >= 0 \
            & map_item.tag != 0:
        return speed_very_slow(), turn_right()
    if robot.sensors[0] <= 8 & robot.sensors[0] >= 0 & robot.sensors[1] <= 8 \
            & robot.sensors[1] >= 0 & robot.sensors[2] <= 15 & robot.sensors[2] >= 4 \
            & map_item.tag != 0:
        return speed_very_slow(), turn_left()
    if robot.sensors[0] <= 8 & robot.sensors[0] >= 0 & robot.sensors[1] <= 15 \
            & robot.sensors[1] >= 4 & robot.sensors[2] <= 8 & robot.sensors[2] >= 0 \
            & map_item.tag != 0:
        return speed_very_slow(), no_angle()
    if robot.sensors[0] <= 15 & robot.sensors[0] >= 4 & robot.sensors[1] <= 8 \
            & robot.sensors[1] >= 0 & robot.sensors[2] <= 8 & robot.sensors[2] >= 0 \
            & map_item.tag != 0:
        return speed_very_slow(), turn_right()
    if robot.sensors[0] <= 8 & robot.sensors[0] >= 0 & robot.sensors[1] <= 8 \
            & robot.sensors[1] >= 0 & robot.sensors[2] <= 8 & robot.sensors[2] >= 0 \
            & map_item.tag != 0:
        return speed_very_slow(), no_angle()

    # Now checking when map_item is actually a wall
    if robot.sensors[0] <= 8 & robot.sensors[0] >= 0 & robot.sensors[1] <= 15 \
            & robot.sensors[1] >= 4 & robot.sensors[2] <= 15 & robot.sensors[2] >= 4 \
            & map_item.tag == 0:
        return speed_very_slow(), rapidly_right()
    if robot.sensors[0] <= 15 & robot.sensors[0] >= 4 & robot.sensors[1] <= 8 \
            & robot.sensors[1] >= 0 & robot.sensors[2] <= 15 & robot.sensors[2] >= 4 \
            & map_item.tag == 0:
        return speed_very_slow(), rapidly_right()
    if robot.sensors[0] <= 15 & robot.sensors[0] >= 4 & robot.sensors[1] <= 15 \
            & robot.sensors[1] >= 4 & robot.sensors[2] <= 8 & robot.sensors[2] >= 0 \
            & map_item.tag == 0:
        return speed_very_slow(), rapidly_left()
    if robot.sensors[0] <= 8 & robot.sensors[0] >= 0 & robot.sensors[1] <= 8 \
            & robot.sensors[1] >= 0 & robot.sensors[2] <= 15 & robot.sensors[2] >= 4 \
            & map_item.tag != 0:
        return speed_very_slow(), rapidly_right()
    if robot.sensors[0] <= 8 & robot.sensors[0] >= 0 & robot.sensors[1] <= 15 \
            & robot.sensors[1] >= 4 & robot.sensors[2] <= 8 & robot.sensors[2] >= 0 \
            & map_item.tag == 0:
        return speed_very_slow(), turnaround()
    if robot.sensors[0] <= 15 & robot.sensors[0] >= 4 & robot.sensors[1] <= 8 \
            & robot.sensors[1] >= 0 & robot.sensors[2] <= 8 & robot.sensors[2] >= 0 \
            & map_item.tag == 0:
        return speed_very_slow(), rapidly_left()
    if robot.sensors[0] <= 8 & robot.sensors[0] >= 0 & robot.sensors[1] <= 8 \
            & robot.sensors[1] >= 0 & robot.sensors[2] <= 8 & robot.sensors[2] >= 0 \
            & map_item.tag == 0:
        return speed_very_slow(), turnaround()


# Functions for speed
def speed_fast():
    return random.randint(18, 30)


def speed_medium():
    return random.randint(12, 20)


def speed_slow():
    return random.randint(6, 15)


def speed_very_slow():
    return random.randint(0, 7)


# functions for angle
def no_angle():
    return math.radians(random.randint(-10, 10))


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
