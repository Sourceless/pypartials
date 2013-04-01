from inspect import getargspec

class partial(object):
    """
    Takes a function, returning a partial object which 
    captures arguments until there's enough to call the function.
    """
    def __init__(self, f, *varargs):
        self._f = f
        self._min_args = len(getargspec(f).args)
        self._positional_args = list(varargs)

        self.__call__() # Execute immediately if there's enough arguments.


    def __call__(self, *varargs):
        self._positional_args.extend(list(varargs))

        if self._enough_args():
            return self._f(*self._positional_args)
        else:
            return self


    def _enough_args(self):
        """
        Return a boolean indicating if there are enough arguments or not.
        """
        num_args = len(self._positional_args)

        if num_args < self._min_args:
            return False
        else:
            return True
            # Author's Note: right now it doesn't deal with there being
            #                too many arguments. Instead it just lets the
            #                function fail.


def test():
    f = partial(lambda a,b,c: (a,b,c))
    g = f('a', 'b')
    print g('c')
