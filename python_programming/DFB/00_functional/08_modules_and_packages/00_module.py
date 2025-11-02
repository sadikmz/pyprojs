def func():
    a = 10
    return a

print(func())

# global(): return diction of all the global Namespace dictionary details
# print(globals())
# print(locals() )

def func():
    a = 10
    b = 20
    print(locals())

func()


import math
# print(math)
# print(type(math))

# Those objects in global environment can also cached via sys module

import sys
# print(sys.modules)

import fractions

# print(sys.modules['fractions'])
# print(fractions.__dict__)

# Whwre is python installed
print(sys.prefix)

# path

print(sys.path)