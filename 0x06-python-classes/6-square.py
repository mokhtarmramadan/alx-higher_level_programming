#!/usr/bin/python3
""" a class Square that defines a square by: (based on 2-square.py) """


class Square:

    ''' Instantiation with optional size '''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    ''' Public instance method: area that returns the current square area '''
    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if not isinstance(position, tuple) or len(position) != 2 \
                or not isinstance(position[0], int) \
                or not isinstance(position[1], int)\
                or not position[0] >= 0 or not position[1] >= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    ''' prints in stdout the square with the character # '''
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print("")
