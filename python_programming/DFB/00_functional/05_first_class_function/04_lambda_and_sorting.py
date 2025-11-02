help(sorted)

l={1,2,3,4,5,33,6,7,8,9,10}
print(sorted(l))
print(sorted(l,reverse=True))

l = ['c','B','D','a']
print(sorted(l))
print(ord('A'))
print(ord('B'))
print(ord('a'))
print(ord('c'))

print(sorted(l, key=lambda x:x.upper()))

d = {'abc':1000,
     'def':400,
     'ghi':500,
     'mnp':350,
     'jkl':600 }

print(sorted(d.items()))

print(sorted(d.items(), key=lambda e:e[1]))


def dist_sq(x):
    return (x.real)**2 + (x.imag)**2

print(dist_sq(1+1j))

ll = [3+3j,1-1j,3+0j]

# print(sorted(ll))
print(sorted(ll,key=dist_sq))
print(sorted(ll,key=lambda x:(x.real)**2 + (x.imag)**2))

l = ['Cleese', 'Idle','Palin','Chapman','Gilliam','Jone']
print(sorted(l))
print(sorted(l,key=lambda x:x[-1]))

# Python use stable sort:if two elements are equal, python keeps the initial order.

