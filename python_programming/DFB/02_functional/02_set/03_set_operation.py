s1 = {1, 2, 3}
s2 = {2,3, 4}

print(s1, id(s1))
print(s2, id(s2))

s1 = s1 & s2
print(s1, id(s1))
print(s2, id(s2))

print(globals()['s1'])

# union update

s1 = {1, 2, 3}
s2 = {2,3, 4}

print(id(s1))
s1 |=s2
print(id(s1))
print(s1)
s1.update(s2)
print(id(s1))
print(s1)

# intersection
s1 = {1, 2, 3}
s2 = {2,3, 4}
print(id(s1))
s1 &= s2
print(s1)
print(id(s1))

s1 = {1, 2, 3}
s2 = {2,3, 4}
print(id(s1))
s1.intersection_update(s2)
print(id(s1))

# difference
s1 = {1, 2, 3}
s2 = {2,3, 4}
print(id(s1))
s1 -=s2
print(s1)
print(id(s1))

s1 = {1, 2, 3}
s2 = {2,3, 4}
print(id(s1))
s1.difference_update(s2)
print(id(s1))

s1 = {1, 2, 3,4}
s2 = {2,3}
s3 = {3,4}

result = (s1 - s2) - s3
print(result)
s1 -= s2 - s3
print(s1)

s1 = {1, 2, 3,4}
s2 = {2,3}
s3 = {3,4}

s1.difference_update(s2, s3)
print(s1)

# symmetric difference

s1 = {1, 2, 3,4}
s2 = {2,3}
s3 = {3,4}

print(id(s1))
s1 ^= s2^s3
print(s1)
print(id(s1))

s1 = {1, 2, 3}
s2 = {3,4,5}
s3 = {5,6,7}

print(id(s1))
s1 |= s2 | s3
print(s1)
print(id(s1))

s1 = {1, 2, 3}
print(id(s1))
s1.update([1,2,4],(5,6,7,8),'abc')
print(s1)
print(id(s1))

# or
s1 = {1, 2, 3}
print(id(s1))
s1 |= set([3,4,5]) | set([6,7,8]) | set('abc')
print(s1)
print(id(s1))

def combine(string,target):
    target.update(string.split(' '))

def cleanup(combined):
    words = {'the', 'and', 'a','or', 'is', 'of'}
    combined -= words

result = set()

combine('luberjack sleep all night', result)
combine('the ministry of silly walks', result)
combine('this parrrot is a late parrot', result)
cleanup(result)
print(result)

#
def gen_read_data():
    yield ['Paris', 'Beijing', 'New York', 'London', 'Madrid', 'Mumbai']
    yield ['Hyderabad', 'New York', 'Milan', 'Phoenix', 'Berlin', 'Cairo']
    yield ['Stockholm', 'Cairo', 'Paris', 'Barcelona', 'San Francisco']

data = gen_read_data()
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))

def filter_incoming(*ciites, data_set):
    data_set.difference_update(ciites)

result = set()
data = gen_read_data()
for page in data:
    result.update(page)
    filter_incoming('Paris', 'London', data_set=result)

print(result)