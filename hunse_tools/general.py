import functools


def none_default(x, *defaults):
    assert len(defaults) > 0
    i = 0
    while x is None and i < len(defaults):
        x = defaults[i]
        i += 1
    return x


def partial(func, /, *args, **kwargs):
    new = functools.partial(func, *args, **kwargs)
    functools.update_wrapper(new, func)
    return new


def prod(x):
    """Take the product of all elements in a sequence.

    The advantage over np.prod is this will return an integer 1 on an empty list/tuple,
    rather than a float.
    """
    return functools.reduce(lambda a, b: a * b, x, 1)
