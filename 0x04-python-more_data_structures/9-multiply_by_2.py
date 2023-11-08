#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """A function that returns a new dictionary with all values multiplied by 2

    Parameters:
        @a_dictionary: the dictionary

    Return:
        The new dictionary of multiples of two
    """
    if a_dictionary is None:
        return None
    return {key: val * 2 for key, val in a_dictionary.items()}
