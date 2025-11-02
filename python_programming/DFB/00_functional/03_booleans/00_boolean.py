# Booleans: Integer subclass
# The bool class: PEP 285
# a = True
# print(isinstance(bool, int))
# print(isinstance(True, int))
# print(isinstance(a, int))

# is vs ==
# is for identity identifier to compare memory addresses
# ==: compares numerical values
# singleton object: Retain a single memory object throughout the lifetime of the application
# print(True is 1)
# print(1 is True)
# print(1 == True)
# print(True == 1)

print(id(True) == id(1))
print(id(int(True)) == id(1))
print(id(int(True)) == id(True))
print(hex(id(True)))
print(hex(id(1)))
print(id(True))
print(id(1))
print(id(int(True)))
# print(True is 1)
print(True == 1)

# Boolean as integers
print(True > False)
print((1==2)==False)
print((1==2)==0)
print(1==0)

print(True + True + True)
print((True + True + True)//2)
print(-True)
print(100*False)

# The boolean constructor
# The truth value (truthyness) of an object
print(bool(0))
print(bool(1))
print(bool(100))
print(bool(-1))
# print(help())
issubclass(bool,int)
print(type(True),id(True),int(True))
print(type(False),id(False),int(False))
print(type(3<4),id(3<4), id(3>4))
print((3<4) is True)
print(None is False)

# True and False are singleton objects

print((1==2)==False)
print(1==2==False) # chains becareful

# polymorphism
print(int(True),int(False))
print(True + 1)
print(False * 100)
print(True > False)
print((True + True + True)//2)
print(-True)
print(True and False)
print(False and True)
print(bool(0), bool(1))

# Booleans truth value
# Every object has a True value, except:
# None
# False
# 0 in any numeric type
# empty sequences (eg. List, tuple, string,...)
# empty mapping types (dictionary, set ...)
# Custom classes that implement a __bool__ or __len__ method that returns False or 0
# > Which have a False truth value

# integer

# def __bool__(self):
#     return self !=0

print(bool([1,2,3]))
print(bool([]))
print(bool(None))
print(bool('abc'))
print(bool(''))

# print(bool([])) is equivalent to
# if my_list:
    # code block
# code block will execute if and only if my_list is both not None and not empty
# this is equivalent to
# if my_list is not None and len(my_list) > 0:
#     code block

