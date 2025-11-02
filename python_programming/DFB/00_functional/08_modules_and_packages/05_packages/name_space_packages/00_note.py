a, b = "Hello", "world"

print(f"{a}, {b}")
print(f"a={a}, b={b}")



# timeit

from timeit import timeit
import math
from math import sqrt

print(timeit(stmt='math.sqrt(2)', setup='import math'))
print(timeit(stmt='sqrt(2)', setup='from math import sqrt'))
print(timeit(stmt='sqrt(2)', globals=globals()))