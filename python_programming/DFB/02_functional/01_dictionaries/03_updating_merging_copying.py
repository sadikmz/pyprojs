# updating, merging and copying
d = {'a': 1, 'b': 2, 'c': 3}

# update1
d['b'] = 400
print(d)

#update 2
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d1.update(d2)
print(d1)

# update3
d1 = {'a': 1, 'b': 2}
d1.update(x=200, c=30, a=40)
print(d1)

# using iterable
d1.update([('a', 1), ('b', 20), ('c', 3),('d', 4)])
print(d1)

# Using generate expressinon
d1.update((k, ord(k)) for k in 'python')
print(d1)

# unpack dictionary to new dictionary
l1 = [1, 2, 3]
l2 = 'abc'
l = [*l1, *l2]
print(l)

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

d = {**d1, **d2}
print(d)


d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'd': 4}
d = {**d1, **d2}
print(d)

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'd': 4}
d3 = {'b': 4, 'c': 50,'e': 6}
d = {**d1, **d2, **d3}
print(d)

conf_defaults = dict.fromkeys(('host', 'port', 'user', 'pwd','database'), None)
print(conf_defaults)

conf_global = {
    'port': 5432,
    'databse': 'deepdive',
}

conf_dev = {
    'host': 'localhost',
    'user': 'test',
    'pwd': 'test'
}

conf_prd = {
    'host': 'prodgpg.deepdive.com',
    'user': '$prod_user',
    'pwd': '$prod_pwd',
    'database': 'deepdive_prod',
}


# conf_defaults ----> global_cont ---> dev / prod

conf = {**conf_defaults,**conf_global,**conf_dev}
print(conf)
conf = {**conf_defaults,**conf_global,**conf_prd}
print(conf)

# dictionary unpacking using passing keyword arguments

def my_func(*, kw1, kw2, kw3):
    print(kw1, kw2, kw3)

d = {'kw2':20, 'kw1':1, 'kw3':3 }

my_func(**d)

# other way

def my_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

my_func(b=2,a=1)
my_func(**d)

# make copies of dictionaries
d = {'a': [1,2], 'b': [3, 4] }
d1 = d.copy()

print(id(d), id(d1))
print(id(d['a']))
print(id(d1['a']))
d1['a'].append('test')
print(d)
print(d1)
# del d['a']
# print(d)
# print(d1)
# print(d)

# Deepcopy
from copy import deepcopy

d = {'id': 123445,
    'person': {
        'name': 'John',
        'age': 78},
     'posts': [100, 105, 200]
    }
d_deep = deepcopy(d)
d_shallow = d.copy()
print(id(d), id(d_deep), id(d_shallow))
print(id(d['person']), id(d_shallow['person']), id(d_deep['person']))
print(id(d['posts']), id(d_shallow['posts']), id(d_deep['posts']))

d1 = {'a': [1,2], 'b': [3, 4] }
d = {**d1, 'c':100}
print(d)
print(id(d), id(d1))
print(id(d['a']), id(d1['a']))

d1 = {'a': [1,2], 'b': [3, 4] }
d2 = dict(d1)

print(id(d1['a']), id(d2['a']))
