import pytest

from calculator.calculator import Calculator


@pytest.mark.parametrize('a, b, result', ((7, 2, 9), (2, 5, 7)))
def test_add_2(a: float, b: float, result: float):
    assert Calculator.add(a, b) == result


@pytest.mark.parametrize('a, b, c, result', ((7, 2, 1, 10), (2, 5, 1, 8)))
def test_add_3(a: float, b: float, c: float, result: float):
    assert Calculator.add(a, b, c) == result


@pytest.mark.parametrize('a, result', (((7, 2, 1), 10), ((2, 5, 1), 8)))
def test_add(a: list[float], result: float):
    assert Calculator.add(*a) == result


@pytest.mark.parametrize('a, b, result', ((5, 2, 3), (7, 2, 5)))
def test_sub_2(a: float, b: float, result: float):
    assert Calculator.sub(a, b) == result


@pytest.mark.parametrize('a, b, result', ((5, 2, 10), (3, 6, 18)))
def test_multiply(a: float, b: float, result: float):
    assert Calculator.multiply(a, b) == pytest.approx(result)


@pytest.mark.parametrize('a, result', (((5, 2, 1), 10), ((3, 6, 1), 18)))
def test_multiply_many(a: list[float], result: float):
    assert Calculator.multiply(*a) == pytest.approx(result)


@pytest.mark.parametrize('a, b, result', ((5, 2, 2.5), (10, 5, 2), (10, 0, float('inf'))))
def test_div(a: float, b: float, result: float):
    assert Calculator.div(a, b) == pytest.approx(result)