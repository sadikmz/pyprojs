**Python has many tools for working with iterables**
- You should already know almost all of these:
  - iter, reversed, next, len, slicing
  - zip
  - filter,
  - sorted
  - enumerat
  - min, max, sum
  - all, any
  - map
 - these all are built-in
 - and *reduce* from functools module 

**The itertools module**
- slicing, islice 
- selecting and filtering: dropwhile, takewhile, compress, filterfalse
- mapping and reducing: starmap, accumulate 
- infinite iterators: count, cycle, repeat
- zipping: zip_longest
- combinatorics: product, permutations, combinations, combinations_with_replacement

**Aggregators**
- functions that iterate through an iterable and returns a single value that (usually) takes into account every element of the iterable.
```
min(iterable) --> minimum value in the iterable.
max(iterable) --> maximum value in the iterable.
sum(iterable) --> sum of all the values in the iterable.
```

**Associated truth values**
- You should already know that, but let's review briefly:
- Every object in Python has an associated truth value, ---> bool(obj) ---> True / False
- Every object has a True truth value, execpt 
  - None 
  - False
  - 0 in any numeric type (0, 0.0, 0 + 0j)
  - empty sequences (eg. list, tuple, string,...)
  - empty mapping types (eg. dictionary, set,...)
  - custom classes that implement a \_\_bool__ or \_\_len__ method that returns False or 0
- Which have a False truth value 

**The *any* and *all* functions**
- any(iterable) --> returns *True* if any (one or more) element in iterable is truthy 
                --> False otherwise
- all(iterable) --> returns *True* if all the elements in iterable are truthy

**Leveraging the any and all functions**
- often, we are not particularly interested in the direct truth value of the elements in our iterables 
- want to know if any, or all, satisfy some condition, --> if the condition is True
- A function that takes a single argument and returns True or False is called a *predicate*
- We can make *any* and *all* more useful by applying a predicate to each element of the iterable

*Example*
- Suppose we have some iterable, l = [1,2,3,4,10]
- We want to know if every element is less than 10. 
- First define a suitable predicate: pred = lambda x: x < 10
- Apply this predicate to every element of the iterable:
```
l = [1,2,3,4,100]
pred = lambda x: x < 10
result = [pred[1], pred(2), pred(3), pred(4), pred(100)]
```
- Then we use all on these result: all(result) ---> False

**How do we apply that predicate?**
```
# The map function 
map(fn, iterable)
--> applies fn to every element of the iterable

# A comprehension 
(fn(item) for item in iterable)

# Or even for loop
new_list = []
for item in iterable:
    new_list.append(fn(item))
```

**Slicing: itertool.islice**
- We know that we can slice sequence types 
```
seq[i:j:k]
seq[slice(i,j,k)]
```
- We can also slice general iterables (including iterators)
```aiignore
islice(iterable, start, stop, step)

from itertools import islice
l = [1,2,3,4]
result = islice(l,0,3)
list(resutl) ---> [1,2,3]
```
- islice is a lazy iterator
```aiignore
list(result) ---> []
```
**Selecting and Filtering**

**Infinit iterator: itertools.count**
- The count function is an infinit iterator 
- similar to range ---> start,step
- different from range ---> no stop ----> infinte
  - start and step can be any numeric type
    - float
    - complex
    - decimal
    - bool
      - False ---> 0
      - True  ---> 1
- Example
```
count(10,2) ----> 10, 12, 14, ...
count(10.5,0.1) ----> 10.5, 10.6, 10.7,...)
takewhile(lambda x: x < 10.8, count(10.5, 0.1)) ----> 10.5, 10.6, 10.7
```

**itertools.cycle**
- The cycle function allow us to loop over a finite iterable indefinitely
- Example
```
clyle(['a','b','c']) ----> 'a','b','c',  'a','b','c',....
```
*Important*
- if the argument of cycle is itself an iterator, cycle will produce an infinte sequence 

**itertools.repeat**
- The repeat function simply yield the same value indefinitely
```
repeat('spam') ----> 'spam', 'spam', 'spam', 'spam',...
```
- Optionally, you can specify a count to make the iterator finite
```
repeat('spam',3) ----> 'spam', 'spam', 'spam'

```

*Caveat*
- The items yielded by *repeat* are the same object
  - they each reference the same object in memorey - if they are mutable object - need to be careful. 


**Chaining and Teeing**

*Chaining and Teeing: itertools.chain(\*args)* ----> lazy iterator 
- each of the arguments should be iterables 
- this is analogous to sequence concatenation but not the same.
  - dealing with iterables (including iterators)
  - chaining is itself a lazy iterator 
- We can manually chian iterable this way:
```aiignore
iter1 iter2 iter3

for it in (iter1, iter2, iter3):
    yield from it
```
- Or, we can use *chain* as follows:
```aiignore
for item in chian(iter1, iter2, iter3):
    print(item)
```
- Variable number of positional arguments - each arguments must be an iterable. 
- What happens if we want to cain from iterables contained inside another, single, iterable?
```aiignore
l = [iter1, iter2, iter3]
chain (l) ---> l
```
- What we really want is to chai iter1, iter2, iter3
- we can can try using unpacking --chain(*l)
  - produces chained elements from iter1, iter2, and iter3
- BUT, unpacking is *eagar* not *lazy*
- if l was a lazy iterator, we esssentially iterated through l (not the sub iterator), just to unpack!
- This could be a problem if we really wanted the entire chining process to be lazy.
- Instead we can use this alternate method called from_iterable from *itertools.chian.from_iterable(it)* ---> lazy iterator
- We could try this approach
```aiignore
def chain_lazy(it):
    for sub_it in it:
        yield from sub_it
```
- Or we can use chain.from_iterable
```aiignore
chain.from_iterable(it)
```
- This achieves the same result
  - iterates lazily over it
    - in turm, iterates lazily over each iterable in it

**Copying iterators: itertools.tee(iterable,n)**
- Sometimes we need to iterate through the same iterator multple times, or even in parallel
- we could create the iterator multiple times manually
```aiignore
iters = []
for _ in range(10):
    iter.append(create_iterator())
```
- Or we can use *tee* in *itertools*
  - returns independent iterator in a tuple 
```aiignore
tee(iterable, 10) ---> (iter1, iter2, iter3,..., iter10)
```
- all of the iterable are different objects

*Teeting iterables*
- Important thing to note:
  - the elements of the returned tuple are lazy iterators
    - always 
    - even if the orginal argument was not!
- Example:
```aiignore
l = [1,2,3,4]
tee(l, 3) ----> (iter1, iter2, iter3)
```
**Mapping and Accumulation / Reducing function**
- Mapping ---> applying a callable to each element of an iterable 
- map(fn, iterable)
- Accumulation ---> reducing an iterable down to a single value
  - sum(iterable)---> calculates the sum of every element in an iterable
  - min(iterable)---> calculates the minimum element of the iterable
  - max(iterable)---> returns the maximal element of the iterable
  - reduce(fn, iterable, [initializer])
    - fn is a function of two arguments
    - applies fn cumulatively to every elements of iterable 

*map*
- map(fn,iterable) applies fn to every element of iterable, and returns an iterator (lazy)
  - fn must be a callable that requires a single argument
    - map(lambda x: x**2, [1,2,3,4]) --> 1, 4, 9, 16 ---> lazy iterator 
- we can easily do the same thing using a generator expression too
- maps = (fn(item) for item in iterable)

*reduce*
- l = [1,2,3,4]
- sum(l) ---> 10
- reduce(lambda, x,y: x+y, l)
  - 1
  - 1+2 = 3
  - 3+3 = 6
  - 6+4 = 10
- To find the product of all elements
  - reduce(lambda x,y: x*y, l)
    - 1
    - 1*2 = 2
    - 2*3 = 6
    - 6*4 = 24
We can specify a different 'start' value in the reduction 
    - reduce(lambda x,y: x+y, l, 100)

*itertools.starmap*
- starmap is very similar to map
  - it unpacks every sub-element of the iterable argument, and passes that to the map function
  - useful for mapping a multi-argument function on an iterable of iterables
    - l = [[1,2],[3,4]] 
    - map(lambda item: item[0] * item[1], l) ---> 2,12
- we can also use starmap: starmap(operator.mul, l) ---> 2, 12
  - we could also just use a generator expression to do the same thing
    - (operator.mul(*item) for item in l)
- We can also use iterables that contain more than just two values
  - l = [[1,2,3],[10,20,30],[100,200,300]]
  - starmap(lambda x,y,z = x+y+z, l) ----> 6, 60, 600

*itertools.accumulate(iterable,fn)* -----> lazy iterator 
- the accumulate function is very similar to the *reduce* function 
- But it returns a *lazy* *iterator* producing all the intermediate results
  - reduce only returns the final result
- Unlike reduce, it does not accept an initializer 
- Note
  - the argument order is not the same
    - reduce(fn, iterable)
    - accumulate(iterable,fn)
- Example
```
l = [1,2,3,4]
functools.reduce(operator.mul,l)    --> 1           --------> 24
                                    --> 1*2 = 2
                                    --> 2*3 = 6
                                    --> 6*4 = 24

itertools.accumulate(l,operator.mul)               --------> 24
```

*zip*

*grouping*

**Combinatorics**
- The itertools module contains a few functions for generating *permutations* and *combinations*
- it also has a function to generate the *Cartesian product* of multiple iterables
- All these functions return lazy iterator
```aiignore
#Cartesian product
{1,2,3} x {a,b,c}
    (1,a)
    (1,b)
    (1,c)
    (2,a)
    (2,b)
    (2.c)
    (3,a)
    (3,b)
    (3,c)

#Two dimentional: 
A X B = {(a,b) | a E A, b E b}
# n-dimentional:
A1 X ...An = {(a1,a2,....an) | a1 E A1 ....., an E An}

```

- Let's say we wanted to generate the cartesian product of two list
```aiignore
l1 = [1,2,3]
l2 = ['a', 'b', 'c','d']
def cartesian_product(l1,l2):
    for x in l1:
        for y in l2:
            yield (x, y)

cartesian_product(l1,l2)
(1,'a),.....(3,'d')


itertools.product(*args) -----> lazy iterator
l3 = [100,200]

product(l1,l2,l3)
    (1,'a',100),
    (1,'b',100),
    (1,'c',100),
    (2,'a',100),
    ...
    (3,'d',200),
```

*Permutations*
- This function will produce all the possible permutations of a given iterable
- In addition, we can specify the length of each permutation 
  - maxes out at the length of the iterable
- itertools.permutations(iterable,r=None)
  - r is the size of permutation
  - r = None means length of each permutation mean the length of the iterable
- Elements of the iterable are considered unique based on their position, not their value. 
- If iterable produces repeat values, then permutations will have repeat value too. 

**Combinations*
- Unlike permutations, the order of element in a combination is not considered.
  - OK to always sort the elements of a combination 
- Combination of length r, can be picked from a set
  - without replacement ---> once an element has been picked from the set it cannot be picked again. 
  - with replacement ----> once an element has been picked from teh set it can be picked again

```aiignore
iterools.combinations(iterable,r)
itertools.combinations_with_replacement(iterable,r)
```
- Just like for permutations:
  - the elements of an iterable are unique based on their position, not their value
- the different combinations produced by these functions are sorted based on the original ordering in the iterable.
