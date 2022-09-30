#!/usr/bin/python3
'''class of a square'''
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    '''class of a square inherited from Rectangle'''

    def __init__(self, size):
        '''initialize size'''
        BaseGeometry.integer_validator(self, "size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        '''string representation'''

        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
