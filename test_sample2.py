import pytest

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a/b

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 0.5),
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (0, 1, 0),
    (0, 1, 0),
])

def test_divide(a, b, expected):
    assert divide(a, b) == expected

@pytest.mark.parametrize("a, b", [
    (1, 0)
])
def test_divide_zero_division(a, b):
    with pytest.raises(ZeroDivisionError):
        divide(a, b)


# Even or not

def isEven(num):
    if num % 2 == 0:
        return True
    else :
        return False
    
@pytest.mark.parametrize("num, expected",[
    (2, True),
    (3, False),
    (4, True),
    (0, True)
])
def test_isEven(num, expected):
    result = isEven(num)
    assert result == expected

