# Memory address

# my_var = 10
# print(my_var)
# print(id(my_var))
# print(hex(id(my_var)))

greeting = 'Hello'
# print(greeting)
# print(id(greeting))
# print(hex(id(greeting)))

#Reference counting

my_var = 10
other_var = my_var

# finding the Reference count
import sys
a = [1,2,3]
print(id(a))
print(sys.getrefcount(a))

import ctypes

def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

print(ref_count(id(a)))

b = a
print(id(b))
print(sys.getrefcount(b))
print(ref_count(id(b)))