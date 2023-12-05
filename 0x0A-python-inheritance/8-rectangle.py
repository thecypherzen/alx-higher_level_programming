#!/usr/bin/python3
"""0x0A. Python - Inheritance module - Task 8

Classes:
    Rectangle: BaseGeometry child.
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
