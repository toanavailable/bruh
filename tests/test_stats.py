import pytest

from calculator import mean, normalize


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5


def test_mean_empty_raises():
    with pytest.raises(ValueError):
        mean([])


def test_normalize():
    assert normalize([10, 15, 20]) == [0.0, 0.5, 1.0]


def test_normalize_constant_values():
    assert normalize([7, 7, 7]) == [0.0, 0.0, 0.0]


def test_normalize_empty_raises():
    with pytest.raises(ValueError):
        normalize([])
