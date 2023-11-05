#!/usr/bin/python3

if __name__ == "__main__":

    """Prints the result of the addition of all commandline
    arguments.

    Args:
        Nill

    Return:
        None
    """
    import sys
    from calculator_1 import add
    args_list = sys.argv
    args_len = len(args_list)

    sum = 0
    if args_len == 1:
        print("0")
    else:
        for i in range(1, args_len):
            sum = (add(sum, int(args_list[i])))
        print(sum)

