#!/usr/bin/python3
'''Unittest for Square'''
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestSquare(unittest.TestCase):
    '''tests class Rectangle using unitest'''

    def setUp(self):
        '''Seting up the objects or instances to be tested'''

        Base.__nb_objects = 0
        self.squ1 = Square(1, 2, 3, 4)
        self.squ2 = Square(5, 6, 7, 8)
        self.squ3 = Square(10, 200, 35, 0)
        self.squ4 = Square(1, 5, 3, 40)

    def test_id(self):
        '''Test the ids'''

        self.assertEqual(self.squ1.id, 4)
        self.assertEqual(self.squ2.id, 8)
        self.assertEqual(self.squ3.id, 0)
        self.assertEqual(self.squ4.id, 40)

    def test_get_width(self):
        '''Test getter for width'''

        self.assertEqual(self.squ1.width, 1)
        self.assertEqual(self.squ2.width, 5)
        self.assertEqual(self.squ3.width, 10)
        self.assertEqual(self.squ4.width, 1)

    def test_area(self):
        '''test area method'''

        self.assertEqual(self.squ1.area(), 1)
        self.assertEqual(self.squ2.area(), 25)
        self.assertEqual(self.squ3.area(), 100)
        self.assertEqual(self.squ4.area(), 1)

    def test_set_width(self):
        '''test setter for width'''

        self.assertEqual(self.squ1.width, 1)
        self.assertEqual(self.squ2.width, 5)
        self.assertEqual(self.squ3.width, 10)
        self.assertEqual(self.squ4.width, 1)
        squ5 = Square(1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            squ5.size = "hey"
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            squ5.width = 1.5
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            squ5.width = 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            squ5.width = -1
