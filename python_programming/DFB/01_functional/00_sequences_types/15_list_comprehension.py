# squares = []
# for i in range(100):
#     squares.append(i**2)
#
# print(squares[0:10])
#
#
# squares = [(i**2) for i in range(100)]
# print(squares[0:10])
from nbformat import v1

# squares = []
#
# for i in range(100):
#     if i % 2 == 0:
#         squares.append(i**2)
#
# print(squares[0:10])
#
# squares = [(i**2) for i in range(1,101) if i % 2 == 0]
# print(squares[0:10])
#
# squares = [(i**2) for i in range(1,101) if i % 2]
# print(squares[0:10])
#
# squares = [(i**2) for i in range(1,101)
#            if i % 2]
# print(squares[0:10])

# Comprehensions

# compiled_code = compile('[i**2 for i in (1,2,3)]',
#                         filename='string', mode='eval')
#
# print(compiled_code)

# disassembly to see what python is doing

import dis
# dis.dis(compiled_code)

# create a multiplication table

# table = []
#
# for i in range(1,11):
#     row = []
#     for j in range(1,11):
#         row.append(i*j)
#     table.append(row)
#
# print(table)

# create comprehension for the above
# table = [[i*j for i in range(1,11)] for j in range(1,11)]
# print(table)


# pascal's triangle

# C(n,k) = n! / (k! (n-k)!)

# from math import factorial
#
# def combo(n,k):
#     return factorial(n)//(factorial(k)*factorial(n-k))
#
# size = 10

# using a nested comphrehension
# pascal = [[combo(n,k) for k in range(n+1)] for n in range(size + 1) ]
# print(pascal)

# nested loops for comprehensions
l1 = ['a','b','c']
l2 = ['x','y','z']

# result = [i+j for i in l1 for j in l2]
# print(result)

l1 = ['a','b','c']
l2 = ['b','c','d']

# result = [i+j
#           for i in l1
#           for j in l2
#           if i != j
          # ]
# print(result)

l1 = ['a','b','c']
l2 = ['b','c','d']

# result = [i+j
#           for i in l1
#           for j in l2
#           if i != j ]
# print(result)

l1 = [1,2,3,4,5,6,7,8,9]
l2 = ['a','b','c','d']

#  create zip
# result = list(zip(l1,l2))
# print(result)
#
# creating it with traditional method
# print(list(enumerate(l1)))
# print(list(enumerate(l2)))

result = []

# for index_1, value_1 in enumerate(l1):
#     for index_2, value_2 in enumerate(l2):
#         if index_1 == index_2:
#             result.append((value_1,value_2))
#
# print(result)

# With list comprehension

# result = [(value_1,value_2)
#           for index_1, value_1 in enumerate(l1)
#           for index_2, value_2 in enumerate(l2)
#           if index_1 == index_2]
# print(result)

# using sum function on dot product of two dimentional coordinates

# dot = 0
# for i in range(len(v1)):
#     dot += v1[i] * v2[i]
#     print(dot)

v1 = [1,2,3,4,5,6]
v2 = [10,20,30,40,50,60]

# dot = 0
# for i in range(len(v1)):
#     dot += v1[i] * v2[i]
# print(dot)

# print(sum([i*j for i,j in zip(v1,v2)]))
# print(sum(i*j for i,j in zip(v1,v2)))

# Something to watch out
# l = []
# for number in range(5):
#     l.append(number**2)
# print(number)

# if 'number' in globals():
#     del number

# l = [number**2 for number in range(5)]
# print('number' in globals())

# fn_0 = lambda n: n**0
# fn_1 = lambda n: n**1
# fn_2 = lambda n: n**2
# fn_3 = lambda n: n**3
#
# funcs = [lambda n: n**0, lambda n: n**1, lambda n: n**2, lambda n: n**3 ]
#
# for i in range(4):
#     print(funcs[i](10))
#
# if 'i' in globals():
#     del i
#
# funcs = []
#
# for i in range(6):
#     print(i)
    # funcs.append(lambda x: x**i)
# print(i)
# del i
# print(funcs)
# print(funcs[0])
# print(funcs[0](10))
# print(funcs[1](10))
# print(funcs[2](10))
# print(funcs[3](10))

# del i

# def funcs():
#     fn = []
#     for i in range(6):
#         fn.append(lambda x: x**i)
#     del i
    # return fn
#
# print('i' in globals())
#
# f = funcs()
# print(f[0](10))
# print(f[1](10))
# print(f[2](10))
#

# print('fn' in globals())

# The same issue with closures

# funcs = [lambda n: n**i for i in range(6)]
# print('i' in globals())
# print(funcs[0](10))
# print(funcs[1](10))

# from datetime import datetime
#
# def log(msg, current_dt = datetime.now() ):
#     print(msg, current_dt)
#
# log('abc')
# log('cde')
# log('a')

# solution
funcs = [lambda x, p=i : x**p for i in range(5)]
# print('i' in globals())
print(funcs[0](10))
print(funcs[1](10))
print(funcs[2](10))
print(funcs[3](10))
print(funcs[4](10))
# print(funcs[5](10))