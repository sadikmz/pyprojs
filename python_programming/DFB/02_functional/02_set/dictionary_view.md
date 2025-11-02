**A long time ago**
- how could we iterate over all keys, values or items of a dictionary
  - d.keys(), d.values, d.items, ----> created and returned a list of these things
  - list is static 
 ```aiignore
d = {'a': 1, 'b':2}
keys = d.keys()         ---> keys = ['a','b']
d['c']=3                ---> keys = ['a', 'b']
``` 
   - list duplicates data - not good for storage dictionaries - can be slow
   - inefficient for membership testing
     - d = {'a': 1, 'b':2}
     - vaues - = d.values()
       - 2 in values        ----> linear search 
- To help with iteration 
  - d.iterkey(), d.ietervaulue, d.iterms() ----)> were introduced 
  - iterators --> better than a new list ----> didi not duplicate data ---> more efficient
  - still does not help with membership testing
  also not easy to answer such questions such as, given d1 and d2
    - what keys are common to both
    - what keys are in one but not in other
      - both are set oprations

**Key view**
- instead of keys() returning list, and iterkeys() just being an iterator....
- what if keys also a lighweight dictionary object that maintained a reference to teh dictionary and implementing method ...such as 
```
__iter__            ----> iterable protocl 
__contains__        ----> membership testing
__and__             ----> interseciton of two sets
__or__              ----> union of tow dicitonary 
__eq__              ----> same keys in both viewss
__lh__              ----> is one of keys a subset of the other one ects 
```

**Dictionary view**
- Three ways we may wont to view hte data in dictionary 
  - key only                        ---> keys()                        
  - value onley                     ---> values()
  - key/value pair (key, value)     ---> items()

**Set behaviour**
- The keys() view always behave like a (frozen) set
  - since elements are unique (==) and hashable 
- the items() view method may behave like a (frozen) set
  - if the vaues are hashable
  - uniqueness of tuples are guaranteed since keys are unique 

- the values () view never behave like a set 
  - values not guaranted unique
  - values not guaranteed hashable 

**Modifying the dictionary while iterating over**

- Becareful doing this
  - modifying values usually not a problem
  - modifying keys can lead to exceptions of worse disaster
```aiignore
# This is safe
for key in d.keys():
    d[key] += 1

# This lead to an EXCEPTION
for v in d.values()
    del d['a']
    #Python doest allow modifyhing the size of underlying dictionary whiel literatign oover a few 
   
```

- You technically can modify the keys as lookg as you do not change the size of dictionary 
  - dont' do it!
