t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(id(t1), id(t2))
print(hash(t1), hash(t2))
# print(t1 is t2)
# print(t1==t2)

d = {t1:100}
print(d)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

p1 = Person('John', 78)
p2 = Person('John', 78)

print(p1 is p2)
print(p1 == p2)

print(hash(p1), hash(p2))

p1 = Person('John', 78)
p2 = Person('Eric', 75)

persons = {p1:'John object', p2:'Eric object'}

for k in persons.keys():
    print(k)


# define equality
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False

p1 = Person('John', 78)
p2 = Person('John', 78)

print(p1 is p2)
print(p1 == p2)

# person = {p1:'John p1'}

# adding hash method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False

    def __hash__(self):
        return 100


p1 = Person('John', 78)
p2 = Person('John', 78)

print(p1 is p2)
print(p1 == p2)
print(hash(p1), hash(p2))
person = {p1:'John p1'}

# Making a class not hashable

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f'Person(name={self.name}, age={self.age})'
#
#     def __eq__(self, other):
#         if isinstance(other, Person):
#             return self.name == other.name and self.age == other.age
#         else:
#             return False
#
#     __hash__ = None
# print('------')
# p1 = Person('John', 78)
# p2 = Person('John', 78)
# print(p1 is p2)
# print(p1 == p2)
# print(hash(p1), hash(p2))
# person = {p1:'John p1'}

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False

    def __hash__(self):
        return hash((self.name, self.age))


p1 = Person('John', 78)
p2 = Person('Eric', 78)
persons = {p1:'John object', p2:'Eric object'}
print(persons[p1])
print(persons[Person('John', 78)])

p2 = Person('John', 78)
print(p1 is p2)
print(p1 == p2)
print(persons[p1] is persons[p2])
print(hash(p1), hash(p2))


# equal hashes for unequal objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False

    def __hash__(self):
        return 100

p1 = Person('John', 78)
p2 = Person('Eric', 75)

print(hash(p1) == hash(p2))
print(p1 is p2)

persons = {p1:'John object', p2:'Eric object'}
print(persons[Person('John', 78)])

# create a hashable class Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))

points = {Point(0,0): 'origin', Point(1,1): 'second pt'}
print(points[Point(0,0)])

# checking with tuple
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

    def __eq__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            other = Point(*other)
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))

points = {Point(0,0): 'origin', Point(1,1): 'second pt'}
print(points[(0,0)])

# pt object here is mutable

pt1 = Point(0, 0)
pt2 = Point(1, 1)
points = {pt1:'origin', pt2:'second pt'}
print(points[pt1], points[Point(0,0)])

pt1.x = 10
print(pt1)
# print(points[pt1])

for k, v in points.items():
    print(k, v)

# print(points[Point(10,0)])
# print(points[(10,0)])

# Creating a mutable object
class Person:
    def __init__(self, id, name, age):
        self._id = id
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(id={self._id}, name={self.name}, age={self.age})'

    def __eq__(self, other):
        if isinstance(self, Person):
            return self._id == other._id
        else:
            return False

    def __hash__(self):
        return hash(self._id)

p1 = Person('john', 'John', 7)

persons = {p1:'john object'}
print(persons[p1])

print(persons[Person('john', 'John', 7)])

p1.name = 'Eric'
p1.age = 78
print(p1)