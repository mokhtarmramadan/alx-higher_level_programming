#!/usr/bin/python3

"""
This is a module that supplies one function, matrix_divided()
"""


def matrix_divided(matrix, div):
    """ Divide a matrix by a number and return a new matrix with the result """
    new_matrix = []
    # Checks to make sure that matrix is a list of lists
    if len(matrix) == 0 or not isinstance(matrix, list) or not \
            all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # Check to make sure that div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # Check if div was a zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Iterate over all the list of lists
    count = len(matrix[0])
    for block in matrix:
        row_list = []
        # Making sure that all the rows have the same length
        if len(block) != count:
            raise TypeError("Each row of the matrix must have the same size")
        for num in block:
            # Check to make sure that num is a number
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            row_list.append(round(num / 3, 2))

        new_matrix.append(row_list)
    return new_matrix


if __name__ == '__main__':
    import doctest
    doctest.testmod()
