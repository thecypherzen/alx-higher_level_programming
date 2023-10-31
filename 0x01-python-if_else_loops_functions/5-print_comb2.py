#!/usr/bin/python3
for i in range(100):
    if i != 99:
        sep = ", "
    else:
        sep = "\n"
    print("{:02}".format(i), end=sep)
