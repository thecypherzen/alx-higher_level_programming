#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrieves an element from a list like in C.

    Description:
        - If idx is negative, returns None
        - If idx is > num of element in my_list), it returns None
        - Try/Except is not allowed
        - Module Imports not allowed

    Return:
        The element retrieved from the list
    """
    max = len(my_list)
    if idx < 0 or idx >= max or idx is not int:
        return None
    return my_list[idx]
