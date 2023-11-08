#!/usr/bin/python3
def number_keys(a_dictionary):
    """A function that returns the number of keys in a dictionary.

    Params:
        @a_dictionary: the dictionary

    Return:
        number of keys in dictionary

    Notes:
        - Imports not allowed
    """
    keys_total = 0
    if not a_dictionary:
        return keys_total
    return (len(list(a_dictionary.keys())))
