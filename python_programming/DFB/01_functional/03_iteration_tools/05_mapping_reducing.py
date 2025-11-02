maps = map(lambda x: x ** 2, range(4))
print(type(maps))
print(iter(maps) is maps)

print('__next__' in dir(maps))

print(list(maps))

def add(t):
    return t[0] + t[1]

print(list(map(add,[(0,0),(1,1), range(2,4)])))

def add(x,y):
    return x + y

t = (2,3)

# print(add(*t))

# using list comprehension
print([add(*t) for t in [(0,0),(1,1), range(2,4)]])

# using starmap from itertools

from itertools import starmap

print(list(starmap(add,[(0,0),(1,1), range(2,4)])))

# Accumulation

print(sum([10,20,30]))
print(sum(range(10,40,10)))

from functools import reduce

print(reduce(lambda x, y: x*y,[1,2,3,4]))
# we can specify start value
print(reduce(lambda x,y: x*y,[1,2,3,4], 10))

# write a custom function that will result sum as well as the intermediate results

def sum_(iterable):
    it = iter(iterable)
    acc = next(it)
    yield acc
    for item in it:
        acc += item
        yield acc

for item in sum_([10,20,30]):
    # print('---result----')
    print(item)

#

def running_reduce(fn,iterable,start=None):
    it = iter(iterable)
    if start is None:
        acc = next(it)
    else:
        acc = start
    yield acc

    for item in it:
        acc = fn(acc, item)
        yield acc

print(list(running_reduce(lambda x,y: x+y,[10,20,30])))

import operator

print(list(running_reduce(operator.add, [10,20,30])))
print(list(running_reduce(operator.mul, [1,2,3,4], 10))) # can take start value

from itertools import accumulate

print(list(accumulate([10,20,30])))
print(list(accumulate([10,20,30], operator.mul)))
# accumulate does not take start value but can be worked out with chain
from itertools import chain

# chain([10], [1,2,3,4])
print(list(accumulate(chain([10], [1,2,3,4]), operator.mul)))