"""Basic statistics on numeric data."""

from collections.abc import Sequence
from pathlib import Path

import numpy as np
import numpy.typing as npt


def mean(values: Sequence[float]) -> float:
    """Return the arithmetic mean of ``values``."""
    if len(values) == 0:
        raise ValueError("mean() requires at least one value")
    return float(np.mean(values))


def median(values: Sequence[float]) -> float:
    """Return the median of ``values``."""
    if len(values) == 0:
        raise ValueError("median() requires at least one value")
    return float(np.median(values))


def normalize(values: Sequence[float]) -> list[float]:
    """Scale ``values`` linearly into the range [0, 1]."""
    if len(values) == 0:
        raise ValueError("normalize() requires at least one value")
    array = np.asarray(values, dtype=float)
    low, high = array.min(), array.max()
    if low == high:
        return [0.0] * len(values)
    scaled: list[float] = ((array - low) / (high - low)).tolist()
    return scaled


def load_csv(path: str | Path) -> npt.NDArray[np.float64]:
    """Load a numeric CSV file with a single header row."""
    data: npt.NDArray[np.float64] = np.loadtxt(path, delimiter=",", skiprows=1, ndmin=2)
    return data
