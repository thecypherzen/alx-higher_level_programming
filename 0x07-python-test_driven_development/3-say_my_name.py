#!/usr/bin/python3
"""A module of solutions to Task 2 of ALX TDD project

Functions:
    say_my_name: prints persons's full name

Notes:
    Module imports not permitted
"""


def say_my_name(first_name="", last_name=""):
    """A function that prints ``My name is <first name> <last name>``

    Parameters:
        first_name(:obj:str): person's ``firstname``
        last_name(:obj:str): person's ``firstname``

    Returns:
        None

    Raises:
        TypeError: If first_name and last_name are not strings
            message:
                ``first_name must be a string or last_name must be a string``
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
