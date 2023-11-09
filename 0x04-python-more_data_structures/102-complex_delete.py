#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """A function that deletes keys with a value in a dictionary

    Parameters:
        @a_dictinary: the dictionary
        @value: the value to delete

    Return:
        None

    Notes:
        - If the value doesn't exist, the dictionary won't change
        - All keys having the searched value have to be deleted
    """
    if a_dictionary is None or not a_dictionary \
            or value not in a_dictionary.values():
        pass
    else:
        while (1):
            if value not in a_dictionary.values():
                break
            else:
                for key in a_dictionary.keys():
                    if a_dictionary[key] == value:
                        a_dictionary.pop(key)
                        break
    return a_dictionary
