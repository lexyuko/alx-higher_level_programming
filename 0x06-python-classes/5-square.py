#!/usr/bin/python3
"""defne a class square"""

class Square:
    """represent a square"""

    def __init__(self, size=0):
        """initialize a square
        
        Args:
        size(int): the size of the new square.
        """
        self.size = size
        
        @property
        def size(self):
            """get/set the current size of the square"""
            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0
            raise ValueError(size must be >= 0)

        self.__size = value

        def area(self):
            """ Return the current area of the square."""
            return (self.__size * self.__size)

        def my_print(self):
            """ print the std out of the square"""
            for i in range(0, self.__size):
                [print("#", end="") for x in range(self.__size)]
                print("")
                if  self.__size == 0:
                    print("")
