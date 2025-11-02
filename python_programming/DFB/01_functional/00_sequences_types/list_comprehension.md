**Formatting the comprehension expression**
- For example, let's say we want to create a list of squares of all the integers between 1 and 100 that are not divisible by 2, 3, and 5

sq = [i**2 for i in range(1,101) if i%2 and i%3 and i%5]

or can be written in multiline as 

sq = [i**2 <br>
for i in range(1,101) <br>
if i%2 and i%3 and i%5]

**Comprehension internals**
- Comprehensions have their own local scope - just like a function 
- We should think of a list comprehension as being wrapped in a function that is created by python that will return the new list when executed 

**Comprehension scopes**
- Comprehensions are basically functions 
- They have their own locals: eg item in [item**2 for item in range(100)]
- But they can access global variables eg. num

num = 100

sq = [item**2 for item in range(num)]
- item is local symbol and num is global symbol 

- They also have nonlocal variables: eg. num below

def my_func(num):
    sq = [item **2 for item in range(num)]

- hence, they are closures!

**Nested comprehensions**
[[i*j for j in range(5)] for i in range(5)]

**Nested loops in Comprehensions**
l = []
for i in range(5):
    for j in range(5):
        for k in range(5):
            for l.append((i,j,k))

[(i,j,k) for i in range(5) for j in range(5) for k in range(5)]


**can also contain if statement**
l = []
for i in range(5):
    for j in range(5):
        if i ==j:
            for l.append((i,j))

[(i,j) for i in range(5) for j in range(5) if i==j]


l = []
for i in range(5):
    if i%2==0
    for j in range(5):
        if j%3==0:
            for l.append((i,j))

[(i,j) <br>
for i in range(5) if i%2 == 0 <br> 
for j in range(5) if j%3 == 0]


l = []
for i in range(5):
    for j in range(5):
        if i%2==0
            if j%3==0:
                for l.append((i,j))

[(i,j) <br>
for i in range(5) <br>
for j in range(5) <br> 
if i%2 == 0 <br> 
if j%3 == 0]


[(i,j) <br>
for i in range(5) <br>
for j in range(5) <br> 
if i%2 == 0 and if j%3 == 0]