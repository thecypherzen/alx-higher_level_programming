#!/usr/bin/python3
"""A doctest for 0-add_integer module
"""


def add_integer(a, b=98):
    """A function that adds two numbers

    Params:
        a(:obj:int): the first number
        b(:obj:int): the second number

    Returns:
        sum of a and b

    Notes:
    has only one required positional param (a). b defaults to 98
    Examples:
    >>> add_integer(0)
    98
    >>> add_integer(3, 4)
    7
    >>> add_integer(3, -4)
    -1
    >>> add_integer(-2)
    96

    can take in ints and floats.
    Examples:
    >>> add_integer(2.1, 9)
    11
    >>> add_integer(59.342)
    157

    return type is always int.
    Examples:
    >>> type(add_integer(73, 100))
    <class 'int'>
    >>> isinstance(add_integer(23.45, -9), int)
    True

    a and b must be integers or floats, else TypeError is raised.
    Examples:
    >>> add_integer([2, 3])
    Traceback (most recent call last):
    TypeError: a must be an integer or b must be an integer

    >>> add_integer([2, 3])
    Traceback (innermost last):
    TypeError: a must be an integer or b must be an integer

    >>> add_integer("2", "5")
    Traceback (most recent call last):
    TypeError: a must be an integer or b must be an integer

    >>> add_integer("2", "5")
    Traceback (innermost last):
    TypeError: a must be an integer or b must be an integer
    """
    if any(i is None for i in (a, b)) \
        or any(not isinstance(i, int) and not isinstance(i, float)
               for i in (a, b)):
        raise TypeError("a must be an integer or b must be an integer")
    res = int(a) + int(b)
    return res
