#!/usr/bin/python3

for int in range(97, 123):
    if int == ord('q') or int == ord('e'):
        continue
    print("{}".format(chr(int)), end="")
