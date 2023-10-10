#!/usr/bin/python3
def pascal_triangle(n):
    matrix = []
    for i in range(n):
        """ iterate n times """
        if i == 0:
            row = [1]
            matrix.append(row)
        else:
            """ generate a new row list every base on the previous list """
            row = generate_row(row)
            matrix.append(row)
    return matrix


def generate_row(row):
    """ Generates a new list based on the previous list """
    NewRowLength = len(row) + 1
    new_row = [0] * NewRowLength
    for i in range(NewRowLength):
        if i == 0 or i == NewRowLength - 1:
            """First and last index must be 1"""
            new_row[i] = 1
        else:
            new_row[i] = row[i - 1] + row[i]
    return new_row
