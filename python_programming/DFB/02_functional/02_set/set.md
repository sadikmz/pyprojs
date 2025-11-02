**What is set?**
- Mathematics
  - A set is gathering together into a whole of definite, distinct objects of our perception or of our thoughts - which are called elements of the set
    - George Cantor
- A collection of things 
- will be discussed 
  - set membership
  - size of set (Cardinality)
  - Union
  - Intersection
  - Complement 
    - and more 

**Set theory**
- A set is an ordered collection of distinct objects
  - there is no particular ordering in a set
```
{1,3,5}         {5,3,1}         {3,5,,1} ...are all the same set (equal)
```
- objects are distinct 
```aiignore
{1,1,3}     ----> not possible ---- element 1 is repeated
```
- Python data type: set
  - elements must be hashable
  - elements are distinct - they do not compare equal(==)

*Membership*
- if x is an element contained in some set S, we write
- in Python the *in* operator is a question that returns *True* or *False*
```aiignore
x in S 
```
- Similarly with the *not in* operator
```aiignore
x not in S
```

*Unions and intersection*
- The union of two sets is a set that combines the items from these two sets, keeping only a single instance of any repeating elements
```aiignore
S1 U S2
```
- s1 | s2 
- s1.union(s2)
- the intersection of tow set is a set that only contains the elements common to both
```aiignore
S1 n S2
```
- s1 & s2
- s1.intersection(s2)

*Differences of two sets*
- The difference of two sets is all the element of one set without the elements of the other set
```aiignore
S1 - S2
s1.difference(s2)
```

*Symmmetric difference of two sets*
- the symmetric difference of two sets is the union of both sets without the intersection of both sets 
```aiignore
S1 ^ S2
s1.symmetric_difference(s2)
```

*Empty set, Cardinality and Disjoint set*
- For finite sets, teh *cardinality* of a set is the number of elements in the set
  - len(set)
- An empty set is a set that contains no element --> cardinality is 0
- set() --------> cannot use {} to create an empty set
- this would create an empty set
- Two sets are said to be *disjoint* if there intersection is the empty set
  - len(s1 & s2) ---> 0
  - s1.isdisjoint(s2)  ----> Tue (Boolean)

*Subsets and Supersets*
- A set s1 is subset of s2 if all the element in s1 are in s2
```aiignore
s1 <= s2
s1.issubset(s2)
{1,2,3} <= {1,2,3,4}    ---> True
{1,2,3} <= {1,2,3,4}    ---> True
```
- A set s1 is proper subset of s2 if s1 is a subset of s2 and s1 is not equal to s2
  - i.e s1 is a subset of s2 and s2 contains some additional elements 
```aiignore
s1 < s2
{1,2,3} <= {1,2,3,4}    ---> True
{1,2,3} <= {1,2,3,4}    ---> False
```
- A set s1 is a superset of s2 if s2 is a subset of s1
```aiignore
s1 >= s2
s1.issuperset(s2)
```
- A set s1 is a proper superset of s2 if s2 is subset set or s1
```aiignore
s1 > s2
```

**Python Set**
- Python has an implementation of sets that supports many set operations
```aiignore
cardinality         --> len()
membership testing  --> in, not in
unions              --> s1 | s2, s1.union(s2)
intersections       --> s1 & s2, s1.intersection(s2)
differences         --> s1 - s2, s1.difference(s2)
symmetric differences-> s1 ^ s2, s1.symmetric_differnece(s2)
subsets              --> s1 <= s2, s1.issubset(s2)
                     --> s1 < s2
superset             --> s1 >= s2, s1.issuperset(s2)
                     --> s1 > s2
disjointness         --> s1.isdisjoint(s2)                
```
- The type is set
- set literals ---> {'a',10,10.5}
- empty set ----> set()
- Notice how the literal notation of for set uses the same braces {} as dictionaries
- in fact sets are hash tables as well
- Unlike dictionary hash tables, sets only contain the "keys", not the values
  - set(iterables)-----> iterables must be hashable 
- Elements of a set:
  - must be unique (distinct)
  - must be hashable
  - have no guaranteed order
- A set is a mutable collection ----add and remove elements
- A set is therefore not hashable,
  - cannot be used as a dictionary key,
  - cannot be used as an element of in another set

*Frozen sets*
- Frozen sets are immutable equivalent of sets 
  - frozenset
  - frozenset(iterables)
  - think of tuples and lists
- elements of frozenset 
  - must be unique (distinct)
  - must be hashable
  - have no guaranteed order
- can convert any set to a frozenset
  - frozenset({1,2,3})
  - no literal for a frozenset
- A frozenset is hashable
  - can be used as a dictionary key
  - can be used as an element of a set (or frozenset)

*Membership testing*
- Testing membership of an element in set is extremely efficient (hash table lookup)
  - in, not in
- In fact, instead of writing code like 
  - if a in [10, 20, 30]:
  - or 
  - if a in (10, 20, 30):
  - prefer using (as long as elements are hashable)
    - if a in {10, 20, 30}: ----> higher storage costs

**Creating sets**
- elements must be hashable 
- we cannot use literal 
- {} is an empty dict and instead use set() to create empty set
- set comprehension: element must be hashable 
  - {c for c in 'python'}
```aiignore
{'a', 10, 3.14159}
set(iterable)

# Creating empty set
set()

# using set comprehension 
{c for c in 'python'}

# or simply 
set('python')
```
*unpacking sets*
- Unpacking 
  - unpacking iterables *my_list
  - unpacking dictionaries **my_dict
  - unpacking sets *my_set
    - order in which elements are unpacked is essentially unknown
```aiignore
s1 = {'a', 10, 3.14}
s2 = set('abc')
{*s1, *s2}              ----> {'a', 'b','c' 10, 3.14}
[*s1, *s2]              ----> ['a', 'a', 'b','c' 10, 3.14]
my_func(*s1,  *s2)      ----> works, but what's teh order of the arguments                            
```

**Common operation**
*cardinality and membership*
```aiignore
len(s)      --> number of elements in s     ---> (cardinality of s)
in, not in  --> x in s                      ---> tests if x is in the set
                                            ---> like dicitonary keys, use equality (==) not identity (is)
```
- membership testing in set is fast ---> hash table lookup
  - membership testing in a list of tuple is slow (in comparison)   ---> linear scan
    - but sts have more memory overhead than lists of tuples
    - tradeoff - speed vs memory 

*Adding elements*
- lists have ordering
  - append
  - insert
- sets have no ordering
  - add
  - s.add('python')
    - mutates the set

*Removing elements*
- lists have ordering
  - can remove element by position: del l[1]
  - can remove specific elements: l.remove(30)
- set have no ordering
  - cannot use position
  - can remove specific elements
```aiignore
s = {'a', 'b', 'c'}
s.remove('b')   ---> {'a', 'c'}
s.remove('z')   ---> KeyError exception

# To avoid KeyError exception 
s.discard('b')   ---> {'c'}
s.discard('z')   ---> {'c'}

s.pop()
--> removes and returns an arbitrary element
--> KeyError if set is empty

s.clear()
--> removes all elements from set
```

**Set operations**
- Union
- Intersection 
- Difference
- symmetric difference 
- containment 
  - strict and non-strict
- In general, we have two ways of doing these operations
  - methods 
    - s1.intersection(s2)
      - s2 could be an iterable (of hashable elements)
  - operators 
    - s1 & s2 
      - s1 and s2 mush both be sets
*Intersection*
```aiignore
{1,2,3} & {2,3}                 ---> {2}
{1,2,3}.intersection({2,3})     ---> {2}
{1,2,3}.intersection([2,3])     ---> {2}

s1 & s2 & s3 & s4
s1.intersection(s2, s3, s4)
--> returns a st
```

*Union*
```aiignore
{1,2,3} | {2,4}                 ---> {1,2,3,4}
{1,2,3}.union({2,4})            ---> {1,2,3,4}
{1,2,3}.union([2,4])            ---> {1,2,3,4}

s1 | s2 | s3 | s4
s1.union(s2, s3, s4)
```

*Disjointedness*
- Tow sets are disjoint if their intersection is empty 
- len(s1 & s2) ---> 0
  - empty sets are flasy 
```aiignore
if s1 & s2:
    print('sets are not disjoint')

if not (s1 & s2):
    print('sets are disjoint')

if not s1 & s2:
    print('sets are disjoint')

s1.isdisjoint(s2)
```

*Differences*
```aiignore
{1,2,3,4} - {2,3}                                   ----> {1,4}
{1,2,3,4}.differences({2,3})                        ----> {1,4}
{1,2,3,4}.differences([2,3])                        ----> {1,4}

s1 - s2 - s3
s1.difference(s2,s3)

# Beware 
s1 - (s2 - s3) is not the same as (s1 - s2) - s3
# Python is left-associative 
s1 - s2 - s3 ---> (s1 - s2) - s3  
s1.difference(s2, s3) ----> (s1 - s2) - s3  
```

*Symmetric differences*
```
s1 = {1,2,3,4}
s2 = {3,4,5,6}
s1 ^ s2 -----> {1, 2, 5,6}
#Union - intersection 
(s1 | s2) - (s1 & s2)
s1.symmetric_difference(s2)
s1.symmetric_difference([3,4,5,6])
```

*Containment*
```aiignore
s1 < s2     ----> is s1 strictly contained in 2
s1 <= s2    ----> is s2 contained in (possibly equal to) s2 ---> s1.issubset(s2)
s1 > s2     ----> does s1 strictly contain s2
            ----> is s2 strictly contained in s1
s1 >= s2    ----> does s1 contain (possibliy equal to) s2  ----> s1.issuperset(s2)
            ----> is s2 contained in (possiblity equal to) s1 
```

**Updating sets**
- sets have no ordering ---> No indexing 
  - lists ---> l[2] = 100 cannot do that with sets
- we can add and remove elements ---> mutates the set
- we can create
  - union
  - intersection 
  - differences
  - symmetric differences
- But these operation create new sets 
```aiignore
# List analogy 
l1 = [1,2,3]
l2 = [4,5,6]
l1 + l2 ----> new list [1,2,3,4,5,6]
#but 
l1 +=l2 mutates l1    l1---> [1,2,3,4,5,6]
```
*Analogous set mutating updates*
- |=
- &=
- -=
- ^=
- all these operation mutate teh left hand side
- Equivalent methods 
  - s1 |= s2    s1.update(s2)
  - s1 &= s2     s1.intersection_update(s2)
  - s1 -= s2     s1.difference_update(s2)
  - s1 ^= s2     s1.symmetric_update_update(s2)
```aiignore
s1.update(s2,s3)                    s1 |= s2 | s3
s1.intersection_update(s2,s3)       s1 &= s2 & s3   

# Beware
s1.difference_update(s2,s3) is not the same as s1 -= s2 - s3
                                                        RHS is evalutated first
```
- set differences are not associative
- in general, s1 - (s1 - s2) not same as (s1 - s2) - s3

**Copying sets: Shallow vs deep copies**
- shallow copy
  - s2.copy(s1)
  - s2 = set(s1)
  - s2 = {*s1} unpacking 
- deep copy
  - from copy import deepcopy 
  - s2 = deepcopy(s1)

**Frozen sets**
- immutable sets
  - same properties and behavior as sets
    - except they cannot be mutated
- Their elements can be mutable
- if all elements in a frozen set are hashable, then the frozen set is also hashable
  - can be used as a key in a dictionary 
  - can be an element of another set
- frozenset() ---> no literal expressions to create frozen sets

*copying frozen sets*
- Think back to tuples and sets
```aiignore
l1 = [1,2,3]        l2 = list(l1)       l1 is l2 --> False
t1 = (1,2,3)        t2 = tuple(t1)      t1 is t2 --> True
```
- safe for Python to not make a copy of tuple - since it is immutable 
```aiignore
s1 = frozenset({1,2,3})             s2 = frozenst(s1)       s1 is s2  --> True
                                    s2 = s1.copy()          s1 is s2  --> True
```
- Deep copies do not behave that way

*set operation*
- non-mutating set operations: &, |, -. ^
- these operations can be performed on mixed set and frozensets
- resulting type depends on the type of the first operand
```aiignore
s1 & s2     --> set if s2 is a set, even if s2 is a frozenset
            --> frozenset if s1 is a frozenset, even if s2 is a set
    
```

*Equality and identity*
- Numbers
```aiignore
1.0 is 1    ---> False      1 + 0j is 1 ---> False      True is 1   ---> False
1.0 == 1    ---> True       1 + 0j == 1 ---> True      True == 1    ---> True
```
- the same thing with set and frozenset
```aiignore
s1 = {1,2,3}
s2 = frozenset([1,2,3])

s1 is s2 ---> False
s2 == s2 ---> True
```

*Application: Memoization*
- take a look at http://en.wikipedia.org/wiki/Memoization
- Python has a decorator available for memoization: functools.lru_cache
- But that decorator has one drowback
```aiignore
@lru_cache
def my_func(*,a,b):
    ----

my_func(a=1, b=1) ---> result is computed and cached 
my_func(a=1, b=1) ---> result is returned directely from cache
my_func(b=1, a=1) ---> result is computed again, and cached 
```