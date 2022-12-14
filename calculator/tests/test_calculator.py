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


@pytest.mark.parametrize('a, b, result', ((5, 0, 'you cannot multiply by 0'),))
def test_multiply_by_0(a: float, b: float, result: str):
    with pytest.raises(ValueError) as exc:
        Calculator.multiply(a, b)

    assert result in str(exc.value)


@pytest.mark.parametrize('a, result', (((5, 5), 5), ((10, 10), 10), ([], 0)))
def test_avg(a: list[float], result: str):
    assert Calculator.avg(a) == pytest.approx(result)


@pytest.mark.parametrize('a, ut, result', (((2, 5, 12, 98), 90, 6.333333),))
def test_avg_with_ut(a: list[float], ut: float, result: str):
    assert Calculator.avg(a, ut=ut) == pytest.approx(result)


@pytest.mark.parametrize('a, lt, result', (((2, 5, 12, 98), 10, 55),))
def test_avg_with_lt(a: list[float], lt: float, result: str):
    assert Calculator.avg(a, lt=lt) == pytest.approx(result)


@pytest.mark.parametrize('a, lt, ut, result', (((12, 98), 15, 90, 0), ([], 15, 90, 0), ((12, 98), 0, 0, 0)))
def test_avg_with_lt_and_ut(a: list[float], lt: float, ut: float, result: str):
    assert Calculator.avg(a, lt=lt, ut=ut) == pytest.approx(result)
