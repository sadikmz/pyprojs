# let's go with two ways of creating iterator using a factorial of a number

import math

class FactIter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            result = math.factorial(self.i)
            self.i += 1
            return result


# fact_iter = FactIter(5)

# print(list(fact_iter))
# print(next(fact_iter))
# print(next(fact_iter))

# Second way - using the second form of iter function which requires a callable and iteration stop value (sentinel value)
# we are implementing with closures
def fact():
    i = 0

    def inner():
        nonlocal i
        result = math.factorial(i)
        i += 1
        return result

    return inner

f = fact()
print(f)
# print(f())
# print(f())
# print(f())
# print(f())
# print(f())
# print(f())

# create a finite iterator using iter function
fact_iter = iter(fact(), math.factorial(5))
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))
# print(next(fact_iter))

# Using the yield statement

def my_func():
    print('Line 1')
    # yield 'Flying'
    print('Line 2')
    # yield 'Flying'
print(my_func)
f = my_func()


def my_func():
    print('Line 1')
    yield 'We are now at the first yield'
    print('Line 2')
    yield 'We are now at the second yield'
print(my_func)

f = my_func()
print(type(f))
print('__iter__' in dir(f))
print('__next__' in dir(f))
print(iter(f) is f)
print(next(f))
print(next(f))
# print(next(f))

# Whenever it reaches a return value, it will stop (A return value could be implicit)
# Example

def silly():
    yield 'the'
    yield 'ministry'
    yield 'of'
    yield 'silly'
    yield 'walks'


gene = silly()
print(next(gene))
print(next(gene))
print(next(gene))
print(next(gene))
print(next(gene))
# print(next(gene))

def silly():
    yield 'the'
    yield 'ministry'
    yield 'of'
    yield 'silly'
    yield 'walks'
    return None

gene = silly()
print(next(gene))
print(next(gene))
print(next(gene))
print(next(gene))
print(next(gene))
# print(next(gene))


def silly():
    yield 'the'
    yield 'ministry'
    yield 'of'
    yield 'silly'
    if True:
        yield 'walks'
    yield 'walks'
    return None

gene = silly()
print(next(gene))
print(next(gene))
print(next(gene))
print(next(gene))
print(next(gene))
print(next(gene))


def silly():
    yield 'the'
    yield 'ministry'
    yield 'of'
    yield 'silly'
    if True:
        return "fuck-off, the iteration is done!"
    yield 'walks'
    return None

gene = silly()
print(next(gene))
print(next(gene))
print(next(gene))
print(next(gene))
# print(next(gene))
# print(next(gene))

# Rewriting the factorial function with generator
class FactIter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            result = math.factorial(self.i)
            self.i += 1
            return result

# doing for all
def fact(n):
    for i in range(n):
        print(math.factorial(i))

fact(5)

# using generator function
def fact(n):
    for i in range(n):
        yield math.factorial(i)

# print(type(fact))

gene = fact(5)
print(type(gene))
print(next(gene))
print(next(gene))
print(next(gene))
print(next(gene))
print(next(gene))
# print(next(gene))
print(list(gene))

# For squares generator function

def Squares(n):
    for i in range(n):
        yield (i**2)

sq = Squares(5)
for x in sq:
    print(x)
print(list(sq))