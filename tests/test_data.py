from pathlib import Path

import numpy as np

from calculator import load_csv, mean

DATA_FILE = Path(__file__).parent.parent / "data" / "sample.csv"


def test_data_file_exists():
    assert DATA_FILE.exists(), f"{DATA_FILE} is missing (run `dvc pull` if tracked by DVC)"


def test_data_shape():
    data = load_csv(DATA_FILE)
    assert data.shape == (5, 2)


def test_data_has_no_missing_values():
    data = load_csv(DATA_FILE)
    assert not np.isnan(data).any()


def test_data_mean_score():
    data = load_csv(DATA_FILE)
    assert mean(data[:, 1].tolist()) == 7.0
