# reducing function arguments
from functools import partial

def my_func(a,b,c):
    print(a,b,c)

my_func(1,2,3)

# reduce the arqument required to pass in to my_func

def f(x,y):
    return my_func(10,x,y)

f(100,200)

f = lambda x,y: my_func(10,x,y)
f(100,200)

f = partial(my_func,10)
f(20,30)

def my_func01(a,b,*args,kw1,kw2,**kwargs):
    print(a,b,kw1,kw2,kwargs)

my_func01(10,20,kw1='a', kw2= 'b', k3='c', k4='d', k5=500)

def my_func01(a,b,*args,kw1,kw2,**kwargs):
    print(a,b,kw1,kw2,kwargs)

# my_func01(10,20,kw1='a', kw2= 'b', k3='c', k4='d', k5=500)

def f01(x,*vars,kw,**kwvars):
    return my_func01(10,x,*vars, kw1='a', kw2=kw, **kwvars)

f01(20,100,200,kw='b',k3=1000, k4=2000)

f = partial(my_func01, 10, kw1='a')
f(20,100,200,kw2='b',k3=1000, k4=2000)

def pow(base,exponent):
    return base ** exponent

sq = partial(pow, exponent=2)

print(sq(5))
cu = partial(pow, exponent=3)
print(cu(5))
print(cu(base=5, exponent=2))

a = 2
sq = partial(pow, exponent=a)
print(sq(5))
a = 3
# sq = partial(pow, exponent=a)
print(sq(5))

def my_func02(a,b):
    print(a,b)


a = [1,2]

f = partial(my_func02, a)
f(100)
a.append(3)
print(a)

f = partial(my_func02, a)
f(9)

origin = (0,0)
# print(origin)
l = [(1,1),(0,2),(-3,2),(0,0),(10,10)]
dist2 = lambda a, b: (a[0]-b[0])**2 + (a[1]-b[1])**2
# print(dist2((1,1),origin))

print(sorted(l))
f = partial(dist2,origin)
print(f((1,1)))
print(sorted(l, key=f))

f = lambda x:dist2(x,origin)
print(sorted(l, key=f))
print(sorted(l, key=lambda x:dist2(x,origin) ))