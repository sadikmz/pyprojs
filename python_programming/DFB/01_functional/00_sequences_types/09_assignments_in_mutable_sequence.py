l = [1, 2, 3,4,5]
print(id(l))

# Replacement
l[0:3] = 'python'
print(id(l))
print(l)

# Deletion
l = [1, 2, 3,4,5]
print(id(l))

print(l)
l[2:5] = []
print(id(l))
print(l)

l = [1, 2, 3,4,5]
print(id(l))

l[2:5] = ''
print(id(l))
print(l)

# Insertion

l = [1, 2, 3,4,5]
print(id(l))

l[2:2] = ('a',100,200)
print(id(l))
print(l)

# Insertng any iterable
l = [1, 2, 3,4,5]
print(id(l))

l[0:3] = {100,'X','a'}
print(id(l))
print(l)

# Replacement for extended slices: We cannot do insertions and deletions using extended slicing
# Replacement length should be equal in length.

l = [1, 2, 3,4,5]
print(id(l))
l[0:5:2] = 'abc'

print(id(l))
print(l)


l = [1, 2, 3,4,5]
print(id(l))
l[0:5:2] = [1,3,5]

print(id(l))
print(l)


# Using different length

# l = [1, 2, 3,4,5]
# print(id(l))
# l[0:5:2] = 'abcd'
#
# print(id(l))
# print(l)
