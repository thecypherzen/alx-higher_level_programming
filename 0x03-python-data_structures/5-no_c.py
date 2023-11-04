#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters c and C from a string

    Details:
        - Module imports not allowed
        - str.replace() not allowed

    Parameters:
        @my_string: The string to slice

    Return:
        the new string without characters c and C
    """
    if my_string is None:
        return None

    newstr = ""

    for c in my_string:
        if c == 'c' or c == 'C':
            pass
        else:
            newstr += c
    return newstr
