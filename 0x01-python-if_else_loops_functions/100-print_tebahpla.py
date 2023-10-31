#!/usr/bin/python3

"""
# A program that prints the ASCII alphabet, in reverse
    order, alternating lowercase and uppercase
    (z in lowercase and Y in uppercase) , not followed
    by a new line.
# Only one print function with string format
# Can only use one loop
# Variables not allowed
# Module imports not allowed
"""


for n in range(122, 96, -1):
    if not (n % 2):
        print("{}".format(chr(n)), end="")
    else:
        print("{}".format(chr(n - 32)), end="")
