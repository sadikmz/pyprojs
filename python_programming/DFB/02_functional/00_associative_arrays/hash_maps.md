**Hash Maps (aka Hash Table)**
- One common concrete implementation on an associative array (aka dictionary) is a hash map
- suppose we have an array of 7 slots, initially containing these maps
  - 'john'-->John
  - 'eric'-->Eric
  - 'michael'-->Michael
  - 'graham'-->Graham
- We'll define a function that will return an integer value for all these strings ('john', 'eric', etc)
  - that will be unique for each of these strings
  - is between 0 and 6
  - always returns the same integer for the same string (deterministic)

**Hash Table**

```
h(s) = 
   'john'-->    1
   'eric'-->    4
   'michael'--> 0
   'graham'-->  5
```

- Storing a key / value pair:
  - calculate h(key)-->idx
  - store value in slot idx
- Looking up a value by key
  - calculate h(key) ---> idx
  - return value in slot idx

**Hash Functions**
- Creating the function h(key) when we know all the possible keys ahead of time is easy. 
- Reality check: most of the time we don't know all teh possible keys ahead of time
- In reality, creating such function is hard
- Bounding the returned index value is not difficult ----> module x % 7 ----> 0, 1,2,3,4,5,6
- Ensuring uniqueness is hard
  - how to ensure that h(k1) = ! h(k2) if k1 != k2
  - maybe we don't need to 
- A hash function is a function (in the mathematical sense)
```aiignore
x = y => f(x) = f(y)
```
- that maps from a set (domain) of arbitrary size (possibly infinite) to another (smaller) set of fixed range
```aiignore
h: D--->R    where X(R) < X(D) cardinality of X < cardinality of Y
```
- For our hash tables, we'll also want:
  - the range to be a defined subset of non-negative integers, 0,1,2,3,...
  - The generated indices for expected input values to be uniformly distributed (as much as possible)
- Note that we do allow getting the same output for different keys

``
``
**Dealing with collisions** 
- chaining 
- probing (linear)
    - Fetching element using probe sequences 

**sizing issues**
- When we create a hash table, how big should it be?
- We dont know how big will it become 
- we can't make it arbitrarily large ---> memory constraints 
  - start small, and grow it over time as needed
  - resizing is expensive 
    - recomputing hashes
    - move data around 
  - over allocate (create more slots than necessary)
    - algorithms exist to optimize the cost of doing this

**other issues**
- what happens when item are deleted 
  - this can affect probing algorithm
  - compacting the table when items are deleted
- choice of hash function 
- gets complicated 

**Python Dictionaries**
- namespaces
- classes
- modules
- functions 
- sets
- Dictionaries are such aan important part of python that a lot of time and effort was put into making them as efficient as possible
  - key sharing, compact dictionaries 

**key sharing: PEP 412**
- also called split-table dictionary
```
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

john = Person('John', 78)
        john
            ['name', 'John']
            ['age', 78]
eric = Person('Erich', 75)
            ['name', 'Eric']
            ['age', 75]
michael = Person('Michael', 75)
            ['name', 'Michael']
            ['age', 75]
```
- Multiple instance of the same class ----> instance attribute names are the same

```
        john    erich       michael
'name'  ['John' 'Eric'      'Michael']
'age'   [78,    75,         75] 
```
    - called also split-table dictionary

**Compact Dictionaries**

**Python hash() function**
- built-in function: hash() 
  - always returns int
  - if a == b is True, then hash(a) == hash(b) is also True
  - Python truncates hash to some fixed size --> sys.hash_infor.width
  - mutable objects are not hashable - lists and sets
- Why
  - hash values ---> used for tables (dictionaries) ----> position index
  - has values for objects that compare equal remain equal during program run
  - but they can change from run to run ----> strings, bites and datetime
  ->> never rely on hash value being the same for one program run to another 
    - although may be ok sometimes, integers 