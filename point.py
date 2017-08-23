#!/usr/bin/env python 
import os
import sys

class Point:
    # initialization method
    # it is called automatically when a class is called

    # When defining a method, the first parameter refers to the instance being created. It is customary to name this parameter self.

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    
    def distance_from_origin(self):
        dist = (self.x ** 2 + self.y ** 2) ** (0.5)
        return dist

    def __str__(self):
        return 'Point: (' + str(self.x) + ', ' + str(self.y) + ')'

    def __add__(self, other):
        print "Adding ..."
        return Point((self.x + other.x), (self.y + other.y))

    def __sub__(self, other):
        print "Subtracting ..."
        return Point((self.x - other.x), (self.y - other.y))

    def __mul__(self, other):
        print "Point Multiplication ..."
        return Point((self.x * other.x), (self.y * other.y))

    def __rmul__(self, scale):
        print "Scalar Multiplication ..."
        return Point((self.x * scale), (self.y * scale))



if __name__ == '__main__':
    p1 = Point(3, 4)
    print p1

    p2 = Point(5, 12)
    print p2

    p3 = p1 + p2
    print p3

    p4 = p3 - p1
    print p4

    p5 = p1 * p2
    print p5

    p6 = 2 * p5
    print p6

    p7 = p6 * 2
    print p7
