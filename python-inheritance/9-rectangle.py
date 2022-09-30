#!/usr/bin/python3
'''Rectangle of BaseGeometry'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle of BaseGeometry'''

    def __init__(self, width, height):
        '''instation of a rectangle'''
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width

    def area(self):
        '''define the area of a rectangle'''

        return self.__width * self.__height

    def __str__(self):
        '''string representation'''

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
