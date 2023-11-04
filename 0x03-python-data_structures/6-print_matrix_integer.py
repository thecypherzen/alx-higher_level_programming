#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    if matrix is not None:
        for row in matrix:
            if row is not None:
                print(*row)
