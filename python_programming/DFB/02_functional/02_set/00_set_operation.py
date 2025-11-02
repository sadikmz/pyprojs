# create set using literal notation
s = {'a', 100, (1,2)}
print(type(s))

s = {}
print(type(s))

s  = set()
print(type(s))

s = set([1,2,3])
print(type(s))
print(s)

s  = set(range(10))
print(type(s))
print(s)

# s = set([[1,2,3],[1,2]])
print(type(s))

# passing iterables
d = {'a':1, 'b':2}
print(set(d))

# using set comprehension

s = {c for c in 'python'}
print(s)
s = set('python')
print(s)

# set unpacking

s1 = {'a','b','c'}
s2 = {10,20,30,'a'}
s = {*s1, *s2}
print(s)

l = [*s1, *s2]
print(l)
print(type(l))

# passing function
def my_func(a,b,c):
    print(a,b,c)

args = {10,20,30}
my_func(*args)

def averager(*args):
    total = 0
    for arg in args:
        total += arg
    print (total / len(args))

averager(10,20,30)


s1 = {'a','b','c', 'a',}
print(s1)

s1 = set('aabcccnbbba')
print(s1)

def scorer(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    s = s.lower()
    distinct = set(s)
    effective = distinct & alphabet
    return len(effective)/ len(alphabet)

print(scorer('abcdefghijklmnopqrstuvwxy     fjalfjaljf1111'))