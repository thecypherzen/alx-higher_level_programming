#!/usr/bin/python3

"""
# A function that prints the last digit of a number.
# Returns the value of the last digit
# No module Allowed
"""


def print_last_digit(number):
    ret = abs(number) % 10
    print("{}".format(ret), end="")
    return (ret)
