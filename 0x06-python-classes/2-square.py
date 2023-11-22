#!/usr/bin/python3
"""Creation and usage of a square

A module that creates a square class

Attributes:
    Square: the square class
"""


class Square():
    """A class that defines a square

    Attributes:
        size (:obj: `int`): size of the square's side. Defaults to
            0.
            * Must be an int and must be >= 0
            * If type is not int, raises a TypeError
            * If size is < 0, raises a ValueError
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
