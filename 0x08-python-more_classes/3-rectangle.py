#!/usr/bin/python3
'''
documentaation of a simple module with a class and a fewwww! funcs
3-rectangle
'''


class Rectangle:
    '''
    a simple class: Rectangle with a few methods

    attribute:
            height = defualt(0)
            width = default(0)
    '''

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        sqA = self.__width * self.__height
        return sqA

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            peri = 0
        else:
            rectP = self.__height + self.__width
            peri = rectP * 2
        return peri

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])
