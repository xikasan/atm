# -*- coding: utf-8 -*-

import numpy as np

from ..flight.generator import ScenarioGenerator, ScenarioIterator
from .objective import get_obj_single_runway
from ..separation import recat, faa


class Problem:

    def __init__(
            self,
            config,
            seed: int = None,
    ):
        self.cf = cf = config
        self._seed = None
        self.seed(cf, seed=seed)
        self.cf = cf = config
        self.gen = ScenarioGenerator(cf.scenario)
        self.sep = recat.TBS if cf.scenario.standard == "recat" else faa.TBS
        self._vols = self.gen(cf.num)
        self._obj = get_obj_single_runway(
            self._vols,
            self.sep,
            penalty_coef=cf.penalty_coef
        )

        self.size = cf.num

    def evaluate(self, x):
        return self._obj(x)

    @property
    def vols(self):
        return self._vols.copy()

    def __iter__(self):
        return ScenarioIterator(list(self._vols))

    def seed(self, cf=None, seed=None):
        if hasattr(cf.scenario, "seed"):
            seed = cf.scenario.seed
        self._seed = seed = self.generate_seed_if_necessary(seed)
        if hasattr(cf.scenario, "seed"):
            cf.scenario.seed = seed
        else:
            cf.scenario.set("seed", seed)
        return cf

    @staticmethod
    def generate_seed_if_necessary(seed):
        if seed is None:
            return np.random.randint(0, 1e+8)
        return int(seed)
