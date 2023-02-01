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
