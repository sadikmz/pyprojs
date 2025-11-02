**Custom classes and hashing**
- How python finds a key in a dictionary (simplified)
- hash(key)
  - mod dictionary sizes (allocated) --> start index in hash table (sequence of slots)
  - generate probe sequence (sequence of valid indices)
  - loop over probe sequence
    - is slop empty?
      - yes ---> key does not exist in dictionary 
      - no ----> are hashes equal and are keys equal (==)
        - yes ----> found the key
        - no  ----> (caused by hash collision upon insertion / resizing)
          - continue iteration to find key or empty slot
          - loop the entire iteration untile found or empty slot
- more hash collisions --> more inefficient 
- predictable hashes ---> subject to DOS attacks
- In order for this algorithm to work:
  - hash (key) when inserting them
    - must equal hash(key) when retrieving them
    - otherwise we are starting our search in the wrong place!
  - probe sequences remain the same ---> Python controls that, not us
  - so hash of key cannot change after storing in dict

**Object Hashes**
- An object hash in python mush satisfy the following 
  - must be an integer
  - if a==b --> True, then hash(a)==hash(b) ---> True
  - Note: We do not require that if hash(a)==hash() then a==b
    - i.e two objects that are not equal can have the same hash 
      - hash collision
  - Why this is important
  - let's say we have these two tuples
```aiignore
t1 = (1,2)              ----> No gurantee they will have the same id
t2 = (1,2)              ----> but they are equal t1 == t2 ---> True even if t1 is t2 ----> False
d = {t1: 'python'}      ----> works because t1 == t2 and hash(t1) == hash(t2)
d[t1] --> 'Python'      ---> from dictionary's pespective t1 and t2 are the same
d[t2] --> 'Python'
```
**Custom classes**
```aiignore
class Person():
    def __init__(self, name):
        self.name = name
 
p1 = Person('john')
p2 = Person('john')         # By default, custom classes compare == if they have teh same id (is)
p1 == p2 ---> False because p1 is p2 ---> False
```
- By default, Python automatically makes custom object such as the one above hashable
  - it uses hte id to make a hash
    - ids are integers and satisfy the hash rules
    - if p1 == p2 ---> True
      - then p1 is p2 ----> True
      - so id(p1) == id(p2) ---> True
      - so hash(p1) == hash(p2)---> True

- But not always very useful ...
```aiignore
class Person:
    def __init__(self, name):
        self.name  = name
 
p1 = Person('John')
p2 = Person('John')
p1 == p2 ----> False
hash(p1) == hash(p2) ---> False

# Example
d = {p1:78      ----> OK, because p1 is hashable by default
d[p1] ---> 78
d[p2] ---> keyError exceptions
```
- This may not be what we want ...
- in this case we want to consider p1 and p2 as equal
- and be able to lookup the key using either instance

**So we need to define equality for our custom class**
```aiignore
class Person:
    def __init__(self, name):
        self.name  = name
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name
        else:
            return False

p1 = Person('John')
p2 = Person('John')
p1 == p2 ----> False
hash(p1) == hash(p2) ---> True
```
- What about the hashes
  - hash(p1) ----> TypeError: unhashable type: Person
- Makes sense - if Python used the default hash based on id
  - p1 == p2 ----> True
  - but hash(p1) == hash(p2) ----> False
  - Implement \_\_eq__ ---> lose authomatic id based hashing 

**Defining hash for custom classes**
- \_\_hash__ special method
- hash(p1) --> looks for \_\_hash__ method on p1
- remember that \_\_hash__ must return an integer
- how we do indicate that the class is not hashable
  - set \_\_hash__ attribute to None
  - \_\_hash__ = None in class
- this is what happens when we define \_\_eq__, but not \_\_hash__
- we can however override this, by implementing the \_\_hash__ method ourselves
- remember the rules:
  - __hash__ must return an integer
  - if a == b ---> True then \_\_hash__(a) == \_\_hash__(b) ---> True