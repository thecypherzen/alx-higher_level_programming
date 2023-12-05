#!/usr/bin/python3
"""0x0A. Python - Inheritance module - Task 9

Classes:
    Square: Rectangle's child.
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Inherits from Rectangle

    Attributes:
        __init__(method): class initializer
        area(method): calculates area of square
    """
    def __init__(self, size):
        """Square instance initialiser

        Initialises a square from Rectangle class

        Params:
            size: size of square

        Raises: Errors raised by integer_validator in Rectangle
        """
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """Calculates area of square

        Returns: area of square
        """
        return self.__size ** 2
