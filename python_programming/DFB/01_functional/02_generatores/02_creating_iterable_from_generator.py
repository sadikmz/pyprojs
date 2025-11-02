# create a simpel generator function
def squares_gen(n):
    for i in range(n):
        yield (i**2)

sq = squares_gen(5)

for num in sq:
    print(num)

print(list(sq))

class Squares:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return squares_gen(self.n)


# sq = Squares(5)
# for num in sq:
#     print(num)
#
# print(list(sq))



class Squares:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return Squares.squares_gen(self.n)

    @staticmethod
    def squares_gen(n):
        for i in range(n):
            yield (i**2)

# sq = Squares(5)
# for num in sq:
#     print(num)
# #
# print(list(sq))

# a bug that can happen when we use iterators with other iterators and generators with other iterators

def squares(n):
    for i in range(n):
        yield (i**2)

sq = squares(5)
enum_sq = enumerate(sq)

print(list(enum_sq))
print(list(enum_sq))

# l = [1,2,3]
# enum = enumerate(l)
# print(list(enum))
# print(list(enum))


# print(next(sq))
# print(next(sq))

# for num in sq:
#     print(num)


sq = squares(5)
next(sq)
next(sq)

# the remaining elements
print(list(enumerate(sq)))

