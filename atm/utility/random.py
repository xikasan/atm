# coding: utf-8

import numpy as np


def poisson_interval(interval: float, size: int = 1, rs: np.random.RandomState = None):
    if rs is None:
        rs = np.random.RandomState()
    rets = -1 * np.log(rs.rand(size)) / interval
    if size == 1:
        return rets[0]
    return rets
