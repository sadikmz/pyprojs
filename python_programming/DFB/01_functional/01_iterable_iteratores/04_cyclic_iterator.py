# creating our own infinite iterator
class CyclicIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self


    def __next__(self):
        result = self.lst[self.index % len(self.lst)]
        self.index += 1
        return result

iter_cycle = CyclicIterator('NSWE')

for __ in range(12):
    print(next(iter_cycle))

# It doesn't work with for-loop.
# To make it work with for-loop: or make it a finate iterable

class CyclicIterator:
    def __init__(self, lst, length):
        self.lst = lst
        self.index = 0
        self.length = length

    def __iter__(self):
        return self


    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        else:
            result = self.lst[self.index % len(self.lst)]
            self.index += 1
            return result

iter_cycle = CyclicIterator('NSWE',16)
print('----finite iterator----')
for item in iter_cycle:
    print(item)

# using it for any sequence type

# creating our own infinite iterator
class CyclicIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self


    def __next__(self):
        result = self.lst[self.index % len(self.lst)]
        self.index += 1
        return result

iter_cycle = CyclicIterator([10,20,35])

for __ in range(10):
    print(next(iter_cycle))

#
numbers = range(10)

iter_cycle = CyclicIterator('NSWE')

print(list(zip(list(numbers), iter_cycle)))

# for item in iter_cycle:
#     print(item)
# for __ in range(10):
#     print(next(iter_cycle))

# without using the zip funciton

n = 10

iter_cycle = CyclicIterator('NSWE')
for i in range(1,n+1):
    direction = next(iter_cycle)
    print(f'{i}{direction}')

# rework it as a list

n = 10
iter_cycle = CyclicIterator('NSWE')
items = [str(i) + next(iter_cycle) for i in range(1,n+1)]
print(items)

# two ways of using zip

n = 10

iter_cycle = CyclicIterator('NSWE')

items = [str(number) + direction
 for number, direction in zip(range(1,n+1),iter_cycle)]

print('----items-----')
print(items)
print(list(zip(range(1,11), 'NSEW'*30)))
# using repetition
items = [str(number) + direction
         for number, direction in zip(range(1,n+1),'NSWE' * (n//4 + 1))]
print(n)
print(items)

# using pythons built-in method

import  itertools

n  = 10
iter_cycle = CyclicIterator('NSWE')

items=[f'{i}{next(iter_cycle)}' for i in range(1,n+1)]
print(items)

items=['{0}{1}'.format(i, next(iter_cycle)) for i in range(1,n+1)]
print(items)

print('----itertools cyle-----')
n = 10
iter_cycle = itertools.cycle('NSWE')
items=['{0}{1}'.format(i, next(iter_cycle)) for i in range(1,n+1)]
print(items)

s = {100,'a','X','x', 200}
print(list(s))
print(list(s))

# ''''''''

class CyclicIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
        # iterator = iter(self.iterable)
            item = next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            item = next(self.iterator)
        finally:
            return item


iter_cycle = CyclicIterator('abcd')

#
for i in range(10):
    print(i, next(iter_cycle))