#!/usr/bin/python3
def squared(mat=[]):
    if isinstance(mat, int):
        return mat ** 2
    else:
        return [x ** 2 for x in mat]


def square_matrix_simple(matrix=[]):
    results = []
    for mat in matrix:
        results.append(list(map(squared, mat)))
    return (results)
