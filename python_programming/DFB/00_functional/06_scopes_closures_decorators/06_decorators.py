# Decorators:
# In general a decorator function:-
# takes a function as an argument
# returns a closure
# the closure usually accepts any combination of parameters
# runs some code in the inner function (closure)
# the closure function calls the original function using the argument passed to the closure
# returns whatever is returned by that function call

# counter function

def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function {0} was called {1}'.format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner
def add(a,b):
    return a + b

add = counter(add)
result = add(1,2)

# Decorators and @ symbol

# Introspection of decorated functions
def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function {0} (id={1}) was called {1}'.format(fn.__name__, id(fn), count))
        return fn(*args, **kwargs)
    return inner

def add(a: int,b:int=0):
    """
    Adds two numbers together

    """
    return a + b


help(add)
print(id(add))
add = counter(add)
print(id(add))
help(add)

print(add(10,20))
print(add(30,20))

def mult(a:int, b: int,c:int=1,*,d):
    """
    Multiplies four values
    """
    return a * b * c * d

print(mult(1,2,3,d=4))
help(mult)

mult = counter(mult)
print(mult(1,2,3,d=4))
help(mult)
print(mult(1,2,d=4))

# other ways of doing

def my_func(s:str,i:int):
    return s*i

my_func = counter(my_func)

# or

# using @ decorator
@counter
def my_func(s:str,i:int):
    return s*i

print(my_func(10,'a'))

help(my_func)
print(mult.__name__)

#
def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function {0} (id={1}) was called {1}'.format(fn.__name__, id(fn), count))
        return fn(*args, **kwargs)

    inner.__name__ = fn.__name__
    inner.__doc__ = fn.__doc__

    return inner

def mult(a:int, b: int,c:int=1,*,d):
    """
    Multiplies four values
    """
    return a * b * c * d


mult = counter(mult)
help(mult)

# Fixing the documentation string


from functools import wraps

def counter(fn):
    count = 0

    # @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function {0} (id={1}) was called {1}'.format(fn.__name__, id(fn), count))
        return fn(*args, **kwargs)

    inner = wraps(fn)(inner)

    return inner

def mult(a:int, b: int,c:int=1,*,d):
    """
    Multiplies four values
    """
    return a * b * c * d


mult = counter(mult)
help(mult)

# Fixing the documentation string
