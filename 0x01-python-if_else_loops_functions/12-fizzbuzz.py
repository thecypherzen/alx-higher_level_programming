#!/usr/bin/python3

"""
# A function that prints the numbers from 1 to 100 separated by a space.
# For multiples of three print 					Fizz instead
# For multiples of five print  					Buzz instead
# For multiples of both three and five print 	FizzBuzz instead
# Each element should be followed by a space
# No module import allowed
"""


def fizzbuzz():
    for n in range(1, 101):
        sep = "" if n == 100 else " "
        if not n % 3 and n % 5:
            print(f"{'Fizz'}", end=sep)
        elif not n % 5 and n % 3:
            print(f"{'Buzz'}", end=sep)
        elif (not n % 3) and (not n % 5):
            print(f"{'FizzBuzz'}", end=sep)
        else:
            print(f"{n}", end=sep)
