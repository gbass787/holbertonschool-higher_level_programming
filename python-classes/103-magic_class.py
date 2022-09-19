#!/usr/bin/python3
'''Define a MagicClass match bytecode of holberton'''

import math


class MagicClass:
    '''Represents a circle'''

    def __init__(self, radius=0):
        '''Initialize a MagicClass'''
        self.__radius = radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        '''Return the area'''
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        '''Return the circumference'''
        return (2 * math.pi * self.__radius)
