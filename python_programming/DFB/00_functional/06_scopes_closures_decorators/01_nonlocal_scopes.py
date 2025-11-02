# inner function
# We can define functions from inside another function

# def outer_func():
#     # some_code
#     def inner_func():
        # some_code
# Both functions have access to the global and built-in scopes as well their respective local scopes
# But the inner function also has access to its inclosing scope - the scope of the outer function

# nonlocal keyword

# Nonlocal and global variables

# Referencing variables from the enclosing scope
# Module.py
def outer_func():
    a = 10

    def inner_func():
        print(a)

    inner_func()

outer_func()
#Example

a = 100
def outer_func():
    def inner_func():
        print(a)

    inner_func()
outer_func()

# Modifying global variable

a = 1000

def outer_func():
    global a
    a = 150
outer_func()
print(a)

# Using nested function

def outer_func_00():
    def inner_func_00():
        global a
        a = 'hello'
    inner_func_00()
outer_func_00()
print(a)

# modifying nonlocal variable

def outer_func_01():
    x = 'Hello'
    def inner_func_01():
        x = 'Python'
    inner_func_01()

    print(x)
outer_func()

# Explicitly tell python

def outer_func_02():
    x = 'Hello'

    def inner_func_02():
        nonlocal x
        x = 'Python'

    inner_func_02()

    print(x)

outer_func_02()


# Nonlocal variables: Whenever Python is told that a variable is nonlocal - it will look for it in the enclosing local scopes chain until it first encounters the specified variable name
# it will only look in the local scopes: it will not look in the global scope

def outer_func_03():
    x = 'Hello'

    def inner_func_03():
        def inner_func_04():
            nonlocal x
            x = 'Hello Python World'
        inner_func_04()

    inner_func_03()

    print(x)

outer_func_03()

#
def outer_func_04():
    x = 'Hello'
    def inner_func_04():
        x = 'Python'
        def inner_func_05():
            nonlocal x
            x = 'Monty'
        print('Inner(before)', x)
        inner_func_05()
        print('Inner(after)', x)
    inner_func_04()
    print('outer_func_04()', x)
outer_func_04()

#
def outer_func_05():
    x = 'Hello'

    def inner_func_06():
        nonlocal x
        x = 'Python'
        def inner_func_07():
            nonlocal x
            x = 'Monty'
        print('Inner(before)', x)
        inner_func_07()
        print('Inner(after)', x)

    inner_func_06()
    print('outer_func_06', x)
outer_func_05()


#
x = 100

def outer():
    x = 'python'

    def inner1():
        nonlocal x
        x = 'monty'

        def inner2():
            global x
            x = 'Hello'
            print('inner2', x)
        print('inner(before)', x)
        inner2()
        print('inner(after)', x)

    inner1()
    print('outer', x)

outer()

print('outer', x)