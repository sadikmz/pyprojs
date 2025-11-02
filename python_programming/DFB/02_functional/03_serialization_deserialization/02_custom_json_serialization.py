# serializing some data type do not work and need a custom serializer format

from datetime import datetime

current  = datetime.now()
print(current)

import json

# json.dumps(current)

# format:ISO-8641
'''
'YYYY-MM-DDThh:mm:ss' 
'''

def format_iso(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%S')

print(format_iso(current))

# python method

print(current.isoformat())

# serilize a dictionary containing datetime

log_record = {
    'time': datetime.now().isoformat(),
    'message': 'testing'
}

json_record = json.dumps(log_record)
print(json_record)

#

log_record = {
    'time': datetime.now(),
    'message': 'testing'
}

json_record = json.dumps(log_record, default=format_iso)
print(json_record)

def format_general(arg):
    return 'Unknown serialization'

print(json.dumps(log_record, default=format_general))

# extending unserializer object

log_record = {
    'time': datetime.now(),
    'message': 'testing',
    'args': {10, "test"}
}


print(json.dumps(log_record, default=format_general))


log_record = {
    'time1': datetime.now(),
    'time2': datetime.now(),
    'message': 'Testing',
    'args': {1,2,3}

}


# print(json.dumps(log_record, default=format_iso))
# print(type((1,2,3)))
# print(type({1,2,3,3}))
# print({1,2,3,3})

def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)


print(json.dumps(log_record, default=custom_json_formatter))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.create_dt = datetime.now()

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def toJSON(self):
        return {
            'name': self.name,
            'age': self.age,
            'create_dt': self.create_dt.isoformat(),

        }

p = Person('John', 82)
print(p.toJSON())

def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)

log_record = dict(time=datetime.now(),
                  message='Created new person record',
                  person=p)

p_json = json.dumps(log_record, default=custom_json_formatter)
print(p_json)

def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)
    elif isinstance(arg, Person):
        return arg.toJSON()

p_json = json.dumps(log_record, default=custom_json_formatter)
print(p_json)

# update person class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.create_dt = datetime.now()

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def toJSON(self):
        return vars(self)
        # return {
        #     'name': self.name,
        #     'age': self.age,
        #     'create_dt': self.create_dt
        #
        # }

p = Person('Python', 45)

log_record = {
    'time1': datetime.now(),
    'time2': datetime.now(),
    'message': 'Testing',
    'person': p

}

p_json = json.dumps(log_record, default=custom_json_formatter)
print(p_json)

# point class

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'


# tweak json formatter
def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)
    elif isinstance(arg, Person):
        return arg.toJSON()
    else:
        try:
            return arg.toJSON()
        except AttributeError:
            try:
                return vars(arg)
            except TypeError:
                return str(arg)

from decimal import Decimal

pt1 = Point(1, 2)
p = Person('John', 82)
pt2 = Person(Decimal('10.5'), Decimal(100.5))
log_record = dict(time=datetime.now(),
                  message='Created new point',
                  point=pt1,
                  point2=pt2,
                  created_by=p
                  )

pt1_json = json.dumps(log_record, default=custom_json_formatter)

print(pt1_json)

# using single dispatch decorator

from functools import singledispatch

@singledispatch
def json_format(arg):
    print(arg)
    try:
        print('\ttrying to use toJSON')
        return arg.toJSON()
    except AttributeError:
        print('\ttrying to use vars')
        try:
            return vars(arg)
        except TypeError:
            print('\tfailed - using string representation')
            return str(arg)

# Register different types
@json_format.register(datetime)

def _(arg):
    return arg.isoformat()

@json_format.register(set)
def _(arg):
    return list(arg)

log_record = dict(time=datetime.now(),
                  message='Created new point',
                  point=pt1,
                  created_by=p
                  )

# print(json.dumps(log_record, indent=2, default=json_format))

from decimal import Decimal
from fractions import Fraction

d = dict(a = 1+1j,
         b = Decimal(0.5),
         c = Fraction(1, 3),
         d = Person('Python', 82),
         time = datetime.now()
         )

d_ser  = json.dumps(d, default=json_format)
# print(d)
print(d_ser)

@json_format.register(Decimal)
def _(arg):
    return f'Decimal({str(arg)})'

d_ser  = json.dumps(d, default=json_format)
# print(d)
print(d_ser)