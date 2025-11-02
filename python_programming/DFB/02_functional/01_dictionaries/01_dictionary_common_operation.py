# Creating dictionary
d = dict(a=1, b=2, c=3)
print(d)

d= dict(zip('abc', range(1,4)))
print(d)

print(len(d))
# print(d['python'])

print(d.get('python'))

result = d.get('python')
print(result)
print(type(result))

print(d.get('a', 'N/A'))

# example
text = 'Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit amet consectetur adipisci[ng] velit, sed quia non-numquam [do] eius modi tempora inci[di]dunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur?'

counts = dict()
for c in text:
    counts[c] = counts.get(c, 0) + 1
print(counts)

# Refine
counts = dict()
for c in text:
    key = c.lower().strip()
    if key:
        counts[key] = counts.get(key, 0) + 1
print(counts)

# membership testing

d = dict(a=1, b=2, c=3)
print('a' in d)
print('b' in d)
print('c' not in d)

# Removing elements from a dictionary
d = dict.fromkeys('abcd',0)
print(d)
del d['a']
print(d)
# del d['z']
# d.pop('z')

d = dict(a=1, b=2)
print(d.pop('a',100))
print(d)
print(d.pop('z',100))
print(d)

# pop.item method
d = dict({i:i**2 for i in range(1,5)})
print(d)
print(d.popitem())
print(d)
print(d.popitem())
print(d.popitem())
print(d.popitem())
# print(d.popitem())

# inserting a default value when the key doesn't exist
d = dict(a=1, b=2, z=0)
if 'z' not in d:
    d['z'] = 100

print(d)

#
def insert_if_not_present(d, key, value):
    if key not in d:
        d[key] = value
        return value
    else:
        return d[key]

d = dict(a=1, b=2, z=0)
print(insert_if_not_present(d, 'z', 100))
print(insert_if_not_present(d, 'x', -10))

# using setdefault

d  = dict(zip('abc', range(1,4)))
print(d)
print(d.setdefault('a', 100))

#
counts = dict()
for c in text:
    key = c.lower().strip()
    if key:
        counts[key] = counts.get(key, 0) + 1
print(counts)

import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)

catergories = {}
for c in text:
    if c != ' ':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else:
            key = 'other'
        if key not in catergories:
            catergories[key] = set()

        catergories[key].add(c)

for cat in catergories:
    print(f'{cat}: ', ''.join(catergories[cat]))
print(catergories)

# Modify
catergories = {}
for c in text:
    if c != ' ':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else:
            key = 'other'
        catergories.setdefault(key, set()).add(c)

for cat in catergories:
    print(f'{cat}: ', ''.join(catergories[cat]))
print(catergories)

# simplify further
def cat_key(c):
    if c == ' ':
        return None
    elif c in string.ascii_lowercase:
        return 'lower'
    elif c in string.ascii_uppercase:
        return 'upper'
    else:
        return 'other'

catergories = {}
for c in text:
    key = cat_key(c)
    if key:
        catergories.setdefault(key, set()).add(c)

for cat in catergories:
    print(f'{cat}: ', ''.join(catergories[cat]))
print(catergories)

#  Other way

def cat_key(c):
    catergories = {' ': None,
                   string.ascii_lowercase: 'lower',
                   string.ascii_uppercase: 'upper'}
    for key in catergories:
        if c in key:
            return catergories[key]
    else:
        return 'other'

for cat in catergories:
    print(f'{cat}: ', ''.join(catergories[cat]))
print(catergories)

# creating categories dictionaries of individuals we're interested in.

# How to merger dictionaries
from itertools import chain

def cat_key(c):
    cat_1 = {' ': None}
    cat_2 = dict.fromkeys(string.ascii_lowercase, 'lower')
    cat_3 = dict.fromkeys(string.ascii_uppercase, 'upper')

    categories = dict(chain(cat_1.items(),
                            cat_2.items(),
                            cat_3.items()))
    # categories ={**cat_1, **cat_2, **cat_3}
    print(cat_1)
    print(cat_2)
    print(cat_3)
    print(categories)

    return categories.get(c, 'other')

print(cat_key('A'))
# print(cat_key('b'))
# print(cat_key(''))

# def cat_key(c):
#     if c == ' ':
#         return None
#     elif c in string.ascii_lowercase:
#         return 'lower'
#     elif c in string.ascii_uppercase:
#         return 'upper'
#     else:
#         return 'other'

catergories = {}

for c in text:
    key = cat_key(c)
    if key:
        catergories.setdefault(key, set()).add(c)

for cat in catergories:
    print(f'{cat}: ', ''.join(catergories[cat]))
print(catergories)

# clear out all the items from dictionaries

print(d)
print(id(d))
d = {}
print(id(d))
d = dict(zip('abc','def'))
print(d)
print(id(d))
d.clear()
print(id(d))