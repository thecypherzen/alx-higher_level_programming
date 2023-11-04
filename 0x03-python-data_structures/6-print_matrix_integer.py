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
    if matrix is not None:
        for row in matrix:
            if row is not None:
                sz = len(row)
                for i in range(sz):
                    sep = "\n" if i == sz - 1 else " "
                    print("{}".format(row[i]), end=sep)
