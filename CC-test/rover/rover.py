#!/usr/bin/env python

import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{round(self.x, 2):.2f} {round(self.y, 2):.2f}"

    def __repr__(self):
        return str(self)

    def __sub__(self, other):
        return (self.y - other.y) / (self.x - other.x)


class Rover:
    def __init__(self, wheelBase):
        self.postion = Point()
        self.wheelBase = wheelBase

    def steer(self, angle):
        self.angle = math.radians(angle)
        self.turnRadius = self.wheelBase / math.sin(self.angle)

    def rg(self, dist):
        return math.sin(self.angle)/(math.sin(self.R())/(dist/self.angle))

    def R(self):
        return (math.pi - self.angle) / 2

    def newPos(self, dist):
        a = math.pi/2 - self.R()
        rg = self.rg(dist)
        return Point(math.sin(a) * rg, math.cos(a) * rg)

    def move(self, dist):
        self.newPosition = self.newPos(dist)
        self.newAngle = math.pi/2 - self.R()

    def __str__(self):
        return f"{self.newPosition} {self.newAngle}"

    def __repr__(self):
        return str(self)


r = Rover(1)
r.steer(30)
r.move(1)
print(r)
