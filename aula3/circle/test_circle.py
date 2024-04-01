import pytest
import math


def get_area(radius)->float:
    return math.pi*(radius**2)
    
def get_perimeter(radius)->float:
    return 2*math.pi*radius

@pytest.mark.parametrize(
    argnames="radius",
    argvalues=[
        (15.8)
    ]
)

def test_rectangle(radius):
    round(get_area(radius) ,2) == 784.27
    round(get_perimeter(radius) ,2) == 99.27
