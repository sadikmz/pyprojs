from math import sqrt

s = [1, 2, 3]
len(s)
print(s)

print(sqrt(s[1]))


def func_1():
    print('running func_1')


func_1()


def func_2(a: int, b: int):
    print('running func_2')
    return a * b


print(func_2([2, 3], 3))
print(func_2('a', 2))


def func_3():
    return func_4()

def func_4():
    return 'Running func_4()'

print(func_3())


# using lambda
# print(type(func_3()))
lambda x: x**2

fn1 = lambda x: x**2
print(fn1(12))