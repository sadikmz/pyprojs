i=100
def counter():
    i = 0

    def inc():
        nonlocal i
        i += 1
        return i
    return inc

cnt = counter()

print(cnt())
print(cnt())
print(cnt())

class CounterIterator:
    def __init__(self, counter_callable):
        self.counter_callable = counter_callable

    def __iter__(self):
        return self

    def __next__(self):
        return self.counter_callable()

cnt = counter()

cnt_iter = CounterIterator(cnt)

for i in range(5):
    print(next(cnt_iter))

# This is an infinite iteration and add stop iteration

class CounterIterator:
    def __init__(self, counter_callable, sentinel_value):
        self.counter_callable = counter_callable
        self.sentinel_value = sentinel_value

    def __iter__(self):
        return self

    def __next__(self):
        result = self.counter_callable()
        if result == self.sentinel_value:
            raise StopIteration
        return result

# cnt = counter()
# print(type(cnt))
#
# cnt_iter = CounterIterator(cnt,10)
#
# # for i in range(4):
# #     print(next(cnt_iter))
#
# for i in cnt_iter:
#     print(i)
#
# print(next(cnt_iter))
# print(next(cnt_iter))
# print(next(cnt_iter))
# print(next(cnt_iter))


class CounterIterator:
    def __init__(self, counter_callable, sentinel_value):
        self.counter_callable = counter_callable
        self.sentinel_value = sentinel_value
        self.consumed = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.consumed:
            raise StopIteration
        else:
            result = self.counter_callable()
            if result == self.sentinel_value:
                self.consumed = True
                raise StopIteration
            else:
                return result

cnt_iter = CounterIterator(cnt,10)

# for i in cnt_iter:
#     print(i)
#
# print(next(cnt_iter))
# print(next(cnt_iter))
# print(next(cnt_iter))
# print(next(cnt_iter))

# refine

class CallableIterator:
    def __init__(self, callable_, sentinel_value):
        self.callable_ = callable_
        self.sentinel_value = sentinel_value
        self.consumed = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.consumed:
            raise StopIteration
        else:
            result = self.callable_()
            if result == self.sentinel_value:
                self.consumed = True
                raise StopIteration
            else:
                return result

cnt_iter = CallableIterator(cnt,10)

# for i in cnt_iter:
#     print(i)

# print(next(cnt_iter))

# The second form of the iter fucntion

help(iter)

cnt = counter()
cnt_iter = iter(cnt, 5)
# for c in cnt_iter:
#     print(c)
# print(next(cnt_iter)
#
#
import random
random.seed(0)

for i in range(10):
    print(i, random.randint(0,10))

random_iter = iter(lambda : random.randint(0,10),4)

random.seed(0)
for num in random_iter:
    print(num)


def countdonw(start=10):
    def run():
        nonlocal start
        start -=1
        return start
    return run

takeoff = countdonw(10)

for _ in range(15):
    print(takeoff())

takeoff = countdonw(10)

takeoff_iter = iter(takeoff, -1)

for _ in range(15):
    print(next(takeoff_iter))


for num in takeoff_iter:
    print(num)
