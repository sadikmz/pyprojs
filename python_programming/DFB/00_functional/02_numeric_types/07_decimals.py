# PEP324
# infinit binary expression for float 0.1 : We dont have exact binary expression in computer memory
# contexts
# precision during arithmetic operations
# rounding algorithm

# context manager

import decimal
from decimal import Decimal

# context: something that specifies certain properties that will affect how the decimals work

print(decimal.getcontext())
print(decimal.getcontext().prec)
print(decimal.getcontext().rounding)

decimal.getcontext().prec = 6
print(decimal.getcontext())

g_ctx = decimal.getcontext()
g_ctx.rounding = decimal.ROUND_UP
print(g_ctx)

g_ctx.prec = 28
g_ctx.rounding = decimal.ROUND_HALF_EVEN
print(g_ctx)
# reset
decimal.getcontext()
print(decimal.getcontext())

# local context
decimal.localcontext()

x = Decimal('1.25')
y = Decimal('1.35')

# print(type(decimal.getcontext()))
with decimal.localcontext() as ctx:
    print(type(ctx))
    print(ctx.prec)
    ctx.prec = 6
    ctx.rounding = decimal.ROUND_HALF_UP
    print(ctx)
    print(decimal.getcontext())
    print(id(ctx) == id(decimal.getcontext()))
    # Rounding
    print(round(x, 1))
    print(round(y, 1))
print(round(x, 1))
print(round(y, 1))
