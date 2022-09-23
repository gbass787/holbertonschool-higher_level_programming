#!/usr/bin/python3
"""This module defines a class 'Rectangle'"""


class Rectangle:
    """Defines a Rectangle, some attributes and functions for Rectangles"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        """creates a string of rectangle"""
        rect = ""
        if self.area == 0:
            return ""
        for i in range(self.height):
            for j in range(self.width):
                rect += '#'
            if i != self.height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """sting of an object"""
        return "{}({}, {})".format(self.__class__.__name__,
                                   self.width, self.height)

    @property
    def width(self):
        """getter for private attribute width"""
        return self.__width

    @width.setter
    def width(self, newWidth):
        """setter method for private attribute width"""
        if type(newWidth) is not int:
            raise TypeError("width must be an integer")
        if newWidth < 0:
            raise ValueError("width must be >= 0")
        self.__width = newWidth

    @property
    def height(self):
        """getter for private attribute height"""
        return self.__height

    @height.setter
    def height(self, newHeight):
        """setter method for private attribute height"""
        if type(newHeight) is not int:
            raise TypeError("height must be an integer")
        if newHeight < 0:
            raise ValueError("height must be >= 0")
        self.__height = newHeight

    def area(self):
        '''calculates the area'''
        return self.width * self.height

    def perimeter(self):
        '''calculates the perimeter'''
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __del__(self):
        """handling destruction"""
        print("Bye rectangle...")
