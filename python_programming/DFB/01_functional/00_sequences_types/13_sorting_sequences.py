# the ASCII character code for characters / alphabets
# print(ord('A'))
# print(ord('a'))
# print(ord('x'))

# sorted

l = [3,0,2,4,5,1]
print(sorted(l))

# sort dictionary by values

d = {'a': 100, 'b': 50, 'c': 10, 'd': 400, 'e': 15}
print(sorted(d.items()))
print(sorted(d, key = lambda k: d[k]))

# tuple
t = 'this','parrot','is','a','late','bird'
print(sorted(t))

# sorting based on the length of the string
def sort_key(s):
    return len(s)

print(sorted(t, key = sort_key))

t = 'aaaa','bbbb','cccc','dddd','eeee'

print(sorted(t, key = lambda s: len(s)))

t = 'aaaa','bbbb', 'e'*4, 'dddd','c'*4
print(sorted(t, key = lambda s: len(s)))

# sorted a tuple of complex number based on the distance from origin

t = 0,10+10j, 3-3j, 4+4j, 5-2j

print(sorted(t, key = abs))
print(sorted(t, key = abs, reverse = True))
print(sorted(t, key = abs, reverse = False))
print(sorted(t, key = lambda s: s.imag))
print(sorted(t, key = lambda s: s.real))
t = 'this','parrot','is','a','late','bird'

print(sorted(t, key = lambda s: -len(s)))

# sort function: it is in-place sorting and it mutates the objsect
# l = ['this','bird', 'is','a','late','parrot']
l = 'this bird is a late parrot'.split(' ')
print(l)
l.sort()
print(l)

# asses the efficiency of sorted vs srt

from timeit import timeit
import random

random.seed(0)
n=1_000_000
n=10
l = [random.randint(0,100) for n in range(n)]
print(l[0:10])

print(timeit(stmt='sorted(l)', globals=globals(), number=1))

# in-place sort
print(timeit(stmt='l.sort()', globals=globals(), number=1))

# print(l[5_000_000:5_000_010])
# print(timeit(stmt='sorted(l)', globals=globals(), number=1))
#
# # in-place sort
# print(timeit(stmt='l.sort()', globals=globals(), number=1))

class MyClass:
    def __init__(self, name, val):
        self.name = name
        self.val = val

    def __repr__(self):
        return f'MyClass({self.name}, {self.val})'

    def __lt__(self, other):
        print('calling __lt__')
        return self.val < other.val

    def __gt__(self, other):
        print('calling __gt__')
        return self.val > other.val

c1 = MyClass('c1', 20)
c2 = MyClass('c2', 10)
c3 = MyClass('c3', 20)
c4 = MyClass('c4', 10)

print(c1 < c2)
print(sorted([c1, c2, c3, c4]))

l = [c4, c2, c3, c1]

print(sorted(l, key = lambda c: c.name))

# redefine

c1 = MyClass('c1', 20)
c2 = MyClass('c2', 10)
c3 = MyClass('c3', 20)
c4 = MyClass('c4', 10)

l = [c4, c2, c3, c1]
print(sorted(l, key = lambda c: c.name))
