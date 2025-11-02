# identity operator -is: memory address
# equality operator (==): Object state (data)

# None object: They are not set - empty value
# Python memory manager will use a shared reference when assigning a variable to None

a = None
b = a
print(a is None)
print(b is None)
a = 10
print(a is not None)