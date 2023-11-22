#!/usr/bin/python3
"""Creation and usage of a square

A module that creates a square class

Classes:
    Square: the square class

Description:
    No module imports allowed
"""


class Square():
    """A class that defines a square

    Methods:
        __init__: initialises the class
        area: calculates the area of square
    """
    def __init__(self, size=0):
        """Initialises the square class

        Attributes:
            size (:obj: `int`): size of the square's side. Defaults to
            0.
            * Must be an int and must be >= 0
            * If type is not int, raises a TypeError
            * If size is < 0, raises a ValueError
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of square

        Args:
            None

        Returns:
            Area of square
        """
        return self.__size * self.__size
