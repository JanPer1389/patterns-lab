from math import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'x = {self.x}, y= {self.y}'
    
    @staticmethod
    def new_cartesian_method(x,y):
        return Point(x,y)
    @staticmethod
    def new_polar_method(x,y):
        return Point(x * sin(y), x*cos(y))

if __name__=='__main__':
    p = Point(2,5)
    p2= Point.new_polar_method(2,5)
    print(p, p2)