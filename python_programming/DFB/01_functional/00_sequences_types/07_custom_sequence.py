# using __getitem__ method
my_list = [1, 2, 3,4,5,6]
index = 0
while True:
    try:
        item = my_list.__getitem__(index)
    except IndexError:
        break
    print(item ** 2)
    index += 1

for item in my_list:
    print(item **2)

print([item ** 2 for item in my_list])

# using __len__
print(my_list.__len__())


# Creating immutable sequences types
my_list = [1, 2, 3,4,5,6]
len(my_list)
my_list.__len__()

print(my_list[::-1])
print(my_list.__getitem__(slice(None,None,-1)))

for item in my_list:
    print(item ** 2)

index = 0

while True:
    try:
        item = my_list.__getitem__(index)
    except IndexError:
        break
    print(item ** 2)
    index += 1


class Silly:
    def __init__(self, n):
        self.n = n

    # def __len__(self):
    #     print('Called __len__')
    #     return self.n

    def __getitem__(self, value):
        # print(f'Your requested item at {value}')
        if value < 0 or value >= self.n:
            raise IndexError
        else:
            return 'This is a silly element'

silly = Silly(10)

# print(len(silly))

# print(silly.__getstate__(100))
# print(silly.__getstate__(100))
for item in silly:
    print(item)


#
class Silly:
    def __init__(self, n):
        self.n = n

    # def __len__(self):
    #     print('Called __len__')
    #     return self.n

    def __getitem__(self, value):
        print(type(value))
        print(f'Your requested item at {value}')
        return 'This is a silly element'

silly = Silly(10)
print(silly[0:5:2])


# Fibnaci sequence

# def fib(n):
#     if n < 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# using lru caching

from functools import lru_cache

@lru_cache(2*10)
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# print(fib(1000))

# create fib class


class Fib:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0 or s >= self.n:
                raise IndexError
            else:
                return Fib._fib(s)

    @staticmethod
    @lru_cache(2 * 10)
    def _fib(n):
        if n < 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)


f = Fib(8)
print(f[0])
print(f[1])
print(f[2])
print(f[3])
# print(f[7])
print(list(f))
print(list(f))

# handle negative indices


class Fib:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0:
                s = self.n + s
            if s < 0 or s >= self.n:
                raise IndexError
            else:
                return Fib._fib(s)

    @staticmethod
    @lru_cache(2 * 10)
    def _fib(n):
        if n < 2:
            return 1
        else:
            return Fib._fib(n - 1) + Fib._fib(n - 2)

fib = Fib(10)
print(list(fib))
print(fib[-2])
print(fib[1:4])


#
class Fib:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0:
                s = self.n + s
            if s < 0 or s >= self.n:
                raise IndexError
            else:
                return Fib._fib(s)
        else:
            range_tuple = s.indices(self.n)
            print(range_tuple)
    @staticmethod
    @lru_cache(2 * 10)
    def _fib(n):
        if n < 2:
            return 1
        else:
            return Fib._fib(n - 1) + Fib._fib(n - 2)

fib = Fib(10)
print(list(fib))
# print(fib[-2])
fib[0:4]
fib[-1:]
fib[-1:-4:-1]
# print(list(range(*slice(start, stop, step).indices(length))))

# print(type(fib[-1:-4:-1]))

# modify the code to generate range

class Fib:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0:
                s = self.n + s
            if s < 0 or s >= self.n:
                raise IndexError
            else:
                return Fib._fib(s)
        else:
            # range_tuple = s.indices(self.n)
            start, stop, step = s.indices(self.n)
            rng = range(start, stop, step)
            return [Fib._fib(i) for i in rng]
            # rng = range(*s.indices(self.n))
            # print(range_tuple)
    @staticmethod
    @lru_cache(2 * 10)
    def _fib(n):
        if n < 2:
            return 1
        else:
            return Fib._fib(n - 1) + Fib._fib(n - 2)

fib = Fib(10)
print(fib[0:4])
print(fib[-1:-4:-1])