#!/usr/bin/python3
def safe_print_division(a, b):
    """A function that divides 2 integers and prints the result.

    Parameters:
        @a: the first number
        @b: the second number

    Return:
        The value of the division, otherwise: None

    Description:
        - Can assume that a and b are integers
        - The result of the division should print on the
            finally: section preceded by Inside result:
        - Must use try: / except: / finally:
        - Must use "{}".format() to print the result
        - Must not import any module
    """

    res = 0.0
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {}".format(res))
        return res
