# Iteration
import itertools

from numpy import iterable

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0

while i < len(my_list):
    v = my_list[i]
    print(v)
    i += 1

# use range instead

for i in range(len(my_list)):
    v = my_list[i]
    print(v)

# list comprehension

print([my_list[item] for item in range(len(my_list))])

# other way

for v in my_list:
    print(v)

# template

# for name in iterable:
#     statements


# for dictionaries

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for v in d.keys():
    print(v)

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)

for k, v in d.items():
    print(v, k)


# for files

# with open("input_file.txt") as f:
#     for line in f:
#         print(line)
# import os
# for root, dirs, files in os.walk("/Users/sadik/Documents"):
#     for file in files:
#         print(file)


# for num in itertools.count():
#     Once for each integer ... Infinte
#     print(num)


# from itertools import chain, repeat, cycle
#
# seq = chain(repeat(17,3), cycle(range(4)))
# for num in seq:
#     print(num)


# other

# new_list = list(iterable)

# result = [f(x) for x in new_list]
# total = sum(iterable)
# smallest = min(iterable)
# largest = max(iterable)
# comibned = "".join(iterable)

# using the iterator integers

# for i in range(len(my_list)):
#     v = my_list[i]
#     print(i,v)

# using enumerate

print(my_list)
for i, v in enumerate(my_list):
    print(i, v)

print(my_list)
for i, v in enumerate(my_list, start=1):
    print(i, v)
print(dir(enumerate))

i = 0
for v in my_list:
    print(i, v)
    i += 1


names = ['Eiffel Tower', 'Empire State', 'Sears Tower']
heights = [324, 381, 442]

for i in range(len(names)):
    name = names[i]
    height = heights[i]
    print("%s: %s meters" %(name, height))

# Using zip
for name, height in zip(names, heights):
    print("%s: %s meters" %(name, height))

# dict() accepts a stream of pairs

print(dict(zip(names, heights)))

tall_building = dict(zip(names, heights))
print(max(tall_building.values()))
print(max(tall_building.items(), key=lambda x: x[1]))
# print(max(tall_building.items(), key=lambda x: x[0]))
# print(max(tall_building.items(), key=lambda x: x[2]))
print(max(tall_building, key = tall_building.get))

# customizing iteration

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
for n in nums:
    if n % 2 == 0:
        do_something(n)

# other way
# Define a function called even

def evens(stream):
    them = []
    for n in stream:
        if n % 2 == 0:
            them.append(n)
    return them

for n in evens(nums):
    do_something(n)

# Using generator

def evens(stream):
    for n in stream:
        if n % 2 == 0:
            yield n

for n in evens(nums):
    do_somthing(n)

# abstracting your iteration

f = open("my_config.txt")
for line in f:
    line  = line.strip()
    if line.startswith("#"):
        # A comment line, skip it
        continue
    if not line:
        # A blank line, skip it
        continue
    # An interesitng line
    do_something(line)


# Using generator

def interesting_line(f):
    for line in f:
        line = line.strip()
        if line.startswith("#"):
            continue
        if not line:
            continue
        yield line

# once we got out generator we can use it

with open("my_config.txt") as f:
    for lien in interesting_line(f):
        do_something(line)

with open("my_config.txt") as f2:
    for lien in interesting_line(f2):
        do_something_else(line)

