# Python lists have a concept of positional order, but sets do not
#     - A list is a sequences type
#     - A set is not
# Built-in sequence types
# mutable lists byteras
# immutable strings tuples range bytes
# Additional Standard Types: collection package namedtuple
#                                                 deque
#                             array module      array

# Homogeneous vs heterogeneous Sequences

#   - strings are homogeneous sequences: each element is of the type type (a character)  eg. 'python'
# Heterogeneous sequences: each element may be a different type eg. [1, 10.5, 'python]

# Homogeneous sequences are usually more efficient (storage wise at least)
# e.g prefer using a string of character, rather than a list of tuple characters

# Iterable Types vs Sequences Types
# What does it mean for an object to be iterable?
# it is a container type of object we can list out the elements in that object one by one

# So any sequence type is iterable

# But an iterable is not necessarily a sequence type ------> iterables are more general
# eg. set, s = {1,2,3}, ----> for e in s, but can not be indexed s[1]

 # Standard Sequence Methods

 # Built-in sequence types, both mutable and immutable, support the following method
 # x in s
 # x not in s
 # len (s)
 # min(s)
 # max(s)
 # s1+s2 --> contactentaiton
 # s*n (or n * s) (n is an integer) ---> repetition
 # s.index(x) ---> index of first occurrence of x in s
 # s.index(x,i) ----> index of first occurrence of x in s at or after index of i
 # s.index(x,i,j) -----> index of first occurrence of x in s at or after index i and before index j
 # s[i] -----> the element
 # s[i:j] ----> the slice from index i to (but not including j)
 # s[i:j:k] -----> extended slice from index i, to (but not including ) j, in steps of k

 # note that slices will return in the same container type
 # range objects are restrictive:
 #    - no concatenation / repetition
 #    - min, max, in, not in not as efficient

 # Hashing

 # immutable sequence types may support hashing but not if they contain mutable types

s = 'python'

print(s)
print(s[::-1])
print(s[5:0:-1])

l = [[0,0]]
print(l)
print(id(l))
print(id(l[0]))
l2 = l * 2
print(id(l2))
print(id(l2[0]))
print(id(l2[1]))
l[0][0] = 100
print(l)
print(l2)
print(id(l2[0]))
print(id(l2[1]))