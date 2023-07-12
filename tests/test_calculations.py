import pytest

from calculator import calculations


@pytest.mark.parametrize(
    "a, b, expected_output",
    [
        (1, 1, 2),
        (0, 0, 0),
        (420, 69, 489),
    ],
)
def test_add(a, b, expected_output):
    assert calculations.add(a, b) == expected_output


@pytest.mark.parametrize(
    "a, b, expected_output",
    [
        (1, 1, 0),
        (0, 0, 0),
        (420, 69, 351),
    ],
)
def test_subtract(a, b, expected_output):
    assert calculations.subtract(a, b) == expected_output


@pytest.mark.parametrize(
    "a, b, expected_output",
    [
        (1, 1, 1),
        (0, 0, 0),
        (420, 69, 28980),
    ],
)
def test_multiply(a, b, expected_output):
    assert calculations.multiply(a, b) == expected_output


@pytest.mark.parametrize(
    "a, b, expected_output",
    [
        (1, 1, 1),
        (0, 69, 0),
        (420, 2, 210.0),
    ],
)
def test_divide(a, b, expected_output):
    assert calculations.divide(a, b) == expected_output


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculations.divide(420, 0)
