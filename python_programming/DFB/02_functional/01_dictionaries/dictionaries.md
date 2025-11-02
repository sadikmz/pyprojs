**Dictionaries**
*Creating dictionaries*
- literal, dict(), comprehension, and more...

*Common operation*
- membership tests, retrieving, adding, removing elements... 

*Updating* 
- Updating, packing / unpacking, copy, deepcopy

*dictionary views*
- keys, items, value and iterations

*custom classes as keys*
- default hash, custom hashing

**Dictionary element**
- Basic structure of dictionary element --->  key : value
  - value ---> any python object: integer, function, module, custom class or instance, any python object
  - key ----> any hashable object
    - not all objects are hashable
      - strings are hashable
        - lists are never hashable
- hash tables require hash of an object to be constant (for the life of the program)
  - roughly
    - immutable objects are hashable
    - mutable objects are not hashable
    - more subtle than that ...
  
**Hashable Objects**
- Python function: hash(obj)
  - some integer (truncated based on Python build: 32-bit, 64 bit)---> sys.hash_info.width
  - exception: TypeError: unhashable type
-> int, float, complex, binary, Decimal, Fractions,---> immutable ----> hashable
-> string ---> immutable collection ---> hashable
-> frozenset ---> immutable collection ---> elements are required to be hashable ----> hashable
-> tuples ---> immutable collection ---> hashable only if all elements are also hashable
-> set.dictionary ---> mutable collection ---> not hashable 
-> list ---> mutable collection ---> not hashable 
-> functions ---> immutable ---> hashable 
-> custom functions ---> maybe hashable depending on the object 

**Requirements**
- If an object is hashable:
  - the hash of the object must be an integer value
  - if two objects compare equal (==), the hashes must also be equal
  - Important
    - two objects that do not compare equal may still have the same hash (hash collision)
      - more hash collision ---> slower dictionaries 
 
**Dictionary basic operations** 
```aiignore
d[key] = value --> create key if it does not exist already 
               --> assigns value to key
d[key]         --> as an expression returns the value for specified key
               --> exception KeyError if key is not found 
```
- sometimes want to avoid this *KeyError* exception, and return a default value if key is not found
```aiignore
d.get(key)  --> returns values if key is found. None if key is not found
d.get(key, default) --> returns value if key is found. default if key is not found. 
```
*membership testing*: test if a key is present in the dictionary or not
```aiignore
key in d        --> True if key is in d. False if it is not. 
key not in d    --> True if key is not in d. False if it is. 
```
*Number of items in dictionary*
```aiignore
len(d)
```
*Clearing out all items*
```aiignore
d.clear() ---> d is now empty
```
*Removing elements from a dictionary*
```aiignore
del d(key)      --> removes element with that key from d 
                    ---> exception KeyError if key is not in d
d.pop(key)      --> removes element with that key from d
                --> and returns the corresponding value
                    --> exceptions KeyError if key is not in d
```
- sometimes we want to avoid this *KeyError* exception
```aiignore
d.pop(key, default)     --> removes element with that key from d
                        --> and returns the corresping value 
                            --> returns default if key was not found  
```
*Another way to remove items*
```aiignore
d.popitem()         --> removes an item from d
                    --> returns tuple (key, value)
                    --> KeyError if dictioanry is empty
```
- last inserted --> popped first
  - last in first out (LIFO)
    - works like a stack

*Inserting keys with default*
- sometimes want to insert a key with a default value only if key doest not exist 
```aiignore
d = {'a':1, 'b':2}          if 'c' not in d:
                                d['c'] = 0
```
- Combine this with returning the newly inserted (default) value, or existing value if already present
```aiignore
def insert_if_not_present(d, key, value):
    if key not in d:
        d[key] = value
        return value
    else: 
        return d[key]

#Instead
result = d.setdefault(key, value)
```
**Dictionary views: PEP 3106**
- three ways we may want to view the data in  a dictionary
  - keys only           d.keys()
  - values only         d.values() 
  - key/value pair      d.items()
                            --> all are iterables
```aiignore
d = {'a': 1, 'b': 2, 'c':3}
list(d.keys())      ---> ['a', 'b', 'c']
list(d.values())    ---> [1,2,3]
list(d.items())     ---> [('a', 1), ('b', 2), ('c', 3)]
```
- Important: order of keys and values (and items) are the same
  - the position of an item in one view corresponds to the same position in the other views
  - Python 3.6+: in addition, this order is same as dictionary (insertion) order
- They are dynamic ...
  - More to it than just an iterable
  - these views are dynamic 
    - views reflect any changes in the dictionary 
    - but views are not updatable 
```aiignore
d = {'a': 1, 'b': 2, 'c':3}
keys = d.keys()                 keys    --> 'a', 'b'
values = d.values()             values  --> 1,  2
items = d.items()               itmes   --> ('a', 1), ('b' 2)

d['a'] = 10                     keys    --> 'a', 'b'
                                values  --> 10,  2
                                itmes   --> ('a', 10), ('b' 2)

del d['b']                      keys    --> 'a', 'c'
                                values  --> 10,  3
                                itmes   --> ('a', 10), ('c' 3)
```
- More than just iterables
  - The keys() view is more than iterables ----> behaves like a sect
  - makes sense: keys are unique and hashable ---> required for sets
  - union, intersection, difference of these keys view ---> just like sets
- the values() view does not behave like a set
  - in general values are not unique 
  - in general values are not hashable
- The items() view may behave like a sect
  - elements of items() are guaranteed unique (since keys are unique)
  - if all values are hashable ---> behave like a sect

**Set operations**
```aiignore
s1 = {'a', 'b', 'c'}
s2 = {'b', 'c', 'd'}

union       s1 | s2         -> {'a', 'b', 'c', 'd'}
intersect   s1 & s2         -> {'b', 'c'}
difference  s1 - s2         -> {'a'}
```
- can manipulate keys() the same way 
- dictionaries are now considered ordered (insertion order)
- sets are not ordered
  - d1.keys() and d2.keys() are ordered
  - but d1.keys() | d2.keys() is a set
    - ordering of result is not guaranteed 

**Updating, merging and copying dictionaries**

*The 'update' method*
- updates one dictionary based on items in something else
- three forms 
```aiignore
d1.update(d2)
d1.udpate(iterable)         --> iterable must contain iterables with 2 elements each: (key, value)
di.udpate(keywork-arg)      --> argument name will become key
```
*d1.udpate(d2)*
- d1 and d2 are tow dictionaries 
- for every (key, word) in d2
  - if k not in d1, insert (k, v) in d1
  - if k in d1, update k in d1
```aiignore
d1 = {'a':1 'b':2}
d2 = {'b':20,'c':30}
d1.update(d2)       --->    {'a':1, 'b':20, 'c':30}
```

*d1.update(keyword-arg)
- similar to how keyword arguments are used to create a dictioanry 
  - argument names must be a valid identifiers
```aiignore
d1 = {'a':1, 'b':2}
d1.update(b=20,c=30)        d1 ---> {'a':1, 'b':20, 'c':30}
    ---> order of keyword arguments is preserved
```

*d1.update(iterables)*
- must be iterable of iterables containing two elements ---> key, value
```aiignore
(('b', 20),('c', 30)) (('b', 20),['c', 30]) [('b', 20),[c', 30]]
d1 = {'a': 1, 'b':2}
d1.update(iterable) ----> {'a':1,'b':20, 'c':30}
```
- but also more complex iterables ----> even generators
```aiignore
((k, ord(k)) for k in 'bcd) -----> 'b': 98, 'c':99, 'd':100
d1 = {'a': 1, 'b':2}
d1.update(((k, ord(k)) for k in 'bcd) ) ----->  {'a':1, 'b': 98, 'c':99, 'd':100}
```
- insertion order is preserved (3.6+)

*unpacking dictionaries*
- works similar to unpacking a dictionary into keyword arguments in function calls
```aiignore
def func(**kwargs):
    print(kwargs)
   
d1 = {'a': 1, 'b':2}

fund(**d1)              kwargs-----> {'a': 1, 'b':2}
```
- for function arguments, key must be valid identifiers
- not for unpacking dictionaries in general
```aiignore
d1 = {'a': 1, 'b':2}
d2 = {'a': 10, (0,0):'origin'}
d3 = {'b': 20, 'c':30, 'a':100}
d = {**d1, **d2, **d3}
d--> {'a': 100, 'b':20, (0,0):'origin', 'c':30}
    ---> last 'update' wins
```

*Copying dictionaries*
- Shallow copies
  - containers object is new object
  - copied containers element keys/values are shared references with original object
```aiignore
d_copy = d.copy()
d_copy = {**d}
d_copy = dict(d)
d_copy = {k:v for k, v in d.items()} ----> slower
```
- all these methods result shallow copies

*Deep copies*
- no shared references
  - even with nested dictionaries
- can be done manually, ---sometimes requires recursion, have to be careful with circular references
  - this might be needed if we don't want a true copy, but only a partial deep copy
- simply use copy.deepcopy
- from copy import deepcopy 
  - works for custom objects, iterables, dictionaries, etc
