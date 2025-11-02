def process(s):
    print('Initial s # = {}'.format(id(s)))
    s = s + 'world'
    print('Final s # = {}'.format(id(s)))

# my_var = 'Hello'
# print('my_var # = {}'.format(id(my_var)))
# print(process(my_var))


def modify_list(lst):
    print('Initial lst # = {}'.format(id(lst)))
    lst.append(100)
    print('Final lst # = {}'.format(id(lst)))

# my_list = [1, 2, 3]
# print(id(my_list))
# modify_list(my_list)
#
# print(my_list)

# def modify_tuple(t):
#     print('Initial t # = {}'.format(id(t)))
#     t[0].append(100)
#     print('Final t # = {}'.format(id(t)))
#
# my_tuple = ([1, 2], 'a')
#
# print(id(my_tuple))
# modify_tuple(my_tuple)
# print(my_tuple)

# shared reference

a  = 'hello'
b = a

print(hex(id(a)))
print(hex(id(b)))

b = 'hello'

print(hex(id(b)))
b = 'hello world'
print(hex(id(b)))
print(hex(id(a)))

a = [1, 2, 3]
b = a
print(hex(id(a)))
print(hex(id(b)))

b.append(100)
print(hex(id(b)))
print(hex(id(a)))
print(a)
print(b)

a = 10
b = 10
print(hex(id(a)))
print(hex(id(b)))

a = 5000
b = 5000
print(hex(id(a)))
print(hex(id(b)))