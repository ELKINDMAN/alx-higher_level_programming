#!/usr/bin/python3
"""This is a documentation for a square module
    instantiates size and checks for errors
 """
class Square:
    """Square: A class that defines a square by: (based on 1-square.py).
    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
    """
    def __init__(self, size=0):
        self.__size = size

        if not type(self.__size) is int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
