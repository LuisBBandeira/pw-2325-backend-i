import unittest

class Rectangle:

    def __init__(self , width:int ,height:int ):
        self.width = width
        self.height = height
    
    def get_area(self)->int:
        return self.width*self.height
    
    def get_perimeter(self)->int:
        return (self.width*2)+(self.height*2)

class RectangleTest(unittest.TestCase):

    def setUp(self) -> None:
        self.rectangle = Rectangle(width=5 ,height=7)

    def test_calculate_area(self):

        area = self.rectangle.get_area()

        self.assertEqual(area, 35)

    def test_calculate_perimeter(self):
        perimeter = self.rectangle.get_perimeter()
        assert perimeter == 24

if __name__ == "__main__":
    unittest.main()    