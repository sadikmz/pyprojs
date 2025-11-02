from itertools import islice

l = [1,2,3,4,5]
print(l[0:2])

s = slice(0,2)

print(l[s])

import math

def factorials(n):
    for i in range(n):
        yield math.factorial(i)

fact = factorials(5)
# fact[0:2]

# define a function that's going to slice our iterable

def slice_(iterable,start,stop):
    for _ in range(0,start):
        next(iterable)
    for _ in range(start,stop):
        yield next(iterable)

# print(list(slice_(factorials(10), 0,10)))
# print(list(slice_(factorials(10), 3,10)))

# using islice

print(list(islice(factorials(10), 10)))
print(list(islice(factorials(10), 0,10)))
print(list(islice(factorials(10), 0,10,2)))
# help(islice)

# writing our own function to yield the first x elements of infinite loop

def factorials():
    index = 0
    while True:
        print(f"Yielding factorial {index}")
        yield math.factorial(index)
        index += 1

facts = factorials()

for _ in range(0,5):
    print(next(facts))

# Using islice
print(list(islice(factorials(), 3, 10)))
print(list(islice(factorials(), 3, 10,2)))
# print(list(islice(factorials(10), 0, 10)))

# If we pass iterator to islice, it will get consumed.
fact = factorials()
fact_s = islice(factorials(),0, 5 )
print(next(fact_s))
print(next(fact_s))
print(next(fact_s))
print(next(fact_s))
print(next(fact_s))
# print(next(fact_s))