"""
Functions for number theory and things related to numbers.
"""
from __future__ import absolute_import

import numpy as np


def binomial(n, k):
    """Compute generalized binomial coefficient, allowing for negative n.

    https://en.wikipedia.org/wiki/Binomial_coefficient#Generalization_and_connection_to_the_binomial_series
    """
    result = 1
    for i in range(k):
        result *= (n - i) / (k - i)

    return result


def factorial_ratio(num, den=()):
    """Compute ratio of factorials.

    prod(factorial(n) for n in num) / prod(factorial(d) for d in den)
    """

    m = max(max(num), max(den))

    result = 1
    for i in range(1, m + 1):
        q = sum(1 for n in num if i <= n) - sum(1 for d in den if i <= d)
        result *= i**q

    return result


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


def reduce(a, b=1):
    """Reduce fraction"""

    if isinstance(a, float):
        while int(a) != a:
            a = a * 10
            b = b * 10
        a = int(a)

    print("Reducing %d/%d" % (a, b))

    running = True
    while running:
        for i in range(int(np.sqrt(min(a, b))), 1, -1):
            if a % i == 0 and b % i == 0:
                a = a // i
                b = b // i
                break
        else:
            running = False

    print("Reduced to %d/%d" % (a, b))
    return a, b


def birthday(n, k):
    """Compute the n/k 'birthday' number.

    This is the probability of no overlapping choices when choosing ``k`` items from a
    set of ``n``. For example, the probability of no overlapping birthdays in a room of
    30 people is ``birthday(365, 30)``.
    """
    p = 1
    for i in range(1, k):
        p *= (n - i) / n
    return p
