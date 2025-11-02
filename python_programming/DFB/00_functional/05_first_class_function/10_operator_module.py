# Arithmetic functions
import operator
from operator import floordiv, is_not, concat, contains, itemgetter, attrgetter, methodcaller

from numpy.ma.core import negative

# add()
# mul()
# pow()
# mod()
# floordiv()
# neg(a)
# lt(a,b)
# gt(a,b)
# eq(a,b)
# ne(a, b)
# is_not(a,b)
# is_(a,b)
# concat(s1,s2)
# contains(s,val)
# print(operator.neg(10))
# itemgetter
# attrgetter
# help(negative)
# all the list of methods in operator class including dunder (source: https://stackoverflow.com/questions/1911281/how-do-i-get-list-of-methods-in-a-python-class)
method_list = [func for func in dir(operator) if callable(getattr(operator, func))]
# all the list of methods in operator class dunder excluded

method_list = [func for func in dir(operator) if callable(getattr(operator, func)) and not func.startswith('_')]


# for func in method_list:
#     print(func)

print (dir(operator))
# help(operator.iadd)
# print(operator.iadd(-1,20))
help(operator.getitem)
# itemgetter
s = [1,20,3,4]
f=itemgetter(1,2,3)
print(f(s))

# attrgetter: attribute getter

# my_obj=[]
def my_obj():
    return "test"


my_obj.a = 100
my_obj.b = 20
my_obj.c = 30

f = attrgetter('a')
print(f(my_obj))
f = attrgetter('b')
print(f(my_obj))

print(attrgetter('a','b', 'c')(my_obj))

# Calling another callable

s = 'python'
# print(s.upper())
f = attrgetter('upper')
# print(type(f(s)))
print(f(s)())
print(attrgetter('upper')(s)())

# method caller
print(methodcaller('upper')(s))

import operator

# print(dir(operator))

print(operator.add(1,2))
print(operator.mul(1,2))
print(operator.sub(1,2))
print(operator.truediv(1,2))
print(operator.truediv(2,2))
print(operator.floordiv(1,2))
print(operator.truediv(2,2))


from functools import reduce

result = reduce(lambda x,y: x*y, [1,2,3,4])
print(result)
resutl = reduce(operator.mul, [1,2,3,4])
print(resutl)

print(operator.lt(1,2))

from operator import  is_
print(is_('abc','bcd'))
print(operator.truth([1]))

# Attribute getters and setters

my_list = [1,2,3,4]

print(my_list[1])

print(operator.getitem(my_list, 1))
print(operator.getitem(my_list, 2))
del my_list[3]
print(my_list)

my_list = [1,2,3,4]

print(operator.setitem(my_list, 1,100))
print(my_list)

print(operator.delitem(my_list, 3))
print(my_list)

f = operator.itemgetter(1,2)
print(f)

print(f('python'))

print(f(my_list))


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self):
        print("Test method runnning.....")

obj = MyClass()


print(obj.test)


property_a = operator.attrgetter('a')

print(property_a(obj))



property_ab = operator.attrgetter('a','b','test')

print(property_ab(obj))


# using lambda
f = lambda x: x.a
print(f(obj))

a = 5+10j

l = [5-10j,3+3j,2-100j]

print(sorted(l, key=lambda x: x.real))
print(sorted(l, key=operator.attrgetter('real')))

l = [(2,3,4),(1,2,5),(6,),(4,10)]
print(sorted(l, key=lambda x: x[0]))
print(sorted(l, key=operator.itemgetter(0)))

obj = MyClass()

f = operator.attrgetter('test')
# print(f(obj))
f(obj)()
f = operator.methodcaller('test')
f(obj)


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20

    def test(self,c):
        print(self.a, self.b, c)

obj = MyClass()

obj.test(100)

operator.methodcaller('test',100)(obj)
