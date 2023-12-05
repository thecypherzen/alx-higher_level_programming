#!/usr/bin/python3
"""0x0A. Python - Inheritance module - Task 8

Classes:
    BaseGeometry: Base class
    Rectangle: BaseGeometry child
"""


class BaseGeometry:
    """An  geometry base class

    Attributes:
        area(method): raises exception
        integer_validator(method): validates value
    """
    def area(self):
        """Raises an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates class values

        Raises:
            TypeError: if ``value`` is not an integer.
                Message: ``<name> must be an integer``
            ValueError: if value is less or equal to 0:
                Message: ``<name> must be greater than 0``
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry

    Attributes:
        __init__(method): class initializer
    """
    def __init__(self, width, height):
        """Initialises a Rectangle

        Params:
            width: rectangle width
            height: rectangle height

        Returns:
            None

        Raises: Errors raised by BaseGeometry.integer_validator()
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
