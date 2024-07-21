#!/usr/bin/python3
""" A function to find the area and perimeter of a square """


class square():
    """Define a square class"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialize a square class"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Area of the square"""
        return self.width * self.height

    def PermiterOfMySquare(self):
        """Perimeter instance of the square"""
        return (self.height * 2) + (self.height * 2)

    def __str__(self):
        """Print the objects in string format"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """Create an instance for a square"""
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
