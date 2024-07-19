import math
from .shapes import Shape

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def is_right_angle(self):
        return False  # Круг не может быть прямоугольным