# print(round(100.9876,n=100))
from math import copysign

# print(help(round))
# print(round(10489.875562626439))
# print(round(10489.875562626439, None))
# print(round(10489.875562626439, ndigits=1))
# print(round(10489.875562626439, ndigits=0))
# print(round(1.25,1)) # rounding to nearst, with ties away from zero
# print(round(-1.25,1)) # rounding to nearst, with ties away from zero
# print(round(1.35,1)) # rounding to nearst, with ties away from zero
# rounding to nearst, with ties away from zero
# Banker's Rounding: IEE 745 standard
# print(round(-1.35,1))
# print(round(1.45,1))
# print(round(-1.65,1))
print(round(1.15,1))
print(round(1.25,1))
print(round(1.35,1))
print(round(1.45,1))
print(round(1.55,1))
print(round(1.65,1))
print(round(1.75,1))
print(round(1.85,1))
print(round(1.95,1))

# print(round(10.15,-1))
# print(round(1.25,-1))
# print(round(1.35,-1))
# print(round(1.45,-1))
# print(round(1.65,-1))
# print(round(1.75,-1))
# print(round(1.85,-1))
# print(round(1.95,-1))

# sign(x) * int(abs(x)+0.5)
# copysign()

def round_up(x):
    from math import fabs, copysign
    return copysign(1,x) * int(fabs(x) + 0.5)
print(round_up(10.5))

def round_down(x):
    from math import copysign
    return int(x + copysign(0.5,x))

print(round_down(10.5))