# time decorator pseudocode
from datetime import timedelta


def my_func(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(10): # iteration is hard coded restricting to 10 iteration
            start = perf_counter()
            result = fn(*args, **kwargs)
            total_elapsed += (perf_counter() - start)
        avg_elapsed = total_elapsed / 10
        print(avg_elapsed)
        return result
    return inner

# Decorated time

@timed
def my_func():
    if ...:

# or
# my_func = timed(my_func)

# One approach: add reps parameter into timed function
def my_func(fn, reps):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(reps):
            start = perf_counter()
            result = fn(*args, **kwargs)
            total_elapsed += (perf_counter() - start)
        avg_elapsed = total_elapsed / reps
        print(avg_elapsed)
        return result

    return inner

# decorate
# my_func = timed(my_func, reps=10)

# Rethining the solution

@timed
def