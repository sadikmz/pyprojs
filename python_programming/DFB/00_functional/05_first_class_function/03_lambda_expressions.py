# lambda functions also called anonymous functions
# syntax for lambda expression
# lambda [parameter list - optional]: expression
# Expression is evaluated and returned the lambda function is called
# Returns a function object that evalutes and returns the expression when it's called
# it can be assigned to a variable and passed as an argument to another function
# it is a function, just like one created with def

# lambdas, or anonymous functions are not equivalent to closures

a=100
b=200
c=300
var=lambda a,b,c: 2*a +3*b +4*c
print(var(a,b,c))
print(a*2)
print(b*3)
print(c*4)
lambda x: x**2
lambda x,y: x +y
lambda : 'hello'
lambda s:s[::-1].upper()
print(type(var))
print(type(lambda a,b,c: 2*a +3*b +4*c))

lambda_func00 = lambda a: a**2
# my_func=lambda a,b,c: 2*a +3*b +4*c
print(lambda_func00(3))

# pass it to another functions
def my_func01(x,fn):
    return fn(x)

print(my_func01(3,lambda_func00))
lambda_func01 = lambda x:x[1:]*3
print(lambda_func01('310'))

lambda_func02 = lambda x:x+5

def sq(x):
    return x**2

print(sq(3))
print(type(sq))

print(lambda x=2:x**2)
lambda x,y: x+y
print(lambda x,y: x +y)


g = lambda x,y=10: x+y
print(g(1))
print(g)

f = lambda x, *args, y, **kwargs: (x,args,y,kwargs)
print(f)
print(f(1,'a','b',y=100,a=10,c=20))

f = lambda x, *args, y, **kwargs: (x,*args,y,kwargs)
print(f)
print(f(1,'a','b',y=100,a=10,c=20))

f = lambda x, *args, y, **kwargs: (x,args,y,{**kwargs})
print(f)
print(f(1,'a','b',y=100,a=10,c=20))


def apply_func(x,fn):
    return fn(x)

print(apply_func(10,sq))

print(apply_func(10,lambda x:x**2))

print(apply_func(10,lambda x:x**3))

def apply_func(fn, *args,**kwargs):
    return fn(*args, **kwargs)

apply_func(sq,3)
apply_func(lambda x:x**2,3)

print(apply_func(lambda x,*,y: x+y, 1,y=3000))
print(apply_func(lambda *args: sum(args), 1,2,3,4,5,6,7,8,9,10))
print(apply_func(sum,(1,2,3,4,5,6,7,8,9,10)))