#!/usr/bin/python3
"""A module of solutions to Task 3 of ALX TDD project

Functions:
    say_my_name: prints persons's full name

Notes:
    Module imports not permitted
"""

def print_square(size):
    """A function that prints a square with the character #
    
    Parameters:
        size(:obj:int): the length of the square
    
    Returns:
        None
    
    Raises:
        TypeError: if type(size) is not int
            Message:
                ``size must be an integer``
        ValueError: if size < 0
            Message:
                ``size must be >= 0``
        TypeError: if type(size) is float and size < 0
            Message: 
                ``size must be an integer``
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    i = size
    while i:
        j = size
        while j:
            print('#', end="")
            j -= 1
        print()
        i -= 1
