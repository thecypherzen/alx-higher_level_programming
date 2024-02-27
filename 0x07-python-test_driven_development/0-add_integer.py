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
    if a is None or (not isinstance(a, int) and not
                     isinstance(a, float)):
        raise TypeError("a must be an integer")
    if b is None or (not isinstance(b, int)
                     and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    if a != a or b != b:
        raise ValueError("convert float Nan to integer")
    if a == float('inf') or a == -float('inf') \
            or b == float('inf') or b == -float('inf'):
        raise OverflowError("cannot convert float infinity to integer")
    res = int(a) + int(b)
    return res
