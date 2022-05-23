from calculator import Calculator, CalculatorError
import pytest

calcy = Calculator()


def test_add():
    result = calcy.add(10, 20)
    assert result == 30
    result = calcy.add(1, -1)
    assert result == 0

    with pytest.raises(CalculatorError):
        result = calcy.add("two", 3)


def test_add_string():
    result = calcy.add(10, 20)
    assert result == 30
    result = calcy.add(1, -1)
    assert result == 0

    with pytest.raises(CalculatorError) as context:
        result = calcy.add("two", "three")

    assert str(context.value) == "two was not a number"


def test_sub():
    assert calcy.sub(10, 0) == 10
    assert calcy.sub(-1, -1) == 0
    assert calcy.sub(100, -10) == 110


def test_mul():
    assert calcy.mul(10, 10) == 100
    assert calcy.mul(0, 100) == 0
    assert calcy.mul(-1, 100) == -100


def test_div():
    assert calcy.div(10, 10) == 1
    assert calcy.div(0, 10) == 0


def test_div_by_zero():
    with pytest.raises(CalculatorError):
        result = calcy.div(9, 0)


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (3, 5, 8),
    (5, 0, 5),
    (10, -5, 5)
])
def test_with_param(a, b, expected):
    assert calcy.add(a, b) == expected