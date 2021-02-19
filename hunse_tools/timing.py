import timeit

_timers = []


def tic(name=None):
    _timers.append((name, timeit.default_timer()))


def toc(display=True):
    t1 = timeit.default_timer()
    name, t0 = _timers.pop()
    t = t1 - t0

    if display:
        nstr = " (%s)" % name if name is not None else ""
        print("elapsed time%s: %0.6f seconds" % (nstr, t))

    return t
