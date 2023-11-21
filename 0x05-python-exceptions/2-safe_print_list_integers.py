#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """A function that prints the first x elements of a list
        and only integers.

    Parameters:
        @mylist: the list
        @x: number of elements to print

    Return:
        The real number of integers printed

    Description:
        - All integers have to be printed on the same line followed
            by a new line - other types are skipped in silence.
        - the list can contain any type (integer, string, etc.)
        - x represents the number of elements to access in my_list
        - x can be bigger than the length of my_list - if it's
            the case, an exception is expected to occur
        - Must use try: / except:
        - Must use "{:d}".format() to print an integer
        - Not allowed to import any module
        - Not allowed to use len()
    """

    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print("")
    return count
