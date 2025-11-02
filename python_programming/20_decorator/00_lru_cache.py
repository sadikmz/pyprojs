
# Unbounded cache
def cache(func):
    print('Initializing cache...')
    cache_dict = {}
    def inner(*args):
        if args in cache_dict:
            print('Cache hit')
            return cache_dict[args]
        else:
            print('Cache miss')
            result = func(*args)
            cache_dict[args] = result
            return result
    return inner


@cache
def add(a,b):
    print('add running')
    return a+b

@cache
def multiply(a,b):
    print('multiply running')
    return a*b

# print(add.__closure__,multiply.__closure__)

add(1,2)
add(1,2)
add(1,3)
add(1,2)
multiply(1,2)
multiply(1,2)