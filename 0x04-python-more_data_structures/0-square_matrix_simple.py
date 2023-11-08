#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """A Function that computes the square of all integers of a matrix

    Parameters:
        @matrix: the matrix
    Details:
        - @matrix is a 2-d matrix
        - initial matrix should not be modified
        - module imports not allowed
        - allowed to use regular loops, map, etc.

    Return:
        A new matrix:
            - has same size as @matrix
            - Each value should be the square of the value of the input
    """
    if not matrix:
        return None
    return list(list(map(lambda x: x ** 2 if x else None, row))
                for row in matrix if row)
