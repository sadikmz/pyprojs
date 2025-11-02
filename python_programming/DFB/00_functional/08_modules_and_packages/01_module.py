import sys

for key in sorted(sys.modules.keys()):
    print(key)


print('cmath' in sys.modules)
print('cmath' in globals())

from cmath import exp

print('cmath' in globals())
print('exp' in globals())
print('cmath' in sys.modules)

print(exp(10))
# print(cmath.exp(10))

cmath = sys.modules['cmath']
print(cmath.exp(10))
print(cmath.cos(2+2j))
print(dir(cmath))

# using import *

print("----------Before importing all--------")
# print(globals())

for key in sorted(globals().keys()):
    print(key)

print("------After importing all------")
from cmath import *
# print(globals())
for key in sorted(globals().keys()):
    print(key)


from math import *

print("------After importing math------")

for key in sorted(globals().keys()):
    print(key)


# importing as alies

from math import sin as m_sin
from cmath import sin as m_sin

# delete module from sys.module

del sys.modules['cmath']
# print(sys.path)

# import collections
# print(collections.__path__)
print('collections' in sys.modules)
print('collections' in globals())
# del sys.modules['collections']
# import math
# print(math.__spec__)
import fractions
# print(fractions.__spec__)
print(fractions.__file__)