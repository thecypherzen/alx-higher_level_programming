#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """A function that replaces or adds key/value in a dictionary.

    Params:
        @a_dictionary: the dictionary
        @key: key of new value - of type str
        @value: new value - of any type

    Return:
        The dictionary with updated values
    """
    if not a_dictionary:
        return dict()
    if type(key) is not str:
        return a_dictionary
    a_dictionary[key] = value
    return a_dictionary
