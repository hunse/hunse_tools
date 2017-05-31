"""
Functions for number theory and things related to numbers.
"""
from __future__ import absolute_import

import numpy as np


def ifactor(x):
    """Determine the integer factors of x"""
    if x < 1:
        return None
    if x == 1:
        return [1]

    factors = []
    end = np.sqrt(x)
    i = 2
    while i < x:
        if x % i == 0:
            factors.append(i)
            x /= i
        elif i == 2:
            i += 1
        else:
            i += 2

    assert i == x
    factors.append(i)

    return factors
