# docstring  -> PEP 257
def fact(n):
    """Calculates n! (factorial function)

    Inputs:
        n: non-negative integer
    Returns:
        The factorial of n
    """

# print(fact.__doc__)
help(fact)

# Function Annotation PEP 3107
# - gives us an additional way to document function
# def my_funct(a: <expression>, b: <expression>) -> <expression>:
#     pass

def my_func(a: 'a string', b: 'a positive integer') -> 'a string':
    return a*b
help(my_func)

def my_func(a:'str', b:"int > 0") -> 'str':
    return a+b

def my_func(a:'str', b:[1,2,3]) -> 'str':
    return a+b

x=3
y=5
# help(my_func)
def my_func01(a: str) -> 'a repeated ' + str(max(x,y)) + ' times':
    return a*max(x,y)
help(my_func01)