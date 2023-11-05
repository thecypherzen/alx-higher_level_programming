#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers.

    Details:
        - Cannot cast integers to strings
        - must use str.format() to print
        - Module imports not allowed

    parameters:
        @matrix: the matrix

    Return:
        None
    """
    if matrix is None:
        print("{}".format(None))
    else:
        for row in matrix:
            if row is not None:
                print(" ".join(["{:d}"] * len(row)).format(*row))
            else:
                print("{}".format(None))
