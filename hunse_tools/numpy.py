import numpy as np

# def broadcast_object(ndim, axis=-1):
#     """
#     Create an object to broadcast along the given axis.
#     """
#     slices = [slice(None) for i in xrange(nparray.ndim)]
#     slices[axis] = None
#     return slices

# def broadcast(nparray, axis=-1):
#     """
#     Broadcast along the given axis.
#     """
#     return nparray[broadcast_object(nparray.ndim, axis=axis)]


def squasher(x):
    """Squashing function to help plotting signed values with large magnitudes.

    y = { x,                             if abs(x) < 1 }
        { sign(x) * (1 + log(abs(x))),   otherwise     }
    """
    x = np.asarray(x)
    ax = np.abs(x)
    y = 1 + np.log(ax)
    y[ax < 1] = ax[ax < 1]
    return np.sign(x) * y


def rms(x, **kwargs):
    return np.sqrt((x**2).mean(**kwargs))


def is_integer(obj):
    """Check if ``obj`` is an integer type."""
    return isinstance(obj, (int, np.integer))


def legendre(n, x, method="series"):
    """Legendre polynomial of order `n` evaluated at point (or points) `x`.

    See https://en.wikipedia.org/wiki/Legendre_polynomials#Rodrigues'_formula_and_other_explicit_formulas
    """
    if method == "aaron":
        return (-1) ** n * sum(
            binomial(n, k) * binomial(n + k, k) * (-x) ** k for k in range(n + 1)
        )
    if method == "series":
        # the Legendre series is a stable way to compute a Legendre polynomial of high order
        if n == 0:
            return np.ones_like(x)
        x1 = 2 * x - 1
        series = [None, np.zeros_like(x), np.ones_like(x)]
        for i in range(0, n):
            series.pop(0)
            series.append(
                (2 * i + 1) / (i + 1) * x1 * series[-1] - i / (i + 1) * series[-2]
            )
        return series[-1]

    raise ValueError(f"Unknown method '{method}'")
