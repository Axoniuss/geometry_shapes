import unittest
from geometry_shapes.circle import Circle

class TestCircle(unittest.TestCase):
    def test_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483, places=5)

    def test_is_right_angle(self):
        circle = Circle(5)
        self.assertFalse(circle.is_right_angle())

if __name__ == '__main__':
    unittest.main()
