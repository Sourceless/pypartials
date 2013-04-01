from inspect import getargspec

class partial(object):
    """
    Takes a function, returning a partial object
    Captures arguments until there's enough to call
    """
    def __init__(self, f, *varargs):
        self.f = f
        self.maxargs = len(getargspec(self.f)[args])
        self.posargs = varargs

        self._enough_args()

    def _enough_args(self):
        if len(posargs) > self.maxargs:
            pass # Exception goes here
        elif len(posargs) == self.maxargs:
            return True
        else:
            return False
