#!/usr/bin/python3
'''class of BaseGeometry'''


class BaseGeometry():
    '''class of BaseGeometry'''

    def area(self):
        '''area not defined'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''validates the value'''
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
