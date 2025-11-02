l1 = [1,2,3]

l1_copy = []

for item in l1:
    l1_copy.append(item)

print(l1, l1_copy)
print(id(l1), id(l1_copy))

l1_copy = [item for item in l1]

print(l1, l1_copy)
print(id(l1), id(l1_copy))

l1_copy = l1.copy()

print(id(l1), id(l1_copy))

l1 = (1,2,3)
l1_copy = list(l1)
print(l1, l1_copy)
print(id(l1), id(l1_copy))


l1 = [1,2,3]

l1_copy = l1[:]

print(l1, l1_copy)
print(id(l1), id(l1_copy))

t1 = (1,2,3)
t1_copy = t1[:]
print(t1, t1_copy)
print(id(t1), id(t1_copy))


import copy

l1 = [1,2,3]
l2 = copy.copy(l1)
print(l1, l2)
print(id(l1), id(l2))

t1 = (1,2,3)
t1_copy = copy.copy(t1)
print(t1, t1_copy)
print(id(t1), id(t1_copy))


# Deep copies

v1 = [0,0]
v2 = [0,0]

line1 = [v1,v2]
line2 = line1.copy()
print(id(line1), id(line2))
print(id(line1[0]), id(line2[0]))

line2 = [v for v in line1]
print(id(line1[1]), id(line2[1]))
print(line1, line2)

line1[0][0]  = 100
print(line1, line2)

# deep copy

line2 = [v.copy() for v in line1]
print(id(line1), id(line2))
print(id(line1[0]), id(line2[0]))
print(line1[0], line2[0])

line1[0][0] = -100
print(line1, line2)

v1 = [1,1]
v2 = [2,2]
v3 = [3,3]
v4 = [4,4]

line1 = [v1,v2]
line2 = [v2,v3]

plane1 = [line1, line2]

print(plane1)
plane2 = [line.copy() for line in plane1]
print(plane2)

print(id(plane1), id(plane2))
print(id(plane1[0]), id(plane2[0]))
print(plane1[0], plane2[0])
print(id(plane1[0][0]))
print(id(plane2[0][0]))
plane1[0][0][0] = 100
print(plane1)
print(plane2)
plane2[0][0][1] = 100
print(plane1)
# print(id(plane1[0][0]))
# print(id(plane2[0][0]))

v1 = [1,1]
v2 = [2,2]
v3 = [3,3]
v4 = [4,4]

line1 = [v1,v2]
line2 = [v2,v3]

plane1 = [line1, line2]
plane2 = copy.deepcopy(plane1)
print(plane1)
print(plane2)
plane2[0][0][1] = 100
print(id(plane1[0][0]))
print(id(plane2[0][0]))
print(id(plane1), id(plane2))
print(plane1)
print(plane2)