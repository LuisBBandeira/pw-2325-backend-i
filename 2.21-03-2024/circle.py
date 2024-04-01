import unittest
import math

class Circle:
    def __init__ (self , radius):
        self.radius = radius

    def get_area(self)->float:
        return math.pi*(self.radius**2)
    
    def get_perimeter(self)->float:
        return 2*math.pi*self.radius

class CircleTest(unittest.TestCase):

    def setUp(self) -> None:
        self.circle = Circle(radius=15.8)

    def test_calculate_area(self):

        area = self.circle.get_area()

        self.assertEqual(round(area,2), 784.27)

    def test_calculate_perimeter(self):
        perimeter = self.circle.get_perimeter()
        self.assertEqual(round(perimeter,2), 99.27)

if __name__ == "__main__":
    unittest.main() 