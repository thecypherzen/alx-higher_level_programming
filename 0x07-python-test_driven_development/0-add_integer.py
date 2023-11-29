#!/usr/bin/python3
"""This module hosts one function:

add_integer: adds two integers (or floats)
"""


def add_integer(a, b=98):
    """A function that adds two numbers

    Params:
        a(:obj:int): the first number
        b(:obj:int): the second number

    Returns:
        sum of a and b
        always returns type int
    """
    if any(i is None for i in (a, b)) \
        or any(not isinstance(i, int) and not isinstance(i, float)
               for i in (a, b)):
        raise TypeError("a must be an integer or b must be an integer")
    res = int(a) + int(b)
    return res
