#!/usr/bin/python3
""" A module of validators

This module defines functions that are useful for valiating
    certain properties of given variables. These include variable
    type, signess, etc.

Functions:
    int_type_validate: validates variable is of type int
    pos_value_validate: validates that variable is >= 0

    All the functions use the following Args:
        var (`any`): variable to check
        name (`str'): name of variable
        msg (`str`): message to print if validation fails
        file (:obj: `stream`): file to write message to
            doesn't check if file is opened or write permission is given.
"""


def int_type_validate(var, name=None, msg=None):
    """Vaidates an int type

    Raises:
        TypeError: if `var` is not an int
    """
    if type(name) is not str:
        name = "variable"

    if type(msg) is not str:
        msg = "must be an integer"

    if type(var) is not int:
        raise TypeError("{} {}".format(name, msg))


def str_type_validate(var, name=None, msg=None):
    """Vaidates a string type

    Raises:
        TypeError: if `var` is not a string
    """
    if type(name) is not str:
        name = "variable"

    if type(msg) is not str:
        msg = "must be a string"

    if type(var) is not str:
        raise TypeError("{} {}".format(name, msg))


def float_type_validate(var, name=None, msg=None):
    """Vaidates a float type

    Raises:
        TypeError: if `var` is not a float
    """
    if type(name) is not str:
        name = "variable"

    if type(msg) is not str:
        msg = "must be a float"

    if type(var) is not float:
        raise TypeError("{} {}".format(name, msg))


def is_num_validate(var, name=None, msg=None):
    """validates var is a number

    Raises:
        TypeError: if `var` is not a number
    """
    if type(name) is not str:
        name = "variable"

    if type(msg) is not str:
        msg = "must be a number"

    if type(var) is not int and type(var) is not float:
        raise TypeError("{} {}".format(name, msg))


def pos_num_validate(var, name=None, msg=None):
    """Validates variable is a positive number.

    Raises:
        TypeError: if `var` is not a  number
        ValueError: if `var` is < 0
    """
    is_num_validate(var, name, msg)

    if type(name) is not str:
        name = "variable"

    if type(msg) is not str:
        msg = "must be >= 0"

    if var < 0:
        raise ValueError("{} {}".format(name, msg))


def gt_zero_validate(var, name=None, msg=None, typ=None):
    """Validates variable is a > 0.

    Raises:
        TypeError: if `typ` == "float and `var` is a float
                   if `typ` == "int" and `var` is not an int
        ValueError: if `var` is <= 0
    """
    if typ == "float":
        float_type_validate(var, name, msg)
    elif typ == "int":
        int_type_validate(var, name, msg)
    else:
        is_num_validate(var, name, msg)

    if type(name) is not str:
        name = "variable"

    if type(msg) is not str:
        msg = "must be > 0"

    if var <= 0:
        raise ValueError("{} {}".format(name, msg))
