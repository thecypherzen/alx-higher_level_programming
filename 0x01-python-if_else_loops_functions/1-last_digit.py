#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10 if number > 0 else (number * -1) % 10


# function to create response message
def getmsg(num):
    if num > 5:
        return "greater than 5"
    elif num < 6 and num != 0:
        return "less than 6 and not 0"
    else:
        return "0"


print(f"Last digit of {number} is {ld} and is {getmsg(ld)}")
