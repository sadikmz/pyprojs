# def my_func(a,b=1):
#     return a*b
#
# help(my_func)

def my_func(a,b=1):
    'Returns a *b'
    return a*b


def my_func(a,b=1):
    # Some comment here
    '''Returns a *b
    Some additional docs here

    Inputs:

    Outputs:
    '''
    return a*b

# help(my_func)

# Where the docstring been stored

# print(my_func.__doc__)


def my_func(a:'annotation for a',
            b: 'annotation for b'=1)-> 'something with a long annotation':
    """Documentation for my func"""
    return a*b

# help(my_func)
# print(my_func.__doc__)
# print(my_func.__annotations__)

x=3
y=5
def my_func(a):
    return a*max(x,y)
# print(my_func('a'))


def my_func01(a: 'some character', b = max(x,y))-> 'Character a repeated ' + str(max(x,y)) + ' times':
    print(b)
    return a * max(x,y)

# print(my_func01('a'))

# print(my_func01.__annotations__)

# print(int(3)
x = 10
# print(my_func01('a'))
# print(my_func01.__annotations__)

def my_func02(a: str,
           b: 'int > 0' = 1,
           *args: 'some extra positional args',
           k1: 'keyword-only arguments1',
           k2: 'keyword-only arguments2'=100,
           **kwargs: 'some extra keyword args') -> 'something':
    print(a, b, args, k1, k2, kwargs)


# print(my_func02.__annotations__)
my_func02('1',2,3,4,5,k1=10,k3=300,k4=400)

