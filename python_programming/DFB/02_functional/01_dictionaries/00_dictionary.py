a = {'k1': 100, 'k2':200}
print(type(a))
print(a)

# hashing
# print(type((1,2,3)))
# print(hash((1,2,3)))
# print(hash((1,2,3)))
d = {(1,2,3):'This is a tuple'}
print(d[(1,2,3)])
t1 = (1,2,3)
t2 = (1,2,3)
t3 = (1,2,3)
print(t1 == t2)
print(t1 is t2)
print(hash(t1) == hash(t2))
print('hash of t1:', hash(t1))
print('hash of t2:', hash(t2))
#
print(id(t1))
print(id(t2))
print(id(t3))

# print(hash([1,2,3]))

#  using function as key
def my_func(a,b,c):
    print(a, b, c)

print(hash(my_func))
d = {my_func:[10,20,30]}
print(d[my_func])
print(d)

def fn_add(a,b):
    return a+b

def fn_inv(a):
    return 1/a

def fn_mult(a,b):
    return a*b

funcs = {fn_add:(10,20),fn_inv:(2,),fn_mult:(2,8)}
print(funcs)
# iterate through dictionarly
for f in funcs:
    # print(f)
    # print(funcs[f])
    result = f(*funcs[f])
    print(result)

for f, args in funcs.items():
    print(f, args)
    print(f(*args))

# dictionary class constructor

d = dict(x=100, a = 200)
print(d)
d = dict([('a', 200), ('b', 300)])
print(d)

# pass a dictionary to a dictionary constructor

d = {'a': 200, 'b': 200}
d1 = dict(d)
print(d,'\n', d1)
print(id(d), id(d1))

d = {'a': 200, 'b': {'x': 1, 'y': 2},'c':[1,2,3]}
print(d)
d1 = dict(d)
print(d1 is d)

print(id(d), id(d1))
print(id(d1['b']))
print(id(d['b']))
print(id(d1['a']))
print(id(d['a']))
print(id(d1['c']))
print(id(d['c']))

d1['b']['e'] = 200
# d1['b']['e'] = 200
d['c'].append(100)
# d1['b']['e'] = 200

print(d1)
print(d)

key = ['a', 'b', 'c']
values = [1, 2, 3]

d = {}
for k, v in zip(key, values):
    d[k] = v
print(d)

d = {k:v for k, v in zip(key, values)}

print(d)

keys = 'abcd'
values = range(1,5)

d = {k:v for k, v in zip(keys, values) if v % 2 == 0}
print(d)
# print(d)

# nested for loop
x_coords = [-2,-1,0,1,2,3]
y_coords = [-2,-1,0,1,2,3]
grid = [(x,y)
        for x in x_coords
        for y in y_coords
]

print(grid)
import math
print(math.hypot(1,1))
grid_extended = [(x,y, math.hypot(x,y))
                for x, y in grid]

print(grid_extended)

# for dictionary: dictionary comprehension

grid_extended = {(x,y): math.hypot(x,y)
                for x, y in grid}

print(grid_extended)

# fromkey function
counters = dict.fromkeys(('a', 'b', 'c'), 0)
print(counters)
counters = dict.fromkeys(('abc'), 0)
print(counters)
d = dict.fromkeys('Python')
print(d)
print(d)