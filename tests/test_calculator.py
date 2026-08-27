from src.calculator import add, subtract
import pytest

@pytest.mark.parametrize("number1, number2, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (10, 1, 11),
    (0, 0, 0),
    (5, 10, 15),
    (100, -50, 50),
])

def test_add(number1, number2, expected):
    assert add(number1, number2) == expected


@pytest.mark.parametrize("number1, number2, expected", [
    (2, 3, -1),
    (-1, 1, -2),
    (10, 1, 9),
    (0, 0, 0),
    (5, 10, -5),
    (100, -50, 150),
])

def test_subtract(number1, number2, expected):
    assert subtract(number1, number2) == expected
