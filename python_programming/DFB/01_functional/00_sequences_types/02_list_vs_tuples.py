# Constant folding: the process of recognizing and evaluating constant expression at compile time rather than computing them at runn tim.

from dis import dis

print(dis(compile('(1,2,3,"a")', 'string', 'eval')))
print(dis(compile('[0,1,2,3,"a","b"]', 'string', 'eval')))
print(dis(compile('(0,1,2,3,["a","b"])', 'string', 'eval')))


from timeit import timeit

print(timeit("(1,2,3,4,5,6,7,8,9)",number=10_000_000))
print(timeit("[1,2,3,4,5,6,7,8,9]",number=10_000_000))

def fn1():
    pass

dis(compile('(fn1(), 10, 20)', 'string', 'eval'))

print(dis(compile('(0,1,2,3,["a","b"])', 'string', 'eval')))

print(timeit("([1,2],10,20)", number=10_000_000))
print(timeit("(1,2,10,20)", number=10_000_000))

l1 = [1,2,3,4,5,6,7,8,9]
t1 = (1,2,3,4,5,6,7,8,9)

print(id(l1))
print(id(t1))

l2 = list(l1)
print(id(l2))

t2 = tuple(t1)
print(id(t2))

print(t2 is t1)
print(t2 == t1)


print(timeit('tuple((1,2,3,4,5))', number=5_000_000))
print(timeit('list((1,2,3,4,5))', number=5_000_000))

# Storage efficiency

import sys

# t = tuple()

# prev = sys.getsizeof(t)

# for i in range(10):
#     c = tuple(range(i+1))
#     size_c = sys.getsizeof(c)
#     delta, prev = size_c - prev, size_c
#     print(f'{i+1} items: {size_c}, {delta}')


l = list()
prev = sys.getsizeof(l)
for i in range(10):
    c = list(range(i+1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} items: {size_c}, {delta}')


c = list()
prev = sys.getsizeof(c)
print(f'0 items: {prev}')

for i in range(255):
    c.append(i)
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} items: {size_c}, {delta}')


# Retrieving element between list and tuple

t = tuple(range(100_000))
l = list(t)

print(timeit('t[99_999]', globals=globals(), number=10_000_000))
print(timeit('l[99_999]', globals=globals(), number=10_000_000))