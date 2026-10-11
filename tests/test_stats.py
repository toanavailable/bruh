import pytest

from calculator import mean, median, normalize


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5


def test_mean_empty_raises():
    with pytest.raises(ValueError):
        mean([])


def test_median():
    assert median([5, 1, 3]) == 3.0
    assert median([1, 2, 3, 4]) == 2.5


def test_median_empty_raises():
    with pytest.raises(ValueError):
        median([])


def test_normalize():
    assert normalize([10, 15, 20]) == [0.0, 0.5, 1.0]


def test_normalize_constant_values():
    assert normalize([7, 7, 7]) == [0.0, 0.0, 0.0]


def test_normalize_empty_raises():
    with pytest.raises(ValueError):
        normalize([])
