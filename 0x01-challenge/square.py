#!/usr/bin/python3
"""A function that defines a square module"""


class square():
    """Define a square class"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialize an instance of a square class"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Area of the square"""
        return self.width * self.height

    def permiter_of_my_square(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Print the string representation of the square instance"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """Create an instance of a square"""
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
