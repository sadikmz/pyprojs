# slicing

s = slice(0, 2)
print(type(s))
print(dir(s))

l = [1, 2, 3, 4, 5]

print(l[0:2])
print(l[s])

# database data formating

data = []

for row in data:
    first_name = row[0:50]
    last_name = row[50:101]
    ssn = row[101:150]

# first_name, last_name and ssn can be replaced with slice objects as follows
range_fist_name = slice(0, 51)
range_last_name = slice(51, 101)
range_ssn = slice(101, 150)

data = []

for row in data:
    first_name = row[range_fist_name]
    last_name = row[range_last_name]
    ssn = row[range_ssn]

# Slice fundamentals

l = 'python'

print(l[0:1])
print(l[0:6])
print(l[:])
print(l[0:100])

# Extended slices

print(l[0:6:2])

s1 = slice(0, 6, 2)
print(l[s1])
print(l[:4])
s1 = slice(None, 4)
print(l[s1])

start = None
print(l[start:5])

print(l[3:])

# negative value

print(l[3:0:-1])
print(l[3::-1])
print(l[3:-1:-1])
print(l[3:-1])
print(l[3:-1:1])
print(l[3:-1:3])
print("----3:-4----")
print(l[3:-4])
print("----3:-3----")
print(l[3:-3])
print("----3:-2----")
print(l[3:-2])
print("----3:-4:-1----")
print(l[3:-4:-1])
print(l[3:-4:-2])
print(l[3:-4:-3])
print("----3:-4:-1----")
print(l[3:-5:-1])

# slice object

k = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(len(k))
s = slice(1, 5)
print(s.start)
print(s.stop)
print(s.step)
print(s)
print(s.indices(10))
ind = s.indices(10)
print(k[s])
print(ind)
print(slice(1, 100, 2).indices(10))
# print(range(list(slice(1, 100, 2).indices(10))))
print(list(range(*slice(1,100,2).indices(10))))
# list(range(*slice(start, stop, step).indices(length)))
# print(range(ran))
start = None
stop = None
step = -1
length = 10
print( list(range(*slice(start, stop, step).indices(length))))

print(l[3:-1:1])
start = 3
stop = -1
step = -1
length = 6
print(list(range(*slice(start, stop, step).indices(length))))