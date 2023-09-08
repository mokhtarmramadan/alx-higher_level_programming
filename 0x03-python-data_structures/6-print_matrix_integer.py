#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        for i in range(len(mat)):
            print("{} ".format(mat[i]), end='')
        print()
