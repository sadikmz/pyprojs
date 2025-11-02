class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width <= 0:
            raise ValueError('width must be positive')
        else:
            self._width = width

    # def area(self):
    #     return self.width * self.height
    #
    # def perimeter(self):
    #     return 2 * (self.width + self.height)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self._width, self._height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self._width, self._height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self._width == other._width and self._height == other._height
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
# print(r1.set_width(-100))
print(r1.set_width(200))
print(r1)