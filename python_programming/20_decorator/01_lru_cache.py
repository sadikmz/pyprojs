from functools import lru_cache
@lru_cache(maxsize=2)
def add(a, b):
    print('add called...')
    return a + b

add(1, 2)
add(1, 3)
add(1, 1)
add(1, 2)
add(1, 2)
add(1, 2)
add(1, 2)
add(1, 3)
add(1, 3)
add(1, 3)
add(1, 1)
add(1, 1)
# add(1, 2)


