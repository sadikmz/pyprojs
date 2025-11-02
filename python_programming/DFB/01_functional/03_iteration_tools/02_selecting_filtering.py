from _ast import comprehension


def gen_cube(n):
    for i in range(n):
        print(f'yielding {i}')
        yield i**3

# create a predicate
def is_odd(x):
    return x % 2 == 1
print(is_odd(4))

filtered = filter(is_odd, gen_cube(10))
print(list(filtered))
def is_even(x):
    return x % 2 == 0

print(list(filter(is_even, gen_cube(10))))

# using itertools
from itertools import filterfalse
filtered = filterfalse(is_odd, gen_cube(10))
print(list(filtered))


# drowpwhile and teakwhile
from itertools import dropwhile, takewhile
from math import sin, pi

def sine_wave(n):
    start = 0
    max_ = 2 * pi
    step = (max_ - start) / (n-1)

    for _ in range(n):
        yield round(sin(start),2)
        start += step

print(list(sine_wave(15)))

# Takewhile: Iterate until the predicate become false and stops iterating
result = takewhile(lambda x: 0 <= x <= 0.9,sine_wave(15))

print(list(result))
# print(next(result))

# Dropwhile : iterate until it becomes false and then yield the remaining elements (iterate the rest without checking the predicate again)
l = [1,3,5,2,1]

dropwhile(lambda x: x < 5,l)
print(list(dropwhile(lambda x: x < 5,l)))


# Compress function: A basic way to filter the contents of one iterable using another iterable.
data = ['a','b','c','d','e']
selectors = [True, False,1,0] # select based on the truthiness of values

print(list(zip(data,selectors)))
# filtering without using compresess: use list comprehension
print([item for item, truth_value in zip(data,selectors) if truth_value])

# using compress module

from itertools import compress

print(list(compress(data,selectors)))