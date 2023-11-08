#!/usr/bin/python3
def best_score(a_dictionary):
    """A function that gets the biggegs int value from a dictionary

    Parameters:
        @a_dictionary: the dictionary

    Return:
        The key with bigges value integer
    """
    if a_dictionary is None:
        return None
    return sorted(a_dictionary, key=lambda x: a_dictionary[x], reverse=True)[0]
