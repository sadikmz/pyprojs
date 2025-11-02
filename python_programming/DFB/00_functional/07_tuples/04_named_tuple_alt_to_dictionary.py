from collections import namedtuple

# Using the existing dictionary using .key - returns iterable which contains - check key orders.

# Check dictionary key orders

data_dict = dict(key3=300,key2=200, key1=100)

# so keys will be printed in the order that appears in the dictionary.

for i in data_dict.keys():
    print(i)

Data = namedtuple('Data', data_dict.keys())
print(Data)

print(Data._fields)

d1 = Data(*data_dict.values()) # the pitfall is when the key:value pairs of the dictionary and named tuple not in a matching order

print(d1)

# Important to kep the order of the key:value pair to match between the named tuple and the dictionary
# Unpack it as keyword argument

data_dict = dict(key1=100, key2=200, key3=300)

for i in data_dict.keys():
    print(i)

d2 = Data(**data_dict)
print(d2)
print(d2._fields)

key_name = 'key2'
print(data_dict[key_name])

# for named tuples

print(getattr(d2, key_name))