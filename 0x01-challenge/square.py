#!/usr/bin/python3

class Square():
    """
    Class Square representation

    Attributes:
    - height: height of square
    - width: width of square
    """
    
    def __init__(self, width=0, height=0):
        """
        Initializing square values

        Args:
        - height: height of square
        - width: width of square
        """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """
        Area of the square

        Returns:
        Area of the square
        """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """
        Perimeter of the square

        Returns:
        Perimeter of the square
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Returning string representation
        """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
