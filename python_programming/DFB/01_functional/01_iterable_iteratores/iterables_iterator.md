**Iterating sequences**
-\_\_getitem__
- assumed indexing started at 0
- iteration: \_\_getitem__(0), \_\_getitem__(1)
- but iteration can be more general than based on sequencial indexing
- set
  - unordered collection of items 
  - but are iterable

**The concept of next** 
- for the iteration, all we really need is the concept of "get the next item" in the colelction 
- if a collection object implements a get_next_item method
- we can get elements out of the collection, one after the other 
- and we could iterate over the collection 
- But how do we know when to stop asking for the next item? use exceptions - StopIteration ---> built-in exception 

**Iterators and iterables**
- Iterator is an object that implements  
- \_\_iter__
- \_\_next__
- The drawback is that iterators get exhausted 
  - become useless for iterating again
  - become throw away objects

**Separating the Collection from the iterator**
- Maintaining the data of the collection should be oe object
- Iterating over the data should be a separate object ---> iterator
  - that object is throw-away ---> but we dont throw away the collection

**The collection is iterable**
- but the iterator is responsible for iterating over the collection
- the iterable is created once 
- the iterator is created every time we need to start a fresh iteration 

**Consuming iterators manually**

**Python's built-in iterables and iterators***
- Iterables
  - list, tuples, etc 
- Python provides many functions that returns iterable or iterator 
- Additionally, the iterator perform lazy evaluation
- you should always be aware of whether you are dealing with an iterable or an iterator 
- if an object is iterable but not an iterator - you can iterate over it many times
- if an object is an iterator you can iterate over it only once and become exhausted 
- iterable, 
  - range()     ----> iterable 
  - zip(l1,l2) ----> iterator 
  - enumerate(l1) ----> iterator
  - open('cars.csv') -----> iterator
  - dictionary .keys() ----> iterable
  - dictionary .values()---> iterable 
  - dictionary .items() ---> iterable
  - ......many more

**Iter() function**

**Iterating Callables**

**Reversed iteration**
- If we have a sequence type, then iterating over the sequence in reverse order is quite simple. 
````
# This works, but is wasteful because it makes a copy of the sequence 

for item in seq[::-1]:
  print(item)
````

```
# This is more efficient, but the syntax is messy.  

for i in range(len(seq)):
  print(seq[len(seq) -i -1])
  
for in range(len(seq)-1, -1, -1);
  print(seq[i]) 
```
```
# This is cleaner and just as efficient, because it creates an iterator that will iterate
# backwards over teh sequence - it does not copy the data 

for item in reversed(seq):
  print(item)
 
# Both __getitem__ and __len__ must be implemented
# We can override how reversed works by implementing the __reverse__ special method. 
```

**iterating an iterable in reverse**
- Unfortunately, reversed() will not work with custom iterables without a little bit of extra work
- when we call reversed() on a custom iterable, Python will look for and call the \_\_reverse__ function
- that function should return an iterator that will be used to perform the reversed iteration 
- so basically, we have to implement a reverse iterator ourselves 
- Just like the iter() method, when we call reversed() an object:
  - look for and call \_\_reverse__ method
  - if it's not there, uses \_\_getitem__ and \_\_len__ to create an iterator for us.
  - exception otherwise

