from collections import namedtuple

Point = namedtuple('Point', 'x y')
p1 = Point(10.5, 3.2)
# print(p1)

p1 = Point('abc', [1,2,3])
# print(p1)

# points have to be real numbers
# be able to unpack

# determine the type of variable is numerical
import numbers

# test if the variables are instance of numbers classes
# print(isinstance(10,numbers.Number))
# print(isinstance('a',numbers.Number))
# print(isinstance(1.1,numbers.Number))
# Check if a variable is instances of a real number
# print(isinstance(1,numbers.Real))
# print(isinstance((1.1 + 2j),numbers.Real))


# define a point class

class Point:
    def __init__(self, x, y):
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self._pt = (x, y)
        else:
            raise TypeError('Point co-ordinates must be of real number type')

    def __repr__(self):
        return f'Point({self._pt[0]}, {self._pt[1]})'


# p1 = Point(10, 2.5)
# print(p1)

# p1 = Point('10', 2.5)
# print(p1)

# unpacking

# x,y = p1
# print(x,y)

class Point:
    def __init__(self, x, y):
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self._pt = (x, y)
        else:
            raise TypeError('Point co-ordinates must be of real number type')

    def __repr__(self):
        return f'Point({self._pt[0]}, {self._pt[1]})'

    def __len__(self):
        return len(self._pt)

    def __getitem__(self, s):
        return self._pt[s]


# p1 = Point(10, 2)
# x,y = p1
# print(x,y)


class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []

    def __repr__(self):
        return f'Polygon({self._pts})'

# p1 = Polygon((0,0),Point(1,1))
# print(p1)


#

class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []

    def __repr__(self):
        pts_str = ', '.join([str(pt) for pt in self._pts])
        return f'Polygon({pts_str})'

# p1 = Polygon((0,0),Point(1,1))
# print(p1)
# polygon = Polygon(Point(0, 0), Point(1, 1))
# print(polygon)


# sequence type

class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []

    def __repr__(self):
        pts_str = ', '.join([str(pt) for pt in self._pts])
        return f'Polygon({pts_str})'

    def __len__(self):
        return len(self._pts)

    def __getitem__(self, s):
        return self._pts[s]


# p1 = Polygon((0,0),Point(1,1))
# print(p1)
# polygon = Polygon(Point(0, 0), Point(1, 1))
# print(polygon)
#
# print(p1[::-1])

# Define concatenation


class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []

    def __repr__(self):
        pts_str = ', '.join([str(pt) for pt in self._pts])
        return f'Polygon({pts_str})'

    def __len__(self):
        return len(self._pts)

    def __getitem__(self, s):
        return self._pts[s]

    def __add__(self, other):
        if isinstance(other, Polygon):
            new_pts = self._pts + other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError('Can only concatenate with another Polygon')

# p1 = Polygon((0,0),Point(1,1))
# p2 = Polygon((2,2),Point(3,3))
#
# result = p1 + p2
# print(id(result), id(p1), id(p2))

# implement in-place concatenation

class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []

    def __repr__(self):
        pts_str = ', '.join([str(pt) for pt in self._pts])
        return f'Polygon({pts_str})'

    def __len__(self):
        return len(self._pts)

    def __getitem__(self, s):
        return self._pts[s]

    def __add__(self, other):
        if isinstance(other, Polygon):
            new_pts = self._pts + other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError('Can only concatenate with another Polygon')

    def __iadd__(self, other):
        if isinstance(other, Polygon):
            self._pts += other._pts
            return self
        else:
            raise TypeError('Can only concatenate with another Polygon')



# p1 = Polygon((0,0),Point(1,1))
# p2 = Polygon((2,2),Point(3,3))
# print(id(p1), id(p2))
# p1 += p2
# print(id(p1))
# print(p1)
#
# print(id(p2))
# print(p2)


#

class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []

    def __repr__(self):
        pts_str = ', '.join([str(pt) for pt in self._pts])
        return f'Polygon({pts_str})'

    def __len__(self):
        return len(self._pts)

    def __getitem__(self, s):
        return self._pts[s]

    def __add__(self, other):
        if isinstance(other, Polygon):
            new_pts = self._pts + other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError('Can only concatenate with another Polygon')

    def __iadd__(self, other):
        if isinstance(other, Polygon):
            points = other._pts
        else:
            points = [Point(*pt) for pt in other]
            self._pts += self._pts + points
        return  self
            # raise TypeError('Can only concatenate with another Polygon')


# p1 = Polygon((0,0),Point(1,1))
# print(id(p1))
# print(p1)
# p1 +=[(2,2),(3,3),Point(4,4)]
# print(id(p1))
# print(p1)

# add methods append

class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []

    def __repr__(self):
        pts_str = ', '.join([str(pt) for pt in self._pts])
        return f'Polygon({pts_str})'

    def __len__(self):
        return len(self._pts)

    def __getitem__(self, s):
        return self._pts[s]

    def __add__(self, other):
        if isinstance(other, Polygon):
            new_pts = self._pts + other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError('Can only concatenate with another Polygon')

    def __iadd__(self, other):
        if isinstance(other, Polygon):
            points = other._pts
        else:
            points = [Point(*pt) for pt in other]
            self._pts += self._pts + points
        return  self

    # Append method

    def append(self, pt):
        self._pts.append(Point(*pt))

    # Insert methods

    def insert(self, index, pt):
        self._pts.insert(index, Point(*pt))

    # Extend

    def extend(self, pts):
        if isinstance(pts, Polygon):
            self._pts += pts._pts
        else:
            points = [Point(*pt) for pt in pts]
            self._pts += points

            # raise TypeError('Can only concatenate with another Polygon')

# cleaning up the above code


# add methods append

class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []

    def __repr__(self):
        pts_str = ', '.join([str(pt) for pt in self._pts])
        return f'Polygon({pts_str})'

    def __len__(self):
        return len(self._pts)

    def __getitem__(self, s):
        return self._pts[s]

    def __add__(self, other):
        if isinstance(other, Polygon):
            new_pts = self._pts + other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError('Can only concatenate with another Polygon')

    # Append method

    def append(self, pt):
        self._pts.append(Point(*pt))

    # Insert methods

    def insert(self, index, pt):
        self._pts.insert(index, Point(*pt))

    # Extend

    def extend(self, pts):
        if isinstance(pts, Polygon):
            self._pts += pts._pts
        else:
            points = [Point(*pt) for pt in pts]
            self._pts += points

    def __iadd__(self, other):
        self.extend(other)
        return self


# p1 = Polygon((0,0),Point(1,1))
# p2 = Polygon((2,2),Point(3,3))
# print(p1, id(p1))
# print(p2, id(p2))
# p1 +=[(2,2),(3,3),Point(4,4)]
# print(id(p1))
# print(p1)

# p1.append([10,10])
# print(p1, id(p1))
#
# p1.insert(1,[-1,-1])
# print(p1, id(p1))
#
# p1.extend(p2)
# print(p1, id(p1))
#
# # extend by passing iterable
#
# p1.extend([(0,0), Point(1,1)])
# print(p1, id(p1))
#
#
# p1.extend(Point(0,0))
# print(p1, id(p1))


# add setitem method


class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []

    def __repr__(self):
        pts_str = ', '.join([str(pt) for pt in self._pts])
        return f'Polygon({pts_str})'

    def __len__(self):
        return len(self._pts)

    def __getitem__(self, s):
        return self._pts[s]

    # set setitem method

    def __setitem__(self, s, value):
        self._pts[s] = [Point(*pts) for pts in value]

    def __add__(self, other):
        if isinstance(other, Polygon):
            new_pts = self._pts + other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError('Can only concatenate with another Polygon')

    # Append method

    def append(self, pt):
        self._pts.append(Point(*pt))

    # Insert methods

    def insert(self, index, pt):
        self._pts.insert(index, Point(*pt))

    # Extend

    def extend(self, pts):
        if isinstance(pts, Polygon):
            self._pts += pts._pts
        else:
            points = [Point(*pt) for pt in pts]
            self._pts += points

    def __iadd__(self, other):
        self.extend(other)
        return self


p = Polygon((0,0),Point(1,1),(2,2))
print(id(p),p)
print(p[0:2])

# add item
p[0:2] = [(10,10), Point(1,1), (30,30)]

print(id(p),p)

# Adding a single item
# print(p[0])

# p[0] = Point(0,0)

# fixing the script to add a single element



class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []

    def __repr__(self):
        pts_str = ', '.join([str(pt) for pt in self._pts])
        return f'Polygon({pts_str})'

    def __len__(self):
        return len(self._pts)

    def __getitem__(self, s):
        return self._pts[s]

    # set setitem method

    def __setitem__(self, s, value):
        if isinstance(s, int):
            self._pts[s] = Point(*value)
        else:
            self._pts[s] = [Point(*pts) for pts in value]

    def __add__(self, other):
        if isinstance(other, Polygon):
            new_pts = self._pts + other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError('Can only concatenate with another Polygon')

    # Append method

    def append(self, pt):
        self._pts.append(Point(*pt))

    # Insert methods

    def insert(self, index, pt):
        self._pts.insert(index, Point(*pt))

    # Extend

    def extend(self, pts):
        if isinstance(pts, Polygon):
            self._pts += pts._pts
        else:
            points = [Point(*pt) for pt in pts]
            self._pts += points

    def __iadd__(self, other):
        self.extend(other)
        return self


# p = Polygon((0,0),Point(1,1),(2,2))
# print(id(p),p)
# p[0] = Point(-1,-1)
# print(id(p),p)

# assigning a slice

# l = [1,2,3,4]
# l[0:2] = 20

# print(p)

# p[0:2] = Point(20,20)
# p[0] = [Point(10,10), Point(20,20)]

# Cleaning up the code


class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []

    def __repr__(self):
        pts_str = ', '.join([str(pt) for pt in self._pts])
        return f'Polygon({pts_str})'

    def __len__(self):
        return len(self._pts)

    def __getitem__(self, s):
        return self._pts[s]

    # set setitem method

    def __setitem__(self, s, value):
        try:
            rhs = [Point(*pts) for pts in value]
            is_single = False
        except TypeError:
            try:
                rhs = Point(*value)
                is_single = True
            except TypeError:
                raise TypeError("Invalid Point or iterable of Points")

        if (isinstance(s,int) and is_single) or \
                (isinstance(s,slice) and not is_single):
            self._pts[s] = rhs
        else:
            raise TypeError('Incompatible index assignment')

    def __add__(self, other):
        if isinstance(other, Polygon):
            new_pts = self._pts + other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError('Can only concatenate with another Polygon')

    # Append method

    def append(self, pt):
        self._pts.append(Point(*pt))

    # Insert methods

    def insert(self, index, pt):
        self._pts.insert(index, Point(*pt))

    # Extend

    def extend(self, pts):
        if isinstance(pts, Polygon):
            self._pts += pts._pts
        else:
            points = [Point(*pt) for pt in pts]
            self._pts += points

    def __iadd__(self, other):
        self.extend(other)
        return self


p = Polygon((0,0),Point(1,1),(2,2))
print(id(p),p)

# p[0] = [(0,0),(1,1)]
# p[0] = ('a','b')
# print(id(p),p)

# Implement delete key word del

# l = [1,2,3,4]
# del l[0]
# print(l)
# print(l.pop(0))
# print(l)

class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []

    def __repr__(self):
        pts_str = ', '.join([str(pt) for pt in self._pts])
        return f'Polygon({pts_str})'

    def __len__(self):
        return len(self._pts)

    def __getitem__(self, s):
        return self._pts[s]

    # set setitem method

    def __setitem__(self, s, value):
        try:
            rhs = [Point(*pts) for pts in value]
            is_single = False
        except TypeError:
            try:
                rhs = Point(*value)
                is_single = True
            except TypeError:
                raise TypeError("Invalid Point or iterable of Points")

        if (isinstance(s,int) and is_single) or \
                (isinstance(s,slice) and not is_single):
            self._pts[s] = rhs
        else:
            raise TypeError('Incompatible index assignment')

    def __add__(self, other):
        if isinstance(other, Polygon):
            new_pts = self._pts + other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError('Can only concatenate with another Polygon')

    # Append method

    def append(self, pt):
        self._pts.append(Point(*pt))

    # Insert methods

    def insert(self, index, pt):
        self._pts.insert(index, Point(*pt))

    # Extend

    def extend(self, pts):
        if isinstance(pts, Polygon):
            self._pts += pts._pts
        else:
            points = [Point(*pt) for pt in pts]
            self._pts += points

    def __iadd__(self, other):
        self.extend(other)
        return self

    # Delete method
    def __delitem__(self, s):
        del self._pts[s]

    # Pop method

    def pop(self,i):
        return self._pts.pop(i)

    # clear method
    def clear(self):
        self._pts.clear()

p = Polygon((0,0),Point(1,1),(2,2),(3,3))

del p[0]
print(p)

del p[0:2]
print(p)
print(p.pop(0))
print(p)