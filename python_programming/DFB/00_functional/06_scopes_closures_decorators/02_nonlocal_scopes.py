# nonlocal scopes

def out_func():
    x = 'Hello'
    def inner_func():
        print(x)
    inner_func()
out_func()


# nested

def outer_func_00():
    x = 'Hello'
    def inner_func_00():
        def inner_func_01():
            print(x)
        inner_func_01()
    inner_func_00()
outer_func_00()

#
def outer_func():
    x = 'Hello'
    def inner_func():
        x = 'Python'
        print('inner',x)
    inner_func()
    print('outer:',x)
outer_func()

#
def outer_func():
    x = 'Hello'
    print('outer (before)',x)
    def inner_func():
        nonlocal x
        x = 'Python'
        print('inner (before)',x)
    inner_func()
    print('outer (after):',x)
outer_func()

# Go nonlocal one-level up

def outer():
    x = 'Hello'
    def inner1():
        def inner2():
            nonlocal x
            x = 'Python'
        inner2()
    inner1()
    print('outer (After):',x)
outer()

# non-local at different nesting level

def outer():
    x = 'Hello'
    def inner1():
        nonlocal x
        x = 'Python'
        def inner2():
            nonlocal x
            x = 'Monty'
        inner2()
    inner1()
    print(x)
outer()

#

# x = 'python'
# def outer():
#     global x
#     x = 'Monty'
#     def inner1():
#         nonlocal x
#         x = 'Hello'
#     print(x)


x = 'python'
def outer():
    # global x
    x = 'Montty'
    def inner1():
        nonlocal x
        x = 'Hello'
    print(x)
    inner1()
    print(x)
outer()
print(x)