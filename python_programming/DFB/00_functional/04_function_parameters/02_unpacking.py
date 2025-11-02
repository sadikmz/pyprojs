from turtledemo.forest import doit1

(a,b,c,d) = 1,2,3,4
a,b,c ='XYZ'
print(type((a,b,c,d) ))
a,b = 10,20

print(a,b)

for e in '1-0-20hello':
    print(e)

# swapping
a=10
b=20
print('a={a}\tb={b}'.format(a=a,b=b))
a,b = b,a
print('a={a}\tb={b}'.format(a=a,b=b))

# The use case of *
l = [1,2,3,4,5]
l={"a":1,"b":2,"c":3}
# a,b = l[0],l[1:]
# l={"a":1,"b":2,"c":3}
# print('a={a}\tb={b}'.format(a=a,b=b))
# a,*b = l
# print('a={a}\tb={b}'.format(a=a,b=b))

a,*b = [-10,5,2,100]
print('a={a}\tb={b}'.format(a=a,b=b))
a,*b =  (-10,5,2,100)
print('a={a}\tb={b}'.format(a=a,b=b))
l1 = [1,2,3,4,5]
l2 = ["a","b","c","d"]
print(l2)
*c, = l1
*d, = *l1, *l2
print(c)
print(d)

s1 = {1,2,3,4,5}
s2 = {3,4,5}
s3 = *s1, *s2
s4 = {*s1,*s2}
print(s3)
print(s4)
print(type(s3))
print(s1.union(s2))


# dictionaries

d1 = {'key1':1,'key2':2,'key3':3}
d2 = {'key2':5,'key3':3,'key4':4}
d3 = {*d1,*d2}
d4 = {**d1,**d2}
print(d3)
print(d4)

d5 = {'key1':1,**d2}
print(d5)

# Nested unpacking

a,b,e = [1,2,'XY']
c,d = e
# print(a,b,c,d,e)
# a,b,(c,d) = (1,2,'XY')
# print(a,b,c,d)
a,b,(c,d,*e) = [1,2,'python']
# print(a,b,c,d,e)

# using slicing
# l = [1,2,3,4,'whateverishere']
l = (1,2,3,4,['a','b','c','d','f','g'])
a,*b,(c,d,*e) = l
print(a,b,c,d,e)
# print(l[0],l[1:4],l[4])
# print(l[0],l[1:4],l[-1])
# print(l[0],l[1:4],l[-1][0:1], l[-1][1:2], list(l[-1][2:]))
# l3= l[0],l[1:4],l[-1][0:1], l[-1][1:2], list(l[-1][2:])
# print(type(l3))
# print(l[0],l[1:4],l[-1][0:1], l[-1][1:2], list(l[-1][2:]))
print(l[0],l[1:4],l[-1][0], l[-1][1], list(l[-1][2:]))
# a,*b,(c,d,*e) = l[0],l[1:4],l[-1][0:1], l[-1][1:2], list(l[-1][2:])
print(a,b,c,d,e)
# a,b,c,d,e = l[0],l[1:4],l[-1][0:1], l[-1][1:2], list(l[-1][2:])
# print(a,b,c,d,e)