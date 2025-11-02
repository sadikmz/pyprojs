x = 0.1 + 0.1 + 0.1
y = 0.3

# print(x==y)
# print(format(x,'.25'))

# option 1: round()?
# option 2: use appropriate range

# def is_equal(x,y,eps):
#     return math.fabs(x-y) < eps

# Can be tweaked by specifying that the differencem between the two numbers be a percentage of their size

# Using absolute tolerance
# print(x==y)
# print(format(x,'.25'))
# print(format(y,'.25'))

x = 0.1 + 0.1 + 0.1
y = 0.3

a = 10000.1 + 10000.1 + 10000.1
b = 30000.3

print(format(x,'.20f'))
print(format(y,'.20f'))
import math
print(math.fabs(x-y))

# combine absolute and relative tolerances

x = 1000.01
y = 1000.02
print(math.isclose(x,y))
print(math.isclose(x,y, abs_tol=1e-5))
print(math.isclose(x,y, rel_tol=1e-5, abs_tol=1e-5))

# floats: coercing to integer