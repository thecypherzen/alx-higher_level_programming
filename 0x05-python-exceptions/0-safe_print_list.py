#!/usr/bin/python3
"""A function that prints x elements of a list.

Parameters:
    @my_list: the list
    @x: number of elements to print
Return:
    - the actual number of list elements printed
Description:
    - All elements must be printed on the same line followed by a
      new line.
    - x can be bigger than the length of my_list
    - Not allowed to import any module
    - Not allowed to use len()
"""


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            if i == x - 1:
                print("")
            count += 1
    except Exception:
        print("")
    return count



my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))