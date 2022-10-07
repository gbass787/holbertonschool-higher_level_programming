#!/usr/bin/python3
'''Rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''class Rectangle from Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialize class'''

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        '''String representation of Rectangle'''

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    @property
    def width(self):
        '''getter for width'''

        return self.__width

    @width.setter
    def width(self, value):
        '''setter for width'''

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''getter for height'''

        return self.__height

    @height.setter
    def height(self, value):
        '''setter for height'''

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''getter for x'''

        return self.__x

    @x.setter
    def x(self, value):
        '''setter for x'''

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''getter for y'''

        return self.__y

    @y.setter
    def y(self, value):
        '''setter for y'''

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''area of a rectangle'''

        return self.__height * self.__width

    def display(self):
        '''prints rectangle'''

        for i in range(self.__y):
            print("")
        for j in range(self.__height):
            for z in range(self.__x):
                print(" ", end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        '''assings argument to attributes'''

        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
        if len(args) == 0 and kwargs is not None:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        '''Returns the dictionary for rectangle'''

        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
