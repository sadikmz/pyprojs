# Closure: You can think of the closure as a function plus and extended scope that contains teh free variables.
# The free variable's value is the object the cell points to - to that could change over time!
# Every time the function is the closure is called and the free variable is references - python looks up the cell object, and then whatever the cell is pointing to
from numpy.ma.core import inner


# def outer():
#     a = 100
#
#     # Closure starts
#     x = 'python'
#
#     def inner():
#         a = 100 # Local variable
#         print('{0} rocks!'.format(x))
#     # Closure ends
#
#     return inner
#
# fn = outer() # fn -> inner + extended scope x
#
# # Introspection
#
# def outer():
#     a = 100
#     x = 'python'
#     def inner():
#         a = 10 # local variable
#         print('{0} rocks!'.format(x))
#     return inner
#
# fn = outer()
#
# fn.__code__.co_freevars # free variables and returns all free variables in tuples
# fn.__closure__ #
#
#
# def outer():
#     a = 100
#     x = 'python'
#     print(hex(id(x)))
#     def inner():
#         a = 10  # local variable
#         print(hex(id(x)))
#         print('{0} rocks!'.format(x))
#
#     return inner
#
# fn = outer()
#
#
# # modifying free variables
#
# def counter():
#     count = 0
#
#     def inc():
#         nonlocal count
#         count += 1
#         return count
#     return inc
#
# fn = counter()
# print(fn())
# print(fn())
# print(fn())
#
# # Multiple instance of closure
#
# def counter():
#     count = 0
#
#     def inc():
#         nonlocal count
#         count += 1
#         return count
#     return inc
#
# f1 = counter()
# f2 = counter()
#
# print(fn.__closure__)
# print(f1.__closure__)
# # print(f2.__closure__)
#
# # Shared extended scopes
#
# def outer():
#     count = 0
#
#     def inc1():
#         nonlocal count
#         count += 1
#         return count
#
#     def inn2():
#         nonlocal count
#         count += 1
#         return count
#
#     return inc1, inn2
#
# f1, f2 = outer()
#
# print(f1())
# print(f2())
# print(f1())
# print(f2())
# print(f1())
# print(f2())
#
#
# def adder(n):
#     def inner(x):
#         return n + x
#     return inner
# adder_1 = adder(1)
# adder_2 = adder(2)
# adder_3 = adder(3)
#
#
# # nested closure
#
# def increment(n):
#     # inner
#     def inner(start):
#         current = start
#         # inc + current + n is a closure
#         def inc():
#             nonlocal current
#             current += n
#             return current
#         return inc
#     return inner
#
# fn = increment(2)
#
# inc_2 = fn(100)
# print(inc_2())
# print(inc_2())
# print(inc_2())
#
#
# #
# def outer():
#     x = 'python'
#     def inner():
#         print(x)
#     return inner
# fn = outer()
# print(fn.__code__.co_freevars)
# print(fn.__closure__)

# def outer():
#     x = [1, 2, 3]
#     print(hex(id(x)))
#     def inner():
#         x = [1,2,3]
#         print(hex(id(x)))
#     return inner

# fn = outer()
# fn()

def outer():
    x = [1, 2, 3]
    print(hex(id(x)))
    def inner():
        y = x
        print(hex(id(y)))
    return inner

fn = outer()
print(fn.__closure__)
fn()


#  Closure to modify the free variable

def outer():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
fn = outer()
print(fn.__code__.co_freevars)
print(fn.__closure__)
print(hex(id(0)))
# fn()


print(fn())
print(fn.__closure__)
print(hex(id(1)))


def outer():
    count = 0
    def inc1():
        nonlocal count
        count += 1
        return count
    def inc2():
        nonlocal count
        count += 1
        return count
    return inc1, inc2

fn1, fn2 = outer()

print(fn1.__code__.co_freevars)
print(fn2.__code__.co_freevars)
print(fn1.__closure__)
print(fn2.__closure__)
print(fn1())
print(fn1.__closure__)
print(fn2())
print(fn2.__closure__)


# Closures with different scopes

def pow(n):
    def inner(x):
        return x ** n
    return inner
square = pow(2)
print(square.__closure__)
print(square)
print(square(5))

cube = pow(3)
print(cube.__closure__)
print(hex(id(2)))
print(hex(id(3)))

print(square(5))


# Caveat: inadvertently created labels shared between scopes

def adder(n):
    def inner(x):
        return x + n
    return inner

adder_1 = adder(1)
adder_2 = adder(2)
adder_3 = adder(3)

print(adder_1.__closure__)
print(adder_2.__closure__)
print(adder_3.__closure__)

print(adder_1(10))
print(adder_2(10))
print(adder_3(10))

# using a loop

adders = []

for n in range(1,4):
    adders.append(lambda x: x + n)

print(adders)

print(adders[0].__closure__)

print(adders[0](11))
print(adders[1](11))
print(adders[2](12))
# print(adders[3](10))




def create_adders():
    adders = []
    for n in range(1,4):
        adders.append(lambda x: x + n)
    return adders

adders = create_adders()
print(adders)
print(adders[0].__closure__)
print(adders[1].__closure__)
print(adders[2].__closure__)
print(adders[0](10))
# print(adders[1](11))


# Evaluation what happens when python creates a function vs when it evaluates
# Solultion: set a default value

def create_adders():
    adders = []
    for n in range(1,4):
        adders.append(lambda x, y=n: x + y ) # Defaults get evaluated at creation time
    return adders

adders = create_adders()

print(adders)

print(adders[0].__closure__)
print(adders[1].__code__.co_freevars)
print(adders[0](10))
print(adders[0]( 10,5))
print(adders[1](10,5))
print(adders[2](10,5))
# print(adders[3](10,5))
# print(adders[4](10,5))
# print(adders[5](10,5))