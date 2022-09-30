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
