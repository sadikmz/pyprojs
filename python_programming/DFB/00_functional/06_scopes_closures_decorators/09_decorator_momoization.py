# Allows to build a cache of a function

# Example using fibonaci numbers
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)

# fib(10)

class Fib:
    def __init__(self):
        self.cache = {1:1,2:1}
    # Define the fibonaci number itself
    def fib(self, n):
        # if the element is in the cache we'll calculate it and store it in the cache
        if n not in self.cache:
            print('Calculating fib({0})'.format(n))
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]

# f = Fib()

# f.fib(10)
#
# print(f.fib(10))

# writing same thing with closure

def fib():
    cache = {1:1,2:1}

    def calc_fib(n):
        if n not in cache:
            print('Calculating fib({0})'.format(n))
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]
    return calc_fib

# f = fib()
# print(f(10))

# using decorator
def memoize_fib(fib):
    cache = dict()
    cache = {1:1,2:1}

    def inner(n):
        if n not in cache:
            cache[n] = fib(n)
        return cache[n]

    return inner

@memoize_fib
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

# print(fib(10))

# Other option using decorator without setting a cache
def memoize_fib(fib):
    cache = dict()
    # cache = {1:1,2:1}

    def inner(n):
        if n not in cache:
            cache[n] = fib(n)
        return cache[n]

    return inner

@memoize_fib
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

# print(fib(10))

#
# using decorator
def memoize(fib):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fib(n)
        return cache[n]

    return inner

@memoize
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)
#
# print(fib(10))
# print(fib(10))
# print(fib(11))
# print(fib(11))

# for any function that requires a single parameter
@memoize
def fact(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 2 else n * fact(n-1)

# print(fact(6))
# print(fact(10))

# with fibonaci large number
@memoize
def fib(n):
    # print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

from time import perf_counter

# start = perf_counter()
# print(fib(35))
# end = perf_counter()
# print(end - start)

# least recently used caching: To limit cache size
# Default cache itmes in lru is ~ 128 caches
from functools import lru_cache

@lru_cache()
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print(fib(10))
print(fib(10))
print(fib(11))

# Modify the cache size

@lru_cache(maxsize=4)
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print(fib(8))
print(fib(8))
# print(fib(9))
# print(fib(2))
# print(fib(1))
print(fib(16))
print(fib(7))