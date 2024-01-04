#!/usr/bin/python3
""" define a class square"""

class Square:
    """represent a class square"""

    def __init__(self, size=0):
        """initialize a new square.

        Args:
        size (int): The size of the new square.
        """
        self.size = size

        @property
        def size(self):
            """Get/set te current size of the square"""
            return self.__size

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("Size must be an integer")
            elif value < 0:
                raise ValueError("Size must be >= 0")
            self.__size = value
            
            def area(self):
                """retuen the currnet area of the square."""
                return (slef.__size * self.__size)


