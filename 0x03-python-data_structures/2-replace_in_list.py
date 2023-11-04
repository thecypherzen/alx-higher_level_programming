#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific index like in C.

    Description:
        - If idx is negative, or out of range, it returns the
            original list without modifying it.
        - Try/Except is not allowed
        - Module Imports not allowed

    Parameters:
        @my_list: the list
        @idx: index to insert or replace new value
        @element: the new value

    Return:
        Modified list on success, unmodified list otherwise
    """
    if my_list is None:
        return None
    max = len(my_list)
    if idx < 0 or idx >= max or type(idx) is not int:
        return my_list
    my_list[idx] = element
    return my_list
