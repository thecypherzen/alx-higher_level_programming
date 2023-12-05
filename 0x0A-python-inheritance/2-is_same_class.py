#!/usr/bin/python3
"""0x0A. Python - Inheritance module - Task 2

Functions:
    is_same_class: checks if an obj is an exact instance of another
"""


def is_same_class(obj, a_class):
    """Tests if an object is an instance of a class

    Checks if `obj` is and instance of `a_class` but not any of
        ``a_class``'s base classes.

    Parameters:
        obj(:obj): some object
        a_class:(:obj): some class object

    Returns:
        True if ``obj`` is an instance of ``a_class`` else False
    """
    return type(obj) is a_class
