"""
pypartial.partial

A decorator class for allowing automatic partial application
on a function.

Limitations: positional arguments only.
"""
from inspect import getargspec


class Partial(object):
    """
    Takes a function, returning a partial object which
    captures arguments until there's enough to call the function.
    """
    def __init__(self, func, *varargs):
        self._func = func
        self._min_args = len(getargspec(func).args)
        self._positional_args = list(varargs)

        self.__call__()  # Execute immediately if there's enough arguments.

    def __call__(self, *varargs):
        self._positional_args.extend(list(varargs))

        if self._enough_args():
            return self._func(*self._positional_args)
            # The line above currently raises a warning while linting.
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
