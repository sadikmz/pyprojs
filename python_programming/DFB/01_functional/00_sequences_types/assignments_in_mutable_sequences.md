**Assigning values via index, slice and extended slices**
- indexing: [i]
- slice: [i:j] or slice(i,j)
- extended slice: [i:j:k] or slice(i,j,k), if k=1, then it's just a standard slice
- Mutable sequencers support assignment via a specific index and they also support assignment via slices
- The value being assigned via slice and extended slicing must be an iterable (any iterable, not just a sequence type)

**Replacing a slice**
- A slice can be replaced with another iterable 
- For regular slices (non-extended), the slice and the iterable need not be the same length.

[//]: # (hi there &nbsp;&nbsp;hi there&nbsp;&nbsp;&nbsp;hihtere)

l = [1,2,3,4,5] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; l[1:3]---> [2,3]

l[1:3] = [10,20,30] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; l -----> [1,10,20,30,4,5]

- The list l was mutated ----> id(l) did not change
- with extended slicing, the extended slice and the iterable must have the same length

l = [1,2,3,4,5] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; l[0:4:2]------> [1,3]

l[0:4:2] = [10,30] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; l ------> [10,2,30,4,5]

- The list l was mutated

**Deleting a slice**
- Deletion is a special case of replacement 
- We simply assign an empty iterable -----> works for a standard slice only (Extended slicing replacement needs same length)

l = [1,2,3,4,5] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; l[1:3] ----> [2,3]

l[2:3] = [] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; l -----> [1,2,4]

The list l was mutated

**Insertion using slicing**
- We can insert elements using alice assignment.
- The slice must be empty - otherwise it would just replace the element in the slice 

l = [1,2,3,4,5] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; l[1:1] ----> []

l[2:3] = 'abc' &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; l -----> [1,'a','b','c' 2,4]

- The list l was mutated
- This will not work with extended slicing.