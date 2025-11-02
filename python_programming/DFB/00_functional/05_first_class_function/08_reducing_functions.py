# Reducing functions: Are function that recombine an interable recursively, ending up with a single return value
# Also called accumulator, aggregator, or folding function
# example: Finding of the max value in an iterable
# a1,a2,a3
# max(a,b)

l = [5,8,6,10,9]
max_value = lambda a,b:a if a > b else b

def max_sequences(sequence):
    result = sequence[0]
    for i in sequence[1:]:
        result = max_value(result,i)
    return result

min_value = lambda a,b:a if a < b else b

def min_sequences(sequence):
    result = sequence[0]
    for i in sequence[1:]:
        result = min(result,i)
    return result

# We could do this
def _reduce(fn,sequence):
    result = sequence[0]
    for i in sequence[1:]:
        result = fn(result,i)
    return result

add = lambda a,b:a+b
print(_reduce(add,[1,2,3,6]))

# The functools module

from functools import reduce
l = [5,8,6,10,9]
print(reduce(lambda a, b: a if a > b else b, l))
print(reduce(lambda a, b: a if a < b else b, l))
print(reduce(lambda a, b: a + b, l))
print(reduce(lambda a, b: a if a < b else b, {10,1,4,5,7}))
print(reduce(lambda a, b: a if a < b else b, 'python'))
print(reduce(lambda a,b: a + ' ' + b, ('python', 'is', 'awesome!', 'Aha', 'okay!')))

# built-in reducing functions
# min()
print(min([10,1,3,4,5]))
print(max([10,1,3,4,5]))
print(sum([1,2,3,4,5]))
print(any([0,1]))
print(all([1,2,3,4,5,None]))

l = [0, '', None, 100]

print(reduce(lambda a,b: bool(a) or bool(b), l))

# calculating the product of all the elements

l = [1,2,3,4,5]
result=reduce(lambda a,b: a*b, l)

print(result)

# calculating n!
# n!=1*2*3*4*n
n=5

result = reduce(lambda a, b: a*b, range(1,n+1))
print(result)

# the reduce initializer
# The reduce function has a third (optional) default parameter: default to None
# If it is specified, it is essentially like adding to the front of the iterable.
# it is often used to provide some kind of default in case the iterable is empty.
# l = []
# result = reduce(lambda a,b: a+b, l)
# print(result)


l = []
# result = reduce(lambda a,b: a+b, l,1) # addition initializer (default value of 1)
result = reduce(lambda a,b: a+b, l,100) # addition initializer (default value of 100)
print(result)


l = [1,2,3,4,5]
# result = reduce(lambda a,b: a+b, l,1) # addition initializer (default value of 1)
result = reduce(lambda a,b: a+b, l,100) # addition initializer (default value of 100)
print(result)

l = [5,8,6,10,9]

_max = lambda x, y: x if x > y else y
print(_max(10,3))
# result = reduce(lambda a,b: a+b, l,100)

def max_sequence(sequence):
    result = sequence[0]
    for i in sequence[1:]:
        result = _max(result,i)
    return result

print(max_sequence(l))

_min = lambda x, y: x if x < y else y


def min_sequence(sequence):
    result = sequence[0]
    for i in sequence[1:]:
        result = _min(result,i)
    return result


print(min_sequence(l))

_add = lambda a,b: a+b

_max = lambda x, y: x if x > y else y



def add_sequence(sequence):
    result = sequence[0]
    for i in sequence[1:]:
        result = _add(result,i)
    return result


print(add_sequence(l))

def _reduce(fn,sequence):
    result = sequence[0]
    for i in sequence[1:]:
        result = fn(result,i)
    return result

print(_reduce(_min, l))
print(_reduce(_max, l))

from functools import reduce

print(reduce(_add, l))
print(reduce(_max,l))
print(reduce(_min,{10,2,3,4,5}))
print(min(l))
print(min({1,3,4,5,0}))
print(sum({1,2,3,4,0,10}))

# and / or
s = {True, 1, 0, None}

print(all(s))
print(any(s))

s = {True, 1, 's'}
print(all(s))
print(bool(True) and bool(1) and bool('s'))

# any
print(any(s))
s3 = {False, 0, '', None}
print(any(s3))
print(all(s3))

s3 = {False, 0, '', None,1}
print(reduce(lambda a, b: bool(a) and bool(b), s3))
print(reduce(lambda a, b: bool(a) or bool(b), s3))

s4 = {False, 0, '', None,1}
print(reduce(lambda a, b: bool(a) and bool(b), s4))
print(reduce(lambda a, b: bool(a) or bool(b), s4))


# produce

l = [1,2,3,4]
print(reduce(lambda a,b: a*b, l))
# n! =
print(list(range(1,5+1)))

print(reduce(lambda a, b: a*b, range(1,5+1)))

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

def fact(n):
    return 1 if n < 2 else n*fact(n-1)

print(fact(5))

# Initializer

def _reduce(fn,sequence, initial):
    result = initial
    for i in sequence:
        result = fn(result,i)
    return result

print(l)

print(_reduce(lambda a,b: a+b, l,100))

print(_reduce(lambda a,b: a+b, {1,2,3,4},0))