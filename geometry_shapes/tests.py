import unittest
from shapes import Circle, Triangle, ShapeFactory


class TestGeometry(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483, places=5)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0, places=5)

    def test_triangle_is_right(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right())

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)

    def test_shape_factory_circle(self):
        circle = ShapeFactory.create_shape('circle', 5)
        self.assertIsInstance(circle, Circle)
        self.assertAlmostEqual(circle.area(), 78.53981633974483, places=5)

    def test_shape_factory_triangle(self):
        triangle = ShapeFactory.create_shape('triangle', 3, 4, 5)
        self.assertIsInstance(triangle, Triangle)
        self.assertAlmostEqual(triangle.area(), 6.0, places=5)

    def test_shape_factory_invalid(self):
        with self.assertRaises(ValueError):
            ShapeFactory.create_shape('square', 2)


if __name__ == '__main__':
    unittest.main()
