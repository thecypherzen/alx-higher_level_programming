#!/usr/bin/python3
"""0x0A. Python - Inheritance module - Task 13

Classes:
    Square: Rectangle's child.
"""


def add_attribute(obj, name, value):
    """A function that adds an attribute to an object if possible

    Parameters:
        obj(:obj:object): the object
        name(:obj:str): the attribute's name. Must be a string
        value(:obj:object): the attribute's value

    Returns: None

    Raises:
        TypeError: if it is not possible to add an attribute to `obj`
            or if the ``name`` passed is not a string
            Message: ``can't add new attribute``
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    if type(name) is not str:
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
