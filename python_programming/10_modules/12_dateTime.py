# dateutil
# pytz
import time
## modules
# time
# datetime

# time module

from time import perf_counter, sleep

perf_counter()

t1 = perf_counter()
sleep(1)
t2 = perf_counter()

# print(t1)
# print(t2)
print(t2 - t1)
print(time.gmtime(0))
print(time.time())