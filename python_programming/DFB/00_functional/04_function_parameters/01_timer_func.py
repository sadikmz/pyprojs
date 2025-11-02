import time

def time_it(fn,*args, rep =1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start)/rep

print(time_it(print,1,2,3,sep=' - ', end=' ***\n', rep=1))

def compute_power_1(n,*,start=1,end):
    # using a for loop
    result = []
    for i in range(start,end):
        result.append(n ** i)
    return result

print(compute_power_1(n=2,start=1,end=5))


def compute_power_2(n,*,start=1,end):
    # Using a list comprehensition
    return [n**i for i in range(start,end)]

print(compute_power_2(n=2,start=1,end=5))

# Using generators

def compute_power_3(n,*,start=1,end):
    # using generators
    return (n**i for i in range(start,end))

# print(list(compute_power_3(n=2,start=1,end=5)))
#
# print(time_it(compute_power_1,2,start=0,end=20000,rep=5))
# print(time_it(compute_power_2,n=2,start=0,end=20000,rep=5))
# print(time_it(compute_power_3,2,start=0,end=20000,rep=5))

a = (2**i for i in range(5))
print(a)
print(list(a))