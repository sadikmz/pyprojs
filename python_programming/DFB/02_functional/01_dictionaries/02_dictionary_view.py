# views: keys, values and items

s1 = {1, 2, 3,4,5}
s2 = {4, 5, 6}
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s2 - s1)
print(s1 ^ s2) # not shared
print(s2 ^ s1)

# look views

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = dict(zip('cde', [30,4,5]))
print(d1, d1)
# print(d1, d2)

for key in d1:
    print(key)
    print(d1[key])
    print(key, d1[key])

for key in d1.keys():
    print(key)

for value in d1.values():
    print(value)
    print(value)

print(list(d1.keys()))
print(list(d1.values()))

for item in d1.items():
    print(item)

for k, v in d1.items():
    print(k, v)

# iterables: when iterated and reached the end, it will grab the start and get restarted - they don't get exhausted
# iterators: get exhausted once it reaches the end

keys = d1.keys()
print(list(keys))

# views are dynamic
d1['d'] = 0
print(d1)

# order do not change
print(list(d1.keys()))
print(list(d1.values()))
print(list(d1.items()))

print(list(d1.items())== list(zip(d1.keys(), d1.values())))

# set properites
print(d1)
print(d2)
del d1['d']
print(d1)

print(type(d1.keys()))
# print(type(d1.values()))
print(type(d2.keys()))

union = set(d1.keys()) | set(d2.keys())
print(union)
print(type(union))

# intersection
intersection = set(d1.keys()) & set(d2.keys())
print(intersection)
print(type(intersection))

# for items
print(d1.items() | d2.items())
d2['c']=3
print(d1)
print(d2)
print(d1.items() | d2.items())

# checking values hashability
print(d1.values(), d2.values())
# print(d1.values() | d2.values())

# operand

d3 = {'a': [1,2], 'b': [3,4]}
d4 = {'b': [30, 40], 'c': [5,6]}

print(d3.items())
# print(hash(('a',[1,2])))
print(hash(('a',1)))

# let say we have two dictionaries and we want to create a new dictionary that contains all the items
# in both dictionaries and we want the value / the associated value to be a tuple containing the vaules from both dictionary

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 30, 'd': 4}

k1 = d1.keys()
k2 = d2.keys()

print(k1 & k2)

new_dict = {}
for key in d1.keys() & d2.keys():
    new_dict[key] = d1[key], d2[key]
print(new_dict)

new_dict = {key: (d1[key], d2[key]) for key in d1.keys() & d2.keys()}
print(new_dict)

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 30, 'd': 4}

new_dict = {}
for key in d1.keys() & d2.keys():
    new_dict[key] = d2[key]
print(new_dict)

new_dict = {key: d2[key] for key in d1.keys() & d2.keys()}
print(new_dict)


# semetric difference
d1 = {'a': 1, 'b': 2, 'c': 3, 'd':4}
d2 = {'a': 10, 'b': 20, 'c': 30, 'e': 5}
print(d2.keys())
print(d1.keys() ^ d2.keys())

new_dict = {}
for key in d1.keys() ^ d2.keys():
    if key in d1.keys():
        new_dict[key] = d1[key]
    elif key in d2.keys():
        new_dict[key] = d2[key]
print(new_dict)


# new_dict = {key: (d1[key],  for key in d1.keys() ^ d2.keys()}
# print(new_dict)
new_dict = {}
for key in d1.keys() ^ d2.keys():
    new_dict[key] = d1.get(key) or d2.get(key)
print(new_dict)

union = set(d1.keys()) | set(d2.keys())
intersection = set(d1.keys()) & set(d2.keys())
sem_dif = union - intersection
print(sem_dif)

for key in sem_dif:
    new_dict[key] = d1.get(key) or d2.get(key)
print(new_dict)
new_dict = {key: d1.get(key) or d2.get(key) for key in sem_dif}
print(new_dict)

new_dict = {key: d1.get(key) or d2.get(key) for key in d1.keys() ^ d2.keys()}
print(new_dict)