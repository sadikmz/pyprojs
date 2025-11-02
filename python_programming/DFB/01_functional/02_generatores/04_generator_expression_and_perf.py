# List comprehension
l = [i ** 2 for i in range(5)]
print(type(l))
print(l)

# using parenthesis

g = (i ** 2 for  i in range(5))
print(type(g))
for i in g:
    print(i)

# let's disassmble

import dis

exp = compile('[i**2 for i in range(5)]',
              filename='<string>',
              mode='exec')

# disassemble the expresion
dis.dis(exp)

# for generator expression
exp = compile('(i**2 for i in range(5))',
              filename='<string>',
              mode='exec')

# disassemble the expression
dis.dis(exp)

#
l = [i ** 2 for i in range(5)]
# print(type(l))
print(l)
print(l)
# using parenthesis

g = (i ** 2 for  i in range(5))
for i in g:
    print(i)

for i in g:
    print(i)
# print(g)
# print(g)

# Nesting of generator expression

start = 1
stop = 10

mult_list = [[i*j
              for i in range(start, stop+1)]
             for j in range(start, stop+1)]

print(mult_list)

# for generator

mult_list = ((i*j
              for i in range(start, stop+1))
             for j in range(start, stop+1))

print(mult_list)
# to retrieve the elements

mult_list = ((i*j
              for i in range(start, stop+1))
             for j in range(start, stop+1))

print([list(row) for row in mult_list])

mult_list = ((i*j
              for i in range(start, stop+1))
             for j in range(start, stop+1))
for row in mult_list:
    for item in row:
        print(item)

#

mult_list = ((i*j
              for i in range(start, stop+1))
             for j in range(start, stop+1))
for row in mult_list:
    print(', '.join([str(item) for item in row]))

#
start = 1
stop = 10

mult_list = ((i*j
              for i in range(start, stop+1))
             for j in range(start, stop+1))
for row in mult_list:
    for item in row:
        print(item, end=' ')
    print('')


# We can do list comprehension inside generator
start = 1
stop = 10

mult_list = ([i*j
              for i in range(start, stop+1)]
             for j in range(start, stop+1))
print(list(mult_list))
# for row in mult_list:
#     for item in row:

# or

start = 1
stop = 10

mult_list = ([i*j
              for i in range(start, stop+1)]
             for j in range(start, stop+1))
# print(list(mult_list))
for row in mult_list:
    print(row)

# Let's do pascal's triangle
# def c(0,0)
#       c(1,0), c(1,1)
#       c(2,0), c(2,1), c(2,2)
#       c(3,0), c(3,1), c(3,2), c(3,3)

from math import factorial

# combination function
def combo(n,k):
    return factorial(n) // (factorial(k) * factorial(n-k))

size = 10 # global variable

# Create a pascal triangle using a list comprehension
pascal = [[combo(n,k) for k in range(n + 1)] for n in range(size + 1) ]
print(pascal)

# We can use generated instead
pascal = ((combo(n,k) for k in range(n + 1)) for n in range(size + 1) )
print([list(row) for row in pascal])


# timing

from timeit import timeit

size = 600
print(timeit('[[combo(n,k) for k in range(n + 1)] for n in range(size + 1) ]',
       globals=globals(),number=1))

print(timeit('((combo(n,k) for k in range(n + 1)) for n in range(size + 1) )',
             globals=globals(),number=1))

print(timeit('([combo(n,k) for k in range(n + 1)] for n in range(size + 1) )',
             globals=globals(),number=1))


#

def pascal_list(size):
    l = [[combo(n,k) for k in range(n + 1)] for n in range(size + 1) ]
    for row in l:
        for item in row:
            pass


def pascal_gen(size):
    l = ((combo(n,k) for k in range(n + 1)) for n in range(size + 1) )
    for row in g:
        for item in row:
            pass

size = 600
print(timeit('pascal_list(size)',globals=globals(),number=1))
print(timeit('pascal_gen(size)',globals=globals(),number=1))

# interms of memory consumption

import tracemalloc

def pascal_list(size):
    l = [[combo(n,k) for k in range(n + 1)] for n in range(size + 1) ]
    for row in l:
        for item in row:
            pass
    stats = tracemalloc.take_snapshot().statistics('lineno')
    print(stats[0].size, 'bytes')



def pascal_gen(size):
    l = ((combo(n,k) for k in range(n + 1)) for n in range(size + 1) )
    for row in l:
        for item in row:
            pass
    stats = tracemalloc.take_snapshot().statistics('lineno')
    print(stats[0].size, 'bytes')

tracemalloc.start()
tracemalloc.clear_traces()
tracemalloc.start()
pascal_list(300)

# 1998644/1024/1020 mb

tracemalloc.start()
tracemalloc.clear_traces()
tracemalloc.start()
pascal_gen(300)

# 448/1024/1020 mb
