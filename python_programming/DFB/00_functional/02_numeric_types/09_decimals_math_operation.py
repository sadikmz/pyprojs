import decimal
from decimal import Decimal
import math

# div (//) and mod (%) operator
# should satisfy: n = d * (n//d) +(n%d)

decimal.getcontext().prec = 28
x = 0.01
x_dec = decimal.Decimal('0.01')
# print(x_dec)
root = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()

print(format(root, '1.27f'))
print(format(root_mixed, '1.27f'))
print(root_dec)

print(format(root*root, '.27f'))
print(format(root_mixed*root_mixed, '.27f'))
print(root_dec*root_dec)