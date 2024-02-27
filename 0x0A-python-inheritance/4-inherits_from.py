#!/usr/bin/python3
"""0x0A. Python - Inheritance module - Task 4

Functions:
    inherits_from: checks if an object is a child of a class
"""


def inherits_from(obj, a_class):
    """Tests if an object is a subclass of a class

    Checks if `obj` is a subclass of `a_class`

    Parameters:
        obj(:obj): some object
        a_class:(:obj): some class object

    Returns:
        True if ``obj`` is a subclass of ``a_class``
        else False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
