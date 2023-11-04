#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Prints all integers of a list

    - Prints one int per line

    Parameters:
        my_list:
            The list

    Return:
        None
    """
    for x in my_list:
        print("{:d}".format(x))
