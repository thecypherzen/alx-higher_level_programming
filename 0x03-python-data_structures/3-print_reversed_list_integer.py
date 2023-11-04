#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints integer elements of a list in reversed order.

    Description:
        - Prints one integer per line
        - Cannot cast integers to strings
        - Try/Except is not allowed
        - Module Imports not allowed
        - Must use str.format() to print

    Return:
        None
    """
    if my_list is None:
        return None
    max = len(my_list) - 1
    for i in range(max, -1, -1):
        print("{:d}".format(my_list[i]))
