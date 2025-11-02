# In-place concatenation

l1 = [1,2,3,4]
l2 = [5,6]

print(id(l1))
print(id(l2))

# Concatenate
l1 = l1 + l2
print(id(l1))
print(id(l2))
