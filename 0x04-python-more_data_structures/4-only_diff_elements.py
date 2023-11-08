#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """A function that returns a set of all elements present in
        only one set.

    Parameters:
        @set_1: the first set
        @set_2: the second set

    Return: a set of exclusives

    Notes:
        - No imports allowed
    """
    if not set_1 and set_2:
        return set_2
    if set_1 and not set_2:
        return set_1
    if not set_1 and not set_2:
        return set()
    return set((set_1 | set_2) - (set_1 & set_2))
