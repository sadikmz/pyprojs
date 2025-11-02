# A generic sequence iterator

# class SeqIterator:
#     def __init__(self, seq):
#         self.seq = seq
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         try:
#             item = self.seq[self.index]
#             self.index += 1
#             return item
#         except IndexError:
#             raise StopIteration

class Squares:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, i):
        if i >= self.n:
            raise IndexError
        else:
            return i ** 2

# sq = Squares(5)

# for i in sq:
#     print(i)

# sq_iter = iter(sq)
# print(type(sq_iter))
#
# print('__next__' in dir(sq_iter))
# print(next(sq_iter))
# print(next(sq_iter))

#
class Squares:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, i):
        if i >= self.n:
            raise IndexError
        else:
            return i ** 2

# sq_iter = iter(Squares(5))


class Squares:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, i):
        if i >= self.n:
            raise IndexError
        else:
            return i ** 2

class SquaresIterator:
    def __init__(self, squares):
        self._squares = squares
        self._index = 0

    # iterator protocol
    def __iter__(self):
        return self

    # define next method

    def __next__(self):
        if self._index >= len(self._squares):
            raise StopIteration
        else:
            result = self._squares[self._index]
            self._index += 1
            return result

sq = Squares(5)
#
# sq_iter = SquaresIterator(sq)
# # print(sq_iter)
# print(next(sq_iter))
# print(next(sq_iter))
# print(next(sq_iter))
# print(next(sq_iter))
# print(next(sq_iter))
# print(next(sq_iter))


class SequenceIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    # iterator protocol
    def __iter__(self):
        return self

    # define next method

    def __next__(self):
        if self._index >= len(self._sequence):
            raise StopIteration
        else:
            result = self._sequence[self._index]
            self._index += 1
            return result

# how to we test whether the object is iterable or not.
# Two ways:
# it either have the getitem method or
# it implement the iterable or iterator procol

# how do we figure out
# if the __iter__ is the implemented in that class that returns itself
# does it have the __getitem__ method

class SimpleIter:
    def __init__(self):
        pass

    def __iter__(self):
        return 'Nope'

s = SimpleIter()

print('__iter__' in dir(s))
# iter(s) : it doesn't work
#

# Two different ways of exception handling
# 1: Look before you leave - ask permission first
def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

print(is_iterable(s))
print(is_iterable(sq))


obj=100
if is_iterable(obj):
    for item in obj:
        print(item)
else:
    print('Error: Object is not iterable')

# obj=100
# for i in obj:
#     print(i)

# 2: Ask forgiveness later:
# it's easier to ask forgiveness than ask permission
obj = 100
try:
    for i in obj:
        print(i)
except TypeError:
    print('Error: Object is not iterable')
