"""This file contains all the exercises relating to the Vector Exercises (9.4-9.7)."""

import math


class Vector:
    """A class that represents a Vector, defined by the endpoint :math:`(x,y)`."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def scale(self, s):
        v_scaled = Vector(self.x * s, self.y * s)
        return v_scaled

    def add(self, v):
        v3 = Vector(self.x + v.x, self.y + v.y)
        return v3

    def dot(self, v):
        v3 = (self.x * v.x) + (self.y * v.y)
        return v3


if __name__ == "__main__":
    v1 = Vector(2, 3)
    v_scale = v1.scale(1.5)
    print(v_scale)
