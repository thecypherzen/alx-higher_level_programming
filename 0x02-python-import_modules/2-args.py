#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the number of and list of command line arguments

    Args:
        Nill

    Return:
        None
    """
    import sys
    import dis
    args = sys.argv
    len = len(args)

    if len == 1:
        print("0 arguments.")
    else:
        a_msg = "arguments" if len > 2 else "argument"
        print("{} {}:".format(len - 1, a_msg))
        for i in range(1, len):
            print("{}: {}".format(i, args[i]))

