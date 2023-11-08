#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """A function that prints a dictionary by ordered keys.

    Params:
        @a_dictionary: the dictionary

    Return:
        None

    Notes:
        - No imports allowed
    """
    if a_dictionary:
        for key in sorted(a_dictionary):
            print("{}: {}".format(key, a_dictionary[key]))
