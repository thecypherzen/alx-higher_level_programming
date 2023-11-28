#!/usr/bin/python3
"""A Module for More Classes and Objects ALX Project"""


class Rectangle:
    """A Class that defines a rectangle

    Class Methods:
    Instnce Methods:
        __init__: initialises instance of Rectangle
            with optional args @width and @height
        __str__: creates and returns a string representation of class
        __repr__: creates official class object representation
        __del__: detects class instance deletion
        area: calculates the area of rectangle instance
        perimeter: calculates the perimeter of rectangle instance
        bigger_or_equal: compares two rectangle instances
            and returns the bigger one

    Variables:
        number_of_instances(class attr:int): number of instances of class
        print_symbol(class attr:any): symbol used to represent class instances
            can be of any type
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
    number_of_instances: int = 0  # number of class instances
    print_symbol = '#'  # defines class representation symbol

    def __init__(self, width=0, height=0):
        """A method that initialises class instance

        Instantiates a class object
        Increases count of instances

        Params:
            __height: private property: the height
            __width: private property: the width

        Returns: None
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """creates a representation of rectangle instance"""
        if not self.height or not self.width:
            return ""
        res = ""
        j = self.height
        while j:
            i = self.width
            while i:
                res += str(self.print_symbol)
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
        Reduces count of class instances
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles by area

        Params:
            rect_1: the first rectangle
            rect_2: the second retangle

        Returns:
            the bigger rectangle of the two,  or
            rect_1 if both are of the same size

        Raises:
            TypeError: if any(or both) of the rectangles is(are)
                not an instance(instances) of class Rectangle
                Message:
                    ``rect_n must be an instance of Rectangle``,
                    where n corresponds to rect_1 or rect_2 respectively
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError(f"{rect_1} must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError(f"{rect_2} must be an instance of Rectangle")
        return rect_1 if Rectangle.area(rect_1) >= Rectangle.area(rect_2)\
            else rect_2

    @classmethod
    def square(cls, size=0):
        """Returns new rectangle of height = width = size"""
        return cls(size, size)
