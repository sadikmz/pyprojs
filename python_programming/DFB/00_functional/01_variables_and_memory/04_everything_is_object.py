# integers
# booleans
# floats
# strings
# lists
# tuples
# sets
# dictionaries
# None
# Operators: (+, -, ==, is, ...)
# function
# class
# Types

# Objects are instances of classes
# print(type(int))
# a = 10
# print(type(a))
# a = 10
#
# c = int()
# print(c)
# c = int('11', base=2)
# print(c)
# # help(int)

def square(a):
    return a * a
# print(type(square))
# f = square
# print(type(f))
# print(id(f))
# print(id(square))

def cube(a):
    return a **3

def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube

# f = select_function(1)
#
# print(f is square)
# print(f(2))
#
# f = select_function(2)
# print(f is cube)
# print(f(2))

# print(select_function(2)(4))
# print(select_function(2)(3))

def exec_function(fn,n):
    return fn(n)

print(exec_function(cube,3))
print(exec_function(square,3))