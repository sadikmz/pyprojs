import datetime
from datetime import datetime


def log(message, *, dt='10'):
    dt = dt or datetime.now()
    print('{0}: {1}'.format(dt, message))

log('hello world')
log('hello world', dt=None)


print(datetime.now())

def log(msg, *, dt=datetime.now()):
    print('{0}: {1}'.format(dt, msg))
    # dt = dt or datetime.now()
log('hello world')
log('message 3')
log('message 4')


def log(msg, *, dt=None):
    dt = dt or datetime.now()
    print('{0}: {1}'.format(dt, msg))

log('hello world')
log('message 5')
log('message 6')
log('message 7')

my_list = (1,2,3,4,5)

def func(a=my_list):
    print(a)
func(my_list)
# print(my_list.append(7))
func(my_list)

# Using mutable object

def add_item(name,quantity,unit,grocery_list):
    grocery_list.append("{0} ({1} {2})".format(name,quantity,unit))
    return grocery_list

store1 = []
store2 = []

add_item("banana",2, 'units', store1)
add_item("milk",1, 'units', store1)
print(store1)

add_item('Python', 1, 'medium-rare', store2)
print(store2)

# del store1[0]
# del store2[0]

def add_item(name,quantity,unit,grocery_list=[]):
    grocery_list.append("{0} ({1} {2})".format(name,quantity,unit))
    return grocery_list

store1 = add_item("banana",2, 'units')
add_item("milk",1, 'units', store1)
print(store1)
print(id(store1))
store2 = add_item("Python", 1, 'medium-rare')
print(store2)
print(id(store2))

# Solution: Do not set mutable object as default unless targeting specific use cases

def add_item(name,quantity,unit,grocery_list=None):
    if not grocery_list:
        grocery_list = []
    grocery_list.append("{0} ({1} {2})".format(name,quantity,unit))
    return grocery_list


store1 = add_item("banana",2, 'units')
add_item("milk",1, 'units', store1)
print(store1)
store2 = add_item("Python", 1, 'medium-rare')
print(store2)
print(id(store1))
print(id(store2))


# Leveraging mutable default object

def factorial(n):
    if n < 1:
        return 1
    else:
        print('Calculating factorial of {0}'.format(n))
        return n * factorial(n-1)
print(factorial(5))


# cache = {}

def factorial(n,*,cache):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('Calculating factorial of {0}'.format(n))
        result = n * factorial(n-1, cache=cache)
        # cache[n] = result
        cache[n] = result
        return result

cache = {}

print(factorial(5, cache=cache))
print(cache)

print(factorial(3, cache=cache))
print(factorial(6, cache=cache))

# improved version

def factorial(n,*,cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('Calculating factorial of {0}'.format(n))
        result = n * factorial(n-1)
        # cache[n] = result
        cache[n] = result
        return result

print(factorial(5))
print(factorial(3))
print(factorial(4))
print(factorial(7))

