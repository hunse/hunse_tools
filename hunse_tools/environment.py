import os


# --- Display
def has_display():
    return ('DISPLAY' in os.environ)


# --- iPython
_is_ipython = None


def is_ipython():
    global _is_ipython
    if _is_ipython is None:
        try:
            __IPYTHON__
            _is_ipython = True
        except NameError:
            _is_ipython = False

    return _is_ipython
