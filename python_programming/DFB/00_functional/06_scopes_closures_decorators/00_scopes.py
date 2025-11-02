# Global and local scopes
# Built-in scope
# lexical scope of a variable
# namespace
# Maskin namespace
# Nested scope
# Namespace lookups
# out of scope
# Retrieving the value of a global variable from inside a function.
# The global keyword
# Global and local scoping
from traceback import print_tb

a = 10
def func00():
    print(a)

func00()

def func01():
    global a
    a += 100
    print(a)

print(a)
func01()
print(a)


def func02():
    a = 100
    print(a)

print(a)
func02()
print(a)

# Coding

a = 10

def func03(n):
    c = n ** 2
    return c

def my_func04(n):
    print('global a', a)
    c = a ** n
    return c
print(my_func04(2))


def my_func05(n):
    a = 20
    c = a ** n
    return c

print(a)
print(my_func05(2))
print(a)

# declare global variable

def my_func06(n):
    global a
    a = 20
    c = a ** n
    return c

print(a)
print(my_func06(2))
print(a)


def my_func07():
    global var
    var = 'Hello world'
    return var

# print(var)
print(my_func07())
print(var)

a = 10

def my_func08():
    print('global a:', a)

my_func08()
print(a)


def my_func09():
    global a
    a = 'Hello'
    print('global a:', a)

my_func09()
print(a)

a = 10

def my_func10():
    # print('global a:', a)
    a = 'Hello world'
    print(a)

my_func10()

f  = lambda n: print(a ** n)

print(a)
f(1)

print(True)

# Redefine function

def print(x):
    return 'Hell {0}'.format(x)
del print
# print('world')

#

for i in range(10):
    x = 2*i

print(x)