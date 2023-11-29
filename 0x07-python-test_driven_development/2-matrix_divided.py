#!/usr/bin/python3
"""Solution to Task of TDD Project

This module contains my solution to the Test-driven Development
project of my ALX SE journey, Task 2.

In Summary:
    Functions: 1
"""


def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix.

    Parameters:
        matrix(:obj:list): a matrix(of lists only)
        div(:obj:int or :float): the dividing number

    Returns:
        a new matrix.

    Raises:
        TypeError: If:
            - ``matrix`` is not a ``list of (list`` of ``int``
                or ``float`` data types only).
                message:
                ``matrix must be a matrix (list of lists)
                            of integers/floats``
            - each row of the ``matrix`` is not of the same size
                message:
                    ``Each row of the matrix must have the same size``
            - ``div`` is not of type ``int`` or ``float``
                message:
                    ``div must be a number``
        ZeroDivisionError: If ``div`` can't be equal to 0(zero)
            message:
                `division by zero``

    Notes:
        All elements of ``matrix`` are divided by div and
            rounded to 2 decimal places
    """
    # check for valid div
    if (not isinstance(div, int) and not isinstance(div, float))\
            or div != div:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # check for valid matrix
    if not isinstance(matrix, list) or len(matrix) == 0 or \
        any(not isinstance(row, list) or
            len(row) == 0 for row in matrix):
        raise TypeError("matrix must be a matrix " +
                        "(list of lists) of integers/floats")
    if any(any(not isinstance(val, int) and
               not isinstance(val, float) for val in row)
           for row in matrix):
        raise TypeError("matrix must be a matrix " +
                        "(list of lists) of integers/floats")
    lenrow = len(matrix[0])
    if any(len(row) != lenrow for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    res_matrix = []
    for row in matrix:
        res_matrix.append([round(i/div, 2) for i in row])
    return res_matrix
