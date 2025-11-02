# args
# Recall from iterable unpacking
# It supports the star '*' unpacking
# In a function '*' with a parameter or called *args (star args) means it supports multiple argument
# *args exhaust positional arguments
# Example:
# def func1(a,b,*args,d):
#     code

# invoking func1 as follows will not work because *args expect two or more arguments before 'd'
# func1(1,2,'a',100)

# Unpacking arguments
# def func2(a,b,):
#     code here

# l = [10,20,30]
# The above will not work: l first need to be unpacked and passed to func2

# *args
# a, b, *c = 10,20,'a','b'
# print(a,b,c)

# def func1(a,b,*c):
#     print(a)
#     print(b)
#     print(c)
#     print(type(c))


# func1(10,0,0,9)

# def ave(*args):
#     print(args)
#     print(sum(args))
#     print(len(args))
#     print(type(args))


# ave()
# ave(10,20,30,40)
# ave(1,2,3,4)
# ave()

def ave(*args):
    # print(args)
    count = len(args)
    total = sum(args)
    if count == 0:
        return 0
    else:
        return total/count

    # print(type(args))
# print(ave(1,2,3,4,5,6,7,8,9,10,100))


# short-circuiting
# def ave(*args):
#     # print(args)
#     count = len(args)
#     total = sum(args)
#     return count and total/count
#
# print(ave(1,2,3,4,5,6,7,8,9,10,100))
# print(ave(0))


# def ave(a,*args):
#     # print(args)
#     count = len(args) + 1
#     total = sum(args) + a
#     return total/count
#
# print(ave(1,2,3,4,5,6,7,8,9,10,100))
# # print(ave(0))
# print(ave())

# unpack iterable into positional argument

def func1(a,b,c,*args):
    print(a)
    print(b)
    print(c)
    print(args)

l = [10,20,30,40,50]

# pass 10, 20, and 30
# func1(l)
# func1(l,'x','y')
func1(*l)

def func2(a,b,*args):
    print(a)
    print(b)
    print(args)


# func2(10,20)
# func2(10,20,30,20,20,20)


# functions that handle arbitrary number of arguments

def func3(*args):
    count = len(args)
    total = sum(args)

    if count == 0:
        return 0
    else:
        return total/count
    # print(args)
print(func3())
print(func3(10,20))

def func3(*args):
    count = len(args)
    total = sum(args)
    # Short-circuting
    return count and total/count
    # print(args)
print(func3())
print(func3(10,20))

# Option saying you must specific one positional parameter and other optional parameters
def func3(a,*args):
    count = len(args) + 1
    total = sum(args) + a
    # Short-circuting
    return total/count
    # print(args)
# print(func3())
print(func3(10,20))


# Keyword arguments

def func3(a,b,c):
    print(a)
    print(b)
    print(c)


func3(1,10,20)
func3(c=10,b=9,a=0)

# Forcing keyword argument

def func4(a,b,*args):
    print(a,b,*args)
print(1,2,3,4,6,'a')

# force keyword arguments
def func5(a,b,c,*args,d,e):
    print(a)
    print(b)
    print(c)
    print(args)
    print(d)
    print(e)

#
func5(1,2,3,4,d=5,e=1)

# no mandatory optional parameters
def func6(*args,d):
    print(args,d)

func6(d='b')
func6(1,2,3,4,6,d='a')


# No positional parameter is allowed

def func7(*,d):
    print(d)

# func7(1,2)
func7(d=2)


# two postional parametes and keyword parameters

def func8(a,b,*,d):
    print(a,b,d)


func8(1,2,d=3)
func8(10,20,d=40)


# default vaules for keyword

def func9(a,b=2,*args,d):
    print(a)
    print(b)
    # print(d)
    print(args)
    print(d)

func9(1,2,3,4,6,d=5)


def func9(a,b=20,*args,d=0,e):
    print(a,b,args, d,e)
    # print(a)
    # print(b)
    # print(d)
    # print(args)
    # print(d)
    # print(e)


# func9(1,2,3,4,6,d=5)
func9(1,2,3,4,6,d=5,e="test")

# f
# def func10(a,b,c,*,d,e):
func9(10,1,d='good morning',e='python')

def func10(*,d):
    print(d)

# func10(190,d=20)
func10(d='a')

def func11(a,b,*, c):
    print(a,b,c)

# func11(1,2)
func11(11,22,c=1)

# default value for positional arguments

def func12(a,b=2,*args,d):
    print(a,b,args,d)

func12(10,d=1)
func12(1,d=2)

# defautl values keyword arguments

def func13(a,b=2,*args,d=0,e=True):
    print(a,b,args,d,e)

func13(1,3,4,5,d=6,e='test')
func13(1,0,4,5,d=6,e='python')

# **kwargs: Keyword arguments
# *args: is used to scoop up variable amount of remaining positional arguments to tuple
# The parameter name is arbitrary - * is the real performer

# **kwargs is used to scoop up a variable amount of remaining keyword arguments to dictionary
# The parameter kwargs is arbitrary - ** is the real performer

# **kwargs can be specified even if the positional arguments have not been exhausted (Unlike keyword-only arguments)

# No parameters can come after **kwargs

# def func14(*,d,**kwargs):
    # code

def func15(**kwargs):
    print(kwargs)

func15(a=1,b=2,c=3,d=4,e=5)
func15()

def func16(*args,c, **kwargs):
    print(args, c, kwargs)

func16(1,2,c=3,d=4,e=5)

def func17(**kwargs):
    print(kwargs)

func17(a=1,b=2,c=3,d=4,e=5)

def func18(*args, **kwargs):
    print(args, kwargs)

func18(1,2,c=3,d=4,e=5)
# func18(1,2,c=3,d=4,e=5,1)

def func19(a, b, **kwargs):
    print(a, b, kwargs)

func19(1,2,c=3,d=4,e=5)

def func20(a, b, *,d, **kwargs):
    print(a, b, d, kwargs)

func20(1,2,c=0,d=44,e=5)

def func21(a, b, **keywords):
    print(a, b, keywords)

func21(1,2,c=3,d=4)


# Putting it together

def func22(a, b, *args):
    print(a, b, args)


func22(1,2,'x','y','z')

def func23(a, b=2, c=3,*args):
    print(a, b, c, args)

func23(1,b=2)
func23(1,2,3,'x','y','z')

# func23(1)
# func23(1,b=2,c=5,'x','y','z')

def func24(a, b=2,*args,c=3,d):
    print(a, b, c, args, d)

func24(1,10,'x','z',c=3,d=3)
func24(1,2,3,'x','y','z',d=2)
func24(1,2,3,'x','y',d=0)
# func24(1,'x','y','z',b=2, d=10)
func24(1,2,3,'x','y',d=10)


def func25(a, b, *args, c=10, d= 20,**kwargs):
    print(a, b, args,c, d, kwargs)

func25(1,2, 'x','y','z',c=100,d=200,x=0.1,y=0.2)
# help(print)
# print(1,2,sep="-", end="******\n")

def calc_hi_lo_avg(*args,log_to_console=False):
    hi = int(bool(args)) and max(args)
    lo = min(args) if len(args) > 0 else 0
    avg = (hi+lo)/2
    if log_to_console:
        print('hi={0}, lo={1}, avg={2}'.format(hi,lo,avg))
    return avg


print(calc_hi_lo_avg(1,2,3,4,5))
is_debug=True
print(calc_hi_lo_avg(1,2,3,4,5, log_to_console=is_debug))

def func26(a,*,c,d):