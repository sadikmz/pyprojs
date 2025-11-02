# Properties also called modifiers that helps to control attribute properties - how we read and write attributes
# they are basically going through methods
import math


class Circle:
    def __init__(self, radius):
        if not (isinstance(radius, float) or isinstance(radius, int)):
            raise ValueError('radius must be a float or int.')
        if radius < 0:
            raise ValueError('radius must be a positive number.')
        self._radius = radius

    @property
    def radius(self):
        print('radius getter called..')
        return self._radius

    @radius.setter
    def radius(self, value):
        print('radius getter called..')
        if not (isinstance(value, float) or isinstance(value, int)):
            raise ValueError('radius must be a float or int.')
        if value < 0:
            raise ValueError('radius must be a positive number.')
        self._radius = value

    @property
    def area(self):
        print('area property called..')
        return math.pi * self._radius ** 2

c = Circle(1)
print(c.radius)

c.radius= -10
print(c.radius)
# print(c.area)