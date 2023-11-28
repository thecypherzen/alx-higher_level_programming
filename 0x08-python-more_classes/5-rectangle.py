#!/usr/bin/python3
"""A Module for More Classes and Objects ALX Project"""


class Rectangle:
    """A Class that defines a rectangle

    Attributes:
    Methods:
        __init__(method): initialises instance of Rectangle
            with optional args @width and @height
        __str__(method): creates and returns a string representation of class
        __repr__(method): creates official class object representation
        __del__(method): detects class instance deletion
        area(method): calculates the area of rectangle instance
        perimeter(method): calculates the perimeter of rectangle instance

    Variables:
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

    def __str__(self):
        """creates a representation of rectangle instance"""
        if not self.height or not self.width:
            return ""
        res = ""
        j = self.height
        while j:
            i = self.width
            while i:
                res += '#'
                i -= 1
            if j > 1:
                res += '\n'
            j -= 1
        return res

    def __repr__(self):
        """creates a representation of rectangle instance"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Detects class instance deletion

        Prints a simple message
        """
        print("Bye rectangle...")

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

    def area(self):
        """Calculates and returns area of rectangle

        Returns:
            area of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns perimeter of rectangle

        Returns:
            perimeter of rectangle
        """
        if not self.height or not self.width:
            return 0
        return 2 * (self.height + self.width)
