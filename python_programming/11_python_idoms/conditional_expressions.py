# expr1 if condition else expr2

# With if statement
if n >=0:
    param = n
else:
    param = -n
result = foo(param)

# With conditional expression
param = n if n >=n else -n
result = foo(param)

# With no need to assign the compound expression to a variable
result = foo(n if n >=0 else -n)