from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    def __repr__(self):
        return 'Point({0}, {1})'.format(self.x, self.y)


# unpack tuple

p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0, 0)

print(abs(p1))
print(p1 is p2)
print(p2 is p3)
print(p1 == p2) # both are in different momory address and their is not implementation of equality in the Point class


from math import sqrt

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


p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0, 0)

# print(p1 is p2)
# print(p1 == p2)


# implement ordering in the Point
# print(p1 < p2)

# add ordering functionality


from math import sqrt

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
    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented

p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0, 0)

print(p1 is p2)
print(p1 == p2)
print(p1 < p2)
print(p3 < p1)
p4 = Point(100, 100)
print(p4 > p1) # Not harded coded and python figured it out by reflection
print(p1 <= p4) # not working here and <= need to be defined





