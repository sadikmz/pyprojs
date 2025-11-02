from decimal import Decimal
import sys

a = 3.1415
b = Decimal('3.1415')

print(sys.getsizeof(a))
print(sys.getsizeof(b))

import time
#
# def run_float(n=1):
#     a = 3.1415
#     for i in range(n):
#         a / a
#         # a = 3.1415
#
#
# def run_decimal(n=1):
#     a = 3.1415
#     for i in range(n):
#         a / a
#         # a = Decimal('3.1415')

# n = 100000000
# start = time.perf_counter()
# run_float()
# end = time.perf_counter()
# print('float: ', end - start)
#
# start = time.perf_counter()
# run_decimal()
# end = time.perf_counter()
# print('decimal: ', end - start)

import math
n = 50000000000000
def run_float(n=1):
    a = 3.1415
    for i in range(n):
        # a / a
        # a = 3.1415
        math.sqrt(a)



def run_decimal(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        # a / a
        # a = Decimal('3.1415')
        a.sqrt()



start = time.perf_counter()
run_float()
end = time.perf_counter()
print('float: ', end - start)

start = time.perf_counter()
run_decimal()
end = time.perf_counter()
print('decimal: ', end - start)