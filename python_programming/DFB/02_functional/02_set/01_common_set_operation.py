s = {1,2,3}

print(len(s))
print(1 in s)
print(4 not in s)

# timing look up
from timeit import timeit

n = 100_000
s = {i for i in range(n)}
l = [i for i in range(n)]
d = {i:None for i in range(n)}

# number = 30_000
# search = 99_999
# t_list = timeit(f'{search} in l', globals=globals(), number=number)
# t_set = timeit(f'{search} in s', globals=globals(), number=number)
# t_d = timeit(f'{search} in d', globals=globals(), number=number)
# print(t_list)
# print(t_d)
# print(t_set)


# number = 30_000
# search = -1
# t_l = timeit(f'{search} not in l', globals=globals(), number=number)
# t_s = timeit(f'{search} not in s', globals=globals(), number=number)
# t_d = timeit(f'{search} not in d', globals=globals(), number=number)
# print(t_list)
# print(t_d)
# print(t_set)

print(l.__sizeof__())
print(d.__sizeof__())
print(s.__sizeof__())

#
s = set()
d = dict()
l = list()
print(d.__sizeof__())
print(s.__sizeof__())
print(l.__sizeof__())

s.add(10)
d[10]=None
l.append(10)

print(d.__sizeof__())
print(s.__sizeof__())
print(l.__sizeof__())

# adding element to set
s = {30, 20, 10}

s.add(11)
print(s)

# remove elements
s.remove(11)
print(s)
# s.remove(3)
s.discard(3)
print(s)

# s.pop()
# print(s)
# s.pop()
# print(s)
# s.pop()
# print(s)
# s.pop()
# print(s)

# s  = set('Python')
# while len(s) > 0:
#     e = s.pop()
#     print(e)

s  = set('Python')
while True:
    try:
        e = s.pop()
        print(e)
    except KeyError:
        break

# clearn elements of set
s  = set('Python')
s.clear()
print(s)