# dir() return attribute of a function
import math
from inspect import ismethod, isfunction, isroutine
from traceback import print_tb


def func(a,b=2,c=2,*,kw1,kw2=5):
    i= 10
    b = min(i,b)
    return a * b
print(dir(func))
print(func.__name__)
print(func.__call__)
print(func.__defaults__)
print(func.__kwdefaults__)
print(func.__code__)
print(func.__code__.co_varnames)
print(func.__code__.co_argcount)
print(func.__code__.co_kwonlyargcount)

import inspect
# ismethod()
# isfunction()
# isroutine()

# What is the difference between a function and a method?
# Classes and objects have attributes - an object that is bound (to the class or the object)
# An attribute that is callable, is called a methods

def my_func(): # is a function and not a method
    pass

def MyClass():
    def func(self): # an instance method and is a method
        pass
my_obj = MyClass()
print(isfunction(my_func))
print(ismethod(my_func))
print(isfunction(my_obj))
# print(isfunction(my_obj.func))
print(ismethod(my_obj))
print(isroutine(my_obj))

# Code introspection

print(inspect.getsource(my_func))
print(inspect.getmodule(my_obj))
print(inspect.getmodule(math.sin))
print(inspect.getfile(my_func))


# Function comments

# Setting up variable
i = 10
# TODO: Implement function
# Some additional notes
def my_func(a,b=2,c=2,*,kw1,kw2=5):
    pass

print(inspect.getcomments(my_func))


# Collable signatures
print(inspect.signature(my_func).parameters)

def my_func(a: 'a string',
            b: 'int'=2,
            *args: 'additional positional args',
            kw1: 'first keyword-only arg',
            kw2: 'second keyword-only arg'=10,
            **kwargs: 'additional keyword-only args') -> str:
    """Do something.
       or do other"""
    pass

print(inspect.signature(my_func).parameters.values())

# dummy code
i = 100

# TODO: Fix this function
# Currently does nothing
def my_func(a: "Mandatory positional argument",
            b: "Optional positional argument"=1,
            c=2,
            *args: 'add extra positional args here',
            kw1: 'first keyword-only arg',
            kw2=5,
            kw3=100,
            **kwargs: 'Provide keyword-only args') -> 'does nothing':
    """This is does nothing but does have various
    parameters and annotation"""
    i = 10
    j = 20

    a = i + j

    return a

    # print(a,b,c,args,kw1,kw2,kw3,kwargs)

print(my_func.__doc__)
my_func.short_discription = "This is a short description"
print(my_func.short_discription)
print(dir(my_func))

print(my_func.__name__)
print(id(my_func))
def func(f):
    print(id(f))
    print(f.__name__)

# func(my_func)

print(my_func.__defaults__)
print(my_func.__kwdefaults__)
print(my_func.__code__)
print(dir(my_func.__code__))
print(my_func.__code__.co_name)
print(my_func.__code__.co_varnames)
print(my_func.__code__.co_argcount)

from inspect import isfunction, isroutine

a=10
print(isfunction(a))
print(isroutine(my_func))

class MyClass01:
    def f(self):
        pass
my_obj00 = MyClass01()
print(isfunction(MyClass01))
print(ismethod(MyClass01))
print(ismethod(my_obj00.f))
print(isroutine(my_obj00.f))

print(inspect.getsource(my_func))
print(inspect.getmodule(my_obj00))
print(inspect.getmodule(print))
print(inspect.getmodule(math.sin))
print(inspect.getcomments(my_func))

print(inspect.signature(my_func).parameters)
print(dir(inspect.signature(my_func)))

print(my_func.__annotations__)
print(inspect.signature(my_func).return_annotation)

sig = inspect.signature(my_func)

print(sig.parameters)

for param in sig.parameters.values():
    # print('Key: ', k)
    print('Name: ', param.name)
    print('Default: ', param.default)
    print('Annotation: ', param.annotation)
    print('Kind: ', param.kind)
    print('-----------------')
    # print(dir(v))
    # print(k, type(v))

help(divmod)
print(divmod(10,3))
# print(divmod(x=10,y=3))
for param in inspect.signature(divmod).parameters.values():
    print(param.kind)




