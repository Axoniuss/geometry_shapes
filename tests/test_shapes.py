import unittest
from geometry_shapes.utils import calculate_area, is_right_angle
from geometry_shapes.circle import Circle
from geometry_shapes.triangle import Triangle

class TestShapes(unittest.TestCase):
    def test_calculate_area_circle(self):
        circle = Circle(5)
        self.assertAlmostEqual(calculate_area(circle), 78.53981633974483, places=5)

    def test_calculate_area_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(triangle), 6.0, places=5)

    def test_is_right_angle_circle(self):
        circle = Circle(5)
        self.assertFalse(is_right_angle(circle))

    def test_is_right_angle_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(is_right_angle(triangle))

if __name__ == '__main__':
    unittest.main()
