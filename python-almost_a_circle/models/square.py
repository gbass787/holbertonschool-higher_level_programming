#!/usr/bin/python3
'''class of a square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class of a square from a rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''initialize class'''

        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''String representation of Square'''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        '''Getter method for size'''

        return self.width

    @size.setter
    def size(self, size):
        '''Setter for size '''

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        '''update the values'''

        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        if len(args) == 0 and kwargs is not None:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        '''Returns the dictionary for square'''

        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
