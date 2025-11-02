from functools import lru_cache

@lru_cache(maxsize=5)
def fib(n):
    print(f'fib({n}) called')
    if n <= 1:
        return n
    return  fib(n-1) + fib(n-2)
fib(10)
fib(10)
# fib(15)
