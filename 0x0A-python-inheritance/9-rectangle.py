#!/usr/bin/python3
"""0x0A. Python - Inheritance module - Task 9

Classes:
    Rectangle: BaseGeometry child.
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry

    Attributes:
        __init__(method): class initializer
        __repr__(method): defines representation of rectangle
        area(method): calculates area of rectangle
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

    def area(self):
        """Calculates area of rectangle

        Returns: area of rectangle
        """
        return self.__width * self.__height

    def __repr__(self):
        """Representation of rectangle

        Returns: ``[Rectangle] <width>/<height>``
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
