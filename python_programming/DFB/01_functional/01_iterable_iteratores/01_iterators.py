# The iterator protocol: a protocol is simply a fancy way of saying that our class is going to implement certain functionality that python can count on
# The iterator protocol - the class needs to implement two methods
# __iter__: ---> This method should return the object (class instance) itself
# __next__: This method is responsible for handing back the next element from the collection and raising the StopIteration exception when all elements have been handed out.

# square class

class Square:
    def __init__(self, length):
        self.length = length
        self.i = 0

    # def __len__(self):
    #     return self.length

    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

sq = Square(3)
# next(sq)
# next(sq)
# next(sq)
# next(sq)

# for item in sq:
#     print(item)

# print(item)
# print(item)
# print(item)
# print(item)

# adding __iter__ method

class Square:
    def __init__(self, length):
        self.length = length
        self.i = 0

    # def __len__(self):
    #     return self.length

    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result
    def __iter__(self):
        return self
#
sq = Square(5)
# # next(sq)
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
# print(next(sq))

#
sq = Square(5)

print('new items')

for item in sq:
    print(item)
#
# del item
print(item)
# print(item)
# print(item)
# print(item)

# with list comprehension
sq = Square(5)

l  = [item for item in sq]
print(l)
l  = [item for item in sq]
print(l)
print('item' in globals())

# Using enumerate funciton

l = ['a','b','c']
print(list(enumerate(l)))

sq = Square(5)
print(list(enumerate(sq)))

sq = Square(5)
print(sorted(sq, reverse=True))

sq = Square(5)

while True:
    try:
        item = next(sq)
        print(item)
    except StopIteration:
        break


#

class Square:
    def __init__(self, length):
        self.length = length
        self.i = 0

    # def __len__(self):
    #     return self.length

    def __next__(self):
        print('__next__ called')
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result
    def __iter__(self):
        print('__iter__ called')
        return self


sq = Square(5)

while True:
    try:
        item = next(sq)
        print(item)
    except StopIteration:
        break

sq = Square(5)

for item in sq:
    print(item)


sq = Square(5)

l = [item for item in sq if item % 2 == 0]
print(l)


sq = Square(5)
sq_iterator = iter(sq)
print(id(sq_iterator), id(sq))

while True:
    try:
        item = next(sq)
        print(item)
    except StopIteration:
        break
