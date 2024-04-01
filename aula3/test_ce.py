import pytest

def sum(a:int, b:int) -> int:
    return a+b

@pytest.mark.parametrize(
    argnames="a,b,result",
    argvalu=[
        (1,2,3),
        (2,2,'a')
    ]
)

def test_cenas(a,b,result):
    assert sum(a,b) is result

def two():
    assert 1 ==1

        