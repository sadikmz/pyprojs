# Truth table
# Commutability
# A or B == B or A
# A and B == B and A
#
# Distributivity
# A and (B or C) == (A and B) or (A and C)
# A or (B and C) == (A and B) and (A and C)
import string

# Associativity
# A or (B or C) == (A or B) or C > A or B or C
# A and (B and C) == (A and B) and C > A and B and C

# De Morgan's Theorem
# not(A or B) == (not A) and (not B)
# not(A and B) == (not A) or (not B)

# Miscellaneous
# not(X < Y) == X >= Y not(X>=Y) == X<Y
# not(X > Y) == X <= Y not(X<=Y) == X>Y
# not(not A) == A

# Operator Precedence: Highest to lowest precedence
# ()
# <> <= >= == != in is
# not
# and
# or


# Short-Circuit Evaluation
# Without implementing short-circuiting
# if symbol in watch_list:
#     if price(symbol) > threashold:
#         do something

# Implementing short-circuiting
# if symbol in watch_list and print(symbol) > threashold:
#     do soemthing

# Before implementing short-circuiting
# if name[0] in string.digits:
#     do something

# Because of short-circuiting and truth values
# if name and name[0] in string.digits:
# do something


print(True or True and False)
print((True or True) and False)
print((False or False) and True)
print((False or True) and True)

# Short-circuiting

# True or Y --> True
# False and Y --> False

a = 10
b = 0

# if a / b > 2:
#     print('a is at least twice b')

# if b > 0 and a / b :
#     print('a is at least twice b')
# if b > 0:
#     if a / b > 2:
#         print('a is at least twice b')

# if b and a / b > 2:
#     print('a is at least twice b')


import string

# print(help(string))

print('strings')
a = 'c'
print(a)
print(string.ascii_lowercase)
print(a in string.ascii_letters)
# print(string.ascii_letters)

name = None
if name and name[0] in string.digits:
    print("Name cannot start with digits")
#
# s = 'a'
#
# if s:
#     return s[0]
# else:
#     return ''
#
# print(s)

# return s and s[0]
print('a' or [1, 2])
print('' or [1, 2])

print(1 or 1 / 0)
# print(0 or 1/0)

# Using the or boolean for defaulting purpose

s1 = None
s2 = ''
s3 = 'abc'

s1 = s1 or 'n/a'
s2 = s2 or 'n/a'
s3 = s3 or 'n/a'

print(s1, s2, s3)
print([], [0])

# X and Y: if X is falsy, return X, otherwise evaluate and return Y
print(None and 100)
print([] and [0])

#
a = 2
b = 1

if b==0:
    print(0)
else:
    print(a / b)

a = 2
b = 0
print(b and a / b)


s1 = None
s2 = ''
s3 = 'abc'

print((s1 and s1[0]) or '')
print((s2 and s2[0]) or '')
print((s3 and s3[0]) or '')

# Not operator
print(not True)
print(not False)
print(not bool(''))
print(not 'abc')
print(type(not 'abc'))

print(not 'None')