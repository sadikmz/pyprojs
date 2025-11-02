# range

r = range(10)

for i in iter(r):
    print(i)


# zip function returns iterator
z = zip([1,2,3],'abc')
# for i in z:
#     print(i)

for i,k in z:
    print('here0')
    print(i,k)


for i,k in z:
    print('here1')
    print(k,i)


print('__iter__' in dir(z))
print('__next__' in dir(z))

# open function returns iterator

f = open('cars.csv')
print(next(f))
print(next(f))
print(next(f))
print(f.__next__())
print(f.readline())
print(f.seek(1))
f.close()
with open('cars.csv') as f:
    for row in f:
        print(row, end='')

with open('cars.csv') as f:
    print(type(f))
    print('__iter__' in dir(f))
    print('__next__' in dir(f))

with open('cars.csv') as f:
    print(iter(f) is f)

l = [1,2,3]
# print(iter(l) is l)

# with open('cars.csv') as f:
#     l = f.readlines()
#     print(l)

origins = set()
with open('cars.csv') as f:
    rows = f.readlines()

for row in rows:
    origin = row.strip('\n').split(';')[-1]
    origins.add(origin)
# print(origins)

del origins

origins = set()

with open('cars.csv') as f:
    next(f)
    next(f)
    for row in f:
        origin = row.strip('\n').split(';')[-1]
        origins.add(origin)

# print(origins)

# Enumerate function is also a lazy iterator

e = enumerate('Python Rocks!')
print(iter(e) is e)
print('__next__' in dir(e))

print(list(e))
print(list(e))

# dictionary - iterables

d = {'a':1, 'b':2, 'c':3}

keys = d.keys()
print(iter(keys) is keys)
print('__iter__' in dir(keys))
print('__next__' in dir(keys))

# values and iterms