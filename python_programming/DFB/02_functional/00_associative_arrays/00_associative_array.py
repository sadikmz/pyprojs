import sys
print(sys.hash_info)
print(sys.hash_info.width)

a = [1, 2, 3]
print(a)
print(id(a))

a.append(4)
print(a)
print(id(a))
print(hash('a'))
print(hash('a'))