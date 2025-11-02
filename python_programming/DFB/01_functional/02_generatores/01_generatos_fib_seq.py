# fibonacci sequence
# 1 1 2 3 5 8 13 ...
# so it could be approached with
# Fib(n) = Fib(n-1) + Fib(n-2)
# Fib(0) = 1
# Fib(1) = 1

# Calculate nth fibonacii number
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

print([fib_recursive(i) for i in range(7)])
# But when n become larger and larger it becomes heavier to calculate

from timeit import timeit

print(timeit('fib_recursive(10)', globals=globals(), number=10))
print(timeit('fib_recursive(28)', globals=globals(), number=10))
print(timeit('fib_recursive(29)', globals=globals(), number=10))

# We could try to use memoization

from functools import lru_cache

@lru_cache()
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

print('----after lru_cache----')
print(timeit('fib_recursive(10)', globals=globals(), number=10))
print(timeit('fib_recursive(28)', globals=globals(), number=10))
print(timeit('fib_recursive(29)', globals=globals(), number=10))
# print(timeit('fib_recursive(2000)', globals=globals(), number=10))

# The best approach for something like this is to use non-recursive approach


def fib(n):
    fib_0 = 1
    fib_1 = 1
    for i in range(n):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
    return fib_1

# print([fib(i) for i in range(10)])

print('---- non-recursive ----')
print(timeit('fib(10)', globals=globals(), number=10))
print(timeit('fib(28)', globals=globals(), number=10))
print(timeit('fib(29)', globals=globals(), number=10))
print(timeit('fib(2000)', globals=globals(), number=10))

# create iterator that returns fib numbers

class FibIter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            result = fib(self.i)
            self.i += 1
            return result

fib_iter = FibIter(7)
for i in fib_iter:
    print(i)
# print(list(fib_iter))

# print('---- using iterator that returns fib number ----')
# print(timeit('FibIter(10)', globals=globals(), number=10))
# print(timeit('FibIter(28)', globals=globals(), number=10))
# print(timeit('FibIter(29)', globals=globals(), number=10))
# print(timeit('FibIter(2000)', globals=globals(), number=10))

# using iterator function

def fib(n):
    fib_0 = 1
    fib_1 = 1
    for i in range(n-1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1

gen = fib(7)
for num in gen:
    print(num)

# Fixing to yield the first two values

def fib(n):
    fib_0 = 1
    yield fib_0
    fib_1 = 1
    yield fib_0
    for i in range(n-1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1

gen = fib(7)
for num in gen:
    print(num)


def fib(n):
    fib_0 = 1
    yield fib_0
    fib_1 = 1
    yield fib_0
    for i in range(n-2):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1

gen = fib(7)
for num in gen:
    print(num)
# 1 1 2 3 5 8 13