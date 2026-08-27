from calculator import add
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
