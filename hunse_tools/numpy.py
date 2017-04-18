
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
