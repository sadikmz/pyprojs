class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        # print("getting width")
        return self._width

    # set setter - methods
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("width must be positive")
        else:
            self._width = width
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("Height must be positive")
        else:
            self._height = height


    # def set_width(self, width):
    #     if width <= 0:
    #         raise ValueError('width must be positive')
    #     else:
    #         self.width = width

    # def area(self):
    #     return self.width * self.height
    #
    # def perimeter(self):
    #     return 2 * (self.width + self.height)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False
        # return self.width == other.width and self.height == other.height

    # def __lt__(self, other):
    #     if isinstance(other, Rectangle):
    #         return self.area() < other.area()
    #     else:
    #         return NotImplemented

r1 = Rectangle(10, 20)



# print(r1.area())
# print(r1.perimeter())
# print(str(r1))
# print(hex(id(r1)))
# print(r1.to_string())
# print(str(r1))
# print(repr(r1))

# r2 = Rectangle(100, 200)

# print(r1 is r2)
# print(r1 == r2)
# print(r1 == 100)
# print(r1 < r2)
# print(r2 > r1)
# print(r1 <= r2)
# print(r1 > r2)
# print(r1 >= r2)
# print(r1.setwidth(-100))
# print(r1.setwidth(200))
print(r1.width)
r1.width = 1000
print(r1.width)
# r1.height = -1000
r1 = Rectangle(100, -20)
print(r1)