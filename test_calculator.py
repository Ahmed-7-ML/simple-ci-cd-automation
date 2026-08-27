from calculator import add
import pytest

@pytest.fixture
def number1():
    return 5


@pytest.fixture
def number2():
    return 10


def test_add(number1, number2):
    assert number1 + number2 == add(number1, number2)
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
