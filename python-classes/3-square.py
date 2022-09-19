#!/usr/bin/python3
'''This module contains the Square class'''


class Square:
    '''This class defines the attributes of a Square'''

    def __init__(self, size=0):
        '''This method creates a new instance of Square'''
        try:
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be a integer")

    def area(self):
        '''This method calculates the area of a square'''
        return self.__size ** 2
