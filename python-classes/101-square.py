#!/usr/bin/python3


class Square:
    ''' class square'''

    def __init__(self, size=0, position=(0, 0)):
        '''init'''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''property size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''size.setter'''
        self.__size = value

    @property
    def position(self):
        '''property position'''
        return self.__position

    @position.setter
    def position(self, value):
        ''' position.setter'''
        self.__position = value

    def area(self):
        '''calcs area'''
        return self.__size ** 2

    def my_print(self):
        '''prints'''
        pass
