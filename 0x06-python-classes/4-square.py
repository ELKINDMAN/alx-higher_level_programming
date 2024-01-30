#!/usr/bin/python3

'''a module for python class "Square"...'''

class Square:

'''class Square that defines a square by: (based on 3-square.py)'''

    def __init__(self, size=0):
        '''public initialization method'''

        self.__size = size
    @property
    def size(self):
        '''getter property to retrive __size'''

        print("retrieving a private attr...")
        return self.__size

    @size.setter
    def size(self, value):
        '''property setter to modify the private attr...'''
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''public method: returns the current square area'''

        sqA = self.__size ** 2
        return sqA
