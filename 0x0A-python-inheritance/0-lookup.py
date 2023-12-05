#!/usr/bin/python3
"""0x0A. Python - Inheritance module

Functions:
    lookup: lists available attributes and methods of an object.
"""


def lookup(obj):
    """A function that lists a method's attributes and methods

    Parameters:
        obj: the object to lookup

    Returns:
        a list object of `obj`'s methods and attributes
    """
    return dir(obj)
