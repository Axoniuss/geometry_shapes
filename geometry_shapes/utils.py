from .circle import Circle
from .triangle import Triangle

def calculate_area(shape):
    return shape.area()

def is_right_angle(shape):
    return shape.is_right_angle()
