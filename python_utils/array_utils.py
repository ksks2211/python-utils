from typing import TypeVar

import numpy as np
import pandas as pd

T = TypeVar("T", int, float)


# 백분위
def percentile(arr: list[T], percent: T):
    return np.percentile(arr, percent)


def divide_by_bins(arr: list[T], bins: list[T]):
    return pd.cut(arr, bins)


def divide_by_quantiles(arr: list[T], num_of_sections: int):
    return pd.qcut(arr, num_of_sections)
