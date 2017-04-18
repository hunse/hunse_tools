import time

_timers = []


def tic(name=None):
    _timers.append((name, time.time()))


def toc(display=True):
    t1 = time.time()
    name, t0 = _timers.pop()
    t = t1 - t0

    if display:
        nstr = " (%s)" % name if name is not None else ""
        print("elapsed time%s: %0.6f seconds" % (nstr, t))

    return t
