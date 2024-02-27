#!/usr/bin/python3
"""A module of solutions to Task 3 of ALX TDD project

Functions:
    say_my_name: prints persons's full name

Notes:
    Module imports not permitted
"""


def text_indentation(text):
    """A function that prints a text with 2 new lines
        after each of these characters: . ? :

    Parameters:
        text(:obj:int): the text literal

    Returns:
        None

    Raises:
        TypeError: if type(text) is not str
        Message:
            ``text must be a string``

    Note:
        There should be no space at the beginning or
        at the end of each printed line
    """
    pass

delims = list(".:")
txt = "this.is;the,new'way of life. ?where is the . lie ? :"
print(txt)
print()
for delim in delims:
    txt = txt.replace(delim, '?')
#for line in txt.split('?'):
#    print("{}({})".format(line, len(line)))
print(txt)