#!/usr/bin/python3
"""0x0A. Python - Inheritance module - Task 2

Functions:
    is_same_class: inherits from ``list`` object
"""

def is_same_class(obj, a_class):
    """Tests if an object is an instance of a class

    Parameters:
        obj(:obj): some object
        a_class:(:obj): some class object

    Returns:
        True if ``obj`` is an instance of ``a_class`` else False
    """
    return type(obj) == a_class
