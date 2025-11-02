
d = {'a': 1, 'b': 2}
keys = d.keys()
values = d.values()
items = d.items()

print(id(keys), id(values), id(items))

print(keys)
print(values)
print(items)

d['z'] = 10
print(id(keys), id(values), id(items))

print(keys)
print(values)
print(items)

d = dict(zip('abc', range(1,3)))
print(d)

# for k, v in d.items():
#     print(k, v)
#     del d[k]
# print(d)

# for k, v in d.items():
#     print(k, v)
#     d['z'] = 100

d = dict(zip('abc', range(1,4)))
for k, v in d.items():
    print(k, v)
    d[k] = 100
print(d)

d = dict(zip('abc', range(1,4)))
for k, v in d.items():
    print(k, v)
    d['c'] = 1000
    # print(k, v)


# print(d)

# d = dict(zip('abc', range(1,4)))
# for k in d.keys():
#     print(k)
#     del d['c']

d = dict(zip('abc', range(1,4)))
# for v in d.values():
#     print(v)
#     del d['c']
    # print(k, v)

# d = dict(zip('abc', range(1,4)))
# for key in d.keys():
#     d[key] = 100
# print(d)

# Iteration of keys: using keys view or over the dictionary directly

d = dict.fromkeys('python',0)
print(d)
for k in d:
    print(k)

d_iter = iter(d)
for k in d_iter:
    print(k)

d_iter = iter(d)
print(next(d_iter))
print(next(d_iter))
print(next(d_iter))
print(next(d_iter))
print(next(d_iter))
print(next(d_iter))
# print(list(next(d_iter)))

# modifying dictionary as we iterating over dictionary
# d = {'a': 1, 'b': 2, 'c': 3}
# for k, v in d.items():
#     print(k, v)
#     del d[k]
#Option1: make static list of key/values
d = {'a': 1, 'b': 2, 'c': 3}
keys = list(d.keys())
print(keys)
for k in keys:
    v = d[k]
    print(k, v**2)
    del d[k]
print(d)

#Options2: using pop
d = {'a': 1, 'b': 2, 'c': 3}

for k in list(d.keys()):
    v = d.pop(k)
    print(k, v**3)
    # del d[k]
print(d)

#Option3: using popitem

d = {'a': 1, 'b': 2, 'c': 3}
for _ in range(len(d)):
    k, v = d.popitem()
    print(k, v**2)
print(d)

#Option4: Using while loop

d = {'a': 1, 'b': 2, 'c': 3}
while len(d) > 0:
    k, v = d.popitem()
    print(k, v**2)
print(d)

#Option5: Using while loop and catch KeyError
d = {'a': 1, 'b': 2, 'c': 3}

while True:
    try:
        k, v = d.popitem()
    except KeyError:
        break
    else:
        print(k, v**2)

print(d)

# Option6
d = {'a': 1, 'b': 2, 'c': 3}

for k, v in d.items():
    print(k, v)
    del d[k]
    d[k*3] = v ** 2

print(d)