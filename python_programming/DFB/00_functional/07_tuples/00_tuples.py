# Tuples vs List vs Strings
# Homogeneous tuple
print((10,20,30))
print(10,20,30)
a = 10,20,30

for i in a:
    print(i)
print(a[1])
print(a[1:3])

# Unpack tuple

# a = 'a', 10, 20, 30
# a, b, c ,d= a
# print(a, b, c)

a = ('a', 10, 20, 30, 40, 50,60,70,80,90)
x, *other,y,z = a
print(x, other,y,z)
print(*other)
# for i in other:
#     print(i)


#

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'

pt = Point2D(10, 20)
print(pt)
print(id(pt))
pt.x = 100
print(id(pt))

a = Point2D(10, 20), Point2D(30, 40)
print(id(a))
print(a)
a[0].x = 100
a[0].y = 200
print(id(a))
print(a)
# a.y = 200

pt1 = (0,0)
pt2 = (10,20)
print(id(pt1))
print(id(pt2))

#
london = 'London', 'UK', 8_700_000
new_york = 'New York', 'USA', 8_500_000
bejing = 'Bejing', 'China', 21_500_000

cities = [london, new_york, bejing]

print(london)

# calculating total

total = 0
for city in cities:
    print(city[2])
    print(type(city[2]))
    total += city[2]
print(total)

# Using list comprehension

total = 0
print([city[2] for city in cities])
print(sum([city[2] for city in cities]))
print(sum(city[2] for city in cities))

record = 'DJIA', 2018, 1, 19, 20_987, 26_072, 25_942, 26_072
print(record)
symbol, year, month, day, open_, high, low, close = record
symbol, *_, close = record
print(symbol, _, close)

for city, country, population in cities:
    print(city, country, population)

for item in enumerate(cities):
    print(item)

for index, city in enumerate(cities):
    print(index, city)

# Return data from tuple: Calculate an approximate value of pi

from random import uniform
from math import sqrt

def random_shot(radius):
    random_x = uniform(-radius,radius)
    random_y = uniform(-radius,radius)

    # check if this coordinate is inside the circle
    # and x and y whether it's inside the circle or not

    if sqrt(random_x**2+random_y**2) <= radius:
        is_in_circle = True
    else:
        is_in_circle = False

    return random_x, random_y, is_in_circle

num_attempts = 100
count_inside = 0

for attempt in range(num_attempts):
    *_, is_in_circle = random_shot(1)
    if is_in_circle:
        count_inside += 1

print(f'Pi is approximately {4 * count_inside/num_attempts}')
