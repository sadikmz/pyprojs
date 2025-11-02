import json
import pprint

d1 = {'a':100, 'b': 200}
print(d1)
d1_json = json.dumps(d1)
print(d1_json)
print(type(d1_json))
# prety print
print(json.dumps(d1, indent=2))
# revese
d2 = json.loads(d1_json)
print(type(d2))
print(d2)
print(d1 is d2)

d1 = {1:100, 2: 200}
d1_json = json.dumps(d1)
print(d1_json)
d2 = json.loads(d1_json)
print(d2)
print(d1 is d2)

d_json = '''
{
    "name": "John Cleese",
    "age": 82,
    "height": 1.96,
    "walksFunny": true,
    "sketches": [
        {
        "title": "Dead Parrot",
        "costars": ["Michael Palin"]
        },
        {
        "title": "Ministry of Silly Walks",
        "costars": ["Michael Palin", "Terry Jones"]
        }
    ],
    "boring": null    
}
'''

print(type(d_json))
d = json.loads(d_json)
print(type(d))
print(d)
from pprint import pprint
pprint(d)
print(d['age'], d['height'], d['walksFunny'], d['sketches'])
print(type(d['sketches']))

# serializing tuples

d = {'a':(1,2,3)}
ser = json.dumps(d)
print(ser)
d = json.loads(ser)
print(d)

# bad_json = '''
# {'a':(1,2,3)}
# '''
#
# d = json.loads(bad_json)
# print(d)


from decimal import Decimal

# d = {'a':Decimal('0.5')}
# ser = json.dumps(d)
# print(ser)

try:
    json.dumps({'a':1+1j})
except TypeError as ex:
    print(ex)


# person object

class Person:
    def __init__(self, name, age,):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

p = Person('John Cleese', 82)
print(p)

# p_json = json.dumps(p)

# Write our own serializer

class Person:
    def __init__(self, name, age,):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def toJSON(self):
        return vars(self)
        return dict(name=self.name, age=self.age)



p = Person('John Cleese', 82)
print(p)
print(vars(p))
p_json = json.dumps({"john": p.toJSON()}, indent=2)
print(p_json)


#serialing a set


d = {"a": {1,2,3}}
print(d)
d = {"a": list({1,2,3})}

d_json = json.dumps(d)
print(d_json)
d = json.loads(d_json)
print(d)