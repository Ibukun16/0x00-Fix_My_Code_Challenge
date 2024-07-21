#!/usr/bin/python3

class square():
    """
    A function that defines a square class

    Attributes:
    - width: The width of the square.
    - height: The height of the square.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize an instance of a square class

        Args:
        - width: The width of the square
        -height: The height of the square
        """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """Calculate and return area of the square"""
        return self.width * self.height

    def PermiterOfMySquare(self):
        """Calculate and return perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Print the string representation of the square instance"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
