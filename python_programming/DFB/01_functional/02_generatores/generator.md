**Generators**
- A type of iterators
- Generator functions 
  - generator factories
  - they return a generator when called 
  - they are not a generator themselves
- Generator expression 
  - uses comprehension expression syntax
  - a more concise way of creating generators
  - like list comprehensions, useful for simple situations
- Performance considerations

**Yielding and Generator function**
- Let's recall how we would write a simple iterator for factorial 
```
class FactIter:
    def __iter__(self, n):
        self.n = n
        self.i = 0
        
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            result = math.factorial(self.i)
            self.i += 1
            return result  
```
- Now that is quite a bit of work for a simple iterator

**There has to be a better way***
** What if we could do something like this instead:
```
def factorials(n):
    for i in range(n):
        emit factorrial(i)
        pause execution here
        wait for resume 
    return 'done'
```
and in our code we would want to do something like this maybe 
```
facts = factorials(4)
get_next(fact) --> 01
get_next(fact) --> 1!
get_next(fact) --> 2!
get_next(fact) --> 3!
get_next(fact) --> done!
```
- Of course, getting 0!, 1!, 2!, 3! followed by a string is odd
- and what happens if we call get_next again?
- maybe we should consider raising an exception --> StopIteration ?
- and instead of calling get_next, why not just use next?
- What about that emit, pause, resume?-------> uses yield keyword

**Yield to teh rescue---***
- The *yield* keyword does exactly what we want 
  - it emits a value 
  - the function is effectivcely suspended (but it retains its current state)
  - calling next on teh function resumes running the function right after the yield statement 
  - if function returns somthing instead of yielding (finishes running) -> StopIteration exception 
  
```
def song():
    print('line 1')
    yield 'I am a lumberjack I am okay'
    print('line2')
    yield 'I sleep all night taht I work all day'

lines = song()    ---> no output 

line = next(lines) ---> 'line 1' is printed in console 
                         line ---> 'I am a lumberjack I am okay'
line = next(lines) ---> 'line 2' is printed in console 
                         line ---> 'I sleep all night taht I work all day'
line = next(lines) ---> StopIteration 
```
***Generators**
- A function that uses the *yield* statement, is called a *generator function* 
````
def my_func():
    yeild 1
    yeild 2
    yield 3
````
- my_func is just a regular function 
- calling my_func() returns a generator object
- we can think of functions that contain the *yield* statement as *generator factories*
- The generator is created by Python when the function is called --> gene = my_func()
- the resulting generator is executed by calling *next()* --> next(gene)
  - the function body will execute until it encounters a *yield* statement 
  - it yields the value (as *return* value of *next()*) then it *suspends* itself
  - until *next* is called again --> suspended function *resumes* executio 
  - if it encounters *return* before a yield 
    - StopIteration exception occurs 

**Generator example**
```
def my_func():
  yield 1
  yeild 2 
  yeild 3
  
  gen = my_func() ---> gene is a generator
  
  next(gene) ---> 1
  next(gene) ---> 2
  next(gene) ---> 3
  next(gene) ---> StopIteration  
```

- *next* and *StopIteration* should reminds you of iterator
- in fact generators are iterators --> they implement the iterator protocol \_\_iter__ and \_\_next__ 
  - they become exhausted when function return a value or None
  - when it does it receives StopIteration exception message

example of a simple iterator for factorial 
```
class FactIter:
    def __iter__(self, n):
        self.n = n
        self.i = 0
        
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            result = math.factorial(self.i)
            self.i += 1
            return result  

# To get the iterator, we have to call back iter (Create the iterator and call back itself with __iter__)
fact_iter = FactIter(5)
```
using generator 

```
def factorials(n):
  for i in range(n):
    yield math.factorial(i)
    
# get the iterator
fact_iter = factorial(5)

```
**Summary: Generators**
- Generator functions are functions which contain at lest one *yield* statement 
- when a generator function is called, Python creates a generator object
- Generator implement the iterator protocol 
- Generators are inherently lazy iterators (can be infinite)
- Generators are iterators, and can be used in the same way (for loop, comprehensions, etc)
- Generators become exhausted once the function returns a value 

**Making an iterable from a generator**
- Generator functions are functions that uses *yield*
- A generator function is a *generator factory* --> they return a (new) generator when called
- Generators are iterators
  - they can become exhausted (consumed)
  - they cannot be "restarted"
- This can lead to bugs if you try to iterate twice over a generator
- example

```
def squares():
  for i in range(n):
    yield i ** 2
   
sq = squrares(5) ---> sq is a new generator (iterator)
l  = list(sq) ------> l --> [0,1,4,9,16] and sq has been exhausted
l = list(sq) -------> l --> []
```
- This of course can lead to unexpected behaviour somethigs 
```
def squares(n):
  for i in range(n):
    yield i ** 2

sq = squares(5)
enum1 = enumerate(sq)       enumerate is lazy --> hasn't iterated through sq yet
next(sq) ---> 0
next(sq) ---> 1
list(enum1) --> [(0,4), (1,9), (2,16)]
            --> enumerated started at i=2
            --> the index value returned by enumerate is 0, not 2 
```

*Making an iterator*
- this behaviour is no different than with any other iterator 
- As we saw before, the solution is to create an iterable that returns a new iterator everytime 
```aiignore
def squares(n):
    for i in range(n):
        yield i ** 2


class Squares:
    def __init__(self,n):
        self.n = n
       
    def __iter__(self):
        return squares(n) # a new instance of the generator 

sq = Squares(n)

l1 = list(sq)   l1----> [0,1,4,9,16]
l2 = list(sq)   l2----> [0,1,4,9,16]
```
**Generator Expression and Performance**
*Comprehension syntax* 
- We already covered comprehension syntax when we studied list comprehension
```aiignore
l = [l ** 2 for i in range(50)]
```
- As well as more complicated syntax
  - if statement 
  - multiple nested loops
  - nested comprehensions

```
[(i,j)
    for i in range(1,6) if i%2=00
    for j in range(1,6) if j%3==0]

[[i * j] for j in range(5)] for i in range(5)]
```
*Generator expression uses the same syntax* 
- Instead of using [] it use ()

**Yield from**
- delegating to another iterator 
- we can replace inner loop by using a simpler syntax 
```
def read_all_data():
  for file in ('file1.csv', 'file2.csv', 'file3.csv'):
    with open(file) as f:
      for line in f:
        yield line
 
 # can be rewritting as 
 
 def read_all_data():
  for file in ('file1.csv', 'file2.csv', 'file3.csv'):
    with open(file) as f:
      yield from f
```

















