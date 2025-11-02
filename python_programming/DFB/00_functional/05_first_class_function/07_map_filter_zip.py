# High-order function: A function that takes a function as a parameter and or returns a function as its return value
# example:sorted,

# map function
# map(func,*iterables)

l = [2,3,4]
def sq(x):
    return x**2

list(map(sq, l))
print(list(map(sq, l)))

l1 = [1,2,3]
l2 = [10,20,30]

def add(x,y):
    return x+y
list(map(add, l1, l2))
print(list(map(add, l1, l2)))
print(list(map(lambda x,y: x+y, l1, l2)))


# The filter function: It takes a single function and a single argument
# filter(func,iterable)

l = [0,1,2,3,4]
print(list(filter(None,l)))

def is_even(x):
    return x % 2 == 0


print(list(filter(is_even, l)))


# The zip function: is the higher-order function
# zip(*iterables) - combined each iterable pair-wise - returns tuple
print(list(zip([1,2,3],['a','b','c'])))
l1 = [1,2,3,4]
l2 = [10,20,30,40]
# l3 = ['a','b','c','d']
l3 = 'python'
print(list(zip(l1,l2,l3)))

# List comprehension alternative to map
l = [2,3,4]
def sq(x):
    return x**2

print(list(map(sq, l)))
print(list(map(lambda x:x**2, l)))
result = []
for i in l:
    result.append(i**2)

print(result)

# List comprehension
print([x**2 for x in l])

l1 = [1,2,3]
l2 = [10,20,30]
print(list(map(lambda x,y:x+y, l1,l2)))
print(list(zip(l1,l2)))
print([x+y for x, y in zip(l1,l2)])

 # With filter funciton

l  = [1,2,3,4,5]
print(list(filter(lambda x:x%2==0, l)))
print([x for x in l if x%2==0])

# expression for list comprehension
# [<expression> for <varname> for <iterable> if <expression>]

l = range(10)

print(list(filter(lambda y: y<25, map(lambda x:x**2, l))))
# using list comprehenstion
print([x**2 for x in range(10) if x**2 < 25])

def fact(n):
    return 1 if n < 2 else n*fact(n-1)

print(fact(3))


resutl = map(fact, range(6))
resutl = list(map(fact, range(6)))

for x in resutl:
    print("first")
    print(x)

for x in resutl:
    print("second")
    print(x)


l1 = [1,2,3,4]
l2 = [10,20,30]
l3 = [100,200,300]
resutl = list(map(lambda x, y, z: x+y+z, l1,l2,l3))
print(resutl)

# resutl = map(lambda x, y: x+y, l1,l2,l3)
# # print(resutl)
# for x in resutl:
#     # print("first")
#     print(x)


# Filter function

x = range(25)
# print(x)

for i in x:
    print(i)

print(list(filter(lambda x:x%3==0, range(25))))
# l1 = [1,2,3,4]

print(list(filter(None,[1,0,4,'a','',None, True, False])))

# Zip function

l1 = [1,2,3,4]
l2 = [10,20,30,40]
l3 = 'python'

result=(zip(l1,l2,l3))

for x in result:
    print(x)

for x in result:
    print("check this")
    print(x)


result = zip(range(1000),'python')
for x in result:
    print(x)

# list comprehension

l = range(10)
print(list(l))
print(list(l))

result = [fact(x) for x in l]
print(result)

result = (fact(x) for x in range(10))
print(result)
for x in result:
    print(x)

for x in result:
    print(x)


result = [fact(x) for x in range(10)]
print(result)
for x in result:
    print(x)

for x in result:
    print(x)


l1 = [1,2,3,4,5,6]
l2 = [10,20,30,40]

print(list(map(lambda x,y:x+y,l1,l2)))
print([x+y for x, y in zip(l1,l2)])
print(list(filter(lambda x:x%2==0, map(lambda x,y:x+y,l1,l2))))
result=((x+y for x, y in zip(l1,l2) if (x+y)%2==0))
for i in result:
    print(i)
# l1 = [1,2,3,4]
# l2 = [10,20,30]