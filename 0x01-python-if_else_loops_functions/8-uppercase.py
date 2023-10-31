#!/usr/bin/python3


# A function that prints a string in uppercase followed by a new line
def uppercase(str):
    new = ""
    for i in range(len(str)):
        c = str[i]
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        new += c
    print("{}".format(new))
