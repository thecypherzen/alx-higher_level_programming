#!/usr/bin/python3
def safe_print_integer_err(value):
    """A function that prints an integer.

    Parameters:
        @value: the integer to print

    Return:
        - True if value has been correctly printed
            (it means the value is an integer), otherwise
        - False and prints in stderr the error preceded
            by Exception:

    Description:
        - value can be any type (integer, string, etc.)
        - Must use try: / except:
        - Must use "{:d}".format() to print as integer
        - Use of type() not allowed
    """

    import sys
    status = False
    try:
        print("{:d}".format(value))
        status = True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
    return status
