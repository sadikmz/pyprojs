# binary64
# Representation: decimal
# Numbers can be represented as base-10 integers and fractions
# help(float)
# Internal representation being infinit
from fractions import Fraction
print(float(10))
print(float(10.4))
print(float(Fraction(11,10)))
print(0.1)
print(format(0.125, '.25f'))

a = 0.1 + 0.1 + 0.1
b = 0.3
print(a==b)
print(format(a,'.25'))
print(format(b,'.25'))
