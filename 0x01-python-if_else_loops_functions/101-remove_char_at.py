#!/usr/bin/python3
"""
# A Function that creates a copy of the string,
    removing the character at the position n
    (not the Python way, the “C array index”).
# Module import not allowed
"""


def remove_char_at(str, n):
    sz = len(str)
    if n <= sz:
        newstr = str[:n] + str[n+1:sz]
    else:
        newstr = str[:sz]
    return newstr
