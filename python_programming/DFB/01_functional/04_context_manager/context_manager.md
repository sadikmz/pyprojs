**try....finally...**
- The finally section of a try always executes
```aiignore
try:
   ...
except:
    ...
finally:
    ...always executes...
    ...even if an exception occures in except block...
```
- Works even if inside a function and a *return* is in the *try* or *except* blocks 
- Very useful for writing code that should execute no matter what happens 
- But this can get cumbersome!

*Pattern*
- create some object
  - do some work with that object
- clean up the object after we are done using it
- We want to make this easy - automatic cleanup after we are done using the object

**Context Managers: PEP 343**
```aiignore
with context as obj_name:
    *with block (can use obj_name)
# after the with block, context is cleaned up automatically
```
```aiignore
with open(file_name) as f:      <--------- enter the context (optional) an object is returned
    # file is now open          <--------- Exit the contxt
# file is closed now 
```

*The context management protocol*
- Classes implement the contxt management protocol by implementing two methods:
  - \_\_enter__     -----> setup, and optionally returns the same object
  - \_\_exit__      -----> tear down / cleanup 

```aiignore
with CtxManager() as obj:
    # do something
# done with context
```

```aiignore
#Oversimplified, not considered exception handling 
mgr = CtxManager()
obj = mgr.__enter__()
try:
    # do something
finally:
    # done with context
    mgr.__exit__() 
```
*Use cases*
- Very common usage is for opening a file (creating resource) and closing the file (releasing resource)
- Context managers can be used for much more than creating and releasing resources

*Common Patterns*
- Open - Close
- Lock - Release
- Change - Reset
- Start - Stop
- Enter - Exit

*Example*
- File context managers
- Decimal contexts

*How Context Protocol Works*
```aiignore
class MyClass:
    def __init()__(self):
        # init class
    def __enter__(self):
        return obj
    def __exit__(self):
        # clean up obj
```
- works in conjunction with a *with* statement
- my_obj = MyClass()
  - works as a regular class
    - \_\_enter__, \_\_exit__ were not called
- with MyClass() as obj:
  - creates an instance of MyClass      ----> no associated symbol, but an instance exists ----> my_instance
  - calls my_instance.\_\_enter__()
  - return value from \_\_enter__ is assigned to obj
    - (not the instance of MyClass that was created)
- after the *with* block, or if an exception occurs inside the with block:
  - my_instance.\_\_exit__ is called

Scope of '*with*' block
- The *with* block is not like a function or a comprehension 
- The scope of anything in the with block (including the object returned from \_\_enter__) is in teh same scope as teh with statement itself
```aiignore
# module.py
with open(fname) as f:  <----------- f is a symbol in global scope
    row = next(f)       <----------- row is also in the global scope
print(f)                <----------- f is closed, but the symbol exists 
```

*The \_\_enter__ method*
- def \_\_enter__(self):
  - this method should perform whatever setup it needs to 
  - it can optionally return the object -----> as returned_obj

*The \_\_exit__ method*
- Remember the *finally* in a *try* statement ---> always runs even if an exception occurs
- \_\_exit__ is similar ----> runs even if an exception occurs in with block
- But should it handle things differently if an exception occurred?
  - maybe -----> so it needs to know about any exceptions that occurred
          -----> it also needs to tell Python whether to silence the exception, or let it propagate

*The \_\_exit__ method
```aiignore
with MyContext() as obj:
    raise ValueError
print('done')
```
*Scenario 1*
- \_\_exit__method receives error, performs some clean up and silences error
- print statement runs
- no exception is seen

*Scenario 2*
- \_\_exit__ method receives error, perform some clean up and let's error propagate 
- print statement does not run
- the ValueException is seen

*The \_\_exit__ method
- Needs three arguments
  - the exception type that occurred (if any, None otherwise)
  - the exception value that occurred (if any, None otherwise)
  - the traceback object if an exception occurred (if any, None otherwise)
- Returns *True* or *False*
  - *True* = silence any raised exception 
  - *False* = do not silence a raised exception 

```aiignore
def __exit__(self, exc_type, exc_value, exc_trace):
    # do clean up work here
    return True # or False
    
ValueError                                  Traceback (most recent call last)
<ipyhton-input-14-39......322> in <module>()
    1 with MyContext() as obj:
    2    raise ValueErro
```
**Pattern: Open - Close**
```aiignore
Open file
    operate on open file
close file
```

**Pattern: Open - Close**
```aiignore
Open socket
    operate on socket
close socket
```

**Pattern: Start - Strop**
```aiignore
Open database transaction
    perform database operations
commit or rollback transaction
```

```aiignore
Start timeer
    perform operations
Stop timer
```

**Pattern: Lock - Release**
```aiignore
acquire thread lock
    perform some operations
release thread lock
```

**Pattern: Change - Reset**
```aiignore
change Decimal context precision
    perform some operations using the new precision
reset Decimal context precision back to orginal value
```
```aiignore
redirect stdout to a file
    perform some operations that write to stdout 
reset stdout to orginal value 
```
**Pattern: Wacky stuff**
```aiignore
with tag('p'):
    print('some text', end='') -----> <p>some text</p>
```

```aiignore
with tag('p'):
    print('some', end='') 
    with tag('b'): -----> <p>some <b>bold<b> text</p>
        print('bold ', end='')
    print('text', end='=')
```

**Pattern: Wacky stuff**
```aiignore
with ListMaker(title='Items', prefix='- ', 
indent=3, stdout='myfile.txt') as lm:
    lm.print('Item 1')          Item 1
    with lm :                   >> myfile.txt
        lm.print('item 1a')         item 1a
        lm.print('item 1b')         item 1b
    lm.print('Item 2')          Item 2
    with lm:                        
        lm.print('item 2a')         item 2a
        lm.print('item 2b')         item 2b
    
```
**So far...**
- We saw how to create a context manager using a class and a generator function 
```aiignore
def gen_func():
    ....
    try:
        yield obj   <--------------- single yield   the return value of __enter__
    finally:        <--------------- cleanup phase                      __exit__
        
```

```aiignore
class GenContextManager:
    def __init__(gen_func):
        self.gen = gen_func()
    
    def __enter__(self):
        return next(self.gen)       <------------- return what was yielded 
    
    def __exit__(self,...):
        next(self.gen)              <------------- run the finally block
```