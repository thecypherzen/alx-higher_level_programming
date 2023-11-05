#!/usr/bin/python3

def multiple_returns(sentence):
    """Checks the length and first character of a string

    Parameters:
        @sentence: the sentence

    Return:
        A tuple with the length of the string at pos 1 and
        the first char in string at pos2

    Constriants:
        - If sentence is empty, the first character is set to None
        - Not to use any module imports
    """
    if sentence is None:
        return (None, None)
    senlen = len(sentence)
    if not senlen:
        return (0, None)
    return (senlen, sentence[0])
