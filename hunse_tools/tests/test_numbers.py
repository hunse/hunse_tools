import numpy as np

rng = np.random.RandomState(3)  # TODO: add rng fixture

from hunse_tools.numbers import ifactor


def test_ifactor():
    for x in rng.randint(1000000, size=100):
        factors = ifactor(x)
        assert np.prod(factors) == x
