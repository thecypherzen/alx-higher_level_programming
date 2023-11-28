#!/usr/bin/python3
"""A Module for More Classes and Objects ALX Project"""


class Rectangle:
    """A Class that defines a rectangle

    Attributes:
        __init__(method): initialises instance of Rectangle
            with optional args @width and @height

        width(:obj:int:private): the width of Rectangle instance
            - Must be an integer
            - Has a @property

            Raises:
                TypeError: if width is not an integer
                    Message: ``width must be an integer``
                ValueError: if width is < 0
                    Message: ``width must be >= 0``
        height(:obj:int:private): the height of Rectangle
            Must be an integer
            Has @property and @setter

    """
    def __init__(self, width=0, height=0):
        """A method that initialises class instance

        Params:
            __height: private property: the height
            __width: private property: the width

        Returns: None
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """gets the height of rectangle

        Params:
            self(:obj:Rectangle): instance of object

        Returns:
            rectangle's height
        """
        return self.__height

    @property
    def width(self):
        """gets the width of rectangle

        Params:
            self(:obj:Rectangle): the instance of rectangle object

        Returns:
            rectangle's width
        """
        return self.__width

    @height.setter
    def height(self, height):
        """The setter method for height property

        Params:
            self: instance object of rectangle
            height(:obj:int): height of rectangle

        Returns:
            None

        Raises:
            TypeError: if height is not an integer:
                Message: ``height must be an integer``
            ValueError: if height is < 0
                Message: ``height must be >= 0``
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @width.setter
    def width(self, width):
        """The setter method for height property

        Params:
            self: instance object of rectangle
            width(:obj:int): width of rectangle

        Returns:
            None

        Raises:
            TypeError: if width is not an integer:
                Message: ``width must be an integer``
            ValueError: if width is < 0
                Message: ``width must be >= 0``
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
