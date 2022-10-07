#!/usr/bin/python3
'''Unittest for Rectangle'''
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    '''tests class Rectangle'''

    def setUp(self):
        '''Seting up the objects or instances to be tested'''

        Base._Base__nb_objects = 0
        self.rect1 = Rectangle(1, 2)
        self.rect2 = Rectangle(1, 2, 3)
        self.rect3 = Rectangle(1, 2, 3, 4, 5)
        self.rect4 = Rectangle(10, 200, 0, 35)

    def test_id(self):
        '''Test the ids'''

        self.assertEqual(self.rect1.id, 1)
        self.assertEqual(self.rect2.id, 2)
        self.assertEqual(self.rect3.id, 5)
        self.assertEqual(self.rect4.id, 3)

    def test_get_width(self):
        '''Test getter for width'''

        self.assertEqual(self.rect1.width, 1)
        self.assertEqual(self.rect2.width, 1)
        self.assertEqual(self.rect3.width, 1)
        self.assertEqual(self.rect4.width, 10)

    def test_get_height(self):
        '''Test getter for height'''

        self.assertEqual(self.rect1.height, 2)
        self.assertEqual(self.rect2.height, 2)
        self.assertEqual(self.rect3.height, 2)
        self.assertEqual(self.rect4.height, 200)

    def test_area(self):
        '''test area method'''

        self.assertEqual(self.rect1.area(), 2)
        self.assertEqual(self.rect2.area(), 2)
        self.assertEqual(self.rect3.area(), 2)
        self.assertEqual(self.rect4.area(), 2000)

    def test_set_width(self):
        '''Test setter for width'''

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect5 = Rectangle("string", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect5 = Rectangle(1.5, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect5 = Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect5 = Rectangle(-1, 1)

    def test_setter_height(self):
        '''Test setter for height'''

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect5 = Rectangle(1, "string")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect5 = Rectangle(1, 1.5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect5 = Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect5 = Rectangle(1, -1)

    def test_constructor_raiases_x_y(self):
        '''Tests contructor with invalid X or Y coordinates'''

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect5 = Rectangle(1, 2, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect5 = Rectangle(1, 2, 3, -1)
