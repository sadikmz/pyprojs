from functools import total_ordering
from math import sqrt

# Point class and decorate it with complete_ordering

@total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    def __repr__(self):
        return 'Point({0}, {1})'.format(self.x, self.y)

    def __eq__(self,other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False
    def __gt__(self, other):
        if isinstance(other, Point):
            return abs(self) > abs(other)
        else:
            return NotImplemented

p1, p2, p3, p4 = Point(2, 3), Point(2, 3), Point(0, 0), Point(100, 100)

print(p1 >= p2)
print(p1 <= p4)
print(p1 == p2)
print(p1 < p2)
print(p3 > p1)
print(p3 != p1)


