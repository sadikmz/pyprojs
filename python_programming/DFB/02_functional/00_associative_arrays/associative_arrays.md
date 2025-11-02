**What is an associative array**
```
persons = [Jonn,Eric,Michael,Graham]
            0     1    2       3
```
- We can think of the indices as eky for the items in the list
  - 0--->John
  - 1--->Eric
  - 2--->Michael
  - 3--->Graham
- So when we want to get hold of Michael object, we just need to remember the key
```aiignore
persons[2] ----> Michael
```
- But remembering a number while we write our code???
- There has to a better way
```aiignore
persons = [('john', John),
           ('erich', Eric),
           ('michael', Michael),
           ('graham'), Graham]
```
- We have associated a string with an object (key, object) format
- to get the *Michael* object:
  - lookup the key *michael* and return the associated value
  - scan the persons list until we find a tuple with first element = key
  - return the second element of the tuple 
- At least we don't have to remember a number anymore!
- let's break it up:
```aiignore
kyes = ['john', 'eric', 'michael', 'graham']
persons = [Jonn, Eric, Michael, Graham]
```
- Notice how the index of *john* matches up with the index of *John* and so on
- What if we could define a function h that would return these results - always 
```aiignore
h('john')--> 0
h('eric')--> 1
h('michael')-->2
h('graham')--3
```
- to get *Michael*, we would first call h('michael')--->2 then persons[2]
```
persons[h('michale')]
```
**Associative Arrays**
- An associative array is an abstract data structure that associates key (keys are unique) to values
- abstractly we can think of it as a collection of (key, value) pairs
- Sometimes also called: maps, dictionaries 
- Can be implemented in different concrete ways
- they support 
  - adding/removing elements
  - modifying an associated value
  - looking up a value via its key
