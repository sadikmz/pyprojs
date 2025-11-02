s1 = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
# s2 = {1,2,3}
# s3 = {[1,2,3]}
# hash(s3)

s2 = frozenset('abc')
print(hash(s2))
print(s2)

s3 = {frozenset({'a', 'n'}), frozenset([1,2,3,4])}
print(s3)
print(type(s3))
# print(hash(s3))
s4 = frozenset(s3)
print(s4)

t1 = (1, 2, [3, 4])
t2 = tuple(t1)
print(t1, id(t1))
print(t2, id(t2))

l1  = [1, 2, 3]
l2 = l1.copy()
print(l1, id(l1))
print(l2, id(l2))

#

s1 = {1, 2, 3}
s2 = s1.copy()
print(s1, id(s1))
print(s2, id(s2))
print(s1 is s2)


s1 = {1, 2, 3}
print(s1, id(s1))
s2 = set(s1)
print(s2, id(s2))
print(s1 is s2)
print(s1 == s2)
# s1.pop()
print(s1)
print(s2)

s1 = frozenset({1, 2, 3})
s2 = frozenset(s1)
print(s1 is s2)
print(id(s1), id(s2))

from copy import deepcopy
s1 = deepcopy(s2)
print(type(s1))
print(s1 is s2)

# operation

s1 = frozenset('ab')
s2 = {1,2}
s3 = s1 | s2
s4 = s2 | s1
print(type(s3))
print(type(s4))

# Equality

s1 = {1,2}
s2 = frozenset({1, 2})
print(s1 is s2)
print(s1 == s2)


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __repr__(self):
        return f'Person(name={self._name}, age={self._age})'

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def key(self):
        return frozenset({self.name, self.age})

p1 = Person('John', 78)
p2 = Person('John', 75)
d = {p1.key():p1, p2.key():p2}
print(d)
print(d[frozenset({'John', 78})])
print(d[p1.key()])
print(p1 == Person('John', 78))

# Memoization
from functools import lru_cache

@lru_cache()
def my_func(*, a, b):
    print('calculating a + b')
    return a + b

# my_func(a=1, b=2)
# my_func(a=1, b=2)
# my_func(b=2, a=1)

# my_func(a=[1,2,3], b=[3,4,5])

def memoizer(fn):
    cache = {}

    def inner(*args, **kwargs):
        key = (*args, frozenset(kwargs.items()))
        if key not in cache:
            result = fn(*args, **kwargs)
            cache[key] = result
        return cache[key]
    return inner

@memoizer
def my_func(*, a, b):
    print('calculating a + b')
    return a + b

my_func(a=1, b=2)
my_func(a=1, b=2)
my_func(b=2, a=1)

def memoizer(fn):
    cache = {}

    def inner(*args, **kwargs):
        key = frozenset(args) | frozenset(kwargs.items())
        if key in cache:
            return cache[key]
        else:
            result = fn(*args, **kwargs)
            cache[key] = result
            return result
    return inner

@memoizer
def adder(*args):
    print('calculating a + b!')
    return sum(args)

print(adder(1,2,3,4))
print(adder(1,2,3,4))



