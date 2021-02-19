import numpy as np

from hunse_tools.timing import tic, toc


def test_tic_toc():
    rng = np.random.RandomState(0)
    n = int(1e6)

    tic()
    rng.normal(size=n)
    t0 = toc()

    tic()
    rng.normal(size=5 * n)
    t1 = toc()

    assert 0.001 <= t0 <= 10
    assert 3 * t0 <= t1 <= 30
