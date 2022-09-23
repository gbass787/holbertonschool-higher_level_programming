#!/usr/bin/python3
'''File contains Rectangle class'''


class Rectangle:
    '''defines a class named Rectangle
    that takes a width and a height'''

    def __init__(self, width=0, height=0):
        '''creates an instance of a class'''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''returns width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''validates width input and defines it'''
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''returns height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''validates height input and defines it'''
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''returns area of rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''returns perimeter of rectangle'''
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        '''returns string made up of '#' in the shape/size
        of the rectangle'''

        str_rectangle = ""

        if self.width == 0 or self.height == 0:
            return str_rectangle

        for y in range(0, self.__height):
            for x in range(0, self.__width):
                str_rectangle += '#'
            if (y + 1) < self.__height:
                str_rectangle += '\n'

        return (str_rectangle)
