#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list

    Parameters:
        @my_list: the list of numbers

    Return:
        A new list with True or False, depending on whether
        the integer at the same position in my_list is a
        multiple of 2

    Constraints:
        - Module imports not allowed
        - The new list must be of same size as my_list
    """
    if not my_list:
        return []
    return [True if x % 2 == 0 else False for x in my_list]
