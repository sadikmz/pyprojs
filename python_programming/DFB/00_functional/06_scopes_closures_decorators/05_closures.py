# a counter with initial value and increment the value by one each time
def counter(initial_value=0):
    def inc(increment=1):
        nonlocal initial_value
        initial_value += increment
        return initial_value
    return inc

count1 = counter()
# count2 = counter()

print(count1())
print(count1())
print(count1())

# How many times a function been called

def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print('{0} has been called {1} time'.format(fn.__name__, cnt))
        return fn(*args, **kwargs)
    return inner

def add(a, b):
    return a + b

def mult(a, b):
    return a * b

counter_add = counter(add)

# print(counter_add.__closure__)
# print(counter_add.__code__.co_freevars)
print(counter_add(10,20))
print(counter_add(10,20))
result = counter_add(10,20)
counter_mult = counter(mult)
result2 = counter_mult(10,20)


# Store the value somewhere

counters = dict()
def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print('{0} has been called {1} time'.format(fn.__name__, cnt))
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner

counted_add = counter(add)
counted_mult = counter(mult)

print(counted_add(10,20))
print(counted_add(20,30))
print(counted_mult(2,5))
print(counters)

# modify


# counters = dict()

def counter(fn, counters):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        # print('{0} has been called {1} time'.format(fn.__name__, cnt))
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner

c = dict()
counted_add = counter(add,c)
counted_mult = counter(mult,c)

print(counters)

print(counted_add(10,20))
print(counted_add(20,30))
print(counted_mult(2,5))
print(counted_mult(2,5))

print(counters)
print(c)

# A factorial function

def fact(n):
    product = 1
    for i in range(1,n+1):
        product *= i
    return product

print(fact(5))
counted_fact = counter(fact,c)
print(counted_fact(5))
print(c)

fact = counter(fact,c)
print(fact.__closure__)
print(fact(2))
print(fact(2))
print(fact(2))
print(fact(2))
counted_mult = counter(mult,c)
print(counted_mult(2,0))
print(counted_mult(2,1))
print(counted_mult(2,2))
print(counted_mult(2,3))
print(counted_mult(2,4))
print(fact(5))
add = counter(add,c)
print(counted_add(10,20))


print(c)