import decimal
from decimal import Decimal

a = Decimal(10)
b = Decimal('20')
c = Decimal((1,(2,3),4))
d = Decimal((1,(2,9),2))
t = (1,2,3)
# e = Decimal(t)
print(type(t))
print(a, b,c)
print(c)
print(d)
# print(help(Decimal))
# print(Decimal(0.25))

# Using the tuple constructor
# (s, (d1,d2,d3),exp), 0 if x>=0 and 1 if x < 0
a = Decimal((1,(3,1,4,1,5),-4))
a = Decimal((1,(3,1,4,1,5),4))
print(a)

# Context Precision and the Constructor
# Context precision affects mathematical operations
# Context precision doest not affect the constructor
decimal.getcontext().prec = 6
a = Decimal('0.12345')
b = Decimal('0.12345')
print(a, b)
print(a+b)

with decimal.localcontext() as ctx:
    ctx.prec = 2
    c = a + b
    print(c)
print(c)