#!/usr/bin/python3
"""
This is a module that supplies one function, add_integer(). for example,
>>> add_integer(1, 2)
3
"""


def add_integer(a, b=98):
    """Returns the sum of two integers.
    >>> [add_integer(n, n) for n in range(5)]
    [0, 2, 4, 6, 8]
    >>> add_integer(5, 6)
    11
    >>> add_integer(5, -1)
    4
    >>> add_integer(5.2, 4.3)
    9
    >>> add_integer(5.2, 4)
    9
    >>> add_integer(5, 4.3)
    9
    >>> add_integer("hello", "world")
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer("hello", 5)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(2, "world")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    else:
        return (int(a) + int(b))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
