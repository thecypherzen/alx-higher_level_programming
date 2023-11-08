#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """A function that deletes a key in a dictionary.

    Params:
        @a_dictionary: the dictionary
        @key: the key

    Return:
        The updated dictionary
    """
    if a_dictionary is None:
        return None
    if a_dictionary.get(key, None) is None:
        return a_dictionary
    a_dictionary.pop(key)
    return a_dictionary
