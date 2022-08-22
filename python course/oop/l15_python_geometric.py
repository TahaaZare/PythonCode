import math

class Rectangle:
    # def __init__(self, hight, width):
    #     self.hight = hight
    #     self.width = width

    def __init__(self,h,w):
        self.hight = h
        self.width = w
        

    def Area(self):
        area = self.width * self.hight
        return area


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return (self.radius * self.radius) * math.pi
