# occur at compile time
# certain things get optimized
# Constant expressions: Expression that evaluates to a constant get pre-calcuated and stored
    # numeric calculations
# Short sequences < 20 in length: it also get pre-calculated and stored
# tradoff between storage and computation
# Membership test
# if e in [1,2,3]
# Set membership - faster to do lookup than list or tuple
# if e in [1,2,3] or if e in (1,2,3)
# write if e in {1,2,3)

def my_func():
    a = 24 * 60
    b = (1,2) * 5
    c = 'abc' *  3
    d = 'ab' * 11
    e = 'The quick brown fox' * 5
    g = ['a','b'] * 30

# print(my_func.__code__.co_consts)
# print(my_func.__code__.co_consts)


def my_func(e):
    if e in [1,2,3]:
        pass

def my_func(e):
    if e in {1,2,3}:
        pass

# print(my_func.__code__.co_consts)
# print(my_func().)
# my_func()._


# membership

import string
import time

# print(string.ascii_letters)

char_list = list(string.ascii_letters)
# print(char_list)

char_tuple = tuple(string.ascii_letters)
# print(char_tuple)

char_set = set(string.ascii_letters)
# print(char_set)

def membership_test(n,container):
    for i in range(n):
        if 'z' in container:
            pass

start = time.perf_counter()
membership_test(10000000,char_list)
end = time.perf_counter()
print('List', end - start)
# start = time.perf_counter()

start = time.perf_counter()
membership_test(10000000,char_tuple)
end = time.perf_counter()
print('Tuple', end - start)

start = time.perf_counter()
membership_test(10000000,char_set)
end = time.perf_counter()
print('Set', end - start)