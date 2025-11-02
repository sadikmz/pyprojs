# paramterizing decorators

def timed(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args,**kwargs)
        end = perf_counter()
        elapsed = end - start
        print('Run time: {0:.6f}s'.format(elapsed))
        return result
    return inner

def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-2) + calc_fib_recurse(n-1)

# def fib(n):
#     return calc_fib_recurse(n)

# print(fib(20))

#decorating fib
@timed
def fib(n):
    return calc_fib_recurse(n)

# print(fib(20))


# long way to decorate

fib = timed(fib)
print(fib(30))

#

def timed(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(10):
            start = perf_counter()
            result = fn(*args,**kwargs)
            end = perf_counter()
            total_elapsed += (end - start)

        ave_run_time = total_elapsed / 10
        print('Run time: {0:.6f}s'.format(ave_run_time))
        return result
    return inner

# decorate

def fib(n):
    return calc_fib_recurse(n)

fib = timed(fib)
print(fib(28))

# dealing with the hard-coded iteration
def timed(fn, reps):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(reps):
            start = perf_counter()
            result = fn(*args,**kwargs)
            end = perf_counter()
            total_elapsed += (end - start)

        ave_run_time = total_elapsed / reps
        print('Run time: {0:.6f}s ({1} reps)'.format(ave_run_time, reps))
        return result
    return inner


#

# decorate
def fib(n):
    return calc_fib_recurse(n)

fib = timed(fib,5)

print(fib(28))

# problems

# @timed(5,)
# def fib(n):
#     return calc_fib_recurse(n)


# fixing: create a decorator factory

def dec(fn):
    print('Running dec')

    def inner(*args, **kwargs):
        print('Running inner')
        result = fn(*args,**kwargs)
    return inner

@dec
def my_func():
    print('Running my_func')

my_func()


#

def dec_factory():
    print('Running dec_factory')
    def dec(fn):
        print('Running dec')

        def inner(*args, **kwargs):
            print('Running inner')
            result = fn(*args, **kwargs)

        return inner
    return dec

dec = dec_factory()


# def my_func():
#     print('Running my_func')

# my_func = dec(my_func)
# my_func()

@dec
def my_func():
    print('Running my_func')

my_func()

@dec_factory()
def my_func():
    print('Running my_func')
# my_func()

# is similar to

my_func = dec_factory()(my_func)
# my_func()

 # injecting some variable

def dec_factory(a, b):
    print('Running dec_factory')
    def dec(fn):
        print('Running dec')

        def inner(*args, **kwargs):
            print('Running inner')
            print('a={0}, b={1}'.format(a, b))
            return fn(*args, **kwargs)

        return inner
    return dec

dec = dec_factory(10,20)

@dec
def my_func():
    print('Running my_func')
my_func()


# other opti

@dec_factory(100,200)
def my_func():
    print('Running my_func')

# my_func()


def my_func():
    print('Running my_func')

# the long syntax
my_func = dec_factory(150,250)(my_func)
my_func()


# dealing with timed

# dealing with the hard-coded iteration
# def timed(fn, reps):
#     from time import perf_counter
#
#     def inner(*args, **kwargs):
#         total_elapsed = 0
#         for i in range(reps):
#             start = perf_counter()
#             result = fn(*args,**kwargs)
#             end = perf_counter()
#             total_elapsed += (end - start)
#
#         ave_run_time = total_elapsed / reps
#         print('Run time: {0:.6f}s ({1} reps)'.format(ave_run_time, reps))
#         return result
#     return inner
#


def dec_factory(reps):
    def timed(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args,**kwargs)
                end = perf_counter()
                total_elapsed += (end - start)

            ave_run_time = total_elapsed / reps
            print('Run time: {0:.6f}s ({1} reps)'.format(ave_run_time, reps))
            return result
        return inner
    return timed

# will return the timed decorator

@dec_factory(5)
def fib(n):
    return calc_fib_recurse(n)

fib(28)

@dec_factory(15)
def fib(n):
    return calc_fib_recurse(n)

fib(28)


# clean up dec_factory and call it timed

def timed(reps):
    def dec(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args,**kwargs)
                end = perf_counter()
                total_elapsed += (end - start)

            ave_run_time = total_elapsed / reps
            print('Run time: {0:.6f}s ({1} reps)'.format(ave_run_time, reps))
            return result
        return inner
    return dec

@timed(15)
def fib(n):
    return calc_fib_recurse(n)
print(fib(28))