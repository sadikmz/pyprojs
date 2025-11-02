# chaining: concatenate multiple iteration / iterables together
from numpy import iterable

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4,8))
l3 = (i**2 for i in range(8,12))

for gen in l1, l2, l3:
    for item in gen:
        print(item)

# create a custom chain iterable function

def chain_iterable(*iterables):
    for iterable in iterables:
        yield from iterable

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4,8))
l3 = (i**2 for i in range(8,12))

for iterm in chain_iterable(l1, l2, l3):
    print(iterm)

# using itertools chain
from itertools import chain

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4,8))
l3 = (i**2 for i in range(8,12))

for item in chain(l1, l2, l2):
    print(item)
# You can not do like this

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4,8))
l3 = (i**2 for i in range(8,12))

lists = (l1, l2, l3)

for item in chain(lists):
    print(item)

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4,8))
l3 = (i**2 for i in range(8,12))

lists = (l1, l2, l3)

for item in chain(lists):
    for i in item:
        print(i)
    # print(item)

# let's use unpacking
l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4,8))
l2 = (i**2 for i in range(8,12))

for item in chain(*lists):
    print(item)

# using iterato

def squares():
    print('---yielding first item')
    yield (i ** 2 for i in range(4))
    print('---yielding second item')
    yield (i ** 2 for i in range(4,8))
    print('---yielding third item')
    yield (i ** 2 for i in range(8,12))

# for item in chain(squares()):
#     print(item)

for item in chain(*squares()):
    print(item)

# alternative constructor in chain

c = chain.from_iterable(squares())

for item in c:
    print(item)

# using a custom script
def chain_from_iterable(iterable):
    for item in iterable:
        yield from item

for item in chain_from_iterable(squares()):
    print(item)

# Copying iterator

from itertools import tee

def squares(n):
    for i in range(n):
        yield i**2

gen = squares(10)

print(gen)

# using tee
iters = tee(gen,3)
# print(iters)

# unpack
# for item in iters:
#     for i in item:
#         print(i)
    # print(item)
gen = squares(10)

iter1, iter2, iter3 = iters
print(iter1 is iter2)
print(iter1 is iter3)
print(iter2 is iter3)
print(next(iter1), next(iter1), next(iter1), next(iter1))
print(next(iter2), next(iter2), next(iter2), next(iter2))
print(next(iter3), next(iter3), next(iter3), next(iter3))

# This works for any iterable

l = [1,2,3,4]
lists = tee(l, 2)
print(type(lists))
print(type(lists[0]))
print(list(lists[0]))
print(list(lists[1]))
print(list(lists[0]))