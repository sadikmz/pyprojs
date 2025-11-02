# def fib(n):
#     if n <= 1:
#         return n
#     return  fib(n-1) + fib(n-2)


# print(fib(4))


def fib(n):
    print(f'fib({n}) called')
    if n <= 1:
        return n
    return  fib(n-1) + fib(n-2)

fib(3)