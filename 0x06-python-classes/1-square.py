#!/usr/bin/python3
"""A module that defines, instatiates and uses squares

Creates a square class and uses it.

Attributes:
    Square: a square defining class
"""


class Square():
    """A class that defines a square.

    Attriubutes:
        __size (:obj: `int`): size of the square's side

    """
    def __init__(self, size):
        self.__size = size
