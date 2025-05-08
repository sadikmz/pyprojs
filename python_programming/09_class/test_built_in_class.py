test = ()
# print(bool(test))

# if bool(test) == False:
#     print("Yes it is. It was False")

# The int class
# print(int())

s = "7f"
print(int(s,16))

# The float class
print(float("3.14"))

test_list = [2,3,5,7,11,13,17,19,23,29,31]
test_tuple = (2,3,5,7,11,13,17,19,23,29,31)
print(list())
print(tuple())
print(type(test_list))
print(type(test_tuple))

backup = list("data")
print(backup)
backup = tuple("data")
print(backup)

backup = (17,)
print(backup)

# str class

print('Hello')
print("Don't")
''' Start here

End here
'''

"""
Start

End
"""
print("Don't")

# The set and frozenset classes

test_set = {0}
test_set = set()
test_set = frozenset()
print(type(test_set))

test_set = set("testset")
print(test_set)

# The dict class
test_dict = dict()
pairs = [(1,2),(3,9 )]
test_dict = dict(pairs)

print(type(test_dict))
print(test_dict)