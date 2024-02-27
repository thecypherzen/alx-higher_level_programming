#!/usr/bin/python3
"""0x0B. Python - Input/Output - Task 12

Function(s):
    pascal_triangle: generates pascal's triangle numbers
    next_list: helps ``pascal_triangle`` to generate the next list

Notes:
    module imports not allowed
"""


def pascal_triangle(n):
    """A function that generates pascal triangle numbers

    Parameters:
        n(:obj:int): the height of pascal's triangle

    Returns:
        a list of lists of pascal's triangle numbers if n > 0, else
        an empty list
    """
    if n <= 0:
        return []
    triangle = [next_list([])]
    for i in range(1, n):
        triangle.append(next_list(triangle[i - 1]))
    return triangle


def next_list(lst):
    """A helper function to ``pascal_triangle``

    Generates the next list in pascal_triangle iterations

    Parameter:
        lst(:obj:list): a list at previous level of pascal's triangle

    Returns: a list of the next pascal's triangle numbers
    """
    ret = []
    itr = len(lst) - 1
    index = 0
    ret.append(1)
    if itr < 0:
        return ret
    while itr:
        ret.append(lst[index] + lst[index + 1])
        index += 1
        itr -= 1
    ret.append(1)
    return ret
