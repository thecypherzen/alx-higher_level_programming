#!/usr/bin/python3
"""0x0A. Python - Inheritance module - Task 3

Functions:
    is_kind_of_class: checks an obj is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """Tests if an object is an instance of a class

    Checks if `obj` is an instance of `a_class` or any of
        ``a_class``'s base classes.

    Parameters:
        obj(:obj): some object
        a_class:(:obj): some class object

    Returns:
        True if ``obj`` is an instance of ``a_class``
        or any of its parent classes, else False
    """
    return isinstance(obj, a_class)
