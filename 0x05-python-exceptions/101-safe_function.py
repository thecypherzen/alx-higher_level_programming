#!/usr/bin/python3
def safe_function(fct, *args):
    """A function that executes a function safely.

    Parameters:
        @fct: pointer to a function
        @args: arguments pointer

    Return:
        - The result of the function on success
        - Otherwise returns None if something happens during
            the function execution and prints in stderr the error precede
            by Exception:

    Description:
        - Must use try: / except:
    """
    import sys
    val = None
    try:
        val = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return val
