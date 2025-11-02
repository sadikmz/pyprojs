s1 = {1, 2, 3}
s2 = {2, 3, 4}

print(s1.intersection(s2))
print(s1.union(s2))

a = 0b101010
b = 0b110100

print(a)
print(b)
c =a & b
print(type(a))
print(True & False)
print(bin(a))
print(bin(b))
print(bin(c))

c = a | b
print(bin(a))
print(bin(b))
print(bin(c))

# x xor y ----> True if x is True or Y is True, but not both
c = a ^ b
print(bin(a))
print(bin(b))
print(bin(c))

l1 = 2
l2 = 3
print(id(l1))
l1 +=l2
print(id(l1))
