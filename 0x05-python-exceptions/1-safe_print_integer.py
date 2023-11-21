#!/usr/bin/python3
def safe_print_integer(value):
    """A function that prints an integer with "{:d}".format().

    Parameters:
        @value: can be any type (integer, string, etc.)
    Return:
        True if value has been correctly printed (it means the
        value is an integer), Otherwise, returns False.
    Description:
        - The integer should be printed followed by a new line
        - Must use try: / except:
        - Must "{:d}".format() to print as integer
        - Module imports not allowed
        - Use of type() not allowed
    """

    status = True
    try:
        print("{:d}".format(value))
    except Exception:
        status = False
    return status
