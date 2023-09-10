#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        for i in range(len(mat)):
            if i == len(mat) - 1:
                print("{:d}".format(mat[i]), end='')
            else:
                print("{:d} ".format(mat[i]), end='')
        print()
