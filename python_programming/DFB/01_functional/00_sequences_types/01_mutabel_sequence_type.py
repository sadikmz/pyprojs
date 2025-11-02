# mutating an object means changing the object's state without creating a new object
# concatentation vs append

# mutating using []
# s[i] = x    ----> element at index i is replaced with x
# s[i:j] = s2 ----> slice replaced by the contents of the iterable s2
# del s[i]    ----> removes element at index i
# del s[i:j]  ----> removes entire slice

# We can assign to extended slice s[i:j:k] = s2

# some methods supported by mutable sequences types such as lists
# s.clear()
# s.append()
# s.insert(i,x)
# s.extend(iterable)
# s.pop()
# s.remove()
# s.reverse()
# s.copy()             -----> returns a shallow copy
# many more ...
#

l = [1,2,3,4,5]
print(id(l))

l[0] = 'a'
print(id(l))

l.clear()
print(l)
print(id(l))


suites = ['Spades', 'Hearts', 'Dimonds', 'Clubs']

alias = suites
print(id(suites))
print(id(alias))
alias.clear()
print(suites)


def something(l):
    l.clear()

something(suites)

print(suites)
# print()


l = [1,2,3,4,5]
print(id(l))
print(l[0:2])

l[0:2] = ('a', 'b')
print(l)
print(id(l))
# help(l.copy())

l =[['a','b'],'c''d']
print(id(l))
print(type(l))
l[1] ='a'

l = [[1,2],3,4,5]
print(id(l))
print(type(l[1]))
l2 = l.copy()
print(id(l2[1]))

l = [['a', 'b'], 'c''d']
l2 = l.copy()
l[0].append('x')
print(l, l2)