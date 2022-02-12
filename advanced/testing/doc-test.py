def add(a,b):
    """
    >>> add(1,10)
    11
    >>> add(1,-10)
    -11
    """
    return a+b


def sub(a,b):
    """
    >>> sub(1,1)
    0
    >>> sub(-1,1)
    2
    """
    return a-b

import doctest
doctest.testmod()