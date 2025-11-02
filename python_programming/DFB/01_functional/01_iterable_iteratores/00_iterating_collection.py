s = {'x','y','a','b','c'}
for i in s:
    print(i)

# print(s[0]
#
# getting the next item in the collection

class Square:
    def __init__(self):
        self.i = 0

    def next_(self):
        result = self.i ** 2
        self.i += 1
        return result

sq = Square()

print(sq.next_())
print(sq.next_())
print(sq.next_())
print(sq.next_())
print(sq.next_())

# How to stop the iteration or say that you reached the iteration of custom sequence

sq = Square()

for i in range(5):
    print(sq.next_())


class Square:
    def __init__(self, length):
        self.length = length
        self.i = 0

    def __len__(self):
        return self.length

    def next_(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

sq = Square(3)
# sq.next_()
# sq.next_()
# sq.next_()
# sq.next_()
# sq.next_()
# sq.next_()

sq = Square(10)
while True:
    try:
        print(sq.next_())
    except StopIteration:
        break
# print(sq.next_())

# python has a built-in method called next that calls __init__


class Square:
    def __init__(self, length):
        self.length = length
        self.i = 0

    def __len__(self):
        return self.length

    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result
sq = Square(3)
# print(next(sq))
# print(next(sq))
# print(next(sq))
# print(next(sq))
# print(next(sq), 'five')
# print(next(sq))

sq = Square(10)
while True:
    try:
        print(next(sq))
    except StopIteration:
        break
# print(next(sq))

# using sequence types which doesn't use indexing
import random

class RandomNumbers:
    def __init__(self, length,*, range_min = 0, range_max = 10):
        self.length = length
        self.range_min = range_min
        self.range_max = range_max
        self.num_requested = 0

    def __len__(self):
        return self.length

    def __next__(self):
        if self.num_requested >= self.length:
            raise StopIteration
        else:
            self.num_requested += 1
            return random.randint(self.range_min, self.range_max)

numbers = RandomNumbers(3)
print(next(numbers))
print(next(numbers))
print(next(numbers))
# print(next(numbers))

numbers = RandomNumbers(3)
print(next(numbers))
print(next(numbers))
print(next(numbers))
# next(numbers)

numbers = RandomNumbers(3)

while True:
    try:
        print(next(numbers))
    except StopIteration:
        break



