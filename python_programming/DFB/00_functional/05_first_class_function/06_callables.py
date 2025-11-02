# callable
import math

print(callable(divmod))

# Different types of callable()
# in class object callables call __name__

print(callable(print))
print(callable(math.ceil))

l = [1,2,3]
print(callable(l.append))

s='abc'

print(callable(s.upper))
print(callable(str.upper))

result = s.upper()
print(callable(result))
print(result)

from decimal import Decimal

print(callable(Decimal))
a = Decimal('10.4')
print(callable(a))
print(type(a))

class MyClass:
    def __init__(self,x=0):
        print('Initializing....')
        self.counter = x
        # self.x = x

print(callable(MyClass))
a = MyClass(100)
print(a)
print(callable(a))


class MyClass:
    def __init__(self,x=0):
        print('Initializing....')
        self.counter = x
        # self.x = x

    def __call__(self,x=1):
        print('Updating counter....')
        self.counter += x

b = MyClass(100)
# print(b)
# print(callable(b))
# class MyClass:
MyClass.__call__(b,10)
# print(MyClass.__call__(b,10))
print(callable(b))
b.counter = 1
b(100000)
print(b.counter)