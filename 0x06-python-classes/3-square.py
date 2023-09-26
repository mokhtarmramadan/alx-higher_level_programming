#!/usr/bin/python3
""" a class Square that defines a square by: (based on 2-square.py) """


class Square:

    ''' Instantiation with optional size '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    ''' Public instance method: area that returns the current square area '''
    def area(self):
        return self.__size ** 2
