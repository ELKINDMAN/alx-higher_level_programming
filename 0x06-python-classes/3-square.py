#!/usr/bin/python3

'''3-square: a python module with minimum funtionalitie, and attribute'''

class Square:

    ''' a class Square that defines a square by: (based on 2-square.py)
Private instance attribute: size
Public instance method: def area(self): that returns the current square area'''

    def __init__(self, size=0):
        '''initalization method for instances of class "Square"'''

        self.__size = size
        if not type(self.__size) is int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):

        """area:
                public instance method that computes the area of square object
            return: current square area"""

        x = self.__size ** 2
        return x
