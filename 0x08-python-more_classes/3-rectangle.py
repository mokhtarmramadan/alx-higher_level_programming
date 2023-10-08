"""
This module supplise only one class as follows
"""


class Rectangle:
    """ defines a rectangle """
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2 + self.height * 2)

    def __str__(self):
        string = ""
        if self.width == 0 or self.height == 0:
            return ""
        for i in range(self.height):
            for j in range(self.width):
                string += "#"
            string += '\n'
        return string[:-1]
