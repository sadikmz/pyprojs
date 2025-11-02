# interning : re-using objects on-demand
# At start-up, Python (CPython), preloads (caches) a global list of integers in the range [-5,256]
# Any time an integer is referenced in that range, Python will use the cached version of that object.
# Singletons object: classes that can only be instantiated once.
# Optimization strategy - small integers show up often.
# Memory overhead?
# python implementations


a = 10
b = 10
print(id(a))
print(id(b))

a = 500
b = 500
print(id(a))
print(id(b))

print(a is b)