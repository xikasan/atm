# -*- coding: utf-8 -*-

import numpy as np


MAX_SEED_VALUE = 2**16


def seeding(seed: int = None):
    if seed is None:
        seed = np.random.randint(1, MAX_SEED_VALUE)
    rs = np.random(seed)
    return rs, seed


class RandomState:

    def __init__(self, seed=None):
        self.rs, self.seed = seeding(seed)

    def rand(self):
        return self.rs.random(size)
