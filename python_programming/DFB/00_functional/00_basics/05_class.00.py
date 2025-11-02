class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

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
print(r1.setwidth(200))
print(r1)