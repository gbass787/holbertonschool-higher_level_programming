#!/usr/bin/python3
"""This module defines a class 'Rectangle'"""


class Rectangle:
    """Defines a Rectangle, some attributes and functions for Rectangles"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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
