from collections import namedtuple


# named tuple is a class factory

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # def __repr__(self):


from collections import namedtuple

Point2D = namedtuple('Point3D', ['x', 'y'])

# type(Point3D)
pt1 = Point2D(1, 2)
print(pt1)
pt3d_1 = Point3D(1, 2, 3)
print(pt3d_1)

Pt2D = namedtuple('Point2D', ['x', 'y'])

pt2 = Pt2D(1, 2)
print(pt2)

pt3d_2 = Point3D(x=100, y=200, z=300)
print(pt3d_2)
print(isinstance(pt2, tuple))
print(isinstance(pt3d_1, tuple))
print(isinstance(pt3d_2, list))

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
print(a == b)

pt1 = Point2D(1, 2)
pt2 = Point2D(1, 2)
print(pt1 == pt2)
print(pt1 is pt2)

pt1 = Point3D(1, 2, 3)
pt2 = Point3D(1, 2, 3)
print(pt1 == pt2)
print(pt1 is pt2)


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y}, z={self.z})'

    # add equalilty

    def __eq__(self, other):
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False


pt1 = Point3D(1, 2, 3)
pt2 = Point3D(1, 2, 3)
print(pt1 == pt2)
print(pt1 is pt2)

pt1 = Point2D(1, 2)
pt2 = Point3D(1, 1, 1)


# print(max(pt1))
# print(max(pt2))


# Looking the dot products of two vectors
# a = a.x, b.x
# b = b.x, b.y
# dot product of a.b
# a.b = a.x * b.x + a.y * b.y

def dot_product_3d(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z
    # only works for 3d notation as it's assuming three coordinates


pt1 = Point3D(1, 2, 3)
pt2 = Point3D(1, 1, 1)
print(dot_product_3d(pt1, pt2))

a = (1, 2)
b = (1, 1)

# zip
print(zip(a, b))

print(sum([e[0] * e[1] for e in zip(a, b)]))  # without the square parenthesis
print(sum(e[0] * e[1] for e in zip(a, b)))


# Writing it as a function

def dot_product(a, b):
    return sum(e[0] * e[1] for e in zip(a, b))
    # it's not assuming the number of coordinates but at least two points


pt1 = Point2D(1, 2)
pt2 = Point2D(1, 1)
print(dot_product(pt1, pt2))

Vector_3D = namedtuple('Vector3D', ['x', 'y', 'z'])
v1 = Vector_3D(1, 2, 3)
v2 = Vector_3D(1, 1, 1)

print(dot_product(v1, v2))

print(v1)
print(tuple(v1))
print(v1[1])
print(v1.y)

Circle = namedtuple('Circle', 'center_x center_y        radius')
c = Circle(0, 1, 2)
print(c)
print(c.radius)
print(c[2])

Stock = namedtuple('Stock', '''symbol 
year 
month 
day 
open 
high 
low 
close''')

djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
print(djia)

print(djia.symbol)
print(djia[0])
print(type(djia))
for item in djia:
    print(item)


# unpack


p = Point2D(1, 2)

x,y = p

print(x,y)

print(djia)

# Extended unpacking
symbol, year, month, day, *_, close = djia
print(symbol)
print(year)
print(month)
print(day)
print(close)
print(_)
print(symbol, year, month, day, close)

Person = namedtuple('Person', 'name age ssn bbn _ccn', rename=True)
p1 = Person(1,2,3,4,5)
print(p1)
print(p1._fields)
print(Person._fields)
print(dir(Person))
print(p1._asdict())
print(Person._fields)

# viewing the source code
# print(Stock._source)
print(dir(Stock))
# print(Stock._fields)
# print(Point2D._source)
print(p1._asdict())