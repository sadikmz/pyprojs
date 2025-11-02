# Boolean truth value
# Integer numbers (Z)
# Rational numbers (Q)
# Real numbers (R)
# Complex numbers (C)

# print(type(100))
import sys
# print(sys.getsizeof(2**1000))
# print(type(2/3))
# print(type(10/0))

import math
# print(math.floor(-3.0000000000000000001))
# a = 33
# b = -16

# print(a/b)
# print(a//b)
# print(math.floor(a/b))
# print(math.trunc(a/b))

# a = b*(a//b)+(a%b)

a = 13
b = -4

print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print( a==b *(a//b) + (a%b) )