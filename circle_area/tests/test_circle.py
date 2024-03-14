import unittest
from circle_area.circle import Circle


class TestCircle(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483, places=2)

    def test_unittest_main(self):
        unittest.main()


if __name__ == '__main__':
    unittest.main()
