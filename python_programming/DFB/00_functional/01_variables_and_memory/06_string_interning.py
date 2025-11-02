# # making a particular string a singleton
#
# a = 'hello'
# b = 'hello'
#
# print(id(a), id(b))
#
# a = 'hello world'
# b = 'hello world'
# print(id(a), id(b))
# print( a == b)
# print( a is b)
#
# a = '_this_is_a_long_string_that_could_be_used_as_an_identifier'
# b = '_this_is_a_long_string_that_could_be_used_as_an_identifier'
# print(a is b)

import sys
# a = sys.intern('hello world')
# b = sys.intern('hello world')
# c = 'hello world'
# print(id(a), id(b), id(c))
# # print(a is c)
# print(a is b is c)


def compare_using_equals(n):
    a = 'a long string that is not interned' * 200
    b = 'b long string that is not interned' * 200
    for i in range(n):
        if a == b:
            pass

def compare_using_interning(n):
    a = sys.intern('a long string that is not interned' * 200)
    b = sys.intern('b long string that is not interned' * 200)
    for i in range(n):
        if a == b:
            pass

import time
start = time.perf_counter()
# compare_using_equals(10000000)
compare_using_interning(10000000)
end = time.perf_counter()
print('equality', end - start)
