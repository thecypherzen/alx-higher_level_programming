#!/usr/bin/python3
def raise_exception_msg(message=""):
    """A function hat raises a name exception with a message.

    Parameters:
        @message: error's associated message

    Return:
        None

    Description:
        - message defaults to empty string
        - Import modules not allowed
    """

    raise NameError(message)
