#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific index, without
        modifying the original is like in C.

    Description:
        - If idx is negative, or out of range, it returns a copy
            of the original list without any modifications.
        - Try/Except is not allowed
        - Module Imports not allowed

    Parameters:
        @my_list: the list
        @idx: index to insert or replace new value
        @element: the new value

    Return:
        Copy of modified list on success, unmodified list copy otherwise
    """
    if my_list is None:
        return None
    listcpy = my_list.copy()
    max = len(listcpy)
    if idx < 0 or idx >= max or type(idx) is not int:
        return listcpy
    listcpy[idx] = element
    return listcpy
