#!/usr/bin/python3
def common_elements(set_1, set_2):
    """A function that returns a set of common elements in two sets.

    Params:
        @set_1: the first set
        @set_2: the second set

    Return:
        A new set of common elements

    Notes:
        - No imports allowed
    """
    if set_1 and not set_2:
        return set_1.copy()
    if set_2 and not set_1:
        return set_2.copy()
    if not set_1 and not set_2:
        return set()
    return set(set_1 & set_2)
