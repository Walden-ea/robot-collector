import math

from classes.sensor import Sensor


class Robot:
    '''
    (todo docs)
     class for a robot
    '''

    def __init__(self,
            item_count: int,
            radius: float,
            sensor_count: int = 3,
            sensor_length: float = 10.0,
            starting_location: tuple = (0.0, 0.0),
            direction: float = 0.0,  # TODO decide wether we need to store velocity in one piece or separately
            speed: float = 0.0,
            capacity: int = 10):


        if item_count > 0:
            self.item_count = item_count
        if radius > 0:
            self.radius = radius
        if sensor_count >= 0:
            self.sensors = [Sensor(sensor_length, math.pi/4), Sensor(sensor_length, 0), Sensor(sensor_length,-math.pi/4)]

        # if (is_free(location,mask(self),radius)): TODO free space checker func if needed in future

        self.location = starting_location
        self.direction = direction
        if speed >= 0:
            self.speed = speed
        if capacity > 0:
            self.capacity = capacity

#    def tick(self):
