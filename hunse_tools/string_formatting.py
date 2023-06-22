import numpy as np

from hunse_tools.numpy import is_integer

# def format_memory(memory_in_bytes):
#     memory_types = ("B", "KB", "MB", "GB", "TB")
#     memory = memory_in_bytes
#     i = 0
#     while i < len(memory_types) - 1 and memory >= 1024:
#         i += 1
#         memory /= 1024

#     return f"{memory:0.1f} {memory_types[i]}"


# def format_magnitude(x, space=False):
#     if x == 0:
#         return "0"

#     mag_types = ("", "k", "M", "B", "T")
#     i = 0
#     for i, mag_type in enumerate(mag_types):
#         if x < 1000:
#             break
#         elif i < len(mag_types) - 1:
#             x = x / 1000

#     return f"{x:0.1f}{' ' if space and mag_type else ''}{mag_type}"


def format_magnitude(
    x,
    *,
    precision=3,
    decimals=None,
    base=10,
    shift=3,
    types=("", "k", "M", "B", "T"),
    space=True,
):
    log = {2: np.log2, 10: np.log10}[base]
    i = 0 if x == 0 else int(log(np.abs(x)) // shift)
    i = min(max(i, 0), len(types) - 1)

    y = x * base ** (-shift * i)
    if decimals is None:
        if is_integer(y) or y == 0:
            decimals = 0
        else:
            j = int(np.floor(np.log10(np.abs(y))))
            decimals = max(-j, precision - 1) if j < 0 else precision - j - 1
            decimals = max(decimals, 0)

    fstr = f"{{:0.{decimals}f}}"
    typ = types[i]
    return f"{fstr.format(y)}{' ' if space and typ else ''}{typ}"


def format_memory(memory_in_bytes, **kwargs):
    kwargs.setdefault("space", True)
    return format_magnitude(
        memory_in_bytes, base=2, shift=10, types=("B", "KB", "MB", "GB", "TB"), **kwargs
    )
