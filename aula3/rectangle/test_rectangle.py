import pytest
from rectangle import Rectangle


@pytest.mark.parametrize(
    argnames="width,height",
    argvalues=[
        (5,7)
    
    ]
)

def test_rectangle(width, height):

    area = Rectangle(width,height).get_area()
    perimeter = Rectangle(width,height).get_perimeter()
    assert area == 35
    assert perimeter == 24



        